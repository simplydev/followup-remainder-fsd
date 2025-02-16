import redis
import json
import os

class RedisUtil:
    def __init__(self, host="localhost", port=6379, db=0):
        self.redis_client = redis.Redis(host=host, port=port, decode_responses=True, db=db)

    ### -------------------- 1. Storing Key-Value with Expiry -------------------- ###
    def set_with_expiry(self, key: str, value: str, expiry: int):
        """
        Store a key-value pair in Redis with an expiry time.
        :param key: Redis key
        :param value: Redis value (string)
        :param expiry: Expiry time in seconds
        """
        return self.redis_client.setex(key, expiry, value)

    def get_value(self, key: str):
        """
        Retrieve a value from Redis by key.
        :param key: Redis key
        :return: Value if exists, else None
        """
        return self.redis_client.get(key)

    ### -------------------- 2. Storing Key-Value (No Expiry) -------------------- ###
    def set_value(self, key: str, value: str):
        """
        Store a key-value pair in Redis without an expiry.
        :param key: Redis key
        :param value: Redis value (string)
        """
        return self.redis_client.set(key, value)

    ### -------------------- 3. Storing JSON -------------------- ###
    def set_json(self, key: str, value: dict):
        """
        Store a JSON object in Redis.
        :param key: Redis key
        :param value: JSON dictionary
        """
        return self.redis_client.set(key, json.dumps(value))

    def get_json(self, key: str):
        """
        Retrieve a JSON object from Redis.
        :param key: Redis key
        :return: JSON object if exists, else None
        """
        value = self.redis_client.get(key)
        return json.loads(value) if value else None

    ### -------------------- 4. Storing JSON with Expiry -------------------- ###
    def set_json_with_expiry(self, key: str, value: dict, expiry: int):
        """
        Store a JSON object in Redis with an expiry time.
        :param key: Redis key
        :param value: JSON dictionary
        :param expiry: Expiry time in seconds
        """
        return self.redis_client.setex(key, expiry, json.dumps(value))

    ### -------------------- 5. Storing Hash -------------------- ###
    def set_hash(self, key: str, value: dict):
        """
        Store a Hash (like a table row) in Redis.
        :param key: Redis key
        :param value: Dictionary of field-value pairs
        """
        return self.redis_client.hset(key, mapping=value)

    def get_hash(self, key: str):
        """
        Retrieve a Hash from Redis.
        :param key: Redis key
        :return: Dictionary of fields if exists, else None
        """
        return self.redis_client.hgetall(key)

    ### -------------------- 6. Storing Hash with Expiry -------------------- ###
    def set_hash_with_expiry(self, key: str, value: dict, expiry: int):
        """
        Store a Hash with an expiry time in Redis.
        :param key: Redis key
        :param value: Dictionary of field-value pairs
        :param expiry: Expiry time in seconds
        """
        self.redis_client.hset(key, mapping=value)
        self.redis_client.expire(key, expiry)

    ### -------------------- Utility Functions -------------------- ###
    def delete_key(self, key: str):
        """
        Delete a key from Redis.
        :param key: Redis key
        """
        return self.redis_client.delete(key)

    def key_exists(self, key: str):
        """
        Check if a key exists in Redis.
        :param key: Redis key
        :return: True if exists, False otherwise
        """
        return self.redis_client.exists(key)

    def get_ttl(self, key: str):
        """
        Get the TTL (time-to-live) of a key in Redis.
        :param key: Redis key
        :return: TTL in seconds, or -1 if key does not expire
        """
        return self.redis_client.ttl(key)