from tornado.web import RequestHandler
from app.utils.Session import SessionManager


class BaseHandler(RequestHandler):
	def prepare(self):
		#获取sessionid
		sessionid = self.get_cookie('xr_cookie','')

		#根据sessionid 获取session对象
		session = SessionManager().getSessionById(sessionid)

		#判断session的id是不是和sessionid相同
		if session.sessionid != sessionid:
			self.set_cookie('xr_cookie',session.sessionid,expires_days=14)
		self.session = session
		self.response_data = {'code':None,'data':[]}
		self.data_dict = {"name":None,"status":None,"type":None}
	def on_finish(self):
		SessionManager.cache2redis(self.session)

	def get_current_user(self):
		return self.session.get('user')