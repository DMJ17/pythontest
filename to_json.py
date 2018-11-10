from sqlalchemy import Column, String, create_engine, Integer, DECIMAL, DateTime, Text, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from django.http import JsonResponse

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime

def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
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
# # 数据集类
class Data_Set():

    # 创建对象的基类:
    def PUB_INDU_CODE(self):
        Base = declarative_base()
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
        # 创建DBSession类型:
        Session = sessionmaker(bind=engine)
        session = Session()

        # 定义INC_INFO_PRO对象:
        class INDU_CODE(Base):
            # 表的名字:
            __tablename__ = 'PUB_INDU_CODE'
            # 表的结构:
            INDU_UNI_CODE = Column(DECIMAL, primary_key=True)

            ISVALID = Column(DECIMAL)
            CREATETIME = Column(DateTime)
            UPDATETIME = Column(DateTime)
            INDU_SYS_PAR = Column(DECIMAL)
            INDU_LEVEL = Column(DECIMAL)
            INDU_CODE = Column(Text)
            INDU_NAME = Column(Text)
            INDU_DES = Column(Text)
            IS_VALID = Column(DECIMAL)
            FST_INDU_UNI_CODE = Column(DECIMAL)
            SED_INDU_UNI_CODE = Column(DECIMAL)
            TRD_INDU_UNI_CODE = Column(DECIMAL)
            FOUR_INDU_UNI_CODE = Column(DECIMAL)

        try:
            ret = session.query(INDU_CODE).limit(2)
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)

            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

if __name__ == '__main__':
    data_set = Data_Set()
    #行业代码信息
    pub_indu_code = data_set.PUB_INDU_CODE()
    print(pub_indu_code)
