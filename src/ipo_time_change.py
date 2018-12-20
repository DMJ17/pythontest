import json
import re
import os
json_file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\\time_json'
json_file_changed = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\\time_change'

"""
时间格式转换 例：（最终格式：年-月-日 / 年-月-日~年-月-日）
    "t2": "2016.12.31",
    "t3": " 2020-05-09 00:00:00",
    "t4": "2016 年 12 月 31 日",
    "t5": "2016 年 4 月",
    "t6": "2018 年",
    "t7": "2017/6/7-2018/5/20 ",
    "t8": "2017.4.1-2020.3.31",
    "t9": "2017年6月21日至2018年6月21日",
    "t10": "2017 年 5 月 1 日至 2018 年 4 月 30 日",
    "t11": "2015 年 1月 30 日至2024 年 10月 29 日期间发生的债权",
    "t12": "2018-01-01 至 2018-12-31",
    "t13": "2015 年 1 月 1 日起至 2017 年 12 月 31 日",
    "t14": " 自 2018年1月21 日至 2018 年 12 月 31 日",
    "t15": "2016 年 1 月 1 日至2017 年 12 月 31 日，协议期满前 30 日内双方如无异议，可自动延期 1 年，顺延次数不限",
    "t16": "合同有效期为 2016 年 1 月 1 日至 2016 年 12 月31 日。《商品合同》约定，任何一方有权在前述合同期限届满至少提前一个月书面通知另一方 于前述期限届满时终止本《商合， 使前述终止权，则本《商品合同》将视为已经由双方默认为无限期续订而有效并对双方具有约束力，在续订期内，任何一方有权提前一个月书面通知另一方以终止本《商品合同》",
"""
# 时间切片，补零
def slice_zero_pad(value):
    if re.search(r'^\d{4}\-\d{1}$', value):
        value_begin = value[0:5]
        value_end = value[5:]
        value = value_begin + '0' + value_end
    if re.search(r'^\d{4}\-\d{1}\-', value):
        value_begin = value[0:5]
        value_end = value[5:]
        value = value_begin + '0' + value_end
    if re.search(r'^\d{4}\-\d{2}\-\d{1}$', value):
        value_begin = value[0:8]
        value_end = value[8:]
        value = value_begin + '0' + value_end
    return value

# 有待优化，不必要所有的判断都得执行
def time_change(time):
    time = str(time)
    value = time.strip()
    value = value.replace('\n', '')

    # 2016.12.31
    if re.search(r'^\d{4}\.\d{1,2}\.\d{1,2}$', value):
        value = value.replace(".", "-")

    # 2020-05-09 00:00:00
    if re.search(r'^\d{4}\-\d{1,2}(\-\d{1,2})\s*\d{2}\:\d{2}\:\d{2}$', value):
        value = value.replace(" 00:00:00", "")

    # 2016 年 12 月 31 日
    if re.search(r'^\d{4}\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日$', value):
        value = value.replace("年", "-")
        value = value.replace("月", "-")
        value = value.replace("日", "")
        value = value.replace(" ", "")

    # 2016 年 4 月
    if re.search(r'^\d{4}\s*年\s*\d{1,2}\s*月$', value):
        value = value.replace("年", "-")
        value = value.replace("月", "")
        value = value.replace(" ", "")

    # 2018 年
    if re.search(r'^\d{4}\s*年\s*$', value):
        value = value.replace("年", "")

    # 2017/6/7-2018/5/20
    if re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}\-\d{4}\/\d{1,2}\/\d{1,2}$', value):
        value = value.replace("-", "~")
        value = value.replace("/", "-")

    # 2017.4.1-2020.3.31
    if re.search(r'^\d{4}\.\d{1,2}\.\d{1,2}\-\d{4}\.\d{1,2}\.\d{1,2}$', value):
        value = value.replace("-", "~")
        value = value.replace(".", "-")

    # 2017年6月21日至2018年6月21日 / 2015 年 1月 30 日至2024 年 10月 29 日期间发生的债权/2015 年 1 月 1 日起至 2017 年 12 月 31 日
    if re.search(r'^[\u4E00-\u9FFF]*\s*\d{4}\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*[\u4E00-\u9FFF]+\s*\d{4}\s*'
                 r'年\s*\d{1,2}\s*月\s*\d{1,2}\s*[\u4E00-\u9FFF]+', value):
        time_list = re.findall(r'\d{4}\s*年\s*\d{1,2}\s*月\s*\d{1,2}', value)
        value = time_list[0] + '~' + time_list[1]
        value = value.replace("年", "-")
        value = value.replace("月", "-")
        value = value.replace("日", "")
        value = value.replace(" ","")

    # 2018-01-01 至 2018-12-31
    if re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}\s*[\u4E00-\u9FFF]+\s*\d{4}\-\d{1,2}\-\d{1,2}$', value):
        time_list = re.findall(r'\d{4}\-\d{1,2}\-\d{1,2}', value)
        value = time_list[0] + '~' + time_list[1]

    # 2018/12/1
    if re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}$', value):
        value = value.replace('/', '-')

    # 2016.12.16至2017.12.15
    if re.search(r'^\d{4}\.\d{1,2}\.\d{1,2}\s*[\u4E00-\u9FFF]+\s*\d{4}\.\d{1,2}\.\d{1,2}$', value):
        time_list = re.findall(r'\d{4}\.\d{1,2}\.\d{1,2}', value)
        value = time_list[0] + '~' + time_list[1]
        value = value.replace('.', '-')


    return value

