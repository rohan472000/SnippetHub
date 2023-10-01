"""
* Redis Integration *

Redis is an open-source, in-memory data store that serves as a high-performance and highly scalable caching and message broker system. This integration provides some redis operations. This integration provides some redis operations. 

Dependency:
1. Redis package: The package link -> https://pypi.org/project/redis/
2. Accessible redis server: It can be downloaded from https://redis.io/. Or easily with docker: `docker run -p 6379:6379 -d redis`

Wikipedia: https://en.wikipedia.org/wiki/Redis
"""

import redis


class RedisClient:
    """
    A simple Redis client class for basic key-value operations.

    Args:
        host (str, optional): The hostname of the Redis server. Defaults to 'localhost'.
        port (int, optional): The port number of the Redis server. Defaults to 6379.
        db (int, optional): The database number. Defaults to 0.
    """
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db)

    def set(self, key, value):
        """
        Set a key-value pair in Redis.

        Args:
            key: The key to set.
            value: The value to associate with the key.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        return self.client.set(key, value)

    def get(self, key):
        """
        Get the value associated with a key from Redis.

        Args:
            key: The key to retrieve the value for.

        Returns:
            bytes: The value associated with the key, or None if the key does not exist.
        """
        return self.client.get(key)

    def delete(self, key):
        """
        Delete a key and its associated value from Redis.
        
        Args:
            key (str): The key to delete.

        Returns:
            int: The number of keys that were deleted (0 or 1).
        """
        return self.client.delete(key)

    def keys(self, pattern='*'):
        """
        Get a list of keys matching the specified pattern.

        Args:
            pattern (str, optional): The pattern to match keys against. Defaults to '*'.

        Returns:
            list: A list of keys matching the specified pattern.
        """
        return self.client.keys(pattern)

if __name__ == "__main__":
    host = "localhost"

    redis_client = RedisClient(host=host)

    # Set a key-value pair
    redis_client.set('my_key', 'my_value')

    # Get a value by key
    value = redis_client.get('my_key')
    print(f'Value for my_key: {value.decode("utf-8")}')

    # Delete a key
    redis_client.delete('my_key')

    # Check if the key still exists
    value = redis_client.get('my_key')
    if value is None:
        print('my_key has been deleted.')

    # Get all keys matching a pattern
    all_keys = redis_client.keys()
    print(f'Keys matching "prefix_*": {all_keys}')