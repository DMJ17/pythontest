import os
import os.path
import pandas
import hashlib

# 资产负债提取
def balance(self, fin_basic_gen, prospectusMD5, file_name):
    data_bala = []
    unit = fin_basic_gen['货币单位']
    roport_data = fin_basic_gen['报表日期']
    if pandas.isnull(unit):
        unit = None
    if pandas.isnull(roport_data):
        roport_data = None

    pkey = str(file_name) + str(roport_data)
    pkey_md5 = md5_passwd(pkey)
    data_bala.append(pkey_md5)
    data_bala.append(prospectusMD5)
    data_bala.append(unit)
    data_bala.append(roport_data)

    for key_bala, value_bala in fin_basic_gen['合并资产负债表'].items():
        for key, value in value_bala.items():
            data_bala.append(value)
    data_sql = tuple(data_bala)
    return data_sql

# 合并现金流提取
def cash_flow(self, fin_basic_gen, prospectusMD5, file_name):
        data = []
        unit = fin_basic_gen['货币单位']
        roport_data = fin_basic_gen['报表日期']
        if pandas.isnull(unit):
            unit = None
        if pandas.isnull(roport_data):
            roport_data = None

        pkey = str(file_name) + str(roport_data)
        pkey_md5 = md5_passwd(pkey)
        data.append(pkey_md5)
        data.append(prospectusMD5)
        data.append(unit)
        data.append(roport_data)

        for key_cash, value_cash in fin_basic_gen['合并现金流量表'].items():
            if pandas.isnull(value_cash):
                value_cash = None
            data.append(value_cash)
        data_sql = tuple(data)
        return data_sql

# 利润表提取
def income(self, fin_basic_gen, prospectusMD5, file_name):
    data = []
    unit = fin_basic_gen['货币单位']
    roport_data = fin_basic_gen['报表日期']
    if pandas.isnull(unit):
        unit = None
    if pandas.isnull(roport_data):
        roport_data = None

    pkey = str(file_name) + str(roport_data)
    pkey_md5 = md5_passwd(pkey)
    data.append(pkey_md5)
    data.append(prospectusMD5)
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
    data_sql = tuple(data)
    return data_sql
    # print(data_sql)

# 主要财务指标表
def financial_indicators(self, fin_basic_gen, prospectusMD5, file_name):
    data = []
    unit = fin_basic_gen['货币单位']
    roport_data = fin_basic_gen['报表日期']
    if pandas.isnull(unit):
        unit = None
    if pandas.isnull(roport_data):
        roport_data = None

    pkey = str(file_name) + str(roport_data)
    pkey_md5 = md5_passwd(pkey)
    data.append(pkey_md5)
    data.append(prospectusMD5)
    data.append(unit)
    data.append(roport_data)

    for key_bala, value_fin in fin_basic_gen['基本财务指标'].items():
        if pandas.isnull(value_fin):
            value_fin = None
        data.append(value_fin)
    # del data[11]
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


