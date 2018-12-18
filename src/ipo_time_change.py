import json
import re
import os
json_file_path = 'C:\\Users\DMJ\Desktop\工作日常记录\资料\\time_json'

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
def time_change(time):
    time = str(time)
    value = time.strip()
    # 2016.12.31
    if re.search(r'^\d{4}\.\d{1,2}\.\d{1,2}$', value):
        value = value.replace(".", "-")

    # 2020-05-09 00:00:00
    if re.search(r'^\d{4}\-\d{1,2}(\-\d{1,2})\s*\d{2}\:\d{2}\:\d{2}$', value):
        value = value.replace(" 00:00:00", "")

    # 2016 年 12 月 31 日
    if re.search(r'^\d{4}\s*[\u4E00-\u9FFF]\s*\d{1,2}\s*[\u4E00-\u9FFF]\s*\d{1,2}\s*[\u4E00-\u9FFF]$', value):
        value = value.replace("年", "-")
        value = value.replace("月", "-")
        value = value.replace("日", "")
        value = value.replace(" ", "")

    # 2016 年 4 月
    if re.search(r'^\d{4}\s*[\u4E00-\u9FFF]\s*\d{1,2}\s*[\u4E00-\u9FFF]$', value):
        value = value.replace("年", "-")
        value = value.replace("月", "")
        value = value.replace(" ", "")

    # 2018 年
    if re.search(r'^\d{4}\s*[\u4E00-\u9FFF]\s*$', value):
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
    if re.search(
            r'^[\u4E00-\u9FFF]*\s*\d{4}\s*[\u4E00-\u9FFF]\s*\d{1,2}\s*[\u4E00-\u9FFF]\s*\d{1,2}\s*[\u4E00-\u9FFF]+\s*\d{4}\s*'
            r'[\u4E00-\u9FFF]\s*\d{1,2}\s*[\u4E00-\u9FFF]\s*\d{1,2}\s*[\u4E00-\u9FFF]+', value):
        value = value.replace("年", "-")
        value = value.replace("月", "-")
        value = value.replace("日", "")
        value = value.replace(" ", "")
        time_list = re.findall(r'\d{4}\-\d{1,2}\-\d{1,2}', value)
        value = time_list[0] + '~' + time_list[1]

    # 2018-01-01 至 2018-12-31
    if re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}\s*[\u4E00-\u9FFF]+\s*\d{4}\-\d{1,2}\-\d{1,2}$', value):
        time_list = re.findall(r'\d{4}\-\d{1,2}\-\d{1,2}', value)
        value = time_list[0] + '~' + time_list[1]

    return value

# 董监高
def time_person_change(dic_data):
    for sup_infor in dic_data['监事基本情况']:
        sup_infor['出生年月'] = time_change(sup_infor['出生年月'])
        sup_infor['起始日期'] = time_change(sup_infor['起始日期'])
        sup_infor['终止日期'] = time_change(sup_infor['终止日期'])

    for dir_infor in dic_data['董事基本情况']:
        dir_infor['出生年月'] = time_change(dir_infor['出生年月'])
        dir_infor['起始日期'] = time_change(dir_infor['起始日期'])
        dir_infor['终止日期'] = time_change(dir_infor['终止日期'])

    for man_infor in dic_data['高管基本情况']:
        sup_infor['出生年月'] = time_change(man_infor['出生年月'])
        man_infor['起始日期'] = time_change(man_infor['起始日期'])
        man_infor['终止日期'] = time_change(man_infor['终止日期'])

    for core_tec_infor in dic_data['核心技术人员基本情况']:
        core_tec_infor['出生年月'] = time_change(core_tec_infor['出生年月'])
        core_tec_infor['起始日期'] = time_change(core_tec_infor['起始日期'])
        core_tec_infor['终止日期'] = time_change(core_tec_infor['终止日期'])

    return dic_data

# 发行人相关信息
def time_issuer_change(dic_data):
    dic_data['发行人基本情况']['成立日期'] = time_change(dic_data['发行人基本情况']['成立日期'])
    return dic_data

# 主要客户
def time_major_client(dic_data):
    for time_temp in dic_data['主要客户']:
        time_temp['时间'] = time_change(time_temp['时间'])
    return dic_data

# 主要供应商
def time_major_supplier(dic_data):
    for time_temp in dic_data['主要供应商']:
        time_temp['时间'] = time_change(time_temp['时间'])
    return dic_data

# 重大合同
def time_major_contract(dic_data):
    for time_temp in dic_data['重大合同']:
        time_temp['履行期限'] = time_change(time_temp['履行期限'])
    return dic_data

# 两层结构
def time_change_common(dic_data, fist_floor, second_floor):
    for time_temp in dic_data[fist_floor]:
        time_temp[second_floor] = time_change(time_temp[second_floor])
    return dic_data

class TimeChange():
    def json_time_change(self):
        # 文件内容读取
        # for index_file, json_file in enumerate(os.listdir(json_file_path)):
        #     print(index_file, json_file)
        #     file_path = os.path.join(json_file_path, json_file)

        with open(r'C:\Users\DMJ\Desktop\工作日常记录\资料\time_json\001_万兴科技股份有限公司.json', encoding='utf-8') as p_file:
            dic_data = json.load(p_file)
            # dic_data = time_person_change(dic_data)
            # dic_data = time_issuer_change(dic_data)
            # dic_data = time_major_client(dic_data)
            # dic_data = time_major_client(dic_data)

            # 重大合同
            dic_data = time_change_common(dic_data, '重大合同', '履行期限')
            # 盈利能力
            dic_data = time_change_common(dic_data, '盈利能力', '报表日期')
            # 资产负债
            dic_data = time_change_common(dic_data, '盈利能力', '报表日期')
            # 财务基本情况及财务指标
            dic_data = time_change_common(dic_data, '财务基本情况及财务指标', '报表日期')

            print(dic_data['财务基本情况及财务指标'])



            # json_data = json.dumps(dic_data, ensure_ascii=False)
            # print(json_data)

        # with open(r'C:\Users\DMJ\Desktop\工作日常记录\资料\time_json\001_万兴科技股份有限公司.json', 'w', encoding='utf-8') as n_file:
        #     n_file.write(json_data)



if __name__ == '__main__':
    temp = TimeChange()
    temp.json_time_change()
