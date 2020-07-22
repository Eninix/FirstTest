import random
import os
import time
def 清空字典(map):
    for i in map:
        map[i] = 0
def 分割线():
    print('-' * 18)
class 抽卡机器:
    def __init__(self):
        self.概率 = {'SSR': 1, 'SR': 15, 'R': 45, 'N': 39}
        self.本次抽卡 = {'SSR': 0, 'SR': 0, 'R': 0, 'N': 0}
        self.累计抽卡 = {'SSR': 0, 'SR': 0, 'R': 0, 'N': 0}
    def 单抽(self):
        temp = random.randint(1, 100)
        if temp <= self.概率['SSR']:
            self.本次抽卡['SSR'] += 1
            self.累计抽卡['SSR'] += 1
        elif temp <= self.概率['SSR'] + self.概率['SR']:
            self.本次抽卡['SR'] += 1
            self.累计抽卡['SR'] += 1
        elif temp <= self.概率['SSR'] + self.概率['SR'] + self.概率['R']:
            self.本次抽卡['R'] += 1
            self.累计抽卡['R'] += 1
        else:
            self.本次抽卡['N'] += 1
            self.累计抽卡['N'] += 1
    def 十连(self):
        i = 0
        while i < 10:
            self.单抽()
            i += 1
    def 累计抽卡数据显示(self):
        print(f'累计抽卡情况:\n{self.累计抽卡}')
    def 本次抽卡数据显示(self):
        print(f'本次抽卡情况:\n{self.本次抽卡}')
    def 理论抽卡概率显示(self):
        print(f"理论抽卡概率显示:\nSSR:{self.概率['SSR']}% || SR:{self.概率['SR']}% || R:{self.概率['R']}% || N:{self.概率['N']}%")
    def 实际抽卡概率显示(self):
        分母 = (self.累计抽卡['SSR'] + self.累计抽卡['SR'] + self.累计抽卡['R'] + self.累计抽卡['N'])/100
        if 分母 != 0:
            print('实际抽卡概率显示:\nSSR:%.2f%%  SR:%.2f%%  R:%.2f%%  N:%.2f%%' % (self.累计抽卡['SSR'] / 分母, self.累计抽卡['SR'] / 分母, self.累计抽卡['R'] / 分母, self.累计抽卡['N'] / 分母))
一个无情的抽卡机器 = 抽卡机器()
def start():
    flag = True
    i = 1
    while True:
        os.system('cls')
        print('欢迎进行血统测试!')
        分割线()
        一个无情的抽卡机器.理论抽卡概率显示()
        分割线()
        一个无情的抽卡机器.累计抽卡数据显示()
        分割线()
        一个无情的抽卡机器.本次抽卡数据显示()
        分割线()
        一个无情的抽卡机器.实际抽卡概率显示()
        分割线()
        if flag == False:
            print(i)
            i += 1
        if flag:
            print(f"单抽 - 1\n十连抽 - 2\n自动抽卡 - 3\n退出 - 0")

            keyhit = input()

            if keyhit == '0':
                break
            elif keyhit == '1':
                清空字典(一个无情的抽卡机器.本次抽卡)
                一个无情的抽卡机器.单抽()
            elif keyhit == '2':
                清空字典(一个无情的抽卡机器.本次抽卡)
                一个无情的抽卡机器.十连()
            elif keyhit == '3':
                清空字典(一个无情的抽卡机器.本次抽卡)
                flag = False
        else:
            一个无情的抽卡机器.十连()
            一个无情的抽卡机器.单抽()
            一个无情的抽卡机器.十连()
            一个无情的抽卡机器.单抽()
            一个无情的抽卡机器.十连()
            一个无情的抽卡机器.单抽()
start()
