from sqlalchemy import Column, String, create_engine, Integer, DECIMAL, DateTime, Text, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

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

# 数据集类
class Data_Set():
# 股票基本信息
    # 创建对象的基类:
    def STK_BASIC_INFO(self):
        Base = declarative_base()
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
        # 创建DBSession类型:
        Session = sessionmaker(bind=engine)
        session = Session()
        # 定义BASIC_INFO对象:
        class BASIC_INFO(Base):
            # 表的名字:
            __tablename__ = 'STK_BASIC_INFO'
            # 表的结构:
            STK_UNI_CODE = Column(DECIMAL, primary_key= True)

            ISVALID = Column(DECIMAL)
            CREATETIME = Column(DateTime)
            UPDATETIME = Column(DateTime)
            COM_UNI_CODE = Column(DECIMAL)
            STK_CODE = Column(Text)
            STK_SHORT_NAME = Column(Text)
            SPE_SHORT_NAME = Column(Text)
            STK_TYPE_PAR = Column(DECIMAL)
            LIST_DATE = Column(DECIMAL)
            SEC_MAR_PAR = Column(DECIMAL)
            LIST_SECT_PAR = Column(DECIMAL)
            LIST_STA_PAR = Column(DECIMAL)
            ISS_STA_PAR = Column(DECIMAL)
            ISIN_CODE = Column(DECIMAL)
            END_DATE = Column(DECIMAL)
            BELONG_PARK = Column(DECIMAL)
            TRANS_WAY = Column(DECIMAL)

        #结果返回一个json数组
        try:
            ret = session.query(BASIC_INFO).all()
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

# 公司主营业务构成按产品分布信息
    def COM_INC_INFO_PRO(self):
        Base = declarative_base()
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
        # 创建DBSession类型:
        Session = sessionmaker(bind=engine)
        session = Session()
        # 定义INC_INFO_PRO对象:
        class INC_INFO_PRO(Base):
            # 表的名字:
            __tablename__ = 'COM_INC_INFO_PRO'
            # 表的结构:
            COM_UNI_CODE = Column(DECIMAL, primary_key= True)
            END_DATE = Column(Date, primary_key= True)
            ITEM_ID = Column(DECIMAL, primary_key= True)
            SHEET_MARK_PAR = Column(DECIMAL, primary_key= True)


            ISVALID = Column(DECIMAL)
            CREATETIME = Column(DateTime)
            UPDATETIME = Column(DateTime)
            SHEET_SOUR_PAR = Column(DECIMAL)
            PRO_NAME = Column(Text)
            PRO_INC = Column(DECIMAL)
            PRO_COST = Column(DECIMAL)
            PRO_PROFIT = Column(DECIMAL)
            GRS_PRFT_VAL = Column(DECIMAL)
            INC_CHAN = Column(DECIMAL)
            COST_CHAN = Column(DECIMAL)
            GRS_PRFT_CHAN = Column(DECIMAL)
            OP_PCT = Column(DECIMAL)

        # 结果返回一个列表
        try:
            ret = session.query(INC_INFO_PRO).all()
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

#行业代码信息
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
            INDU_UNI_CODE = Column(DECIMAL, primary_key= True)

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

        # 结果返回一个列表
        try:
            ret = session.query(INDU_CODE).all()
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

#公司最新从属行业信息
    def PUB_COM_INDU_RELA(self):
        Base = declarative_base()
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
        # 创建DBSession类型:
        Session = sessionmaker(bind=engine)
        session = Session()
        # 定义COM_INDU_RELA对象:
        class COM_INDU_RELA(Base):
            # 表的名字:
            __tablename__ = 'PUB_COM_INDU_RELA'
            # 表的结构:
            COM_UNI_CODE = Column(DECIMAL, primary_key= True)
            INDU_SYS_CODE = Column(DECIMAL, primary_key= True)

            ISVALID = Column(DECIMAL)
            CREATETIME = Column(DateTime)
            UPDATETIME = Column(DateTime)
            INDU_UNI_CODE = Column(DECIMAL)


        # 结果返回一个列表
        try:
            ret = session.query(COM_INDU_RELA).all()
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

