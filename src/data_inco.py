import pymysql
import json
import re
import xlrd
from xlrd import xldate_as_tuple
import datetime
import decimal
from sqlalchemy.exc import SQLAlchemyError
'''
实现对表格和数据库财务数据提取
'''
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

# 公用方法——针对表格中的合并单元格取值
def get_merged_cells(sheet):
    return sheet.merged_cells
def get_merged_cells_value(sheet, row_index, col_index):
    merged = get_merged_cells(sheet)
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and row_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                return cell_value
            break
    return None

# 将表格中数据转为数据字典
def to_dic(self, data, temp, begin, end):
    if end != -1:
        dicdata = {}
        for i in range(begin, end):
            if data[i] == '无' or data[i] == '-' or data[i] == '':
                data[i] = None
                dicdata[temp[i]] = None
            else:
                dicdata[temp[i]] = data[i]
        return dicdata
    else:
        if data[begin] == '无' or data[begin] == '-' or data[begin] == '':
            return None
        else:
            return data[begin]

class TableData():
    def data_financial_situation(self):
        # 获取表格中的数据
        ExcelFile = xlrd.open_workbook(r'C:\Users\DMJ\Desktop\工作日常记录\树磊哥\提取元素表-财务数据.xlsx')
        sheet_name = ExcelFile.sheet_names()
        num = sheet_name.__len__()
        # 循环所有表格
        # print(sheet_name)
        for file_num in range(1):
            sheet = ExcelFile.sheet_by_name(sheet_name[file_num])
            # print(sheet.name,sheet.nrows,sheet.ncols)
            # 读取表格某一列的数据
            rows_num = sheet.nrows
            cols_num = sheet.ncols
            jsondata = []
            for column in range(4, cols_num):
                data = sheet.col_values(column)
                # print(column)
                # 读取.xls文件中日期进行格式转换
                if sheet.cell(1,column).ctype == 3:
                    time = xldate_as_tuple(sheet.cell(1, column).value, 0)
                    value = datetime.datetime(*time)
                    date = value.strftime('%Y-%m-%d')
                    data[1] = date
                    # print(data[1])
                # print(data)

                # 合并单元格取值
                temp = []
                for r in range(rows_num):
                    entity_dict = {}
                    for c in range(cols_num):
                        cell_value = sheet.row_values(r)[c]
                        if (cell_value is None or cell_value == ''):
                            cell_value = (get_merged_cells_value(sheet, r, c))
                        the_key = 'column' + str(c + 1)
                        entity_dict[the_key] = cell_value
                    temp.append(entity_dict['column4'])
                print(temp)
                if data[1].strip() != None:
                    # 营业总收入字典
                    list_value1 = to_dic(self, data, temp, 3, 21)
                    # 营业总成本字典
                    list_value2 = to_dic(self, data, temp, 21, 40)
                    # 营业利润字典
                    list_value3 = to_dic(self, data, temp, 40, -1)
                    # 营业利润字典
                    list_value4 = to_dic(self, data, temp, 41, 63)
                    # 每股收益字典
                    list_value5 = to_dic(self, data, temp, 63, 71)
                    # 其他综合收益	转换
                    list_value9 = to_dic(self, data, temp, 71, -1)
                    # 综合收益总额
                    list_value7 = to_dic(self, data, temp, 72, -1)
                    # 归属于母公司所有者的综合收益总额
                    list_value8 = to_dic(self, data, temp, 83, -1)
                    # 归属于少数股东的综合收益总额
                    list_value8 = to_dic(self, data, temp, 83, -1)

                    dicdata = {}
                    dicdata["财务基本情况及财务指标"] = [{"货币单位": data[2],"报表日期": data[1], "合并资产负债表": {"流动资产": list_value1, "非流动资产": list_value2, "资产总计": list_value3, "流动负债":
                        list_value4,"非流动负债": list_value5, "负债合计": list_value9, "所有者权益（或股东权益）": list_value7, "负债和所有者权益总计": list_value8,
                        }}]
                    jsondata.append(dicdata)
            json_data = json.dumps(jsondata, ensure_ascii=False, cls=DateEncoder)
            #
            # # fp = open(r'D:\python\project\test\docs\资产负债json\%s.json' % sheet.name, "w", encoding='utf-8')
            # # fp.write(json_data)
            # db = pymysql.connect(db="ipo_data", user="root", password="123456", host="172.20.20.100", port=3306)
            # cursor = db.cursor()
            # try:
            #     cursor.execute('insert into fin_sitat_data(id, cmp_name, financial_situation_data, mark) values(null, %s, %s, 0)',(sheet.name,json_data))
            #     db.commit()
            # except SQLAlchemyError as e:
            #     print(e)
            # print(json_data)

if __name__ == '__main__':
    data_finance = TableData()
    data_finance.data_financial_situation()