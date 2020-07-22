'''
    作者: Eninix
    时间: 2020.2.10 1:43 A.M.
'''

import random
import os
import time

#ssr概率范围 %1
ssr = 1
#sr概率范围 %14
sr = (2,15)
#r概率范围 %30
r = (16,45)
#n概率范围 %55
n = (46,100)

#单次十连的储存列表
list1 = []
#总抽卡的存储列表
listTemp = []

def chouka() :
    temp = random.randint(1,100)
    if n[0] <= temp :
        listTemp.append('N')
        list1.append('N')
    elif r[0] <= temp <= r[1] :
       listTemp.append('R')
       list1.append('R')
    elif sr[0] <= temp <= sr[1] :
        listTemp.append('SR')
        list1.append('SR')
    else:
        listTemp.append('SSR')
        list1.append('SSR')

def shilian() :
    i = 0
    while i<10 :
        chouka()
        i += 1 

def tongji() :
    print("目前抽卡情况如下:")
    print("----------------------------")
    print("总抽卡数:" , len(listTemp))
    print("SSR:" , listTemp.count('SSR'))
    print(" SR:" , listTemp.count('SR'))
    print("  R:" , listTemp.count('R'))
    print("  N:" , listTemp.count('N'))
    print("----------------------------")
    if len(list1) == 0:
        print("上次十连情况:","你当前还未开始抽卡!")
    else:
        print("上次十连情况:"," ","N:",list1.count('N')," ","R:",list1.count('R')," ","SR:",list1.count('SR')," ","SSR:",list1.count('SSR'))
        print("----------------------------")
        if len(listTemp) <= 500:
            print("血统评估:","酋长别抽了,回部落好好呆着吧  ╮(๑•́ ₃•̀๑)╭ ")
        elif 500 <= len(listTemp) < 1000:
            print("血统评估:","再怎么抽你也不会变成欧皇的啦,回部落好好呆着吧  ╮(๑•́ ₃•̀๑)╭ ")
        else:
            print("          实在是佩服阁下的毅力  ( ᖛ ̫ ᖛ )ʃ) ")
    print("----------------------------")

def gailv():
    print("----------------------------")
    print('概率公示:')
    print("SSR概率: " , ssr , "%" )
    print(" SR概率: " , (sr[1]-sr[0])+1 , "%")
    print("  R概率: " , (r[1]-r[0])+1 , "%")
    print("  N概率: " , (n[1]-n[0])+1 , "%")
    print("----------------------------")

def start():
    while True:
        os.system('cls')
        print("欢迎测试血统!")
        gailv()
        tongji()
        print("测试血统请按 ' 1 '")
        if len(listTemp) != 0:
            print("恢复初始状态请按 ' 2 '")
        print("退出请按 ' 0 '")
        
        
        key = int(input())
        if key == 1:
            list1.clear()
            shilian()
        elif key == 0:
            print("程序正在退出...")
            time.sleep(1)
            break
        elif key == 2:
            list1.clear()
            listTemp.clear()
        elif key >= 5:
            a = 0
            list1.clear()
            while a <key:
                shilian()
                a += 1
        else:
            print("输入错误,请重新输入!")
            os.system('pause')


start()