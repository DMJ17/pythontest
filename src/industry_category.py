import pymysql
import re
import xlrd

excel_file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\新磊哥\行业分类\P020181022394758143242.xlsx'


class IndustryCategory():
    def industry_category(self):
        db = pymysql.connect(db="industry_category_v2", user="root", password="root", host="127.0.0.1", port=3306)
        cursor = db.cursor()

        ExcelFile = xlrd.open_workbook(excel_file_path)
        sheet_name = ExcelFile.sheet_names()
        print(sheet_name)
        sheet = ExcelFile.sheet_by_name(sheet_name[0])
        cols_num = sheet.ncols
        rows_num = sheet.nrows
        for row_num in range(0,rows_num):
            row_data = sheet.row_values(row_num)
            row_data[3] = row_data[3].replace(' ','')
            if row_data[3] == '—':
                data = []
                data.insert(0, row_data[4])

                fourth_num = row_num
                while fourth_num > 0:
                    fourth_data = sheet.row_values(fourth_num)
                    fourth_leval = fourth_data[1]
                    if fourth_leval != '':
                        if not isinstance(fourth_leval, str):
                            # 从excel中提取的数据有的为float类型，需先转换为int型再转为str
                            fourth_leval = int(fourth_leval)
                            fourth_leval = str(fourth_leval)
                        fourth_leval = str(fourth_leval)
                        if re.search(r'^\d{4}$', fourth_leval):
                            data.insert(0, fourth_leval)
                            break
                    fourth_num = fourth_num - 1
                leval_num = data[0]
                leval_num = str(leval_num)
                third_leval = leval_num[0:3]
                second_leval = leval_num[0:2]
                data.insert(0, third_leval)
                data.insert(0, second_leval)

                first_num = fourth_num
                while first_num > 0:
                    first_data = sheet.row_values(first_num)
                    first_leval = first_data[0]
                    if first_leval != '':
                        first_leval = str(first_leval)
                        if re.search(r'^[A-Z]{1}$', first_leval):
                            data.insert(0, first_leval)
                            break
                    first_num = first_num - 1
                print(data)
        #         try:
        #             data.insert(0, None)
        #             cursor.execute('insert into industry_category values(%s,%s,%s,%s,%s,%s)', data)
        #             db.commit()
        #         except Exception as e:
        #             print(e)
        #             print(data)
        # cursor.close()
        # db.close()






        # for row_num in range(0, rows_num):
        #     row_data = sheet.row_values(row_num)
        #     # print(row_data)
        #     row_data[3] = row_data[3].replace(' ', '')
        #     if row_data[3] == '—':
        #         data = []
        #         data.insert(0, row_data[4])
        #
        #         fourth_num = row_num
        #         while fourth_num > 0:
        #             fourth_data = sheet.row_values(fourth_num)
        #             fourth_leval = fourth_data[1]
        #             if fourth_leval != '':
        #                 if not isinstance(fourth_leval, str):
        #                     fourth_leval = int(fourth_leval)
        #                     fourth_leval = str(fourth_leval)
        #                 if re.search(r'^\d{4}$', fourth_leval):
        #                     data.insert(0, fourth_leval)
        #                     break
        #                 else:
        #                     print(fourth_leval)
        #             fourth_num = fourth_num - 1
        #
        #         third_num = fourth_num
        #         while third_num > 0:
        #             third_data = sheet.row_values(third_num)
        #             third_leval = third_data[0]
        #             if third_leval != '':
        #                 if not isinstance(third_leval, str):
        #                     third_leval = int(third_leval)
        #                     third_leval = str(third_leval)
        #                 third_leval = str(third_leval)
        #                 if re.search(r'^\d{3}$', third_leval):
        #                     data.insert(0, third_leval)
        #                     break
        #             third_num = third_num - 1
        #
        #         second_num = third_num
        #         while second_num > 0:
        #             second_data = sheet.row_values(second_num)
        #             second_leval = second_data[0]
        #             if second_leval != '':
        #                 if not isinstance(second_leval, str):
        #                     second_leval = int(second_leval)
        #                     second_leval = str(second_leval)
        #                 second_leval = str(second_leval)
        #                 if re.search(r'^\d{2}$', second_leval):
        #                     data.insert(0, second_leval)
        #                     break
        #             second_num = second_num - 1
        #
        #         first_num = second_num
        #         while first_num > 0:
        #             first_data = sheet.row_values(first_num)
        #             first_leval = first_data[0]
        #             if first_leval != '':
        #                 first_leval = str(first_leval)
        #                 if re.search(r'^[A-Z]{1}$', first_leval):
        #                     data.insert(0, first_leval)
        #                     break
        #             first_num = first_num - 1
        #         print(data)
        #         try:
        #             data.insert(0, None)
        #             cursor.execute('insert into test values(%s,%s,%s,%s,%s,%s)', data)
        #             db.commit()
        #         except Exception as e:
        #             print(e)
        #             print('--------------------------------------------------------------------------------------------')
        # cursor.close()
        # db.close()

if __name__ == '__main__':
    temp = IndustryCategory()
    temp.industry_category()

