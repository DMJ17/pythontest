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

# 将数据库中中数据转为数据字典
def to_dic1(self, data, temp, begin, end):
    if end != -1:
        dicdata = {}
        for i in range(begin, end):
            # if  data[i] != '-' and data[i] != None and data[i] != '' and data[i] != '—' and data[i] != '--' and data[i] != '‐' and data[i] != '－' and data[i] != '---' and data[i] != '38̹855̹202.59'\
            #         and data[i] != '1̹059̹632.22' and data[i] != '3̹710̹152.02'and data[i] != '40̹868̹107.55':
            if re.search(r'^\d\d{0,2}(,\d\d\d)*.\d+$',str(data[i])):
                print(data[i])
                print(temp[i])
                try:
                    number = float(data[i].replace(',', ''))
                except:
                    print("Error: %s 数据转换格式错误", data[i])
                dicdata[temp[i]] = number
            elif data[i] == '-' and data[i] == '' and data[i] == '—' and data[i] == '--' and data[i] == '‐' and data[i] == '－' and data[i] == '---':
                dicdata[i] = None
            else:
                dicdata[temp[i]] = data[i]
        return dicdata
    else:
        if  re.search(r'^\d\d{0,2}(,\d\d\d)*.\d+$',str(data[begin])):
            number = float(data[begin].replace(',', ''))
            return number
        elif data[begin] == '-' and data[begin] == '' and data[begin] == '—' and data[begin] == '--' and data[begin] == '‐' and data[begin] == '－' and data[begin] == '---':
            return None
        else:
            return data[begin]

class TableData():
    def data_financial_situation(self):
        # 获取表格中的数据
        ExcelFile = xlrd.open_workbook(r'C:\Users\DMJ\Desktop\工作日常记录\树磊哥\提取元素表-财务数据（资产负债表）.xls',formatting_info=True)
        sheet_name = ExcelFile.sheet_names()
        num = sheet_name.__len__()
        # 循环所有表格
        # for file_num in range(68,69):
        for file_num in range(num):
            sheet = ExcelFile.sheet_by_name(sheet_name[file_num])
            # print(sheet.name,sheet.nrows,sheet.ncols)
            # 读取表格某一列的数据
            rows_num = sheet.nrows
            cols_num = sheet.ncols
            print(cols_num)
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
                if data[1].strip() != None:
                    # 流动资产字典
                    list_value1 = to_dic(self, data, temp, 3, 21)
                    # 非流动资产字典
                    list_value2 = to_dic(self, data, temp, 21, 40)
                    # 资产总计数值转换——-1为只进行转换都的标志位
                    list_value3 = to_dic(self, data, temp, 40, -1)
                    # 流动负债字典
                    list_value4 = to_dic(self, data, temp, 41, 63)
                    # 非流动负债字典
                    list_value5 = to_dic(self, data, temp, 63, 71)
                    # 负债合计数值转换
                    list_value9 = to_dic(self, data, temp, 71, -1)
                    # 所有者权益字典
                    list_value7 = to_dic(self, data, temp, 72, 83)
                    # 负债和所有者权益总计字典
                    list_value8 = to_dic(self, data, temp, 83, 84)

                    dicdata = {}
                    dicdata["财务基本情况及财务指标"] = [{"货币单位": data[2],"报表日期": data[1], "合并资产负债表": {"流动资产": list_value1, "非流动资产": list_value2, "资产总计": list_value3, "流动负债":
                        list_value4,"非流动负债": list_value5, "负债合计": list_value9, "所有者权益（或股东权益）": list_value7, "负债和所有者权益总计": list_value8}}]
                    jsondata.append(dicdata)
            json_data = json.dumps(jsondata, ensure_ascii=False, cls=DateEncoder)

            # fp = open(r'D:\python\project\test\docs\资产负债json\%s.json' % sheet.name, "w", encoding='utf-8')
            # fp.write(json_data)
            db = pymysql.connect(db="ipo_data", user="root", password="123456", host="172.20.20.100", port=3306)
            cursor = db.cursor()
            try:
                cursor.execute('insert into fin_sitat_data(id, cmp_name, financial_situation_data, mark) values(null, %s, %s, 0)',(sheet.name,json_data))
                db.commit()
            except SQLAlchemyError as e:
                print(e)
            # print(json_data)


