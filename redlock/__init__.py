from uuid import uuid4

import redis

version = '0.1'


def get_client(host='127.0.0.1', port=6379, timeout=None):
    return redis.StrictRedis(host=host, port=port, db=0, socket_timeout=timeout)


class UnableToLock(Exception):
    pass


class Locker(object):
    UNLOCK_SCRIPT = """
    if redis.call("get", KEYS[1]) == ARGV[1] then
        return redis.call("del", KEYS[1])
    else
        return 0
    end
    """

    def __init__(self, client, key, lock_expire=None):
        """
        `client` is a redis.StrictRedis client.
        `key` is the resource identifier to lock.
        `lock_expire` is the time in milliseconds that the lock will expire.

        """
        self.key = key
        self.client = client
        self.expire = lock_expire

        self.value = str(uuid4())
        self.script = self.client.register_script(self.UNLOCK_SCRIPT)

    def acquire(self):
        return self.client.set(self.key, self.value, px=self.expire, nx=True)

    def release(self):
        res = self.script(keys=[self.key], args=[self.value])
        if res == 1L:
            return True  # We released the lock
        elif res == 0:
            return False

    def __enter__(self):
        if not self.acquire():
            raise UnableToLock('lock previously acquired')

        return self

    def __exit__(self, _type, value, traceback):
        self.release()
