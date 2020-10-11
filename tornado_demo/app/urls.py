import os
from tornado.web import RedirectHandler

from app.views import *

settings = {
	"handlers":[
		(r'/',IndexHandler),
		(r'/login/',LoginHandler),
		(r'/center/',RedirectHandler,{'url':'/center/1/'}),
		(r'/center/(?P<num>\d+)/',CenterHandler), #(?P<name>.+)表示字符串
		(r'/logout/',LogoutHandler),
		#Cluster resource
		(r'/api/namespace/',NamespaceHandler),
		(r'/api/node/', NodeHandler),
		(r'/api/pv/', PVHandler),
		(r'/api/role/',RoleHandler),
		(r'/api/storageclass/',StorageClassHandler),
		#resource of namespace
		(r'/api/daemonset/(?P<namespace>.+)/', DaemonSetHandler),
		(r'/api/deployment/(?P<namespace>.+)/', DeploymentHandler),
		(r'/api/replicaset/(?P<namespace>.+)/', ReplicaSetHandler),
		(r'/api/statefulset/(?P<namespace>.+)/', StatefulSetHandler),
		(r'/api/pod/(?P<namespace>.+)/',PodHandler),
		(r'/api/service/(?P<namespace>.+)/', ServiceHandler),
		(r'/api/configmap/(?P<namespace>.+)/', ConfigMapHandler),
		(r'/api/secret/(?P<namespace>.+)/', SecretHandler),
		(r'/api/pvc/(?P<namespace>.+)/', PVCHandler),
		(r'/api/job/(?P<namespace>.+)/', JobHandler),
		(r'/api/cronjob/(?P<namespace>.+)/', CronJobHandler),
		(r'/api/replicationcontroller/(?P<namespace>.+)/', CronJobHandler),
		(r'/api/ingress/(?P<namespace>.+)/',IngressHandler),


	],#配置urls
	"template_path": os.path.join(os.getcwd(),'templates'),#配置模板文件路径
	"static_path": os.path.join(os.getcwd(),'static'), #配置静态文件路径
}