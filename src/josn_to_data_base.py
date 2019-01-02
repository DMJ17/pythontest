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

# 合并现金流提取
def cash_flow(self, fin_basic_gen, prospectusMD5, file_name):
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
        pkey = str(file_name) + str(roport_data)
        pkey_md5 = md5_passwd(pkey)
        data_cash.insert(0, prospectusMD5)
        data_cash.insert(0, pkey_md5)
        data_sql = tuple(data_cash)
        return data_sql

# 利润表提取
def income(self, fin_basic_gen, prospectusMD5):
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
                if pandas.isnull(value):
                    value = None
                data.append(value)
        else:
            data.append(value_fin)
    data.insert(0, prospectusMD5)
    data.insert(0, None)
    data_sql = tuple(data)
    return data_sql
    # print(data_sql)

# 主要财务指标表
def financial_indicators(self, fin_basic_gen, prospectusMD5):
    data = []
    unit = fin_basic_gen['货币单位']
    roport_data = fin_basic_gen['报表日期']
    if pandas.isnull(unit):
        unit = None
    if pandas.isnull(roport_data):
        roport_data = None
    data.append(unit)
    data.append(roport_data)

    for key_bala, value_fin in fin_basic_gen['基本财务指标'].items():
        if pandas.isnull(value_fin):
            value_fin = None
        data.append(value_fin)
    data.insert(0, prospectusMD5)
    data.insert(0, None)
    del data[11]
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
    print(num)
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
    sql = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = "%s" and table_schema = "ipo_data_v2"' % table_name
    cursor.execute(sql)
    field = cursor.fetchall()
    num = field.__len__()
    return num


