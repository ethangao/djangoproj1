import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=db0)

def addDiscussToTopicThread(discussId, topicId):
    redis = redis.StrictRedis(connection_pool=pool)
    redis.zadd('topic:' + topicId + ':discusses',discussId=0)

