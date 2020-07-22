import random
import os

"""
    作者:Eninix
    时间:2020.3.25 - 16:02
"""


class 抽卡系统(object):
    #   [0]-ssr   [1]-sr   [2]-r   [3]-n
    概率 = [1, 15, 45, 39]
    本次抽卡结果 = [0, 0, 0, 0]
    累计抽卡结果 = [0, 0, 0, 0]

    @classmethod
    def 本次抽卡结果归零(cls):
        for i in range(len(cls.本次抽卡结果)):
            cls.本次抽卡结果[i] = 0

    @classmethod
    def 累计抽卡结果归零(cls):
        for i in range(len(cls.累计抽卡结果)):
            cls.累计抽卡结果[i] = 0

    @classmethod
    def 输出抽卡结果(cls, value):
        if value == '本次':
            value = cls.本次抽卡结果
            str = '本次抽卡结果:'
        elif value == '累计':
            value = cls.累计抽卡结果
            temp = 0
            for i in range(len(cls.累计抽卡结果)):
                temp += cls.累计抽卡结果[i]
            str = f'累计抽卡{temp}次:'

        tempList = ['SSR', 'SR', 'R', 'N']
        print(str)
        for i in range(len(value)):
            print("%s:%d" % (tempList[i], value[i]), end='  ')
        print()
        del tempList

    @classmethod
    def 单抽(cls):
        temp = random.randint(1, cls.概率[0] + cls.概率[1] + cls.概率[2] + cls.概率[3])
        if temp <= cls.概率[0]:
            cls.本次抽卡结果[0] += 1
            cls.累计抽卡结果[0] += 1
        elif temp <= cls.概率[0] + cls.概率[1]:
            cls.本次抽卡结果[1] += 1
            cls.累计抽卡结果[1] += 1
        elif temp <= cls.概率[0] + cls.概率[1] + cls.概率[2]:
            cls.本次抽卡结果[2] += 1
            cls.累计抽卡结果[2] += 1
        else:
            cls.本次抽卡结果[3] += 1
            cls.累计抽卡结果[3] += 1
        del temp

    @classmethod
    def 十连(cls):
        for a in range(10):
            cls.单抽()

    @classmethod
    def 修改概率(cls):
        temp1 = ['SSR的概率', 'SR的概率', 'R的概率', 'N的概率']
        temp2 = ['SSR的概率', 'SR的概率', 'R的概率', 'N的概率']
        try:
            for i in range(4):
                temp2[i] = int(input(f'请输入修改后的{temp1[i]}(请输入数字):'))
        except:
            print('输入出错! 请重新输入!')
            cls.修改概率()
        else:
            for i in range(4):
                cls.概率[i] = temp2[i]
        finally:
            del temp1
            del temp2

    @classmethod
    def 显示理论抽卡概率(cls):
        print('理论抽卡概率如下:')
        tempList = ['SSR', 'SR', 'R', 'N']

        temp = 0
        for i in cls.概率:
            temp += i

        for i in range(len(cls.概率)):
            print("%s\t:%2.2f%%" % (tempList[i], (cls.概率[i]/temp) * 100))
        del tempList

    @classmethod
    def 显示实际抽卡频率(cls):
        print('实际抽卡频率如下:')
        temp = 0
        tempList = ['SSR', 'SR', 'R', 'N']
        for i in range(len(cls.累计抽卡结果)):
            temp += cls.累计抽卡结果[i]
        if temp == 0:
            print('当前没有抽卡记录!')
            return
        for i in range(len(cls.累计抽卡结果)):
            print("%s\t:%3.2f%%" % (tempList[i], (cls.累计抽卡结果[i] / temp) * 100))
        del tempList
        del temp


class 抽卡管理(object):
    def 显示菜单(self):
        print("=> 1 - 单抽\n=> 2 - 十连\n=> 3 - 清空记录\n=> 4 - 修改概率")
        print("=> 0 - 退出")

    def 按键操作(self):
        try:
            keyhit = int(input('请输入需要选择的操作:'))
        except:
            print('输入错误,请重新输入!')
            os.system('pause')
            self.开始血统测试()
        else:
            if keyhit == 1: # 1 - 单抽
                抽卡系统.本次抽卡结果归零()
                抽卡系统.单抽()

            elif keyhit == 2: # 2 - 十连
                抽卡系统.本次抽卡结果归零()
                抽卡系统.十连()

            elif keyhit == 3: # 3 - 清空记录
                抽卡系统.累计抽卡结果归零()

            elif keyhit == 4: # 4 - 修改概率
                os.system('cls')
                抽卡系统.修改概率()
                os.system('pause')

            elif keyhit == 0: # 0
                exit(0)
            else: # default
                pass

    def 分割线(self):
        print('-' * 20)

    def 开始血统测试(self):
        while True:
            os.system('cls')
            print("欢迎来到血统测试仪!")
            self.分割线()
            抽卡系统.显示理论抽卡概率()
            self.分割线()
            抽卡系统.输出抽卡结果('累计')
            self.分割线()
            抽卡系统.输出抽卡结果('本次')
            self.分割线()
            抽卡系统.显示实际抽卡频率()
            self.分割线()
            # main
            self.显示菜单()
            self.按键操作()


一个无情的抽卡机器 = 抽卡管理()
一个无情的抽卡机器.开始血统测试()