# 数据获取并存入数据库
class Json_to_Data_Base():
    def json_to_data_base(self):
        db = pymysql.connect(db="ipo_data_v2", user="root", password="root", host="127.0.0.1", port=3306)
        cursor = db.cursor()
        # 数据库各表格字段数转变为%s的格式
        fromat_prospectus = make_fromat(get_field_num(cursor, 'prospectus'))
        sql_prospectus = 'insert into prospectus values(%s)' % fromat_prospectus

        fromat_balance = make_fromat(get_field_num(cursor, 'balance'))
        sql_balance = 'insert into balance values(%s)' % fromat_balance

        fromat_cash_flow = make_fromat(get_field_num(cursor, 'cash_flow'))
        sql_cash_flow = 'insert into cash_flow values(%s)' % fromat_cash_flow

        fromat_income = make_fromat(get_field_num(cursor, 'income'))
        sql_income = 'insert into income values(%s)' % fromat_income

        fromat_main_financial_indicators = make_fromat(get_field_num(cursor, 'main_financial_indicators'))
        sql_main_financial_indicators = 'insert into main_financial_indicators values(%s)' % fromat_main_financial_indicators

        fromat_controller_information = make_fromat(get_field_num(cursor, 'controller_information'))
        sql_controller_information = 'insert into controller_information values(%s)' % fromat_controller_information

        fromat_major_lawsuit = make_fromat(get_field_num(cursor, 'major_lawsuit'))
        sql_major_lawsuit = 'insert into major_lawsuit values(%s)' % fromat_major_lawsuit

        fromat_fund_raising = make_fromat(get_field_num(cursor, 'fund_raising'))
        sql_fund_raising = 'insert into fund_raising values(%s)' % fromat_fund_raising

        fromat_patent = make_fromat(get_field_num(cursor, 'patent'))
        sql_patent = 'insert into patent values(%s)' % fromat_patent

        fromat_issuer_information = make_fromat(get_field_num(cursor, 'issuer_information'))
        sql_issuer_information = 'insert into issuer_information values(%s)' % fromat_issuer_information

        fromat_major_client = make_fromat(get_field_num(cursor, 'major_client'))
        sql_major_client = 'insert into major_client values(%s)' % fromat_major_client

        fromat_major_supplier = make_fromat(get_field_num(cursor, 'major_supplier'))
        sql_major_supplier = 'insert into major_supplier values(%s)' % fromat_major_supplier

        fromat_major_contract = make_fromat(get_field_num(cursor, 'major_contract'))
        sql_major_contract = 'insert into major_contract values(%s)' % fromat_major_contract

        fromat_issuer_profession = make_fromat(get_field_num(cursor, 'issuer_profession'))
        sql_issuer_profession = 'insert into issuer_profession values(%s)' % fromat_issuer_profession

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
        #     print(file_name)
        #     print(res)
        #     sql = 'insert into file values(%s, %s)'
        #     cursor.execute(sql ,(res, file_name))

        # 从数据库中获取文件名和MD5数据
        sql_get_name = 'select *  from file'
        cursor.execute(sql_get_name)
        file_names = cursor.fetchall()
        for file in file_names:
            # field,prospectus文件名和MD5码
            file_name = file[1]
            prospectusMD5 = file[0]
            file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\json_v2\json_final\%s.json' %  file_name
            contents = codecs.open(file_path, 'r', encoding='utf-8')
            for content in contents:
                dic_data = json.loads(content)

            # 资产负债___________________________json中key和数据字典中不一致
            # for fin_basic_gen in dic_data['财务基本情况及财务指标']:
            #     data_bala = balance(self, fin_basic_gen, prospectusMD5)
            #     # print(data_bala)

            # 现金流
            if dic_data['财务基本情况及财务指标'] != None:
                for fin_basic_gen in dic_data['财务基本情况及财务指标']:
                    if isinstance(fin_basic_gen['合并现金流量表'], dict):
                        data_cash_flow = cash_flow(self, fin_basic_gen, prospectusMD5, file_name)
                        print(data_cash_flow.__len__())
                        print(file_name)
                        try:
                            cursor.execute(sql_cash_flow ,data_cash_flow)
                        except SQLAlchemyError as e:
                            print(e)


            # 利润表
            # if dic_data['财务基本情况及财务指标'] != None:
            #     for fin_basic_gen in dic_data['财务基本情况及财务指标']:
            #         if isinstance(fin_basic_gen['合并利润表'], dict):
            #             data_income = income(self, fin_basic_gen, prospectusMD5)
            #             print(file_name)
                        # if data_income.__len__() == 44:
                            # try:
                            #     cursor.execute(sql_income ,data_income)
                            # except SQLAlchemyError as e:
                            #     print(e)


            # 主要财务指标
            # if dic_data['财务基本情况及财务指标'] != None:
            #     for fin_basic_gen in dic_data['财务基本情况及财务指标']:
            #         if isinstance(fin_basic_gen['基本财务指标'], dict):
            #             data_fin_ind = financial_indicators(self, fin_basic_gen, prospectusMD5)
            #             # print(data_fin_ind)
            #             # print(data_fin_ind.__len__())
            #             if data_fin_ind.__len__() == 17:
            #                 print(file_name)
            #                 try:
            #                     cursor.execute(sql_main_financial_indicators ,data_fin_ind)
            #                 except SQLAlchemyError as e:
            #                     print(e)



            # 控股股东和实际控制人情况___________________________字段名対映问题
            # if dic_data['控股股东简要情况'] != None:
            #     if isinstance(dic_data['控股股东简要情况'], dict):
            #         for key,value in dic_data['控股股东简要情况'].items():
            #             data = []
            #             data.append(None)
            #             data.append(prospectusMD5)
            #             data.append(key)
            #             for infor in value:
            #                 for key,value in infor.items():
            #                     if pandas.isnull(value):
            #                         value = None
            #                     data.append(value)
            #             data_sql = tuple(data)
            #             print(data_sql)
                    # print(data_sql) sql_controller_information

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
            # if dic_data['控股股东简要情况'] != None:
            #     for person_infor in dic_data['董事基本情况']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         data.append('董事基本情况')
            #         if isinstance(person_infor, dict):
            #             for key,value in person_infor.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data_sql = tuple(data)
            #         # print(data_sql.__len__())
            #         # print(data_sql)
            #         try:
            #             cursor.execute('insert into person_information(id, prospectusMD5, information_type, name, nationality, overseas_residency,'
            #                            ' gender, date_of_birth, education,job_title, current_title, start_date, end_date) '
            #                            'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)

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

            # 重大诉讼事项
            # if dic_data['重大诉讼事项'] != None:
            #     for major_lawsuit in dic_data['重大诉讼事项']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         if isinstance(major_lawsuit, dict):
            #             for key, value in major_lawsuit.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data.append(None)
            #             data_sql = tuple(data)
            #             print(data_sql.__len__())
            #             print(file_name)
            #         try:
            #             cursor.execute(sql_major_lawsuit ,data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)


            # 资金募集与运用
            # if dic_data['募集资金与运用'] != None:
            #     for fund_raising in dic_data['募集资金与运用']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         if isinstance(fund_raising, dict):
            #             for key, value in fund_raising.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data_sql = tuple(data)
            #         print(data_sql)
            #         print(data_sql.__len__())
            #         try:
            #             cursor.execute(sql_fund_raising ,data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)

            # 专利
            # if dic_data['专利'] != None:
            #     for patent in dic_data['专利']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         if isinstance(patent, dict):
            #             for key, value in patent.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data_sql = tuple(data)
            #         print(data_sql)
            #         print(data_sql.__len__())
            #         try:
            #             cursor.execute(sql_patent ,data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)


            # 发行人基本情况_________________________________数据格式异常
            # if isinstance(dic_data, dict):
            #     data = []
            #     data.append(None)
            #     data.append(prospectusMD5)
            #     for key, value in dic_data['发行人基本情况'].items():
            #         if pandas.isnull(value):
            #             value = None
            #         data.append(value)
            #         data_sql = tuple(data)
            #     print(data_sql.__len__())
            #     print(data_sql)
            #     if data_sql.__len__() == 13:
            #         try:
            #             print(file_name)
            #             cursor.execute(sql_issuer_information ,data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)

            # 主要客户
            # if dic_data['主要客户'] != None:
            #     for major_client in dic_data['主要客户']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         if isinstance(major_client, dict):
            #             for key, value in major_client.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data.insert(3, '万元')
            #             data_sql = tuple(data)
            #             print(data_sql.__len__())
            #             print(data_sql)
            #         try:
            #             cursor.execute(sql_major_client, data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)
            #         print(data_sql)

            # 主要供应商
            # if dic_data['主要供应商'] != None:
            #     for major_supplier in dic_data['主要供应商']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         if isinstance(major_supplier, dict):
            #             for key, value in major_supplier.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data.insert(3, '万元')
            #             data_sql = tuple(data)
            #             print(data_sql.__len__())
            #             print(data_sql)
            #         try:
            #             cursor.execute(sql_major_supplier, data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)
            #         print(data_sql)

            # 重大合同
            # if dic_data['重大合同'] != None:
            #     for major_contract in dic_data['重大合同']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         if isinstance(major_contract, dict):
            #             for key, value in major_contract.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data_sql = tuple(data)
            #             print(data_sql.__len__())
            #             print(data_sql)
            #             print(file_name)
            #         try:
            #             cursor.execute(sql_major_contract, data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)
            #         print(data_sql)

            # 发行人所处行业
            # if dic_data['发行人所处行业'] != None:
            #     for issuer_profession in dic_data['发行人所处行业']:
            #         data = []
            #         data.append(None)
            #         data.append(prospectusMD5)
            #         if isinstance(issuer_profession, dict):
            #             for key, value in issuer_profession.items():
            #                 if pandas.isnull(value):
            #                     value = None
            #                 data.append(value)
            #             data_sql = tuple(data)
            #             print(data_sql.__len__())
            #             print(data_sql)
            #             print(file_name)
            #         try:
            #             cursor.execute(sql_issuer_profession, data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)
            #         print(data_sql)

            # 盈利能力____________________________________________
            # for issuer_profession in dic_data['盈利能力']:
            #     import_time = issuer_profession['报表日期']
            #     for key, value in issuer_profession['营业收入分析'].items():
            #         temp  = key
            #         for each_one in value:
            #             data = []
            #             data.append(None)
            #             data.append(prospectusMD5)
            #             data.append('营业收入分析')
            #             data.append(temp)
            #             data.append(import_time)
            #
            #             for key, value in each_one.items():
            #                 data.append(value)
            #             data_sql = tuple(data)
            #             print(data.__len__())
            #             print(data_sql)
            #         try:
            #             cursor.execute('insert into profitability(id, prospectusMD5, business_type, composition_type, report_date, currency_unit, product_tpye, amount, proportion, movement)'
            #                            'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)

            # for issuer_profession in dic_data['盈利能力']:
            #     import_time = issuer_profession['报表日期']
            #     for key, value in issuer_profession['营业成本分析'].items():
            #         temp = key
            #         for each_one in value:
            #             data = []
            #             data.append(None)
            #             data.append(prospectusMD5)
            #             data.append('营业成本分析')
            #             data.append(temp)
            #             data.append(import_time)
            #
            #             for key, value in each_one.items():
            #                 data.append(value)
            #             data_sql = tuple(data)
            #             print(data.__len__())
            #             print(data_sql)
            #         try:
            #             cursor.execute(
            #                 'insert into profitability(id, prospectusMD5, business_type, composition_type, report_date, currency_unit, product_tpye, amount, proportion, movement)'
            #                 'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data_sql)
            #         except SQLAlchemyError as e:
            #             print(e)


if __name__ == '__main__':
    temp = Json_to_Data_Base()
    temp.json_to_data_base()