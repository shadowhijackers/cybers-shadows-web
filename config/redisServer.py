from redis import Redis
from config.app_factory import MyAPP
REDIS_INSTANCE = Redis(host=MyAPP.REDIS_HOST(), db=0, socket_connect_timeout=2, socket_timeout=2)