#合并资产负债信息
    def FIN_BALA_SHORT(self):
        Base = declarative_base()
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
        # 创建DBSession类型:
        Session = sessionmaker(bind=engine)
        session = Session()
        # 定义BALA_SHORT对象:
        class BALA_SHORT(Base):
            # 表的名字:
            __tablename__ = 'FIN_BALA_SHORT'
            # 表的结构:
            COM_UNI_CODE = Column(DECIMAL, primary_key = True)
            END_DATE = Column(Date, primary_key = True)

            ISVALID = Column(DECIMAL)
            CREATETIME = Column(DateTime)
            UPDATETIME = Column(DateTime)
            CURY_TYPE_PAR = Column(DECIMAL)
            CURY_UNIT_PAR = Column(DECIMAL)
            BS_11001 = Column(DECIMAL)
            BS_11002 = Column(DECIMAL)
            BS_11003 = Column(DECIMAL)
            BS_11000 = Column(DECIMAL)
            BS_12001 = Column(DECIMAL)
            BS_10000 = Column(DECIMAL)
            BS_21001 = Column(DECIMAL)
            BS_21002 = Column(DECIMAL)
            BS_21000 = Column(DECIMAL)
            BS_22000 = Column(DECIMAL)
            BS_20000 = Column(DECIMAL)
            BS_30001 = Column(DECIMAL)
            BS_30002 = Column(DECIMAL)
            BS_30003 = Column(DECIMAL)
            BS_30004 = Column(DECIMAL)
            BS_31000 = Column(DECIMAL)
            BS_32000 = Column(DECIMAL)
            BS_30000 = Column(DECIMAL)
            BS_11016 = Column(DECIMAL)
            BS_11031 = Column(DECIMAL)
            BS_11067 = Column(DECIMAL)
            BS_11070 = Column(DECIMAL)
            BS_11079 = Column(DECIMAL)
            BS_11082 = Column(DECIMAL)
            BS_12013 = Column(DECIMAL)
            BS_12016 = Column(DECIMAL)
            BS_12019 = Column(DECIMAL)
            BS_12022 = Column(DECIMAL)
            BS_12025 = Column(DECIMAL)
            BS_12031 = Column(DECIMAL)
            BS_12034 = Column(DECIMAL)
            BS_12037 = Column(DECIMAL)
            BS_12040 = Column(DECIMAL)
            BS_12043 = Column(DECIMAL)
            BS_12046 = Column(DECIMAL)
            BS_12049 = Column(DECIMAL)
            BS_12052 = Column(DECIMAL)
            BS_12055 = Column(DECIMAL)
            BS_12058 = Column(DECIMAL)
            BS_12064 = Column(DECIMAL)
            BS_12000 = Column(DECIMAL)
            BS_21003 = Column(DECIMAL)
            BS_21019 = Column(DECIMAL)
            BS_21070 = Column(DECIMAL)
            BS_21079 = Column(DECIMAL)
            BS_21082 = Column(DECIMAL)
            BS_21085 = Column(DECIMAL)
            BS_21088 = Column(DECIMAL)
            BS_21091 = Column(DECIMAL)
            BS_21094 = Column(DECIMAL)
            BS_21097 = Column(DECIMAL)
            BS_21100 = Column(DECIMAL)
            BS_22001 = Column(DECIMAL)
            BS_22004 = Column(DECIMAL)
            BS_22007 = Column(DECIMAL)
            BS_22010 = Column(DECIMAL)
            BS_22013 = Column(DECIMAL)
            BS_22019 = Column(DECIMAL)
            BS_22022 = Column(DECIMAL)
            BS_30005 = Column(DECIMAL)
            BS_30006 = Column(DECIMAL)
            BS_40000 = Column(DECIMAL)
            BS_1100101 = Column(DECIMAL)
            BS_11004 = Column(DECIMAL)
            BS_1100401 = Column(DECIMAL)
            BS_11007 = Column(DECIMAL)
            BS_11010 = Column(DECIMAL)
            BS_11013 = Column(DECIMAL)
            BS_11019 = Column(DECIMAL)
            BS_11022 = Column(DECIMAL)
            BS_11025 = Column(DECIMAL)
            BS_11028 = Column(DECIMAL)
            BS_11034 = Column(DECIMAL)
            BS_11037 = Column(DECIMAL)
            BS_11043 = Column(DECIMAL)
            BS_11046 = Column(DECIMAL)
            BS_11049 = Column(DECIMAL)
            BS_11052 = Column(DECIMAL)
            BS_11055 = Column(DECIMAL)
            BS_11058 = Column(DECIMAL)
            BS_11061 = Column(DECIMAL)
            BS_11064 = Column(DECIMAL)
            BS_1107301 = Column(DECIMAL)
            BS_11076 = Column(DECIMAL)
            BS_CASPEC = Column(DECIMAL)
            BS_12002 = Column(DECIMAL)
            BS_12004 = Column(DECIMAL)
            BS_12007 = Column(DECIMAL)
            BS_12010 = Column(DECIMAL)
            BS_1204601 = Column(DECIMAL)
            BS_12061 = Column(DECIMAL)
            BS_12067 = Column(DECIMAL)
            BS_NCASPEC = Column(DECIMAL)
            BS_ASPEC = Column(DECIMAL)
            BS_2100101 = Column(DECIMAL)
            BS_21004 = Column(DECIMAL)
            BS_21007 = Column(DECIMAL)
            BS_21010 = Column(DECIMAL)
            BS_21013 = Column(DECIMAL)
            BS_21016 = Column(DECIMAL)
            BS_21022 = Column(DECIMAL)
            BS_21025 = Column(DECIMAL)
            BS_21028 = Column(DECIMAL)
            BS_21031 = Column(DECIMAL)
            BS_21034 = Column(DECIMAL)
            BS_21037 = Column(DECIMAL)
            BS_21040 = Column(DECIMAL)
            BS_21043 = Column(DECIMAL)
            BS_21046 = Column(DECIMAL)
            BS_21049 = Column(DECIMAL)
            BS_21052 = Column(DECIMAL)
            BS_21055 = Column(DECIMAL)
            BS_21058 = Column(DECIMAL)
            BS_21061 = Column(DECIMAL)
            BS_21064 = Column(DECIMAL)
            BS_21067 = Column(DECIMAL)
            BS_CLSPEC = Column(DECIMAL)
            BS_22016 = Column(DECIMAL)
            BS_22025 = Column(DECIMAL)
            BS_NCLSPEC = Column(DECIMAL)
            BS_LSPEC = Column(DECIMAL)
            BS_31007 = Column(DECIMAL)
            BS_31022 = Column(DECIMAL)
            BS_31025 = Column(DECIMAL)
            BS_PCESPEC = Column(DECIMAL)
            BS_ESPEC = Column(DECIMAL)
            BS_LESPEC = Column(DECIMAL)
            SPEC_DES = Column(Text)
            INFO_PUB_DATE = Column(Date)
            BS_31037 = Column(DECIMAL)
            BS_11029 = Column(DECIMAL)
            BS_21068 = Column(DECIMAL)

        # 结果返回一个列表
        try:
            ret = session.query(BALA_SHORT).all()
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

