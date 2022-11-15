from testcases.cases import TestCase

if __name__ == '__main__':
    # 一键创建单个项目
    testcase = TestCase("https://test12.ahweimeng.cn")
    testcase.add_one_supplyList()
    testcase.add_two_supplyList()
    testcase.add_project()

    # 批量创建多个项目，range(10) 一键创建10个项目
    # for i in range(10):
    #     testcase = TestCase("https://test12.ahweimeng.cn")
    #     testcase.add_one_supplyList()
    #     testcase.add_two_supplyList()
    #     testcase.add_project()
