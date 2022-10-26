import requests

from Util.AssertUtil import AssertUtil
from Util.DataUtil import SetUtil
from Util.RequestUtil import Request


class TestCase:

    def __init__(self, host):
        """
            1、初始化请求方法
            2、初始化断言方法
            3、初始化自增变量
        """
        self.request = Request()
        self.assert_util = AssertUtil()
        self.host = host
        self.number = SetUtil().setup_autonumber()
        self.time = SetUtil().setup_datetime()
        self.contract_id = self.add_contract()

    def get_token(self):
        """ 获取用户token """
        url = self.host + "/admin/public/login"
        data = {
            "mobile": "19999999999",
            "password": "JKajQrdhoqemXXEog8zgPg=="
        }
        response = self.request.post(url, json=data)
        self.assert_util.assert_code(response['code'], 200)
        try:
            user_token = response['body']['data']
            return user_token
        except:
            print("未取到token，请检查请求参数是否正确！")

    def add_contract(self):
        """ 新增合同 """
        url = self.host + "/admin/contract/add"
        headers = {
            "Authorization": self.get_token(),
            "Content-Type": "application/json"
        }
        data = {
            "advanceCharge": 2,
            "contractName": "rc-upload-1666415394906-4",
            "contractUrl": "https://wmeimob-frame.oss-cn-shanghai.aliyuncs.com/juduo_temp/b562b38e-08cd-6698-536a-dcf72f8f77b7.pdf",
            "firstPartyName": "上海惊鹿",
            "firstPartyPersonChargeIds": "13041151",
            "name": "文涛的测试合同_1" + self.number,
            "operationFunds": 3,
            "outCode": "WBHT_TEST_1" + self.number,
            "paymentReceived": 3,
            "price": 500000,
            "retentionMoney": 2,
            "secondPartyName": "北京世卓泽坤科技有限公司",
            "signPlace": "上海市宝山区中成智谷",
            "signTime": self.time[0]
        }
        response = self.request.post(url, headers=headers, json=data)
        self.assert_util.assert_code(response['code'], 200)
        try:
            contract_id = response['body']['data']
            return contract_id
        except:
            print("未取到合同ID，请检查请求参数是否正确！")
        # contract_id = response['body']['data']
        # return contract_id

    def add_one_supplyList(self):
        """ 新增供货清单 """
        url = self.host + "/admin/contract/supplyList/add"
        headers = {
            "Authorization": self.get_token(),
            "Content-Type": "application/json"
        }
        data = {
            "contractId": self.contract_id,  # 合同ID
            "amount": 55,  # 数量
            "name": "钢丝",  # 采购内容
            "remark": "钢丝采购",  # 备注
            "spec": "100mm",  # 规格
            "unit": "吨",  # 单位
            "unitPrice": 99  # 单价
        }
        response = self.request.post(url, headers=headers, json=data)
        self.assert_util.assert_in_body(response['code'], "'code': 0")
        print(f"供货清单新增成功，采购内容为：{data['name']}, 返回body: {response['body']}")

    def add_two_supplyList(self):
        """ 新增供货清单 """
        url = self.host + "/admin/contract/supplyList/add"
        headers = {
            "Authorization": self.get_token(),
            "Content-Type": "application/json"
        }
        data = {
            "contractId": self.contract_id,  # 合同ID
            "amount": 88,  # 数量
            "name": "废油",  # 采购内容
            "remark": "废气采购",  # 备注
            "spec": "95#",  # 规格
            "unit": "升",  # 单位
            "unitPrice": 8.1  # 单价
        }
        response = self.request.post(url, headers=headers, json=data)
        self.assert_util.assert_in_body(response['code'], "'code': 0")
        print(f"供货清单新增成功，采购内容为：{data['name']}, 返回body: {response['body']}")

    def add_project(self):
        """ 新增项目 """
        url = self.host + "/admin/project/add"
        headers = {
            "Authorization": self.get_token(),
            "Content-Type": "application/json"
        }
        data = {
            "name": "文涛的测试项目_1" + self.number,  # 项目名称
            "contractId": self.contract_id,  # 合同ID
            "projectStartDate": self.time[0],  # 项目开始时间
            "projectEndDate": self.time[10],  # 项目结束时间
            "chargePersonDate": self.time[1],  # 项目总负责人完成时间
            "chargePersonIds": "13041048,13041141,13041082",  # 项目总负责人ID
            "designerDate": self.time[2],  # 设计完工时间
            "designerIds": "13041048,13041141,13041082",  # 设计人员ID
            "productionPreparationDate": self.time[3],  # 生产准备部完工时间
            "productionPreparationIds": "13041048,13041141,13041082",  # 生产准备部人员ID
            "purchaserDate": self.time[4],  # 采购完工时间
            "purchaserIds": "13041048,13041141,13041082",  # 采购人员ID
            "machiningDate": self.time[5],  # 加工完工时间
            "machiningIds": "13041048,13041141,13041082",  # 加工队伍人员ID
            "supplierDate": self.time[6],  # 供应商完工时间
            "supplierIds": "13041050,13041157,13041118",  # 供应商ID
            "rawMaterialManagerDate": self.time[7],  # 原材料/仓库管理员完工时间
            "rawMaterialManagerIds": "13041141,13041048,13041082",  # 原材料/仓库管理员ID
            "siteServiceDate": self.time[8],  # 现场服务完工时间
            "siteServiceIds": "13041141,13041048,13041082",  # 现场服务人员ID
            "logisticsDate": self.time[9],  # 物流完工时间
            "logisticsIds": "13041158,13041121",  # 物流人员ID
            "illustrate": "这里是项目的说明"  # 项目说明
        }
        response = self.request.post(url, headers=headers, json=data)
        self.assert_util.assert_in_body(response['code'], "'code': 40000")
        print(f"项目创建成功，项目名称：{data['name']}, 返回body: {response['body']}")

    def get_contract_list(self):
        """ 获取合同列表 """
        url = self.host + "/admin/contract/list"
        headers = {
            "Authorization": self.get_token()
        }
        data = {
            "pageSize": 20,
            "pageNum": 1
        }
        response = self.request.get(url, headers=headers, params=data)
        print(response['body']['data'])


if __name__ == '__main__':
    testcase = TestCase("https://test12.ahweimeng.cn")
    testcase.add_supplyList()
