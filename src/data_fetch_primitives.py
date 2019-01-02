import json
import datetime
import decimal
import pymysql
from sqlalchemy.exc import SQLAlchemyError


# 重写构造json类，遇到date.time,date and  Decimal特殊处理
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, decimal.Decimal):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)

class DataSetPrimitives():
    def data_set_primitices(self, data_sql):
        db = pymysql.connect(db="tr", user="root", password="root", host="127.0.0.1", port=3306)
        cursor = db.cursor()
        try:
            cursor.execute(data_sql)
            data = cursor.fetchall()
        except SQLAlchemyError as e:
            print(e)
        finally:
            cursor.close()
            db.close()
        # 得到查询结果字段名
        fields = cursor.description
        colum_list = []
        for i in fields:
            colum_list.append(i[0])
        # json转换
        colum_num = colum_list.__len__()
        jsondata = []
        for row in data:
            num = 0
            result = {}
            while num < colum_num:
                result[colum_list[num]] = row[num]
                num = num + 1
            jsondata.append(result)
        json_data = json.dumps(jsondata, ensure_ascii=False, cls=DateEncoder)
        return json_data

class SetRawData():
    def set_raw_data(self, data_sql):
        db = pymysql.connect(db="upchina", user="mysql", password="mysql", host="47.94.1.2", port=3306)
        cursor = db.cursor()
        try:
            cursor.execute(data_sql)
            raw_data = cursor.fetchall()
        except SQLAlchemyError as e:
            print(e)
        finally:
            cursor.close()
            db.close()

        fields = cursor.description
        colum_list = []
        for i in fields:
            colum_list.append(i[0])
        # json转换
        jsondata = []
        for row in raw_data:
            jsondata.append(row)
        json_data = json.dumps(jsondata, ensure_ascii=False, cls=DateEncoder)
        return json_data

if __name__ == "__main__":
    # data_set_primitives = DataSetPrimitives()
    # json_data = data_set_primitives.data_set_primitices('select * from m_worker')
    # print(json_data)

    set_raw_data = SetRawData()
    raw_data = set_raw_data.set_raw_data('select * from PUB_COM_INDU_CHAN limit 3')
    print(raw_data)