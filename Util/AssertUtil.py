# 1、定义封装类
class AssertUtil:
    # 2、初始化数据、日志
    # def __init__(self):
    #     self.log = my_log("AssertUtil")

    # 3、code相等
    def assert_code(self, code, expected_code):
        """
        验证返回状态码
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            print("返回的状态码不匹配，请检查请求参数是否正确！")
            # raise AssertionError("返回的状态码不匹配，请检查请求参数是否正确！")

    # 4、body相等
    def assert_body(self, body, expected_body):
        """
        验证返回结果相等
        """
        try:
            assert body == expected_body
            return True
        except:
            # print("返回的body不匹配，请检查请求参数是否正确！")
            return "返回的body不匹配，请检查请求参数是否正确！"

    # 5、body包含
    def assert_in_body(self, body, expected_body):
        """
        验证返回结果是否包含期望的结果
        """
        try:
            # body = json.dumps(body)
            assert expected_body in body
            return True
        except:
            # print("返回结果不包含期望的结果，请检查请求参数是否正确！")
            return "返回结果不包含期望的结果，请检查请求参数是否正确！"
