from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config import DB,DB_HOST,DB_PASSWD,DB_USER


#连接mysql
conn_url = "mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8" %(DB_USER,DB_PASSWD,DB_HOST,DB)
engine = create_engine(conn_url,encoding='utf-8',echo=True)

#声明ORM基类
Base = declarative_base(bind=engine)