#合并现金流量信息
    def FIN_CASH_SHORT(self):
        Base = declarative_base()
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
        # 创建DBSession类型:
        Session = sessionmaker(bind=engine)
        session = Session()
        # 定义CASH_SHORT对象:
        class CASH_SHORT(Base):
            # 表的名字:
            __tablename__ = 'FIN_CASH_SHORT'
            # 表的结构:
            COM_UNI_CODE = Column(DECIMAL, primary_key = True)
            END_DATE = Column(Date, primary_key = True)

            ISVALID = Column(DECIMAL)
            CREATETIME = Column(DateTime)
            UPDATETIME = Column(DateTime)
            CURY_TYPE_PAR = Column(DECIMAL)
            CURY_UNIT_PAR = Column(DECIMAL)
            CS_11001 = Column(DECIMAL)
            CS_11000 = Column(DECIMAL)
            CS_12000 = Column(DECIMAL)
            CS_10000 = Column(DECIMAL)
            CS_21000 = Column(DECIMAL)
            CS_22000 = Column(DECIMAL)
            CS_20000 = Column(DECIMAL)
            CS_31000 = Column(DECIMAL)
            CS_32000 = Column(DECIMAL)
            CS_30000 = Column(DECIMAL)
            CS_40001 = Column(DECIMAL)
            CS_40000 = Column(DECIMAL)
            CS_11004 = Column(DECIMAL)
            CS_11040 = Column(DECIMAL)
            CS_12001 = Column(DECIMAL)
            CS_12004 = Column(DECIMAL)
            CS_12007 = Column(DECIMAL)
            CS_12037 = Column(DECIMAL)
            CS_21001 = Column(DECIMAL)
            CS_21004 = Column(DECIMAL)
            CS_21007 = Column(DECIMAL)
            CS_21010 = Column(DECIMAL)
            CS_21013 = Column(DECIMAL)
            CS_22001 = Column(DECIMAL)
            CS_22004 = Column(DECIMAL)
            CS_22007 = Column(DECIMAL)
            CS_22013 = Column(DECIMAL)
            CS_31001 = Column(DECIMAL)
            CS_31004 = Column(DECIMAL)
            CS_31007 = Column(DECIMAL)
            CS_31010 = Column(DECIMAL)
            CS_32001 = Column(DECIMAL)
            CS_32004 = Column(DECIMAL)
            CS_32007 = Column(DECIMAL)
            CS_50001 = Column(DECIMAL)
            CS_50000 = Column(DECIMAL)
            CS_11007 = Column(DECIMAL)
            CS_11010 = Column(DECIMAL)
            CS_11013 = Column(DECIMAL)
            CS_11016 = Column(DECIMAL)
            CS_11019 = Column(DECIMAL)
            CS_11022 = Column(DECIMAL)
            CS_11025 = Column(DECIMAL)
            CS_11028 = Column(DECIMAL)
            CS_11031 = Column(DECIMAL)
            CS_11034 = Column(DECIMAL)
            CS_11037 = Column(DECIMAL)
            CS_OCISPEC = Column(DECIMAL)
            CS_12010 = Column(DECIMAL)
            CS_12013 = Column(DECIMAL)
            CS_12016 = Column(DECIMAL)
            CS_12019 = Column(DECIMAL)
            CS_12022 = Column(DECIMAL)
            CS_12025 = Column(DECIMAL)
            CS_12028 = Column(DECIMAL)
            CS_12031 = Column(DECIMAL)
            CS_12034 = Column(DECIMAL)
            CS_OCOSPEC = Column(DECIMAL)
            CS_ICISPEC = Column(DECIMAL)
            CS_22010 = Column(DECIMAL)
            CS_ICOSPEC = Column(DECIMAL)
            CS_3100101 = Column(DECIMAL)
            CS_FCISPEC = Column(DECIMAL)
            CS_3200401 = Column(DECIMAL)
            CS_FCOSPEC = Column(DECIMAL)
            CS_ICESPEC = Column(DECIMAL)
            SPEC_DES = Column(Text)
            INFO_PUB_DATE = Column(Date)


        # 结果返回一个列表
        try:
            ret = session.query(CASH_SHORT).all()
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

