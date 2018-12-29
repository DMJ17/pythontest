import pymysql
import json
import codecs
import os
from src.chanae_ipo_data import InsertData
error_file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\json_v2\error'
# data_file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\json_v3\json_final'
data_file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\\time_change'

# 记录数据库错误信息到,TXT文件中，每重新执行一次刷新一次
def data_error_log():
    error_file_schames = (
        '董事基本情况',
        '重大诉讼事项',
        '募集资金与运用',
        '专利',
        '发行人相关信息',
        '主要客户',
        '主要供应商',
        '重大合同',
        '发行人所处行业',
        '盈利能力',
        '资产负债表',
        '现金流量表',
        '利润表',
        '主要财务指标表',
        '监事基本情况',
        '高管基本情况',
        '核心技术人员基本情况'
    )
    for error_file_schame in error_file_schames:
        error_file_route = os.path.join(error_file_path, error_file_schame + '.txt')
        fp = open(error_file_route, "w", encoding='utf-8')
        fp.close()

# 数据获取并存入数据库
class Json_to_Data_Base():
    def json_to_data_base(self):
        # 记录数据库错误信息到,TXT文件中，每重新执行一次刷新一次
        data_error_log()
        # db = pymysql.connect(db="ipo_data_from_json", user="root", password="123456", host="192.168.5.216", port=3306)
        db = pymysql.connect(db="ipo_data_v2", user="root", password="root", host="127.0.0.1", port=3306)
        cursor = db.cursor()
        insert_data = InsertData()
        # 将公司字典写入数据库
        # insert_data.file(cursor)
        # db.commit()

        # 从数据库中获取文件名和MD5数据
        sql_get_name = 'select *  from file'
        cursor.execute(sql_get_name)
        file_names = cursor.fetchall()
        for file in file_names:
            # field,prospectus为文件名和MD5码
            file_name = file[1]
            prospectusMD5 = file[0]
            # file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\json_v3\json_final\%s.json' %  file_name
            data_file_route = os.path.join(data_file_path, file_name + '.json')
            contents = codecs.open(data_file_route, 'r', encoding='utf-8')
            for content in contents:
                dic_data = json.loads(content)

            # 董事
            insert_data.director_information(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 监事
            insert_data.supervisor_information(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 高管
            insert_data.management_information(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 核心技术人员
            insert_data.core_technician_info(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 重大诉讼————json中无单位
            insert_data.major_lawsuit(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 募集资金与运用
            insert_data.fund_raising(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 专利
            insert_data.patent(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 发行人基本情况
            insert_data.issuer_information(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 主要客户————json中无单位
            insert_data.major_client(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 主要供应商————json中无单位
            insert_data.major_supplier(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 重大合同
            insert_data.major_contract(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 发行人所处行业
            insert_data.issuer_profession(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 盈利能力
            insert_data.profitability(file_name, prospectusMD5, cursor, dic_data)
            # db.commit()
            # 资产负债表
            insert_data.balance(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 现金流量表
            insert_data.cash_flow(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 利润表_缺项
            insert_data.income(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 主要财务指标表————json中多key_总资产周转率(次/年)
            insert_data.main_financial_indicators(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 实际控制人情况
            insert_data.actual_controller_info(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 释义
            insert_data.paraphrase(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
            # 控股股东情况
            insert_data.controlling_shareholder_info(file_name, prospectusMD5, cursor, dic_data)
            db.commit()
        cursor.close()
        db.close()

if __name__ == '__main__':
    temp = Json_to_Data_Base()
    temp.json_to_data_base()