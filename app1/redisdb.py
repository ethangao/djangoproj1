import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

def addDiscussToTopicThread(discussId, topicId):
    redisConn = redis.StrictRedis(connection_pool=pool)
    redisConn.zadd('topic:' + topicId + ':discusses',discussId=0)

