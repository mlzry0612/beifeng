class Bank:
    __userDict = {}

    def __init__(self):
        print("init Bank")

    def add_user(self, user):
        id = user.get_id()
        if self.__userDict.get(id):
            print("这个帐号已经存在: %s" % id)
        else:
            self.__userDict[id] = user

    def show_user_num(self):
        print("---------开户数量---------")
        print("当前开户总数：%s户" % len(self.__userDict.keys()))

    def show_all_user_info(self):
        print("---------所有用户信息---------")
        for userId in self.__userDict.keys():
            user = self.__userDict.get(userId)
            user.print()
            print("\n")

    def show_user_info(self, id, passwd):
        if self.__userDict.get(id):
            user = self.__userDict.get(id)
            userName = user.get_name()
            restMoney = user.get_money()
            if passwd == user.get_passwd():
                print("---------用记信息---------")
                print("用户:%s, 用户名:%s, 余额: %s" % (id, userName, restMoney))

            else:
                print("密码不对")

        else:
            print("找不到用户")

    def save_money(self, id, passwd, money):
        if self.__userDict.get(id):
            user = self.__userDict.get(id)
            if passwd == user.get_passwd():
                user.deposite_money(money)
                restMoney = user.get_money()
                print("---------存钱---------")
                print("id:%s, save money:%s, rest money: %s" % (id, money, restMoney))
            else:
                print("Passwd 不对")

        else:
            print("找不到用户")

    def fetch_money(self, id, passwd, money):
        if self.__userDict.get(id):
            user = self.__userDict.get(id)
            if passwd == user.get_passwd():
                if user.fetch_money(money):
                    restMoney = user.get_money()
                    print("---------取钱---------")
                    print("id:%s, save money:%s, rest money: %s" % (id, money, restMoney))
            else:
                print("Passwd 不对")
        else:
            print("找不到用户")


class User:
    def __init__(self, id, name, passwd, money):
        self.__ID = id
        self.__name = name
        self.__passwd = passwd
        self.__money = money

    def print(self):
        print("卡号： %s" % self.__ID)
        print("用户名： %s" % self.__name)
        print("密码： %s" % self.__passwd)
        print("余额： %s" % self.__money)

    def get_name(self):
        return self.__name

    def get_passwd(self):
        return self.__passwd

    def get_id(self):
        return self.__ID

    def get_money(self):
        return self.__money

    def fetch_money(self, money):
        if money > self.__money:
            print("余额不足")
            return False
        else:
            self.__money -= money
            print("成功取钱")
            return True

    def deposite_money(self, money):
        self.__money += money
        print("存钱成功")


if __name__ == '__main__':
    bank = Bank()
    user1 = User("1001", "wuwu", "111232342111", 100)
    user2 = User("1002", "sssss", "11234234231111", 100)
    bank.add_user(user1)
    bank.add_user(user2)

    bank.show_user_num()
    bank.show_all_user_info()
    bank.fetch_money("1001", "11234321111", 50)
    bank.save_money("1001", "111234111", 100)
    bank.show_user_info("1001", "112341111")
