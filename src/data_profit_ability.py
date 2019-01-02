import pymysql
import json
import xlrd
import datetime
import decimal
import os
data_file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\树磊哥\提取数据\盈利能力.xlsx'
final_data_path = 'D:\\python\project\test\docs\盈利能力12.13'

"""
此段为主要内容
"""
# # 重写构造json类，遇到date.time,date and  Decimal特殊处理
# class DateEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, datetime.date):
#             return obj.strftime("%Y-%m-%d")
#         elif isinstance(obj, decimal.Decimal):
#             return str(obj)
#         else:
#             return json.JSONEncoder.default(self, obj)
#
# # 将表格中数据转为数据字典
# def to_dic(self, data, temp, begin, end):
#     dicdata = {}
#     for i in range(begin, end):
#         if data[i] == '无' or data[i] == '-' or data[i] == '':
#             data[i] = None
#             dicdata[temp[i]] = None
#         else:
#             dicdata[temp[i]] = data[i]
#     return dicdata
#
# class TableData():
#     def data_financial_situation(self):
#         # db = pymysql.connect(db="ipo_data", user="root", password="123456", host="172.20.20.100", port=3306)
#         # cursor = db.cursor()
#         # 获取表格中的数据
#         # ExcelFile = xlrd.open_workbook(r'C:\Users\DMJ\Desktop\工作日常记录\树磊哥\盈利能力.xlsx')
#         ExcelFile = xlrd.open_workbook(data_file_path)
#         sheet_name = ExcelFile.sheet_names()
#         num = sheet_name.__len__()
#         sheet1 = ExcelFile.sheet_by_name(sheet_name[1])
#         temp = sheet1.col_values(3)
#         for file_num in range(num):
#             sheet = ExcelFile.sheet_by_name(sheet_name[file_num])
#             rows_num = sheet.nrows
#             cols_num = sheet.ncols
#             column_index = 4
#             jsondata = {}
#             data = []
#             inco_product = []
#             cost_product = []
#             inco_business = []
#             cost_business = []
#             temp1 = 0
#             temp2 = 0
#             temp3 = 0
#             temp4 = 0
#             while column_index < cols_num:
#                 col = sheet.col_values(column_index)
#                 if column_index < cols_num - 1:
#                     col_next = sheet.col_values(column_index + 1)
#                 else:
#                     col_next[0] = None
#                 # 主营业务收入按产品构成分析字典
#                 list_value1 = to_dic(self, col, temp, 1, 6)
#                 # 主营业务收入按业务构成分析字典
#                 list_value2 = to_dic(self, col, temp, 6, 11)
#                 # 主营业务成本按产品构成分析字典
#                 list_value3 = to_dic(self, col, temp, 11, 16)
#                 # 主营业务成本按业务构成分析字典
#                 list_value4 = to_dic(self, col, temp, 16, 21)
#
#                 if col[0] == col_next[0] and column_index+1 != cols_num:
#                     if list_value1['产品类别'] != None:
#                         temp1 = temp1 + 1
#                         inco_product.append(list_value1)
#                     if list_value3['产品类别'] != None:
#                         temp2 = temp2 + 1
#                         cost_product.append(list_value3)
#                     if list_value2['业务类别'] != None:
#                         temp3 = temp3 + 1
#                         inco_business.append(list_value2)
#                     if list_value4['业务类别'] != None:
#                         temp4 = temp4 + 1
#                         cost_business.append(list_value4)
#                 else:
#                     if temp1 == 0 or list_value1['产品类别'] != None:
#                         inco_product.append(list_value1)
#                     if temp2 == 0 or list_value3['产品类别'] != None:
#                         cost_product.append(list_value3)
#                     if temp3 == 0 or list_value4['业务类别'] != None:
#                         inco_business.append(list_value2)
#                     if temp4 == 0 or list_value4['业务类别'] != None:
#                         cost_business.append(list_value4)
#
#                     dicdata1 = {}
#                     dicdata1["主营业务收入按产品构成分析"] = inco_product
#                     dicdata1["主营业务收入按业务构成分析"] = inco_business
#                     dicdata3 = {}
#                     dicdata3["主营业务成本按产品构成分析"] = cost_product
#                     dicdata3["主营业务成本按业务构成分析"] = cost_business
#
#                     if type(col[0]) == float:
#                         col[0] = int(col[0])
#                     data.append({"报表日期": col[0], "营业收入分析": dicdata1, "营业成本分析": dicdata3})
#                     inco_product = []
#                     cost_product = []
#                     inco_business = []
#                     cost_business = []
#                 column_index = column_index + 1
#                 jsondata['盈利能力'] = data
#                 if  column_index == cols_num:
#                     json_data = json.dumps(data, ensure_ascii=False, cls=DateEncoder)
#                     print(json_data)
#                     print(1)
#                     # fp =open(r'D:\python\project\test\docs\盈利能力12.13\%s.json' % sheet.name,"w" ,encoding='utf-8')
#                     data_file_route = os.path.join(final_data_path, sheet.name + '.josn')
#                     fp =open(data_file_route,"w" ,encoding='utf-8')
#                     fp.write(json_data)
#
#                     # db = pymysql.connect(db="ipo_data", user="root", password="123456", host="172.20.20.100", port=3306)
#                     # cursor = db.cursor()
#                     # try:
#                     #     cursor.execute(
#                     #         'insert into pro_ability_data(id, cmp_name, profit_ability_data, mark) values(null, %s, %s, 2)',(sheet.name, json_data))
#                     #     db.commit()
#                     # except SQLAlchemyError as e:
#                     #     print(e)
#                     # print(json_data)
#
# if __name__ == '__main__':
#     data_finance = TableData()
#     data_finance.data_financial_situation()


