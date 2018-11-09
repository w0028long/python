#!/usr/bin/python3
print("这是一个选择小游戏，可以按照选择走也可以瞎玩。")
def count_sum():
    count = 4
    while count >= 0:
        count -= 1
        trun = str(input("请输入一个方向，right还是left?"))
        if trun == "right":
            print("你选择错了，掉坑里了.")
        elif trun == "left":
            print("继续往下走吧~")
        else:
            print("还有%s次机会" % (count))
        if count == 0:
            print("五次机会用完，恭喜瞎玩完成")
            break
trun = str(input("请输入一个方向，right还是left?"))
if trun == "right":
    print("你选择错了，掉坑里了.摔傻了，结束，可以试试瞎玩")
elif trun == "left":
    print("选择正确~结束")
else:
    count_sum()  #练习结束。
