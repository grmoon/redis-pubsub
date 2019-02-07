import time
import logging
import redis

logger = logging.getLogger()

logger.warning('Sleeping for 5 seconds before connecting to redis')
time.sleep(5)

logger.warning('connecting to redis')
instance = redis.Redis(host='redis', port=6379, db=0)

logger.warning('creating pubsub instance')
pubsub = instance.pubsub()

logger.warning("subscribing to 'shared' channel")
pubsub.subscribe('shared')

logger.warning('Starting to listen for messages')

message_num = 0

for message in pubsub.listen():
    message_num += 1
    logger.warning('recieving message {}'.format(message))

    if message_num == 100:
        break

logger.warning('unsubscribing')
pubsub.unsubscribe()

logger.warning('stopping')

