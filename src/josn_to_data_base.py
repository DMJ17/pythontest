import os
import os.path
import pandas
import math
import pymysql
import json
import hashlib
from sqlalchemy.exc import SQLAlchemyError
import codecs

# 资产负债提取
def balance(self, fin_basic_gen, prospectusMD5):
    data_bala = []
    data_bala.append(fin_basic_gen['货币单位'])
    data_bala.append(fin_basic_gen['报表日期'])
    for key_bala, value_bala in fin_basic_gen['合并资产负债表'].items():
        for key, value in value_bala.items():
            data_bala.append(value)

    data_bala.insert(0, prospectusMD5)
    data_bala.insert(0, None)
    del data_bala[66]
    data_sql = tuple(data_bala)
    return data_sql

# 现金流提取
def cash_flow(self, fin_basic_gen, prospectusMD5):
        data_cash = []
        unit = fin_basic_gen['货币单位']
        roport_data = fin_basic_gen['报表日期']
        if pandas.isnull(unit):
            unit = None
        if pandas.isnull(roport_data):
            roport_data = None
        data_cash.append(unit)
        data_cash.append(roport_data)
        for key_cash, value_cash in fin_basic_gen['合并现金流量表'].items():
            if pandas.isnull(value_cash):
                value_cash = None
            data_cash.append(value_cash)

        data_cash.insert(0, prospectusMD5)
        data_cash.insert(0, None)
        data_sql = tuple(data_cash)
        return data_sql

# 利润表提取
def income(self, fin_basic_gen):
    data = []
    unit = fin_basic_gen['货币单位']
    roport_data = fin_basic_gen['报表日期']
    if pandas.isnull(unit):
        unit = None
    if pandas.isnull(roport_data):
        roport_data = None
    data.append(unit)
    data.append(roport_data)
    for key_fin, value_fin in fin_basic_gen['合并利润表'].items():
        if isinstance(value_fin, dict):
            for key, value in value_fin.items():
                data.append(value)
        else:
            data.append(value_fin)
        data_sql = tuple(data)
    return data_sql
    # print(data_sql)

# 主要财务指标表
def financial_indicators(self, fin_basic_gen):
    data = []
    data.append(fin_basic_gen['货币单位'])
    data.append(fin_basic_gen['报表日期'])

    for key_bala, value_fin in fin_basic_gen['基本财务指标'].items():
            data.append(value_fin)
    data.insert(0, '爱玛科技集团股份有限公司首次公开发行股票招股说明书（申报稿2018年6月22日报送）.json')
    data.insert(0, 1)
    data.insert(0, None)
    data_sql = tuple(data)
    return data_sql

# md5生成
def md5_passwd(file_name):
    md = hashlib.md5()  # 构造一个md5对象
    md.update(file_name.encode())
    res = md.hexdigest()
    return res

# sql生产时values中的字符串生成
def make_fromat(num):
    for i in range(num):
        if i == 0:
            format = '%s'
        elif i == num:
            format = format + ',%s'
        else:
            format = format + ',%s'
    return format

# 获取字段数
def get_field_num(cursor, table_name):
    sql = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = "%s"' % table_name
    cursor.execute(sql)
    field = cursor.fetchall()
    num = field.__len__()
    return num

