#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import json
import pandas as pd
import traceback

from collections import OrderedDict

excel_path = "file/excel"
json_path_origin = "file/json"
json_path_profit = "file/json_profit"
json_path_tmp = "C:\\Users\DMJ\Desktop\工作日常记录\资料\\time_change"
json_path_final = "C:\\Users\DMJ\Desktop\工作日常记录\资料\json_final"


class ExcelExtractor(object):
    """
        extractor for Excel
    """

    def __init__(self, excel_file):
        self.excel = pd.read_excel(excel_file)

    def extractor(self):
        print(self.excel.columns)
        pass

    def to_json(self):
        pass


class JsonCombiner(object):
    """
    """

    def __init__(self, origin_file):
        with open(origin_file) as o_file:
            self.origin_json = json.load(o_file)

    def add_profit(self, target_file):
        """
            融合盈利能力分析
        """
        with open(target_file) as t_file:
            self.target_json = json.load(t_file)

    def rename_json(self, target_file):
        """
            统一命名
        """


class JsonChecker(object):
    """
    """

    def __init__(self, json_file):
        with open(json_file, encoding='UTF-8') as j_file:
            self.json = json.load(j_file)

    def extractor(self):
        """
            json extractor
        """
        self.first_order()
        self.second_order()
        self.third_order()
        self.forth_order()
        self.key_format()

    def first_order(self):
        """
            一级模块顺序
        """
        title_list = (
            "招股说明书名称",
            "释义",
            "发行人基本情况",
            "控股股东简要情况",
            "实际控制人简要情况",
            "董事基本情况",
            "监事基本情况",
            "高管基本情况",
            "核心技术人员基本情况",
            "财务基本情况及财务指标",
            "重大诉讼事项",
            "募集资金与运用",
            "专利",
            "主要客户",
            "主要供应商",
            "重大合同",
            "发行人所处行业",
            "盈利能力"
        )
        # 顺序化
        self.json = OrderedDict([(key, self.json.get(key)) for key in title_list])
        for key in title_list:
            if key not in self.json.keys():
                self.json[key] = ""

    def second_order(self):
        """
            二级模块顺序
        """

        def ordered(origin, target_keys):
            if isinstance(origin, dict):
                origin = OrderedDict([(key, origin.get(key)) for key in target_keys])
                return origin
            elif isinstance(origin, list):
                for index, item in enumerate(origin):
                    if isinstance(item, list):
                        origin[index] = OrderedDict([(key, item[0].get(key)) for key in target_keys])
                    else:
                        origin[index] = OrderedDict([(key, item.get(key)) for key in target_keys])
                return origin
            else:
                print(type(origin))

        def repair(origin, target_keys):
            if isinstance(origin, dict):
                for key in target_keys:
                    if key not in origin.keys():
                        origin[key] = ""
                        print("字典", "二级类目缺失", key)
            elif isinstance(origin, list):
                for item in origin:
                    for key in target_keys:
                        if isinstance(item, dict):
                            if key not in item.keys():
                                item[key] = ""
                                print("列表", "二级类目缺失", key)
                        elif isinstance(item, list):
                            continue
                return

                # 发行人基本情况

        issuer_list = (
            "公司名称",
            "法定代表人姓名",
            "统一社会信用代码",
            "组织机构代码",
            "成立日期",
            "注册资本",
            "注册地址",
            "办公地址",
            "电话",
            "传真号码",
            "电子邮箱",
            "邮政编码"
        )
        print('**' * 20, '发行人基本情况', '**' * 20)
        repair(self.json['发行人基本情况'], issuer_list)
        self.json['发行人基本情况'] = ordered(self.json['发行人基本情况'], issuer_list)

        # 控股股东简要情况
        shareholder_list = (
            "法人",
            "自然人",
            "其他"
        )
        print('**' * 20, '控股股东简要情况', '**' * 20)
        repair(self.json['控股股东简要情况'], shareholder_list)
        self.json['控股股东简要情况'] = ordered(self.json['控股股东简要情况'], shareholder_list)

        # 实际控制人简要情况
        controller_list = (
            "国有控股主体",
            "自然人",
            "其他"
        )
        print('**' * 20, '实际控制人简要情况', '**' * 20)
        repair(self.json['实际控制人简要情况'], controller_list)
        self.json['实际控制人简要情况'] = ordered(self.json['实际控制人简要情况'], controller_list)

        # 董事基本情况
        director_list = (
            "姓名",
            "国籍",
            "境外居留权",
            "性别",
            "出生年月",
            "学历",
            "职称",
            "现任职务",
            "起始日期",
            "终止日期"
        )
        print('**' * 20, '董事基本情况', '**' * 20)
        repair(self.json['董事基本情况'], director_list)
        self.json['董事基本情况'] = ordered(self.json['董事基本情况'], director_list)

        # 监事基本情况
        supervisor_list = (
            "姓名",
            "国籍",
            "境外居留权",
            "性别",
            "出生年月",
            "学历",
            "职称",
            "现任职务",
            "起始日期",
            "终止日期"
        )
        print('**' * 20, '监事基本情况', '**' * 20)
        repair(self.json['监事基本情况'], supervisor_list)
        self.json['监事基本情况'] = ordered(self.json['监事基本情况'], supervisor_list)

        # 高管基本情况
        executive_list = (
            "姓名",
            "国籍",
            "境外居留权",
            "性别",
            "出生年月",
            "学历",
            "职称",
            "现任职务",
            "起始日期",
            "终止日期"
        )
        print('**' * 20, '高管基本情况', '**' * 20)
        repair(self.json['高管基本情况'], executive_list)
        self.json['高管基本情况'] = ordered(self.json['高管基本情况'], executive_list)

        # 核心技术人员基本情况
        technical_list = (
            "姓名",
            "国籍",
            "境外居留权",
            "性别",
            "出生年月",
            "学历",
            "职称",
            "现任职务",
            "起始日期",
            "终止日期"
        )
        print('**' * 20, '核心技术人员基本情况', '**' * 20)
        repair(self.json['核心技术人员基本情况'], technical_list)
        self.json['核心技术人员基本情况'] = ordered(self.json['核心技术人员基本情况'], technical_list)

        # 财务基本情况及财务指标
        financial_list = (
            "货币单位",
            "报表日期",
            "合并资产负债表",
            "合并现金流量表",
            "合并利润表",
            "主要财务指标表"
        )
        print('**' * 20, '财务基本情况及财务指标', '**' * 20)
        repair(self.json['财务基本情况及财务指标'], financial_list)
        self.json['财务基本情况及财务指标'] = ordered(self.json['财务基本情况及财务指标'], financial_list)
        # 重大诉讼事项
        litigation_list = (
            "事项",
            "起诉(申请)方",
            "应诉(被申请)方",
            "承担连带责任方",
            "诉讼仲裁类型",
            "诉讼涉及金额",
            "预计负债金额"
        )
        print('**' * 20, '重大诉讼事项', '**' * 20)
        repair(self.json['重大诉讼事项'], litigation_list)
        self.json['重大诉讼事项'] = ordered(self.json['重大诉讼事项'], litigation_list)

        # 募集资金与运用
        fund_ration_list = (
            "货币单位",
            "项目名称",
            "投资总额",
            "募集资金投资额",
            "募集资金投向"
        )
        print('**' * 20, '募集资金与运用', '**' * 20)
        repair(self.json['募集资金与运用'], fund_ration_list)
        self.json['募集资金与运用'] = ordered(self.json['募集资金与运用'], fund_ration_list)

        # 专利
        patent_list = (
            "专利类型",
            "专利名称",
            "专利号",
            "专利权人",
            "取得成本",
            "最近一期末账面价值",
            "取得日期",
            "使用期限",
            "是否存在权属纠纷"
        )
        print('**' * 20, '专利', '**' * 20)
        repair(self.json['专利'], patent_list)
        self.json['专利'] = ordered(self.json['专利'], patent_list)

        # 主要客户
        customer_list = (
            "时间",
            "货币单位",
            "客户名称",
            "下属单位名称",
            "销售额（万元）",
            "占主营收入比例（%）",
            "占营业收入比例（%）"
        )
        print('**' * 20, '主要客户', '**' * 20)
        repair(self.json['主要客户'], customer_list)
        self.json['主要客户'] = ordered(self.json['主要客户'], customer_list)

        # 主要供应商
        supplier_list = (
            "时间",
            "货币单位",
            "供应商名称",
            "采购内容",
            "采购额（万元）",
            "占总采购金额比例（%）"
        )
        print('**' * 20, '主要供应商', '**' * 20)
        repair(self.json['主要供应商'], supplier_list)
        self.json['主要供应商'] = ordered(self.json['主要供应商'], supplier_list)

        # 重大合同
        contract_list = (
            "货币单位",
            "合同类型",
            "合同对手方名称",
            "标的",
            "合同金额",
            "已履行金额",
            "履行期限",
            "备注"
        )
        print('**' * 20, '重大合同', '**' * 20)
        repair(self.json['重大合同'], contract_list)
        self.json['重大合同'] = ordered(self.json['重大合同'], contract_list)

        # 发行人所处行业
        industry_list = (
            "行业分类标准",
            "行业分类代码",
            "行业分类名称"
        )
        print('**' * 20, '发行人所处行业', '**' * 20)
        repair(self.json['发行人所处行业'], industry_list)
        self.json['发行人所处行业'] = ordered(self.json['发行人所处行业'], industry_list)

        # 盈利能力
        profit_list = (
            "报表日期",
            "营业收入分析",
            "营业成本分析"
        )
        print('**' * 20, '盈利能力', '**' * 20)
        repair(self.json['盈利能力'], profit_list)
        self.json['盈利能力'] = ordered(self.json['盈利能力'], profit_list)

    def third_order(self):
        """
            三级模块顺序
        """

        def ordered(origin, target_keys):
            if isinstance(origin, dict):
                print("初始结果: ", origin.keys())
                origin = OrderedDict([(key, origin.get(key)) for key in target_keys])
                print("转换结果: ", origin.keys())
                return origin
            elif isinstance(origin, list):
                if origin:
                    print("初始结果: ", origin[0])
                    for index, item in enumerate(origin):
                        origin[index] = OrderedDict([(key, item.get(key)) for key in target_keys])
                    print("转换结果: ", origin[0])
                return origin
            else:
                print("未知类型: ", type(origin))
                pass

        def repair(origin, target_keys):
            if isinstance(origin, dict):
                for key in target_keys:
                    if key not in origin.keys():
                        origin[key] = ""
                        print("字典", "三级类目缺失", key)
            else:
                return None

        # 控股股东简要情况-法人
        sharehold_legal_per_list = [
            "名称",
            "企业性质",
            "直接持股比例（%）",
            "间接持股比例（%）"
        ]
        print('==' * 20, '控股股东简要情况-法人', '==' * 20)
        try:
            repair(self.json['控股股东简要情况']['法人'], sharehold_legal_per_list)
            self.json['控股股东简要情况']['法人'] = ordered(self.json['控股股东简要情况']['法人'], sharehold_legal_per_list)
        except:
            print('==' * 20, '控股股东简要情况-法人, ERROR', '==' * 20)
            pass

        # 控股股东简要情况-自然人
        sharehold_natural_per_list = [
            "姓名",
            "身份证号",
            "国籍",
            "直接持股比例（%）",
            "间接持股比例（%）"
        ]
        print('==' * 20, '控股股东简要情况-自然人', '==' * 20)
        try:
            repair(self.json['控股股东简要情况']['自然人'], sharehold_natural_per_list)
            self.json['控股股东简要情况']['自然人'] = ordered(self.json['控股股东简要情况']['自然人'], sharehold_natural_per_list)
        except:
            print('==' * 20, '控股股东简要情况-自然人-ERROR', '==' * 20)

        # 控股股东简要情况-其他
        sharehold_others_list = [
            "名称",
            "性质",
            "直接持股比例（%）",
            "间接持股比例（%）"
        ]
        print('==' * 20, '控股股东简要情况-其他', '==' * 20)
        try:
            repair(self.json['控股股东简要情况']['其他'], sharehold_others_list)
            self.json['控股股东简要情况']['其他'] = ordered(self.json['控股股东简要情况']['其他'], sharehold_others_list)
        except:
            print('==' * 20, '控股股东简要情况-其他-ERROR', '==' * 20)
            pass

        # 实际控制人简要情况-国有控股主体
        con_state_holding_list = [
            "名称",
            "单位负责人",
            "直接持股比例（%）",
            "间接持股比例（%）"
        ]
        print('==' * 20, '实际控制人简要情况-法人', '==' * 20)
        try:
            repair(self.json['实际控制人简要情况']['国有控股主体'], con_state_holding_list)
            self.json['实际控制人简要情况']['国有控股主体'] = ordered(self.json['实际控制人简要情况']['国有控股主体'], con_state_holding_list)
        except:
            print('==' * 20, '实际控制人简要情况-国有控股主体-ERROR', '==' * 20)

        # 实际控制人简要情况-自然人
        con_natural_per_list = [
            "姓名",
            "身份证号",
            "国籍",
            "直接持股比例（%）",
            "间接持股比例（%）"
        ]
        print('==' * 20, '实际控制人简要情况-自然人', '==' * 20)
        try:
            repair(self.json['实际控制人简要情况']['自然人'], con_natural_per_list)
            self.json['实际控制人简要情况']['自然人'] = ordered(self.json['实际控制人简要情况']['自然人'], con_natural_per_list)
        except:
            print('==' * 20, '实际控制人简要情况-自然人-ERROR', '==' * 20)
            pass

        # 实际控制人简要情况-其他
        con_others_list = [
            "名称",
            "性质",
            "直接持股比例（%）",
            "间接持股比例（%）",
            "其中：质押股份数量（万股）"
        ]
        print('==' * 20, '实际控制人简要情况-其他', '==' * 20)
        try:
            repair(self.json['实际控制人简要情况']['自然人'], con_others_list)
            self.json['实际控制人简要情况']['其他'] = ordered(self.json['实际控制人简要情况']['其他'], con_others_list)
        except:
            print('==' * 20, '实际控制人简要情况-其他-ERROR', '==' * 20)

        # 财务基本情况及财务指标-合并资产负债表
        fin_bala_list = [
            "流动资产",
            "非流动资产",
            "资产总计",
            "流动负债",
            "非流动负债",
            "负债合计",
            "所有者权益（或股东权益）",
            "负债和所有者权益总计"
        ]

        # 财务基本情况及财务指标-合并利润表
        fin_profit_list = [
            "营业总收入",
            "营业总成本",
            "营业利润",
            "每股收益",
            "其他综合收益",
            "综合收益总额",
            "归属于母公司所有者的综合收益总额",
            "归属于少数股东的综合收益总额"
        ]

        # 财务基本情况及财务指标-合并现金流量表
        fin_cash_list = [
            "经营活动产生的现金流量",
            "销售商品、提供劳务收到的现金",
            "客户存款和同业存放款项净增加额",
            "向中央银行借款净增加额",
            "向其他金融机构拆入资金净增加额",
            "收到原保险合同保费取得的现金",
            "收到再保险业务现金净额",
            "保户储金及投资款净增加额",
            "处置交易性金融资产净增加额",
            "收取利息、手续费及佣金的现金",
            "拆入资金净增加额",
            "回购业务资金净增加额",
            "收到的税费返还",
            "收到其他与经营活动有关的现金",
            "经营活动现金流入小计",
            "购买商品、接受劳务支付的现金",
            "客户贷款及垫款净增加额",
            "存放中央银行和同业款项净增加额",
            "支付原保险合同赔付款项的现金",
            "支付利息、手续费及佣金的现金",
            "支付保单红利的现金",
            "支付给职工以及为职工支付的现金",
            "支付的各项税费",
            "支付其他与经营活动有关的现金",
            "经营活动现金流出小计",
            "经营活动产生的现金流量净额",
            "投资活动产生的现金流量",
            "收回投资收到的现金",
            "取得投资收益收到的现金",
            "处置固定资产、无形资产和其他长期资产收回的现金净额",
            "处置子公司及其他营业单位收到的现金净额",
            "收到其他与投资活动有关的现金",
            "投资活动现金流入小计",
            "购建固定资产、无形资产和其他长期资产支付的现金",
            "投资支付的现金",
            "质押贷款净增加额",
            "取得子公司及其他营业单位支付的现金净额",
            "支付其他与投资活动有关的现金",
            "投资活动现金流出小计",
            "投资活动产生的现金流量净额",
            "筹资活动产生的现金流量",
            "吸收投资收到的现金",
            "其中：子公司吸收少数股东投资收到的现金",
            "取得借款收到的现金",
            "发行债券收到的现金",
            "收到其他与筹资活动有关的现金",
            "筹资活动现金流入小计",
            "偿还债务支付的现金",
            "分配股利、利润或偿付利息支付的现金",
            "其中：子公司支付给少数股东的股利、利润",
            "支付其他与筹资活动有关的现金",
            "筹资活动现金流出小计",
            "筹资活动产生的现金流量净额",
            "汇率变动对现金及现金等价物的影响",
            "现金及现金等价物净增加额",
            "加：期初现金及现金等价物余额",
            "期末现金及现金等价物余额"
        ]

        # 财务基本情况及财务指标-基本财务指标
        fin_index_list = [
            "流动比率(倍)",
            "速动比率(倍)",
            "资产负债率（合并）",
            "资产负债率(母公司）",
            "无形资产（扣除土地使用权、水面养殖权和采矿权等后）占净资产的比例（%）",
            "应收账款周转率(次/年)",
            "存货周转率(次/年)",
            "总资产周转率(次/年)",
            "息税折旧摊销前利润(元)",
            "利息保障倍数(倍)",
            "扣除非经常性损益后的每股基本收益（元）",
            "每股经营活动产生的现金流量(元)",
            "每股净现金流量(元)",
            "加权平均净资产收益率"
        ]
        try:
            for item in self.json['财务基本情况及财务指标']:
                print('==' * 20, '财务基本情况及财务指标-合并资产负债表', '==' * 20)
                repair(item['合并资产负债表'], fin_bala_list)
                item['合并资产负债表'] = ordered(item['合并资产负债表'], fin_bala_list)

                print('==' * 20, '财务基本情况及财务指标-合并利润表', '==' * 20)
                repair(item['合并利润表'], fin_profit_list)
                item['合并利润表'] = ordered(item['合并利润表'], fin_profit_list)

                print('==' * 20, '财务基本情况及财务指标-合并现金流量表', '==' * 20)
                repair(item['合并现金流量表'], fin_cash_list)
                item['合并现金流量表'] = ordered(item['合并现金流量表'], fin_cash_list)

                print('==' * 20, '财务基本情况及财务指标-基本财务指标', '==' * 20)
                repair(item['基本财务指标'], fin_index_list)
                item['基本财务指标'] = ordered(item['基本财务指标'], fin_index_list)
        except:
            pass

        # 盈利能力-营业收入分析
        profit_income_list = [
            "主营业务收入按产品构成分析",
            "主营业务收入按业务构成分析"
        ]
        # 盈利能力-营业成本分析
        profit_cost_list = [
            "主营业务成本按产品构成分析",
            "主营业务成本按业务构成分析"
        ]

        for item in self.json['盈利能力']:
            print('==' * 20, '盈利能力-营业收入分析', '==' * 20)
            repair(item['营业收入分析'], profit_income_list)
            item['营业收入分析'] = ordered(item['营业收入分析'], profit_income_list)

            print('==' * 20, '盈利能力-营业成本分析', '==' * 20)
            repair(item['营业成本分析'], profit_cost_list)
            item['营业成本分析'] = ordered(item['营业成本分析'], profit_cost_list)

    def forth_order(self):
        """
            四级模块分析
        """

        def ordered(origin, target_keys):
            if isinstance(origin, dict):
                print("初始结果: ", origin.keys())
                origin = OrderedDict([(key, origin.get(key)) for key in target_keys])
                print("转换结果: ", origin.keys())
                return origin
            elif isinstance(origin, list):
                if origin:
                    print("初始结果: ", origin[0])
                    for index, item in enumerate(origin):
                        origin[index] = OrderedDict([(key, item.get(key)) for key in target_keys])
                    print("转换结果: ", origin[0])
                return origin
            else:
                print("未知类型: ", type(origin))
                pass

        def repair(origin, target_keys):
            if isinstance(origin, dict):
                for key in target_keys:
                    if key not in origin.keys():
                        origin[key] = ""
                        print("字典", "四级类目缺失", key)
            else:
                return None

        # 财务基本情况及财务指标-合并资产负债表-流动资产
        fin_bala_current_assets_list = [
            "货币资金",
            "结算备付金",
            "拆出资金",
            "交易性金融资产",
            "应收票据",
            "应收账款",
            "预付款项",
            "应收保费",
            "应收分保账款",
            "应收分保合同准备金",
            "应收利息",
            "应收股利",
            "其他应收款",
            "买入返售金融资产",
            "存货",
            "一年内到期的非流动资产",
            "其他流动资产",
            "流动资产合计"
        ]

        # 财务基本情况及财务指标-合并资产负债表-非流动资产
        fin_bala_current_non_assets_list = [
            "发放委托贷款及垫款",
            "可供出售金融资产",
            "持有至到期投资",
            "长期应收款",
            "长期股权投资",
            "投资性房地产",
            "固定资产",
            "在建工程",
            "工程物资",
            "固定资产清理",
            "生产性生物资产",
            "油气资产",
            "无形资产",
            "开发支出",
            "商誉",
            "长期待摊费用",
            "递延所得税资产",
            "其他非流动资产",
            "非流动资产合计"
        ]

        # 财务基本情况及财务指标-合并资产负债表-资产总计
        fin_bala_asset_all = [
            "资产总计"
        ]

        # 财务基本情况及财务指标-合并资产负债表-流动负债
        fin_bala_current_liability_list = [
            "短期借款",
            "向中央银行借款",
            "吸收存款及同业存放",
            "拆入资金",
            "交易性金融负债",
            "应付票据",
            "应付账款",
            "预收款项",
            "卖出回购金融资产款",
            "应付手续费及佣金",
            "应付职工薪酬",
            "应交税费",
            "应付利息",
            "应付股利",
            "其他应付款",
            "应付分保账款",
            "保险合同准备金",
            "代理买卖证券款",
            "代理承销证券款",
            "一年内到期的非流动负债",
            "其他流动负债",
            "流动负债合计"
        ]

        # 财务基本情况及财务指标-合并资产负债表-非流动负债
        fin_bala_non_current_liability_list = [
            "长期借款",
            "应付债券",
            "长期应付款",
            "专项应付款",
            "预计负债",
            "递延所得税负债",
            "其他非流动负债",
            "非流动负债合计"
        ]

        # 财务基本情况及财务指标-合并资产负债表-负债合计
        fin_bala_liability_all_list = [
            "负债合计"
        ]

        # 财务基本情况及财务指标-合并资产负债表-所有权益
        fin_bala_equity_list = [
            "实收资本（或股本）",
            "资本公积",
            "减：库存股",
            "专项储备",
            "盈余公积",
            "一般风险准备",
            "未分配利润",
            "外币报表折算差额",
            "归属于母公司所有者权益合计",
            "少数股东权益",
            "所有者权益合计"
        ]
        fin_bala_equity_all_list = [
            "负债和所有者权益总计"
        ]

        # 财务基本情况及财务指标-合并利润表-营业收入
        fin_profit_income_all_list = [
            "营业总收入",
            "营业收入",
            "利息收入",
            "已赚保费",
            "手续费及佣金收入"
        ]

        # 财务基本情况及财务指标-合并利润表-营业成本
        fin_profit_cost_all_list = [
            "营业总成本",
            "其中：营业成本",
            "利息支出",
            "手续费及佣金支出",
            "退保金",
            "赔付支出净额",
            "提取保险合同准备金净额",
            "保单红利支出",
            "分保费用",
            "营业税金及附加",
            "销售费用",
            "管理费用",
            "财务费用",
            "资产减值损失",
            "加：公允价值变动收益（损失以“-”号填列）",
            "投资收益（损失以“-”号填列）",
            "其中：对联营企业和合营企业的投资收益",
            "汇兑收益（损失以“-”号填列）"
        ]

        # 财务基本情况及财务指标-合并利润表-营业利润
        fin_profit_operation_list = [
            "营业利润（损失以“-”号填列）",
            "加：营业外收入",
            "减：营业外支出",
            "其中：非流动资产处置损失",
            "四、利润总额（损失以“-”号填列）",
            "减：所得税费用",
            "五、净利润（净损失以“-”号填列）",
            "其中：被合并方在合并前实现的净利润",
            "归属于母公司所有者的净利润",
            "少数股东损益",
        ]

        # 财务基本情况及财务指标-合并利润表-每股收益
        fin_profit_stock_list = [
            "每股收益",
            "基本每股收益",
            "稀释每股收益"
        ]

        try:
            for item in self.json['财务基本情况及财务指标']:
                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-流动资产', '==' * 20)
                item['合并资产负债表']['流动资产'] = ordered(item['合并资产负债表']['流动资产'], fin_bala_current_assets_list)

                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-非流动资产', '==' * 20)
                item['合并资产负债表']['非流动资产'] = ordered(item['合并资产负债表']['非流动资产'], fin_bala_current_non_assets_list)

                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-资产总计', '==' * 20)
                item['合并资产负债表']['资产总计'] = ordered(item['合并资产负债表']['资产总计'], fin_bala_asset_all)

                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-流动负债', '==' * 20)
                item['合并资产负债表']['流动负债'] = ordered(item['合并资产负债表']['流动负债'], fin_bala_current_liability_list)

                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-非流动负债', '==' * 20)
                item['合并资产负债表']['非流动负债'] = ordered(item['合并资产负债表']['非流动负债'], fin_bala_non_current_liability_list)

                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-负债合计', '==' * 20)
                item['合并资产负债表']['负债合计'] = ordered(item['合并资产负债表']['负债合计'], fin_bala_liability_all_list)

                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-所有者权益（或股东权益）', '==' * 20)
                item['合并资产负债表']['所有者权益（或股东权益）'] = ordered(item['合并资产负债表']['所有者权益（或股东权益）'], fin_bala_equity_list)

                print('==' * 20, '财务基本情况及财务指标-合并资产负债表-权益总计', '==' * 20)
                item['合并资产负债表']['负债和所有者权益总计'] = ordered(item['合并资产负债表']['负债和所有者权益总计'], fin_bala_equity_all_list)

                print('==' * 20, '财务基本情况及财务指标-合并利润表-营业总收入', '==' * 20)
                item['合并利润表']['营业总收入'] = ordered(item['合并利润表']['营业总收入'], fin_profit_income_all_list)

                print('==' * 20, '财务基本情况及财务指标-合并利润表-营业总成本', '==' * 20)
                item['合并利润表']['营业总成本'] = ordered(item['合并利润表']['营业总成本'], fin_profit_cost_all_list)

                print('==' * 20, '财务基本情况及财务指标-合并利润表-营业利润', '==' * 20)
                item['合并利润表']['营业利润'] = ordered(item['合并利润表']['营业利润'], fin_profit_operation_list)

                print('==' * 20, '财务基本情况及财务指标-合并利润表-每股收益', '==' * 20)
                item['合并利润表']['每股收益'] = ordered(item['合并利润表']['每股收益'], fin_profit_stock_list)
        except:
            pass

        # 盈利能力-营业收入分析-主营业务收入按产品构成分析
        profit_income_product_list = [
            "货币单位",
            "产品类别",
            "金额",
            "占比（%）",
            "变动比例（%）"
        ]

        # 盈利能力-营业收入分析-主营业务收入按业务构成分析
        profit_income_business_list = [
            "货币单位",
            "业务类别",
            "金额",
            "占比（%）",
            "变动比例（%）"
        ]

        # 盈利能力-营业成本分析-主营业务成本按产品构成分析
        profit_cost_product_list = [
            "货币单位",
            "产品类别",
            "金额",
            "占比（%）",
            "变动比例（%）"
        ]

        # 盈利能力-营业成本分析-主营业务成本按业务构成分析
        profit_cost_business_list = [
            "货币单位",
            "业务类别",
            "金额",
            "占比（%）",
            "变动比例（%）"
        ]
        for item in self.json['盈利能力']:
            print('==' * 20, '盈利能力-营业收入分析-主营业务收入按产品构成分析', '==' * 20)
            item['营业收入分析']['主营业务收入按产品构成分析'] = ordered(item['营业收入分析']['主营业务收入按产品构成分析'], profit_income_product_list)

            print('==' * 20, '盈利能力-营业收入分析-主营业务收入按业务构成分析', '==' * 20)
            item['营业收入分析']['主营业务收入按业务构成分析'] = ordered(item['营业收入分析']['主营业务收入按业务构成分析'], profit_income_business_list)

            print('==' * 20, '盈利能力-营业成本分析-主营业务成本按产品构成分析', '==' * 20)
            item['营业成本分析']['主营业务成本按产品构成分析'] = ordered(item['营业成本分析']['主营业务成本按产品构成分析'], profit_cost_product_list)

            print('==' * 20, '盈利能力-营业成本分析-主营业务成本按业务构成分析', '==' * 20)
            item['营业成本分析']['主营业务成本按业务构成分析'] = ordered(item['营业成本分析']['主营业务成本按业务构成分析'], profit_cost_business_list)

    def key_format(self):
        """
            key_format
        """
        json_format = self.json

        try:
            # 控股股东简要情况自然人姓名更改
            for item in json_format['控股股东简要情况']['自然人']:
                item['名称'] = item.pop('姓名')

            # 实际控制人自然人姓名更改
            for item in json_format['实际控制人简要情况']['自然人']:
                item['名称'] = item.pop('姓名')

            # 重大诉讼事项
            for item in json_format['重大诉讼事项']:
                item["货币单位"] = ""

            # 主要客户
            for item in json_format['主要客户']:
                item["货币单位"] = ""

            # 主要供应商
            for item in json_format['主要供应商']:
                item["货币单位"] = ""

            self.json = json_format
        except:
            traceback.print_exc()

    def value_format(self):
        """
            value_format
        """
        json_format = self.json


