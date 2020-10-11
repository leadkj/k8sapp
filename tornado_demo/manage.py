from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import define,options,parse_command_line


from app.urls import settings


define('port',default=8089,type=int)
define('host',default='0.0.0.0',type=str)


class App(Application):
	def __init__(self):
		Application.__init__(self,**settings)



if __name__ == '__main__':
	parse_command_line()
	app = App()
	app.listen(options.port,options.host)
	IOLoop.instance().start()