class InsertData():
    # 公司字典
    def file(self,cursor):
        # 获取所有文件名，生成公司名对应的md5，一次生成使用，除非公司名做出改变
        path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\json_v3\json_final'
        files = os.listdir(path)
        for file in files :
            file_name = os.path.splitext(file)
            file_name = str(file_name[0])
            res = md5_passwd(file_name)
            print(file_name)
            print(res)
            sql = 'insert into file values(%s, %s)'
            cursor.execute(sql ,(res, file_name))

    # 董事基本情况
    def director_information(self, file_name, prospectusMD5, cursor, dic_data):
        # fp = open(r'C:\Users\DMJ\Desktop\工作日常记录\资料\json_v2\error\董事基本情况.txt', "w", encoding='utf-8')
        fromat_director_information = make_fromat(get_field_num(cursor, 'director_information'))
        sql_director_information = 'insert into director_information values(%s)' % fromat_director_information
        if dic_data['控股股东简要情况'] is not None:
            for person_infor in dic_data['董事基本情况']:
                data = []
                pkey = str(file_name) + str(person_infor['姓名']) + str(person_infor['出生年月'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(person_infor, dict):
                    for key, value in person_infor.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                print(data_sql.__len__())
                print(data_sql)
                try:
                    cursor.execute(sql_director_information, data_sql)
                except Exception as e:
                    print(e)
                    fp = open(r'C:\Users\DMJ\Desktop\工作日常记录\资料\json_v2\error\董事基本情况.txt' ,"a", encoding='utf-8')
                    fp.write('21312\r\n')

    # 重大诉讼事项
    def major_lawsuit(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_major_lawsuit = make_fromat(get_field_num(cursor, 'major_lawsuit'))
        sql_major_lawsuit = 'insert into major_lawsuit values(%s)' % fromat_major_lawsuit
        if dic_data['重大诉讼事项'] is not None:
            for major_lawsuit in dic_data['重大诉讼事项']:
                data = []
                pkey = str(file_name) + str(major_lawsuit['起诉(申请)方']) + str(major_lawsuit['应诉（被申请）方'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(major_lawsuit, dict):
                    for key, value in major_lawsuit.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data.append(None)
                    data_sql = tuple(data)
                    print(data_sql.__len__())
                    print(file_name)
                try:
                    cursor.execute(sql_major_lawsuit, data_sql)
                except Exception as e:
                    print(e)

    # 募集资金与运用
    def fund_raising(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_fund_raising = make_fromat(get_field_num(cursor, 'fund_raising'))
        sql_fund_raising = 'insert into fund_raising values(%s)' % fromat_fund_raising
        if dic_data['募集资金与运用'] is not None:
            for fund_raising in dic_data['募集资金与运用']:
                data = []
                pkey = str(file_name) + str(fund_raising['项目名称'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(fund_raising, dict):
                    for key, value in fund_raising.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                print(data_sql)
                print(data_sql.__len__())
                try:
                    cursor.execute(sql_fund_raising, data_sql)
                except Exception as e:
                    print(e)

    # 专利
    def patent(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_patent = make_fromat(get_field_num(cursor, 'patent'))
        sql_patent = 'insert into patent values(%s)' % fromat_patent
        if dic_data['专利'] is not None:
            for patent in dic_data['专利']:
                data = []
                pkey = str(file_name) + str(patent['专利名称'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(patent, dict):
                    for key, value in patent.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                print(data_sql)
                print(data_sql.__len__())
                try:
                    cursor.execute(sql_patent, data_sql)
                except  Exception as e:
                    print(e)

    # 发行人相关信息
    def issuer_information(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_issuer_information = make_fromat(get_field_num(cursor, 'issuer_information'))
        sql_issuer_information = 'insert into issuer_information values(%s)' % fromat_issuer_information
        if isinstance(dic_data, dict):
            data = []
            pkey = str(file_name) + str(dic_data['发行人基本情况'].get('公司名称', None))
            pkey_md5 = md5_passwd(pkey)
            data.append(pkey_md5)
            data.append(prospectusMD5)
            for key, value in dic_data['发行人基本情况'].items():
                if pandas.isnull(value):
                    value = None
                data.append(value)
                data_sql = tuple(data)
            print(data_sql.__len__())
            print(data_sql)
            if data_sql.__len__() == 13:
                try:
                    print(file_name)
                    cursor.execute(sql_issuer_information, data_sql)
                except Exception as e:
                    print(e)

    # 主要客户
    def major_client(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_major_client = make_fromat(get_field_num(cursor, 'major_client'))
        sql_major_client = 'insert into major_client values(%s)' % fromat_major_client
        if dic_data['主要客户'] is not None:
            for major_client in dic_data['主要客户']:
                data = []
                pkey = str(file_name) + str(major_client['客户名称']) + str(major_client['下属单位名称（如细分到分公司、子公司、下属单位则填写，如未细分则填“未披露”）']) + str(major_client['时间'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(major_client, dict):
                    for key, value in major_client.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                    print(data_sql.__len__())
                    print(data_sql)
                try:
                    cursor.execute(sql_major_client, data_sql)
                except Exception as e:
                    print(e)

    # 主要供应商
    def major_supplier(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_major_supplier = make_fromat(get_field_num(cursor, 'major_supplier'))
        sql_major_supplier = 'insert into major_supplier values(%s)' % fromat_major_supplier
        if dic_data['主要供应商'] is not None:
            for major_supplier in dic_data['主要供应商']:
                data = []
                pkey = str(file_name) + str(major_supplier['供应商名称']) + str(major_supplier['时间'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(major_supplier, dict):
                    for key, value in major_supplier.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                    print(data_sql.__len__())
                    print(data_sql)
                try:
                    cursor.execute(sql_major_supplier, data_sql)
                except Exception as e:
                    print(e)

    # 重大合同
    def major_contract(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_major_contract = make_fromat(get_field_num(cursor, 'major_contract'))
        sql_major_contract = 'insert into major_contract values(%s)' % fromat_major_contract
        if dic_data['重大合同'] is not None:
            for major_contract in dic_data['重大合同']:
                data = []
                pkey = str(file_name) + str(major_contract['合同对手方名称']) + str(major_contract['标的'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(major_contract, dict):
                    for key, value in major_contract.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                    print(data_sql.__len__())
                    print(data_sql)
                    print(file_name)
                try:
                    cursor.execute(sql_major_contract, data_sql)
                except Exception as e:
                    print(e)
                print(data_sql)

    # 发行人所处行业
    def issuer_profession(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_issuer_profession = make_fromat(get_field_num(cursor, 'issuer_profession'))
        sql_issuer_profession = 'insert into issuer_profession values(%s)' % fromat_issuer_profession
        if dic_data['发行人所处行业'] is not None:
            for issuer_profession in dic_data['发行人所处行业']:
                data = []
                pkey = str(file_name) + str(issuer_profession['行业分类代码'])
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(issuer_profession, dict):
                    for key, value in issuer_profession.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                    print(data_sql.__len__())
                    print(data_sql)
                    print(file_name)
                try:
                    cursor.execute(sql_issuer_profession, data_sql)
                except Exception as e:
                    print(e)

    # 盈利能力
    def profitability(self, file_name, prospectusMD5, cursor, dic_data):
        for issuer_profession in dic_data['盈利能力']:
            import_time = issuer_profession['报表日期']
            for key, value in issuer_profession['营业收入分析'].items():
                temp = key
                for each_one in value:
                    data = []
                    pkey = str(file_name) + str(import_time) + str(temp) + str(each_one.get('产品类别', None))
                    pkey_md5 = md5_passwd(pkey)
                    data.append(pkey_md5)
                    data.append(prospectusMD5)
                    data.append(import_time)

                    for key, value in each_one.items():
                        data.append(value)
                    # 0 - 营业收入分析 1 - 营业成本分析',
                    data.append(0)
                    if temp == '主营业务收入按产品构成分析':
                        temp_num = 0
                    elif temp == '主营业务收入按业务构成分析':
                        temp_num = 1
                    data.append(temp_num)

                    data_sql = tuple(data)

                    print(file_name)
                    print(data.__len__())
                    print(data_sql)
                    try:
                        cursor.execute(
                            'insert into profitability(pkey, prospectusMD5, table_date, currency_unit, product_type, amount, proportion, movement, business_type, composition_type)'
                            'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data_sql)
                    except  Exception as e:
                         print(e)
            for key, value in issuer_profession['营业成本分析'].items():
                temp = key
                for each_one in value:
                    data = []
                    pkey = str(file_name) + str(import_time) + str(temp) + str(each_one.get('产品类别', None))
                    pkey_md5 = md5_passwd(pkey)
                    data.append(pkey_md5)
                    data.append(prospectusMD5)
                    data.append(import_time)

                    for key, value in each_one.items():
                        data.append(value)
                    # 0 - 营业收入分析 1 - 营业成本分析',
                    data.append(1)
                    if temp == '主营业务成本按产品构成分析':
                        temp_num = 0
                    elif temp == '主营业务成本按业务构成分析':
                        temp_num = 1
                    data.append(temp_num)

                    data_sql = tuple(data)
                    print(data.__len__())
                    print(data_sql)
                    try:
                        cursor.execute(
                            'insert into profitability(pkey, prospectusMD5, table_date, currency_unit, product_type, amount, proportion, movement, business_type, composition_type)'
                            'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data_sql)
                    except  Exception as e:
                        print(e)

    # 资产负债表
    def balance(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_balance = make_fromat(get_field_num(cursor, 'balance'))
        sql_balance = 'insert into balance values(%s)' % fromat_balance
        if dic_data['财务基本情况及财务指标'] is not None:
            for fin_basic_gen in dic_data['财务基本情况及财务指标']:
                if isinstance(fin_basic_gen['合并资产负债表'], dict):
                    data_bala = balance(self, fin_basic_gen, prospectusMD5, file_name)
                    print(data_bala.__len__())
                    print(file_name)
                    print(data_bala)

                    try:
                        cursor.execute(sql_balance, data_bala)
                    except Exception as e:
                        print(e)


    # 现金流量表
    def cash_flow(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_cash_flow = make_fromat(get_field_num(cursor, 'cash_flow'))
        sql_cash_flow = 'insert into cash_flow values(%s)' % fromat_cash_flow
        if dic_data['财务基本情况及财务指标'] is not None:
            for fin_basic_gen in dic_data['财务基本情况及财务指标']:
                if isinstance(fin_basic_gen['合并现金流量表'], dict):
                    data_cash_flow = cash_flow(self, fin_basic_gen, prospectusMD5, file_name)
                    print(data_cash_flow.__len__())
                    print(data_cash_flow)
                    try:
                        cursor.execute(sql_cash_flow, data_cash_flow)
                    except Exception as e:
                        print(e)

    # 利润表
    def income(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_income = make_fromat(get_field_num(cursor, 'income'))
        sql_income = 'insert into income values(%s)' % fromat_income
        if dic_data['财务基本情况及财务指标'] is not None:
            for fin_basic_gen in dic_data['财务基本情况及财务指标']:
                if isinstance(fin_basic_gen['合并利润表'], dict):
                    data_income = income(self, fin_basic_gen, prospectusMD5, file_name)
                    print(file_name)
                    # print(data_income)
                    try:
                        cursor.execute(sql_income ,data_income)
                    except Exception as e:
                        print(e)

    # 主要财务指标表
    def main_financial_indicators(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_main_financial_indicators = make_fromat(get_field_num(cursor, 'main_financial_indicators'))
        sql_main_financial_indicators = 'insert into main_financial_indicators values(%s)' % fromat_main_financial_indicators
        if dic_data['财务基本情况及财务指标'] is not None:
            for fin_basic_gen in dic_data['财务基本情况及财务指标']:
                if isinstance(fin_basic_gen['基本财务指标'], dict):
                    data_fin_ind = financial_indicators(self, fin_basic_gen, prospectusMD5, file_name)
                    # print(data_fin_ind.__len__())
                    # if data_fin_ind.__len__() == 17:
                    print(file_name)
                    try:
                        cursor.execute(sql_main_financial_indicators ,data_fin_ind)
                    except Exception as e:
                        print(e)

    #实际控制人情况
    def actual_controller_info(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_actual_controller_info = make_fromat(get_field_num(cursor, 'actual_controller_info'))
        sql_actual_controller_info = 'insert into actual_controller_info values(%s)' % fromat_actual_controller_info
        if dic_data['实际控制人简要情况'] is not None:
            if isinstance(dic_data['实际控制人简要情况'], dict):
                for each_one in dic_data['实际控制人简要情况'].get('国有控股主体', None):
                    data = []
                    pkey = str(file_name) + str(each_one.get('名称', None))
                    pkey_md5 = md5_passwd(pkey)
                    data.append(pkey_md5)
                    data.append(prospectusMD5)

                    for key, value in each_one.items():
                        data.append(value)
                    data.insert(6, None)
                    data.insert(7, None)
                    data.insert(8, None)
                    data.insert(9, None)
                    data.insert(10,'国有控股主体')
                    print(data.__len__())
                    print(data)
                    try:
                        cursor.execute(sql_actual_controller_info, data)
                    except Exception as e:
                        print(e)

                for each_one in dic_data['实际控制人简要情况'].get('自然人', None):
                    data = []
                    pkey = str(file_name) + str(each_one.get('姓名', None))
                    pkey_md5 = md5_passwd(pkey)
                    data.append(pkey_md5)
                    data.append(prospectusMD5)
                    for key, value in each_one.items():
                        data.append(value)
                    data.insert(3, None)
                    data.insert(8, None)
                    data.insert(9, None)
                    data.insert(10, '自然人')
                    print(data)
                    try:
                        cursor.execute('insert into actual_controller_info(pkey, prospectusMD5, name, principal, identity_number, '
                                       'nationality, direct_holding_ratio, indirect_holding_ratio, nature, pledged_shares, type) '
                                       'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data)
                    except Exception as e:
                        print(e)


                for each_one in dic_data['实际控制人简要情况'].get('其他', None):
                    data = []
                    pkey = str(file_name) + str(each_one.get('名称', None))
                    pkey_md5 = md5_passwd(pkey)
                    data.append(pkey_md5)
                    data.append(prospectusMD5)
                    for key, value in each_one.items():
                        data.append(value)
                    data.insert(7, None)
                    data.insert(8, None)
                    data.insert(9, None)
                    data.insert(10, '其他')
                    print(data)
                    try:
                        cursor.execute('insert into actual_controller_info(pkey, prospectusMD5, name, nature, direct_holding_ratio,'
                                       ' indirect_holding_ratio, pledged_shares, principal, identity_number, nationality, type) '
                                       'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', data)
                    except Exception as e:
                        print(e)


    # 释义
    def paraphrase(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_paraphrase = make_fromat(get_field_num(cursor, 'paraphrase'))
        sql_paraphrase = 'insert into paraphrase values(%s)' % fromat_paraphrase
        for key, value in dic_data['释义'].items():
            data = []
            pkey = str(file_name) + str(key)
            pkey_md5 = md5_passwd(pkey)
            data.append(pkey_md5)
            data.append(prospectusMD5)
            data.append(key)
            data.append(value)
            data_sql = tuple(data)
            print(data_sql)
            try:
                cursor.execute(sql_paraphrase, data_sql)
            except Exception as e:
                print(e)

    # 控股股东情况
    def controlling_shareholder_info(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_controlling_shareholder_info = make_fromat(get_field_num(cursor, 'controlling_shareholder_info'))
        sql_controlling_shareholder_info = 'insert into controlling_shareholder_info values(%s)' % fromat_controlling_shareholder_info
        if dic_data['控股股东简要情况'] is not None:
            if isinstance(dic_data['控股股东简要情况'], dict):
                for key, value in dic_data['控股股东简要情况'].items():
                    data = []
                    # pkey = str(file_name))
                    # pkey_md5 = md5_passwd(pkey)
                    # data.append(pkey_md5)
                    data.append(prospectusMD5)
                    data.append(key)

                    for infor in value:
                        for key, value in infor.items():
                            if pandas.isnull(value):
                                value = None
                            data.append(value)
                    data_sql = tuple(data)
                    print(data_sql)
                print(data_sql)

        try:
            cursor.execute(sql_controlling_shareholder_info, data_sql)
        except Exception as e:
            print(e)

    # 监事基本情况
    def supervisor_information(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_supervisor_information = make_fromat(get_field_num(cursor, 'supervisor_information'))
        sql_supervisor_information = 'insert into supervisor_information values(%s)' % fromat_supervisor_information
        if dic_data['控股股东简要情况'] is not None:
            for person_infor in dic_data['监事基本情况']:
                data = []
                pkey = str(file_name) + str(person_infor['姓名']) + str(person_infor['出生年月'])
                print(pkey)
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(person_infor, dict):
                    for key, value in person_infor.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                print(data_sql.__len__())
                print(data_sql)
                try:
                    cursor.execute(sql_supervisor_information, data_sql)
                except Exception as e:
                    print(e)

    # 高管基本情况
    def management_information(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_management_information = make_fromat(get_field_num(cursor, 'management_information'))
        sql_management_information = 'insert into management_information values(%s)' % fromat_management_information
        if dic_data['控股股东简要情况'] is not None:
            for person_infor in dic_data['高管基本情况']:
                data = []
                pkey = str(file_name) + str(person_infor['姓名']) + str(person_infor['出生年月'])
                print(pkey)
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(person_infor, dict):
                    for key, value in person_infor.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                print(data_sql.__len__())
                print(data_sql)
                try:
                    cursor.execute(sql_management_information, data_sql)
                except Exception as e:
                    print(e)

    # 核心技术人员基本情况
    def core_technician_info(self, file_name, prospectusMD5, cursor, dic_data):
        fromat_core_technician_info = make_fromat(get_field_num(cursor, 'core_technician_info'))
        sql_core_technician_info = 'insert into core_technician_info values(%s)' % fromat_core_technician_info
        if dic_data['控股股东简要情况'] is not None:
            for person_infor in dic_data['核心技术人员基本情况']:
                data = []
                pkey = str(file_name) + str(person_infor['姓名']) + str(person_infor['出生年月'])
                print(pkey)
                pkey_md5 = md5_passwd(pkey)
                data.append(pkey_md5)
                data.append(prospectusMD5)
                if isinstance(person_infor, dict):
                    for key, value in person_infor.items():
                        if pandas.isnull(value):
                            value = None
                        data.append(value)
                    data_sql = tuple(data)
                print(data_sql.__len__())
                print(data_sql)
                try:
                    cursor.execute(sql_core_technician_info, data_sql)
                except Exception as e:
                    print(e)


# if __name__ == '__main__':
#     temp = Json_to_Data_Base()
#     temp.json_to_data_base()