# 融合盈利能力分析部分
def combine_profit(json_path):
    for index_origin, json_origin in enumerate(os.listdir(json_path)):
        origin_path = os.path.join(json_path, json_origin)
        new_json = os.path.join(json_path_tmp, json_origin)
        if os.path.exists(new_json):
            continue

        print(json_origin)
        for index_profit, json_profit in enumerate(os.listdir(json_path_profit)):
            if json_origin[4:10] in json_profit:
                profit_path = os.path.join(json_path_profit, json_profit)
                print(index_origin, json_origin, json_profit)
                with open(profit_path) as p_file:
                    profit_json = json.load(p_file)

                with open(origin_path) as o_file:
                    origin_json = json.load(o_file)

                origin_json['盈利能力'] = profit_json

                target_json = json.dumps(origin_json, ensure_ascii=False).replace("nan", '无')
                target_json = target_json.replace("null", "\"无\"")
                with open(new_json, 'w') as n_file:
                    n_file.write(target_json)
            else:
                print(index_origin, json_origin, json_profit)
                pass


# json文件重命名
def rename_json(json_path_final):
    for index_origin, json_name in enumerate(os.listdir(json_path_final)):
        origin_path = os.path.join(json_path_final, json_name)
        for index_target, json_target in enumerate(os.listdir('file/pdf/招股书')):
            pdf_path = os.path.join('file/pdf', json_target)
            if json_name[1:10] in json_target:
                new_json_origin = (json_target.split('_')[1]).split('.')[0]
                new_json_origin = new_json_origin.replace(' ','')
                new_origin_path = os.path.join(json_path_final, new_json_origin + '.json')
                try:
                    os.rename(origin_path, new_origin_path)
                except:
                    continue
                print(index_origin, json_name, json_target, new_json_origin)


if __name__ == "__main__":

    # 1. 融合盈利能力分析
    # combine_profit(json_path_origin)

    # 2. json排序, key值标准化，value值标准化
    for index, json_file in enumerate(os.listdir(json_path_tmp)):
        print(json_file)
        json_checker = JsonChecker(os.path.join(json_path_tmp, json_file))
        json_checker.extractor()
        json_format = json_checker.json
        json_format['招股说明书名称'] = json_file.split('.')[0]
        json_final_path = os.path.join(json_path_final, json_file)
        with open(json_final_path, 'w',encoding='UTF-8')  as f_file:
            f_file.write(json.dumps(json_format, ensure_ascii=False))
        # break

    # 3. json重命名
    # rename_json(json_path_final)
