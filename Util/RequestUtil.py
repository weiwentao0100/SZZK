import requests


class Request:  # 创建类
    # def __init__(self):
    #     self.log = my_log("Requests")

    def request_api(self, url, json=None, params=None, data=None, headers=None, cookies=None, method="get"):  # 定义公共方法
        # 增加请求方法的参数method 通过参数判断get或post请求
        if method == "get":
            # get 请求
            rep = requests.get(url, params=params, headers=headers, cookies=cookies)
        else:
            # post 请求
            rep = requests.post(url, json=json, data=data, headers=headers, cookies=cookies)

        # 把重复的内容复制进来
        code = rep.status_code  # 获取状态码
        try:  # 获取返回结果 判断返回数据类型 如果不是json就返回text
            body = rep.json()
        except Exception as e:
            body = rep.text
        _response = dict()  # 定义空字典
        _response['code'] = code  # 将返回的状态码放入字典，key为'code'
        _response['body'] = body  # 将返回的结果放入字典，key为'body'
        return _response  # 将字典返回出去

    # get方法重构
    def get(self, url, **kwargs):  # 定义方法 / **kwargs 定义参数
        return self.request_api(url, method="get", **kwargs)

    # post方法重构
    def post(self, url, **kwargs):
        return self.request_api(url, method="post", **kwargs)


if __name__ == '__main__':
    request = Request()
    response = request.get("https://www.baidu.com")
    print(response.get('body'))
