#引入列和字段类型
from sqlalchemy import Column
from sqlalchemy.types import  Integer,String,Date,DateTime,Float,Text

from app.utils.base_db import Base

#自定义数据表类



class  User(Base):
	__tablename__ = 'user'
	id = Column(Integer,primary_key=True,autoincrement=True)
	username = Column(String(length=20))
	password = Column(String(length=20))

	# 打印对象输出
	def __repr__(self):
		return '<User:%d,%s>'%(self.id,self.username)

class BeautyDownloadUrls(Base):
	__tablename__ = 'beauty_download_urls'
	id = Column(Integer, primary_key=True, autoincrement=True)
	beauty_name = Column(String(length=255))
	beauty = Column(String(length=255))
	url = Column(String(length=255))


#创建数据表
#Base.metadata.create_all()

#删除数据表
#Base.metadata.drop_all()