import uuid
import pickle
import redis
from app.config import REDIS_HOST


class Session(object):
	def __init__(self):
		self._sessionid = uuid.uuid4().hex
		self.cache={}

	def set(self,key,value):
		self.cache[key]=value

	def get(self,key,default=None):
		return self.cache.get(key,default)

	def clear(self):
		self.cache.clear()

	@property
	def sessionid(self):
		return self._sessionid

	#序列化session对象
	def serialization(self):
		return pickle.dumps(self)

	@staticmethod
	def deserialization(str):
		return pickle.loads(str)

class SessionManager(object):
	conn = redis.Redis(REDIS_HOST,port=6379,db=2)

	@classmethod
	def cache2redis(cls,session):
		cls.conn.set(session._sessionid,session.serialization(),ex=14*24*60*60)

	@classmethod
	def getSessionById(cls,sessionid):
		rs = Session.deserialization(cls.conn.get(sessionid)) if cls.conn.get(sessionid) else None
		if not rs:
			rs = Session()
		return rs