# 数据获取并存入数据库
class Json_to_Data_Base():
    def json_to_data_base(self):
        db = pymysql.connect(db="ipo_data_from_table", user="root", password="root", host="127.0.0.1", port=3306)
        cursor = db.cursor()
        # 数据库各表格字段数转变为%s的格式
        # fromat_prospectus = make_fromat(get_field_num(cursor, 'prospectus'))
        # sql_prospectus = 'insert into prospectus values(%s)' % fromat_prospectus

        # fromat_balance = make_fromat(get_field_num(cursor, 'balance'))
        # sql_balance = 'insert into balance values(%s)' % fromat_balance

        # fromat_cash_flow = make_fromat(get_field_num(cursor, 'cash_flow'))
        # sql_cash_flow = 'insert into cash_flow values(%s)' % fromat_cash_flow

        fromat_income = make_fromat(get_field_num(cursor, 'income'))
        sql_cash_flow = 'insert into income values(%s)' % fromat_income

        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))

        # fromat_paraphrase = make_fromat(get_field_num(cursor, 'paraphrase'))
        # sql_paraphrase = 'insert into paraphrase values(%s)' % fromat_paraphrase

        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))
        # fromat1 = make_fromat(get_field_num(cursor, 'prospectus'))

        # 获取所有文件名，生成公司名对应的md5，一次生成使用，除非公司名做出改变
        # path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\json_v2\json_final'
        # files = os.listdir(path)
        # for file in files :
        #     file_name = os.path.splitext(file)
        #     file_name = str(file_name[0])
        #     res = md5_passwd(file_name)
        #     sql = 'insert into prospectus values(%s)' % fromat
        #     cursor.execute(sql ,(file_name, res))

        # 从数据库中获取文件名和MD5数据
        sql_get_name = 'select *  from prospectus'
        cursor.execute(sql_get_name)
        file_names = cursor.fetchall()
        for file_name in file_names:
            # field,prospectus文件名和MD5码
            field = file_name[0]
            prospectusMD5 = file_name[1]
            file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\json_v2\json_final\%s.json' % field
            contents = codecs.open(file_path, 'r', encoding='utf-8')
            for content in contents:
                dic_data = json.loads(content)

            # 资产负债________________json中key和数据字典中不一致
            # for fin_basic_gen in dic_data['财务基本情况及财务指标']:
            #     data_bala = balance(self, fin_basic_gen, prospectusMD5)
            #     # print(data_bala)

            # 现金流
            # if dic_data['财务基本情况及财务指标'] != None:
            #     for fin_basic_gen in dic_data['财务基本情况及财务指标']:
            #         # print(field)
            #         if isinstance(fin_basic_gen['合并现金流量表'], dict):
            #             data_cash_flow = cash_flow(self, fin_basic_gen, prospectusMD5)
            #             print(data_cash_flow.__len__())
            #             print(data_cash_flow)
            #             try:
            #                 cursor.execute(sql_cash_flow ,data_cash_flow)
            #             except SQLAlchemyError as e:
            #                 print(e)

            # 利润表
            if dic_data['财务基本情况及财务指标'] != None:
                for fin_basic_gen in dic_data['财务基本情况及财务指标']:
                    if isinstance(fin_basic_gen['合并利润表'], dict):
                        data_income = income(self, fin_basic_gen)
                        print(file_name)
                        print(data_income)

            #
            # # 主要财务指标
            # for fin_basic_gen in dic_data['财务基本情况及财务指标']:
            #     data_fin_ind = financial_indicators(self, fin_basic_gen)
            #     # print(data_fin_ind)
            #
            # # 控股股东和实际控制人情况
            # for key,value in dic_data['控股股东简要情况'].items():
            #     data = []
            #     data.append(key)
            #     for infor in value:
            #         for key,value in infor.items():
            #             data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)

            # # 释义
            # for key,value in dic_data['释义'].items():
            #     data = []
            #     data.append(prospectusMD5)
            #     data.append(key)
            #     data.append(value)
            #     data.insert(0, None)
            #     data_sql = tuple(data)
            #     print(data_sql)
            #     try:
            #         cursor.execute(sql_paraphrase ,data_sql)
            #     except SQLAlchemyError as e:
            #         print(e)

            # # 人员基本情况
            # for person_infor in dic_data['董事基本情况']:
            #     data = []
            #     for key,value in person_infor.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            # for person_infor in dic_data['监事基本情况']:
            #     data = []
            #     for key,value in person_infor.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            # for person_infor in dic_data['高管基本情况']:
            #     data = []
            #     for key, value in person_infor.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            # for person_infor in dic_data['核心技术人员基本情况']:
            #     data = []
            #     for key, value in person_infor.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            #
            # # 重大诉讼事项
            # for major_lawsuit in dic_data['重大诉讼事项']:
            #     data = []
            #     for key, value in major_lawsuit.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            #
            # # 资金募集与运用
            # for major_lawsuit in dic_data['募集资金与运用']:
            #     data = []
            #     for key, value in major_lawsuit.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            #
            # # 专利
            # data = []
            # for key, value in dic_data['发行人基本情况'].items():
            #     data.append(value)
            #     data_sql = tuple(data)
            # # print(data_sql)
            #
            # # 主要客户
            # for major_client in dic_data['主要客户']:
            #     data = []
            #     for key, value in major_client.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            #
            # # 主要供应商
            # for major_supplier in dic_data['主要供应商']:
            #     data = []
            #     for key, value in major_supplier.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            #
            # # 主要供应商
            # for major_contract in dic_data['重大合同']:
            #     data = []
            #     for key, value in major_contract.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            #
            # # 发行人所处行业
            # for issuer_profession in dic_data['发行人所处行业']:
            #     data = []
            #     for key, value in issuer_profession.items():
            #         data.append(value)
            #     data_sql = tuple(data)
            #     # print(data_sql)
            #
            # # 盈利能力
            # for issuer_profession in dic_data['盈利能力']:
            #     import_time = issuer_profession['报表日期']
            #     for key, value in issuer_profession['营业收入分析'].items():
            #         temp  = key
            #         for each_one in value:
            #             data = []
            #             data.append(import_time)
            #             data.append('营业收入分析')
            #             data.append(temp)
            #             for key, value in each_one.items():
            #                 data.append(value)
            #             data_sql = tuple(data)
            #             # print(data_sql)
            #     for key, value in issuer_profession['营业成本分析'].items():
            #         temp = key
            #         for each_one in value:
            #             data = []
            #             data.append(import_time)
            #             data.append('营业成本分析')
            #             data.append(temp)
            #             for key, value in each_one.items():
            #                 data.append(value)
            #             data_sql = tuple(data)
            #             # print(data_sql)


if __name__ == '__main__':
    temp = Json_to_Data_Base()
    temp.json_to_data_base()