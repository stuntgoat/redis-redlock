# `redis-redlock`
draft of redlock http://redis.io/topics/distlock

### `requirements`

`redis` [https://github.com/andymccurdy/redis-py](https://github.com/andymccurdy/redis-py)

-------------------------------------------

Example:

```python
from redlock import Locker, get_client, UnableToLock


client = get_client('33.33.33.10', 6378)
try:
    with Locker(client, 'unique-resource'):
        # do something with unique resource.
        print 'could do something'
except UnableToLock:
    print 'could not do something'

```
