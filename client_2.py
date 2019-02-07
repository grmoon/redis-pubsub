import redis
import time
import logging

logger = logging.getLogger()

logger.warning('sleeping for 10 seconds before connecting to redis')
time.sleep(10)

logger.warning('connecting to redis')
instance = redis.Redis(host='redis', port=6379, db=0)

logger.warning("publishing to 'shared' channel")
message_num = 0
num_clients = 1

while(num_clients > 0):
    message_num += 1
    num_clients = instance.publish('shared', 'message {}'.format(message_num))
    time.sleep(1)

logger.warning('stopping')