#公司合并利润信息
    def FIN_INCO_SHORT(self):
        Base = declarative_base()
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://mysql:mysql@47.94.1.2:3306/upchina')
        # 创建DBSession类型:
        Session = sessionmaker(bind=engine)
        session = Session()
        # 定义INCO_SHORT对象:
        class INCO_SHORT(Base):
            # 表的名字:
            __tablename__ = 'FIN_INCO_SHORT'
            # 表的结构:
            COM_UNI_CODE = Column(DECIMAL, primary_key = True)
            END_DATE = Column(Date, primary_key = True)

            ISVALID = Column(DECIMAL)
            CREATETIME = Column(DateTime)
            UPDATETIME = Column(DateTime)
            CURY_TYPE_PAR = Column(DECIMAL)
            CURY_UNIT_PAR = Column(DECIMAL)
            IS_10000 = Column(DECIMAL)
            IS_20000 = Column(DECIMAL)
            IS_20001 = Column(DECIMAL)
            IS_20002 = Column(DECIMAL)
            IS_20003 = Column(DECIMAL)
            IS_20004 = Column(DECIMAL)
            IS_30000 = Column(DECIMAL)
            IS_40000 = Column(DECIMAL)
            IS_50000 = Column(DECIMAL)
            IS_50001 = Column(DECIMAL)
            IS_10001 = Column(DECIMAL)
            IS_20005 = Column(DECIMAL)
            IS_20031 = Column(DECIMAL)
            IS_20049 = Column(DECIMAL)
            IS_21001 = Column(DECIMAL)
            IS_21007 = Column(DECIMAL)
            IS_30001 = Column(DECIMAL)
            IS_30004 = Column(DECIMAL)
            IS_40001 = Column(DECIMAL)
            IS_50004 = Column(DECIMAL)
            IS_60001 = Column(DECIMAL)
            IS_60004 = Column(DECIMAL)
            IS_70000 = Column(DECIMAL)
            IS_80000 = Column(DECIMAL)
            IS_80001 = Column(DECIMAL)
            IS_80004 = Column(DECIMAL)
            IS_10004 = Column(DECIMAL)
            IS_10007 = Column(DECIMAL)
            IS_1000701 = Column(DECIMAL)
            IS_1000702 = Column(DECIMAL)
            IS_10010 = Column(DECIMAL)
            IS_1001001 = Column(DECIMAL)
            IS_1001002 = Column(DECIMAL)
            IS_1001003 = Column(DECIMAL)
            IS_1001004 = Column(DECIMAL)
            IS_1001005 = Column(DECIMAL)
            IS_10013 = Column(DECIMAL)
            IS_10016 = Column(DECIMAL)
            IS_1001601 = Column(DECIMAL)
            IS_10019 = Column(DECIMAL)
            IS_10022 = Column(DECIMAL)
            IS_10025 = Column(DECIMAL)
            IS_OISPEC = Column(DECIMAL)
            IS_20006 = Column(DECIMAL)
            IS_20007 = Column(DECIMAL)
            IS_20010 = Column(DECIMAL)
            IS_20013 = Column(DECIMAL)
            IS_20016 = Column(DECIMAL)
            IS_20019 = Column(DECIMAL)
            IS_20022 = Column(DECIMAL)
            IS_20025 = Column(DECIMAL)
            IS_20028 = Column(DECIMAL)
            IS_20043 = Column(DECIMAL)
            IS_20046 = Column(DECIMAL)
            IS_20052 = Column(DECIMAL)
            IS_OCSPEC = Column(DECIMAL)
            IS_2100401 = Column(DECIMAL)
            IS_NOISPEC = Column(DECIMAL)
            IS_IOESPEC = Column(DECIMAL)
            IS_3000401 = Column(DECIMAL)
            IS_IESPEC = Column(DECIMAL)
            IS_NPSPEC = Column(DECIMAL)
            IS_71000 = Column(DECIMAL)
            IS_71001 = Column(DECIMAL)
            IS_7100101 = Column(DECIMAL)
            IS_7100102 = Column(DECIMAL)
            IS_7100103 = Column(DECIMAL)
            IS_71002 = Column(DECIMAL)
            IS_7100201 = Column(DECIMAL)
            IS_7100202 = Column(DECIMAL)
            IS_7100203 = Column(DECIMAL)
            IS_7100204 = Column(DECIMAL)
            IS_7100205 = Column(DECIMAL)
            IS_7100206 = Column(DECIMAL)
            IS_72000 = Column(DECIMAL)
            SPEC_DES = Column(Text)
            INFO_PUB_DATE = Column(Date)
            IS_20053 = Column(DECIMAL)
            IS_2000301 = Column(DECIMAL)
            IS_2000302 = Column(DECIMAL)


        # 结果返回一个列表
        try:
            ret = session.query(INCO_SHORT).all()
            msgs = []
            for msg in ret:
                msgs.append(msg)
            json_data = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
            return json_data
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

