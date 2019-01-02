import pymysql
import xlrd
from sqlalchemy.exc import SQLAlchemyError
'''
实现人工抽取和机器抽取的对比
'''
class DataComparison():
    def  data_comparison(self):
        # 获取表格中的数据
        ExcelFile = xlrd.open_workbook(r'C:\Users\DMJ\Desktop\工作日常记录\树磊哥\提取元素表-财务数据（资产负债表）.xls',formatting_info=True)
        sheet_name = ExcelFile.sheet_names()
        # print(sheet_name[0])
        sheet = ExcelFile.sheet_by_name(sheet_name[202])
        print(sheet_name[203])
        # print(sheet.name,sheet.nrows,sheet.ncols)
        # 读取表格某一列的数据
        cols = sheet.col_values(4)
        # print(cols[40])

        db = pymysql.connect(db="ipo_data", user="root", password="123456", host="172.20.20.100", port=3306)
        cursor = db.cursor()
        try:
            cursor.execute('select BG_11001, BG_11004, BG_11013, BG_11016, BG_11031, BG_11040, BG_11070, BG_11043, BG_11049, BG_11052, BG_11037, BG_11034,'
                           ' BG_11067, BG_11025, BG_11073, BG_11079, BG_11082, BG_11000, BG_12001, BG_12013, BG_12016, BG_12025, BG_12022, BG_12019, BG_12028,'
                           ' BG_12034, BG_12031, BG_12037, BG_12040, BG_12043, BG_12046, BG_12049, BG_12052, BG_12055, BG_12058, BG_12064, BG_12000, BG_10000,'
                           ' BG_21001, BG_21004, BG_LSPEC, BG_21016, BG_21019, BG_21070, BG_21073, BG_21076, BG_21025, BG_21040, BG_21079, BG_21085, BG_21088,'
                           ' BG_21082, BG_21091, BG_21043, BG_21046, BG_21031, BG_21034, BG_21097, BG_21100, BG_21000, BG_22001, BG_22004, BG_22007, BG_22010,'
                           ' BG_22013, BG_22019, BG_22022, BG_22000, BG_20000, BG_31001, BG_31004, BG_31007, BG_31013, BG_31016, BG_31022, BG_31019, BG_31025,'
                           ' BG_31000, BG_32001, BG_32000, BG_30000 from fin_bala_gen where '
                           'ann_title = "2017-12-06_广东文灿压铸股份有限公司首次公开发行股票招股说明书(申报稿2017年12月1日" and col_date =  "2017-6-30"')
            data = cursor.fetchone()
        except SQLAlchemyError as e:
            print(e)
        finally:
            cursor.close()

        count = 0 #比对相同的个数
        num = 3 #数据表格中从第四个数据开始比对
        number = 0 #数据库中一条数据的属性个数
        #用提取数据与人工抽取的进行对
        for temp in data:
            if temp != None and temp != '-' and temp != '':
                number = number+1
                temp = float(temp.replace(',', ''))
                if temp == cols[num]:
                    # print(temp)
                    # print(cols[num])
                    count = count + 1
                else:
                    print(temp,cols[num])
            num = num + 1
        print(num-3)
        print(number)
        print(count)

        count1 = 0 #比对相同的个数
        data_num = 0
        number1 = 0 #数据库中一条数据的属性个数
        # 用人工抽取的与提取数据进行对比
        for temp in cols[3:]:
            if temp != '无' and temp != '-' and temp != '':
                number1 = number1 + 1
                if data[data_num] != None and data[data_num] != '-' and data[data_num] != '':
                    dat = float(data[data_num].replace(',', ''))
                    # print(dat)
                    # print(temp)
                    if temp == dat:
                        count1 = count1 + 1
            data_num = data_num + 1

        print(data_num)
        print(number1)
        print(count1)

data_cmp = DataComparison()
data_cmp.data_comparison()