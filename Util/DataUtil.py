import datetime


class SetUtil:

    def setup_autonumber(self):
        """ 创建自增变量number """
        with open("/Users/weiwentao/wentao_test/SZZK/data/number.txt", "r+") as f:
            number = f.readline()
            auto_number = int(number) + 1
            f.seek(0)
            f.truncate()
            f.write(str(auto_number))
        return str(auto_number)

    def setup_datetime(self):
        """ 生成当天日期 """
        time = datetime.date.today()
        return str(time)


if __name__ == '__main__':
    setutil = SetUtil()
    number = setutil.setup_autonumber()
    print("文涛的测试合同_1" + number)

