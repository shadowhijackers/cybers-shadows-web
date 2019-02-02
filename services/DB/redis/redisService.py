import json

from redis import RedisError

from config import REDIS_INSTANCE


class RedisService():

    redis = REDIS_INSTANCE

    def __init__(self):

        print "Redis module loaded"

    def setItem(self, key, value):

        self.redis.set(key, value)

    def getItem(self, key):

        self.redis.get(key)

    def setJSONItem(self, key, value):

        try:
            data = json.dumps(value)
            self.redis.set(key, value)

        except RedisError:
            print  RedisError

    def getJSONItem(self, key, optData=None):

        try:
            data = self.redis.get(key)
            if data is not None:
                return json.loads(data)
            else:
                return []

        except RedisError, ValueError:
            print RedisError
            print  ValueError
            return optData