# 董监高时间格式规整
def time_person_change(dic_data):

    if dic_data['监事基本情况'] is not None:
        for sup_infor in dic_data['监事基本情况']:
            sup_infor['出生年月'] = time_change(sup_infor['出生年月'])
            sup_infor['起始日期'] = time_change(sup_infor['起始日期'])
            sup_infor['终止日期'] = time_change(sup_infor['终止日期'])

    if dic_data['董事基本情况'] is not None:
        for dir_infor in dic_data['董事基本情况']:
            dir_infor['出生年月'] = time_change(dir_infor['出生年月'])
            dir_infor['起始日期'] = time_change(dir_infor['起始日期'])
            dir_infor['终止日期'] = time_change(dir_infor['终止日期'])

    if dic_data['高管基本情况'] is not None:
        for man_infor in dic_data['高管基本情况']:
            man_infor['出生年月'] = time_change(man_infor['出生年月'])
            man_infor['起始日期'] = time_change(man_infor['起始日期'])
            man_infor['终止日期'] = time_change(man_infor['终止日期'])

    if dic_data['核心技术人员基本情况'] is not None:
        for core_tec_infor in dic_data['核心技术人员基本情况']:
            core_tec_infor['出生年月'] = time_change(core_tec_infor['出生年月'])
            core_tec_infor['起始日期'] = time_change(core_tec_infor['起始日期'])
            core_tec_infor['终止日期'] = time_change(core_tec_infor['终止日期'])

    return dic_data

# 发行人相关信息
def time_issuer_change(dic_data):
    dic_data['发行人基本情况']['成立日期'] = time_change(dic_data['发行人基本情况']['成立日期'])
    return dic_data

# 两层结构
def time_change_common(dic_data, fist_floor, second_floor):
    for time_temp in dic_data[fist_floor]:
        time_temp[second_floor] = time_change(time_temp[second_floor])
    return dic_data

# 时间格式修改合并调用
def json_time_change(dic_data):
    # 董监高
    dic_data = time_person_change(dic_data)
    # 发行人相关信息
    dic_data = time_issuer_change(dic_data)
    # 主要客户
    if dic_data['主要客户'] is not None:
        dic_data = time_change_common(dic_data,'主要客户', '时间')
    # 主要供应商
    if dic_data['主要供应商'] is not None:
        dic_data = time_change_common(dic_data,'主要供应商', '时间')
    # 重大合同
    if dic_data['重大合同'] is not None:
        dic_data = time_change_common(dic_data, '重大合同', '履行期限')
    # 盈利能力
    if dic_data['盈利能力'] is not None:
        dic_data = time_change_common(dic_data, '盈利能力', '报表日期')
    # 财务基本情况及财务指标
    if dic_data['财务基本情况及财务指标'] is not None:
        dic_data = time_change_common(dic_data, '财务基本情况及财务指标', '报表日期')
    # 专利
    if dic_data['专利'] is not None:
        dic_data = time_change_common(dic_data, '专利', '取得日期')
        dic_data = time_change_common(dic_data, '专利', '使用期限')
    # print(dic_data['专利'])

    return dic_data

