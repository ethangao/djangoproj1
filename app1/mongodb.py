import datetime
import pymongo
import redis
from app1 import redisdb

connection = pymongo.Connection('localhost', 28017)
db = connection.db0

def addTopic(userId, topicTitle, topicContent):
    return db.topics.insert({'userId':userId, 'topicTitle':topicTitle, \
                             'topicContent':topicContent, 'date': datetime.datetime.utcnow()})

def addDiscuss(userId, topicId, discussContent):
    discussId = db.discusses.insert({'userId':userId, 'topicId': topicId, \
                                     'discussContent':discussContent, 'date': datetime.datetime.utcnow()})
    redisdb.addDiscussToTopicThread(discussId, topicId)
    return discussId

def getTwentyRandomTopics():
    return ({topicId:topic['topicId'], topicTitle:topic['topicTitle'], \
             topic:desctopic['topicContent'][:2000]} for topic in db.topics.find().limit(3))
