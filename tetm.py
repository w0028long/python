#!/usr/bin/python3
import time
def calcprod():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

starttime = time.time()
prod = calcprod()
endtime = time.time()
print('The result is %s digits long.' % (len(str(prod))))    #返回计算结果的长度
print('Took %s seconds time calculate.'  % (endtime - starttime)) #启用time模块，循环1*10w然后调用开始和结束时间计算完成的时间差
for m in range(3):
    print('tick')
    time.sleep(1)
    print('toke')
    time.sleep(1)
time.sleep(5)   #做个延时操作，各循环3次，每秒输出一个词