# 境外居住权规整
def overseas_residency_change(dic_data):
    if dic_data['监事基本情况'] is not None:
        for sup_infor in dic_data['监事基本情况']:
            if sup_infor['境外居留权'] != '无' and sup_infor['境外居留权'] != None and sup_infor['境外居留权'] != '否' \
                    and sup_infor['境外居留权'] != '无境外居留权':
                sup_infor['境外居留权'] = '有'
            else:
                sup_infor['境外居留权'] = '无'

    if dic_data['董事基本情况'] is not None:
        for dir_infor in dic_data['董事基本情况']:
            if dir_infor['境外居留权'] != '无' and dir_infor['境外居留权'] != None and dir_infor['境外居留权'] != '否' \
                    and dir_infor['境外居留权'] != '无境外居留权':
                dir_infor['境外居留权'] = '有'
            else:
                dir_infor['境外居留权'] = '无'

    if dic_data['高管基本情况'] is not None:
        for man_infor in dic_data['高管基本情况']:
            if man_infor['境外居留权'] != '无' and man_infor['境外居留权'] != None and man_infor['境外居留权'] != '否' \
                    and man_infor['境外居留权'] != '无境外居留权':
                man_infor['境外居留权'] = '有'
            else:
                man_infor['境外居留权'] = '无'

    if dic_data['核心技术人员基本情况'] is not None:
        for core_tec_infor in dic_data['核心技术人员基本情况']:
            if core_tec_infor['境外居留权'] != '无' and core_tec_infor['境外居留权'] is not None and core_tec_infor['境外居留权'] != '否' \
                and core_tec_infor['境外居留权'] != '无境外居留权':
                core_tec_infor['境外居留权'] = '有'
            else:
                core_tec_infor['境外居留权'] = '无'

    return dic_data

def patent_ownership(dic_data):
    if dic_data['专利'] is not None:
        for patent in dic_data['专利']:
            if patent['是否存在权属纠纷'] != '无' and patent['是否存在权属纠纷'] != '否' and patent['是否存在权属纠纷'] is not None:
                patent['是否存在权属纠纷'] = '是'
            else:
                patent['是否存在权属纠纷'] = '否'

    return dic_data

# 性别规范化
def gander_change(dic_data):
    if dic_data['监事基本情况'] is not None:
        for sup_infor in dic_data['监事基本情况']:
            sup_infor['性别'] = sup_infor['性别'].strip()

    if dic_data['董事基本情况'] is not None:
        for dir_infor in dic_data['董事基本情况']:
            dir_infor['性别'] = dir_infor['性别'].strip()

    if dic_data['高管基本情况'] is not None:
        for man_infor in dic_data['高管基本情况']:
            man_infor['性别'] = man_infor['性别'].strip()

    if dic_data['核心技术人员基本情况'] is not None:
        for core_tec_infor in dic_data['核心技术人员基本情况']:
            core_tec_infor['性别'] = core_tec_infor['性别'].strip()

    return dic_data

