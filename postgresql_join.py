import psycopg2
from sqlalchemy import Column, String, create_engine, Integer, ForeignKey

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine.url import URL
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm import sessionmaker,relationship

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime
def new_alchemy_encoder():
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                # 去重
                # if obj in _visited_objs:
                #     return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder


    # 创建对象的基类:
def User_list():
    engine = create_engine('postgres://postgres:postgres@10.202.62.68:5432')
    Base = declarative_base()
    Session = sessionmaker(engine)
    session = Session()

    # 把表抽象成类
    class TestTable(Base):
        __tablename__ = 'test'
        __table_args__ = {'schema': 'mun'}
        id   = Column(Integer, primary_key = True)
        account  = Column(String)
        test_id = Column(Integer)

    class User(Base):
        __tablename__ = 'test'
        __table_args__ ={'schema': 'public'}
        id = Column(Integer, primary_key=True)
        name = Column(String)

    ret = session.query(TestTable,User).join(User, TestTable.test_id == User.id, isouter = True)

    try:
        msgs = []
        for msg in ret:
            msgs.append(msg)
        json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)

        print (json_data)
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()

User_list()