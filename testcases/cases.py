from Util.RequestUtil import Request
from Util.AssertUtil import AssertUtil
from Util.DataUtil import SetUtil


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
            "signTime": self.time
        }
        response = self.request.post(url, headers=headers, json=data)
        self.assert_util.assert_code(response['code'], 200)
        try:
            contract_id = response['body']['data']
            return contract_id
        except:
            print("未取到合同ID，请检查请求参数是否正确！")

    def add_supplyList(self):
        """ 新增供货清单 """
        url = self.host + "/admin/contract/supplyList/add"
        headers = {
            "Authorization": self.get_token(),
            "Content-Type": "application/json"
        }
        data = {
            "contractId": self.add_contract(),  # 合同ID
            "amount": 55,  # 数量
            "name": "钢丝",  # 采购内容
            "remark": "钢丝采购",  # 备注
            "spec": "100mm",  # 规格
            "unit": "吨",  # 单位
            "unitPrice": 99  # 单价
        }
        response = self.request.post(url, headers=headers, json=data)
        self.assert_util.assert_code(response['code'], 200)
        print(response['body'])

    def add_project(self):
        """ 新增项目 """
        url = self.host + "/admin/project/add"
        headers = {
            "Authorization": self.get_token(),
            "Content-Type": "application/json"
        }
        data = {
            "name": "文涛的测试项目_05",  # 项目名称
            "contractId": 67,  # 合同ID
            "projectStartDate": self.time,  # 项目开始时间
            "projectEndDate": "2022-11-05",  # 项目结束时间
            "chargePersonDate": "2022-10-25",  # 项目总负责人完成时间
            "chargePersonIds": "13041141,13041048",  # 项目总负责人ID
            "designerDate": "2022-10-26",  # 设计完工时间
            "designerIds": "13041141,13041048",  # 设计人员ID
            "productionPreparationDate": "2022-10-27",  # 生产准备部完工时间
            "productionPreparationIds": "13041141,13041048",  # 生产准备部人员ID
            "purchaserDate": "2022-10-28",  # 采购完工时间
            "purchaserIds": "13041141,13041048",  # 采购人员ID
            "machiningDate": "2022-10-29",  # 加工完工时间
            "machiningIds": "13041141,13041048",  # 加工队伍人员ID
            "supplierDate": "2022-10-30",  # 供应商完工时间
            "supplierIds": "13041157",  # 供应商ID
            "rawMaterialManagerDate": "2022-10-31",  # 原材料/仓库管理员完工时间
            "rawMaterialManagerIds": "13041141,13041048",  # 原材料/仓库管理员ID
            "siteServiceDate": "2022-10-31",  # 现场服务完工时间
            "siteServiceIds": "13041141,13041048",  # 现场服务人员ID
            "logisticsDate": "2022-11-01",  # 物流完工时间
            "logisticsIds": "13041158",  # 物流人员ID
            "illustrate": "这里是项目的说明"  # 项目说明
        }

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
