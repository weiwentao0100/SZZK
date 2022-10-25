import datetime


class SetUtil:

    def setup_autonumber(self):
        """ 创建自增变量number """
        with open("/Users/weiwentao/wentao_test/SZZK/data/number.txt", "r+") as f:
            _number = f.readline()
            auto_number = int(_number) + 1
            f.seek(0)
            f.truncate()
            f.write(str(auto_number))
        return str(auto_number)

    def setup_datetime(self):
        """ 生成项目各角色的完工日期 """
        time = datetime.datetime.now()
        time_list = [i for i in range(11)]
        days_difference = []
        for i in time_list:
            time_difference = time + datetime.timedelta(days=i)
            everyday_time = time_difference.strftime('%Y-%m-%d')
            days_difference.append(everyday_time)
        return days_difference


if __name__ == '__main__':
    setutil = SetUtil()
    setutil.setup_datetime()