class DataBaseData():
    def data_financial_situation(self):
        column_key = ['货币资金', '结算备付金', '拆出资金', '交易性金融资产', '应收票据', '应收账款', '预付款项', '应收保费',
                      '应收分保账款', '应收分保合同准备金', '应收利息', '应收股利', '其他应收款', '买入返售金融资产', '存货', '一年内到期的非流动资产',
                      '其他流动资产', '流动资产合计', '发放委托贷款及垫款', '可供出售金融资产', '持有至到期投资', '长期应收款', '长期股权投资',
                      '投资性房地产', '固定资产', '在建工程', '工程物资', '固定资产清理', '生产性生物资产', '油气资产', '无形资产', '开发支出',
                      '商誉', '长期待摊费用', '递延所得税资产', '其他非流动资产', '非流动资产合计', '资产总计', '短期借款', '向中央银行借款',
                      '吸收存款及同业存放', '拆入资金', '交易性金融负债', '应付票据', '应付账款', '预收款项', '卖出回购金融资产款', '应付手续费及佣金',
                      '应付职工薪酬', '应交税费', '应付利息', '应付股利', '其他应付款', '应付分保账款', '保险合同准备金', '代理买卖证券款', '代理承销证券款',
                      '一年内到期的非流动负债', '其他流动负债', '流动负债合计', '长期借款', '应付债券', '长期应付款', '专项应付款', '预计负债', '递延所得税负债',
                      '其他非流动负债', '非流动负债合计', '负债合计', '实收资本（或股本）', '资本公积', '减:库存股', '专项储备', '盈余公积', '一般风险准备',
                      '未分配利润', '外币报表折算差额', '归属于母公司所有者权益合计', '少数股东权益', '所有者权益合计', '负债和所有者权益总计']

        db = pymysql.connect(db="ipo_data", user="root", password="123456", host="172.20.20.100", port=3306)
        cursor = db.cursor()
        try:
            cursor.execute('select distinct ann_title from fin_bala_gen')
            ann_title = cursor.fetchall()
            # count--公司个数
            count = ann_title.__len__()
        except SQLAlchemyError as e:
            print(e)

        # 循环获取所有公司json数据
        for cmp_count in range(count):
            try:
                cursor.execute(
                    'select BG_11001, BG_11004, BG_11013, BG_11016, BG_11031, BG_11040, BG_11070, BG_11043, BG_11049, BG_11052, BG_11037, BG_11034,'
                    ' BG_11067, BG_11025, BG_11073, BG_11079, BG_11082, BG_11000, BG_12001, BG_12013, BG_12016, BG_12025, BG_12022, BG_12019, BG_12028,'
                    ' BG_12034, BG_12031, BG_12037, BG_12040, BG_12043, BG_12046, BG_12049, BG_12052, BG_12055, BG_12058, BG_12064, BG_12000, BG_10000,'
                    ' BG_21001, BG_21004, BG_LSPEC, BG_21016, BG_21019, BG_21070, BG_21073, BG_21076, BG_21025, BG_21040, BG_21079, BG_21085, BG_21088,'
                    ' BG_21082, BG_21091, BG_21043, BG_21046, BG_21031, BG_21034, BG_21097, BG_21100, BG_21000, BG_22001, BG_22004, BG_22007, BG_22010,'
                    ' BG_22013, BG_22019, BG_22022, BG_22000, BG_20000, BG_31001, BG_31004, BG_31007, BG_31013, BG_31016, BG_31022, BG_31019, BG_31025,'
                    ' BG_31000, BG_32001, BG_32000, BG_30000,ann_title,col_date from fin_bala_gen where '
                           'ann_title = %s', ann_title[cmp_count])
                data = cursor.fetchall()
            except SQLAlchemyError as e:
                print(e)
            # finally:
            #     if cmp_count == count:
            #         cursor.close()
            #num-- 每个公司的数据条数
            num = data.__len__()
            jsondata = []
            for data_num in range(num):
                # 流动资产字典
                list_value1 = to_dic1(self, data[data_num], column_key, 0, 18)
                # 非流动资产字典
                list_value2 = to_dic1(self, data[data_num], column_key, 18, 37)
                # 资产总计字典
                list_value3 = to_dic1(self, data[data_num], column_key, 37, -1)
                # 流动负债字典
                list_value4 = to_dic1(self, data[data_num], column_key, 38, 60)
                # 非流动负债字典
                list_value5 = to_dic1(self, data[data_num], column_key, 60, 68)
                # 负债合计字典
                list_value6 = to_dic1(self, data[data_num], column_key, 68, -1)
                # 所有者权益字典
                list_value7 = to_dic1(self, data[data_num], column_key, 69, 80)
                # 负债和所有者权益总计字典
                list_value8 = to_dic1(self, data[data_num], column_key, 80, 81)
                # print(list_value8)
                dicdata = {}
                dicdata["财务基本情况及财务指标"] = [{"货币单位": "元","报表日期": data[data_num][82], "合并资产负债表": {"流动资产": list_value1, "非流动资产": list_value2, "资产总计": list_value3, "流动负债":
                        list_value4,"非流动负债": list_value5, "负债合计": list_value6, "所有者权益（或股东权益）": list_value7, "负债和所有者权益总计": list_value8}}]
                jsondata.append(dicdata)
            json_data = json.dumps(jsondata, ensure_ascii=False, cls=DateEncoder)
            try:
                cursor.execute('insert into fin_sitat_data(id, cmp_name, financial_situation_data, mark) values(null, %s, %s, 1)',(data[data_num][81],json_data))
                db.commit()
            except SQLAlchemyError as e:
                print(e)
            # return json_data
            # print(json_data)

if __name__ == '__main__':
    data_finance = TableData()
    data_finance.data_financial_situation()

    # base_data = DataBaseData()
    # base_data.data_financial_situation()