# 金额
def amount_change(dic_data):
    # 基本财务指标
    if dic_data['财务基本情况及财务指标'] is not None:
        for fin_basic_gen in dic_data['财务基本情况及财务指标']:
            if isinstance(fin_basic_gen['合并资产负债表'], dict):
                for key_fist, value_fist in fin_basic_gen['合并资产负债表'].items():
                    for key_second, value_second in value_fist.items():
                        if re.search(r'^(-?\d+)(\.\d+)?$', str(value_second)):
                            if re.search(r'^(-?\d+)(\.\d+)$', str(value_second)):
                                value_second = float(value_second)
                            else:
                                value_second = int(value_second)
                            amount = "{:,}".format(value_second)
                            value_fist[key_second] = amount
            # print(fin_basic_gen['合并资产负债表'])

            if isinstance(fin_basic_gen['合并现金流量表'], dict):
                for key_one, value_one in fin_basic_gen['合并现金流量表'].items():
                        if re.search(r'^(-?\d+)(\.\d+)?$', str(value_one)):
                            if re.search(r'^(-?\d+)(\.\d+)$', str(value_one)):
                                value_one = float(value_one)
                            else:
                                value_one = int(value_one)
                            amount = "{:,}".format(value_one)
                            fin_basic_gen['合并现金流量表'][key_one] = amount
            # print(fin_basic_gen['合并现金流量表'])

            # 金额转换意外错误
            if isinstance(fin_basic_gen['合并利润表'], dict):
                for key_fist, value_fist in fin_basic_gen['合并利润表'].items():
                    if isinstance(value_fist, dict):
                        for key_second, value_second in value_fist.items():
                            if re.search(r'^(-?\d+)(\.\d+)?$', str(value_second)):
                                if re.search(r'^(-?\d+)(\.\d+)$', str(value_second)):
                                    value_second = float(value_second)
                                else:
                                    value_second = int(value_second)
                                amount = "{:,}".format(value_second)
                                value_fist[key_second] = amount

                    else:
                        if re.search(r'^(-?\d+)(\.\d+)?$', str(value_fist)):
                            if re.search(r'^(-?\d+)(\.\d+)$', str(value_fist)):
                                value_fist = float(value_fist)
                            else:
                                value_fist = int(value_fist)
                            amount = "{:,}".format(value_fist)
                            fin_basic_gen['合并利润表'][key_fist] = amount
            # print(fin_basic_gen['合并利润表'])

            if isinstance(fin_basic_gen['基本财务指标'], dict):
                for key_fist, value_fist in fin_basic_gen['基本财务指标'].items():
                    if re.search(r'^(-?\d+)(\.\d+)?$', str(value_fist)):
                        if re.search(r'^(-?\d+)(\.\d+)$', str(value_fist)):
                            value_fist = float(value_fist)
                        else:
                            value_fist = int(value_fist)
                        amount = "{:,}".format(value_fist)
                        fin_basic_gen['基本财务指标'][key_fist] = amount

                # print(fin_basic_gen['基本财务指标'])

    # 盈利能力,正则意外错误
    if dic_data['盈利能力'] is not None:
        for issuer_profession in dic_data['盈利能力']:
            if isinstance(issuer_profession, dict):
                for key_first, value_first in issuer_profession.items():
                    if isinstance(value_first, dict):
                        for key_secount, value_secount in value_first.items():
                            for echo_amount in value_secount:
                                if isinstance(echo_amount, dict):
                                    for key_third, value_third in echo_amount.items():
                                        if re.search(r'^(-?\d+)(\.\d+)?$', str(value_third)):
                                            if re.search(r'^(-?\d+)(\.\d+)$', str(value_third)):
                                                value_third = float(value_third)
                                            else:
                                                value_third = int(value_third)
                                            amount = "{:,}".format(value_third)
                                            echo_amount[key_third] = amount
        # print(dic_data['盈利能力'])

    # 重大合同,正则意外错误
    if dic_data['重大合同'] is not None:
        for major_contract in dic_data['重大合同']:
            if isinstance(major_contract, dict):
                for key_first, value_first in major_contract.items():
                    if key_first != '履行期限':
                        if re.search(r'^(-?\d+)(\.\d+)?$', str(value_first)):
                            if re.search(r'^(-?\d+)(\.\d+)$', str(value_first)):
                                value_first = float(value_first)
                            else:
                                value_first = int(value_first)
                            amount = "{:,}".format(value_first)
                            major_contract[key_first] = amount
        # print(dic_data['重大合同'])

    # 主要供应商
    if dic_data['主要供应商'] is not None:
        for major_supplier in dic_data['主要供应商']:
            if isinstance(major_supplier, dict):
                for key_first, value_first in major_supplier.items():
                    if key_first != '时间':
                        if re.search(r'^(-?\d+)(\.\d+)?$', str(value_first)):
                            if re.search(r'^(-?\d+)(\.\d+)$', str(value_first)):
                                value_first = float(value_first)
                            else:
                                value_first = int(value_first)
                            amount = "{:,}".format(value_first)
                            major_supplier[key_first] = amount
        # print(dic_data['主要供应商'])

    # 主要客户
    if dic_data['主要客户'] is not None:
        for major_client in dic_data['主要客户']:
            if isinstance(major_client, dict):
                for key_first, value_first in major_client.items():
                    if key_first != '时间':
                        if re.search(r'^(-?\d+)(\.\d+)?$', str(value_first)):
                            if re.search(r'^(-?\d+)(\.\d+)$', str(value_first)):
                                value_first = float(value_first)
                            else:
                                value_first = int(value_first)
                            amount = "{:,}".format(value_first)
                            major_client[key_first] = amount
        # print(dic_data['主要客户'])

    # 募集资金与运用
    if dic_data['募集资金与运用'] is not None:
        for fund_raising in dic_data['募集资金与运用']:
            if isinstance(fund_raising, dict):
                for key_first, value_first in fund_raising.items():
                    if re.search(r'^(-?\d+)(\.\d+)?$', str(value_first)):
                        if re.search(r'^(-?\d+)(\.\d+)$', str(value_first)):
                            value_first = float(value_first)
                        else:
                            value_first = int(value_first)
                        amount = "{:,}".format(value_first)
                        fund_raising[key_first] = amount
        # print(dic_data['募集资金与运用'])

    # # 重大诉讼事项
    if dic_data['重大诉讼事项'] is not None:
        for major_lawsuit in dic_data['重大诉讼事项']:
            if isinstance(major_lawsuit, dict):
                for key_first, value_first in major_lawsuit.items():
                    if re.search(r'^(-?\d+)(\.\d+)?$', str(value_first)):
                        if re.search(r'^(-?\d+)(\.\d+)$', str(value_first)):
                            value_first = float(value_first)
                        else:
                            value_first = int(value_first)
                        amount = "{:,}".format(value_first)
                        major_lawsuit[key_first] = amount
        # print(dic_data['重大诉讼事项'])

    # # 专利
    if dic_data['专利'] is not None:
        for major_lawsuit in dic_data['专利']:
            if isinstance(major_lawsuit, dict):
                acquisition_cost = major_lawsuit['取得成本']
                book_value = major_lawsuit['最近一期末账面价值']

                if re.search(r'^(-?\d+)(\.\d+)?$', str(acquisition_cost)):
                    if re.search(r'^(-?\d+)(\.\d+)$', str(acquisition_cost)):
                        acquisition_cost = float(acquisition_cost)
                    else:
                        acquisition_cost = int(acquisition_cost)
                    acquisition_cost = "{:,}".format(acquisition_cost)
                    major_lawsuit['取得成本'] = acquisition_cost

                if re.search(r'^(-?\d+)(\.\d+)?$', str(book_value)):
                    if re.search(r'^(-?\d+)(\.\d+)$', str(book_value)):
                        book_value = float(book_value)
                    else:
                        book_value = int(book_value)
                    book_value = "{:,}".format(book_value)
                    major_lawsuit['最近一期末账面价值'] = book_value
    #     # print(dic_data['专利'])

    return dic_data

class FormatChange():
    def format_change(self):
        # 文件内容读取
        for index_file, json_file in enumerate(os.listdir(json_file_path)):
            print(index_file, json_file)
            file_path = os.path.join(json_file_path, json_file)
            with open(file_path, encoding='utf-8') as p_file:
                dic_data = json.load(p_file)

            # # 时间格式规整
            # dic_data = json_time_change(dic_data)
            #
            # # 境外居住权规整
            # dic_data = overseas_residency_change(dic_data)
            #
            # #是否存在权属纠纷
            # dic_data = patent_ownership(dic_data)
            #
            # # 性别
            # dic_data = gander_change(dic_data)

            # 金额
            # dic_data = amount_change(dic_data)

            # print(dic_data['财务基本情况及财务指标'])


            json_data = json.dumps(dic_data, ensure_ascii=False).replace(" NaN", '"无"')
            # print(json_data)
            file_path_changed = os.path.join(json_file_changed, json_file)
            with open(file_path_changed, 'w', encoding='utf-8') as n_file:
                n_file.write(json_data)


if __name__ == '__main__':
    temp = FormatChange()
    temp.format_change()
