# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# MySQL连接
MYSQL_CONN = 'mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8'.format('root', 'demo', 'localhost', 'great')
engine = create_engine(MYSQL_CONN)

# 一旦flush就能在query中拿到数据，但是不自动提交（不提交就不会真的写到数据库中去）
session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 使用scoped_session的目的主要是为了线程安全。
# scoped_session类似单例模式，当我们调用使用的时候，会先在Registry里找找之前是否已经创建session了。
# 要是有，就把这个session返回。
# 要是没有，就创建新的session，注册到Registry中以便下次返回给调用者。
# 这样就实现了这样一个目的：在同一个线程中，call scoped_session 的时候，返回的是同一个对象.
db_session = scoped_session(session_factory)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在元数据上。
    # 否则你就必须在调用 init_db() 之前导入它们。
    import great.models

    # 如果这些model对应的数据表不存在, 可以通过 Base.metadata.create_all(engine) 来创建所有 Base 派生类所对应的数据表
    Base.metadata.create_all(engine)