# from settings.config import excel_filename
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

# 将表格中数据转为数据字典
def to_dic(self, data, temp, begin, end):
    dicdata = {}
    for i in range(begin, end):
        if data[i] == '无' or data[i] == '-' or data[i] == '':
            data[i] = None
            dicdata[temp[i]] = None
        else:
            dicdata[temp[i]] = data[i]
    return dicdata

class TableData():
    def data_financial_situation(self, initial_position, end_position):
        # file_path = excel_filename["profit_ability_path"]
        # ExcelFile = xlrd.open_workbook(file_path)
        ExcelFile = xlrd.open_workbook(data_file_path)
        sheet_name = ExcelFile.sheet_names()
        num = sheet_name.__len__()
        json_data_list = []
        if num != 491:
            print('error:数据表格缺失！')
        else:
            sheet1 = ExcelFile.sheet_by_name(sheet_name[1])
            temp = sheet1.col_values(3)
            for file_num in range(initial_position, end_position):
                sheet = ExcelFile.sheet_by_name(sheet_name[file_num])
                name = sheet.name
                cols_num = sheet.ncols
                column_index = 4
                jsondata = {}
                data = []
                inco_product = []
                cost_product = []
                inco_business = []
                cost_business = []
                temp1 = 0
                temp2 = 0
                temp3 = 0
                temp4 = 0
                while column_index < cols_num:
                    col = sheet.col_values(column_index)
                    # print(type(col[20]))
                    # # print(type(col[19]))
                    # print(col[19])
                    if column_index < cols_num - 1:
                        col_next = sheet.col_values(column_index + 1)
                    else:
                        col_next[0] = None
                    # 主营业务收入按产品构成分析字典
                    list_value1 = to_dic(self, col, temp, 1, 6)
                    # 主营业务收入按业务构成分析字典
                    list_value2 = to_dic(self, col, temp, 6, 11)
                    # 主营业务成本按产品构成分析字典
                    list_value3 = to_dic(self, col, temp, 11, 16)
                    # 主营业务成本按业务构成分析字典
                    list_value4 = to_dic(self, col, temp, 16, 21)

                    if col[0] == col_next[0] and column_index+1 != cols_num:
                        if list_value1['产品类别'] != None:
                            temp1 = temp1 + 1
                            inco_product.append(list_value1)
                        if list_value3['产品类别'] != None:
                            temp2 = temp2 + 1
                            cost_product.append(list_value3)
                        if list_value2['业务类别'] != None:
                            temp3 = temp3 + 1
                            inco_business.append(list_value2)
                        if list_value4['业务类别'] != None:
                            temp4 = temp4 + 1
                            cost_business.append(list_value4)
                    else:
                        if temp1 == 0 or list_value1['产品类别'] != None:
                            inco_product.append(list_value1)
                        if temp2 == 0 or list_value3['产品类别'] != None:
                            cost_product.append(list_value3)
                        if temp3 == 0 or list_value4['业务类别'] != None:
                            inco_business.append(list_value2)
                        if temp4 == 0 or list_value4['业务类别'] != None:
                            cost_business.append(list_value4)

                        dicdata1 = {}
                        dicdata1["主营业务收入按产品构成分析"] = inco_product
                        dicdata1["主营业务收入按业务构成分析"] = inco_business
                        dicdata3 = {}
                        dicdata3["主营业务成本按产品构成分析"] = cost_product
                        dicdata3["主营业务成本按业务构成分析"] = cost_business

                        if type(col[0]) == float:
                            col[0] = int(col[0])
                        data.append({"报表日期": col[0], "营业收入分析": dicdata1, "营业成本分析": dicdata3})
                        inco_product = []
                        cost_product = []
                        inco_business = []
                        cost_business = []
                    column_index = column_index + 1
                    jsondata['盈利能力'] = data
                    if  column_index == cols_num:
                        # json_data = json.dumps(jsondata, ensure_ascii=False, cls=DateEncoder)
                        # print(json_data)
                        print(name)
                        json_data_list.append(jsondata)

                        print(jsondata)
                        # return(json_data_list)



if __name__ == '__main__':
    data_finance = TableData()
    data_finance.data_financial_situation(397,400)