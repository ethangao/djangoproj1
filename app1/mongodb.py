import datetime
from bson.objectid import ObjectId
import pymongo
import redis
from djangoproj1.app1 import redisdb

connection = pymongo.Connection('localhost', 27017)
db = connection.db0

def addTopic(userId, topicTitle, topicContent, topicTags):
    return db.topics.insert({'userId':userId, 'topicTitle':topicTitle,
                             'topicContent':topicContent, 'date': datetime.datetime.utcnow(),
                             'topicTags': topicTags})

def addDiscuss(userId, topicId, discussContent):
    discussId = db.discusses.insert({'userId':userId, 'topicId': topicId,
                                     'discussContent':discussContent, 'date': datetime.datetime.utcnow()})
    redisdb.addDiscussToTopicThread(discussId, topicId)
    return discussId

def getTwentyRandomTopics():
    return db.topics.find().limit(20)

def getTopic(topicId):
    return db.topics.find_one({'_id': ObjectId(topicId)})

def getDiscussOfaTopic(topicId):
    return db.discusses.find({'topicId': topicId})

def getSpecificDiscuss(discussId):
    return db.discusses.find_one({'_id':ObjectId(discussId)})