if __name__ == "__main__":
    data_set = Data_Set()
    # 股票基本信息
    stk_basic_info = data_set.STK_BASIC_INFO()
    print(stk_basic_info)

    # 公司主营业务构成按产品分布信息
    # com_inc_info_pro = data_set.COM_INC_INFO_PRO()
    # print(com_inc_info_pro[0])
    # print(com_inc_info_pro[0].COM_UNI_CODE)

    #行业代码信息
    # pub_indu_code = data_set.PUB_INDU_CODE()
    # print(pub_indu_code[0])
    # print(pub_indu_code[0].INDU_UNI_CODE)

    #公司最新从属行业信息
    # pub_com_indu_code = data_set.PUB_COM_INDU_RELA()
    # print(pub_com_indu_code[0])
    # print(pub_com_indu_code[0].COM_UNI_CODE)

    #合并资产负债信息
    # fin_bala_short = data_set.FIN_BALA_SHORT()
    # print(fin_bala_short[0])
    # print(fin_bala_short[0].UPDATETIME)

    #合并现金流量信息
    # fin_cash_short = data_set.FIN_CASH_SHORT()
    # print(fin_cash_short[0])
    # print(fin_cash_short[0].UPDATETIME)

    #合并利润信息
    # fin_inco_short = data_set.FIN_INCO_SHORT()
    # print(fin_inco_short[0])
    # print(fin_inco_short[0].UPDATETIME)