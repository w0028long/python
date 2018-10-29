#!/usr/bin/python3
# --*-- coding:utf-8 --*--
with open("nu1.txt","r") as f:
    lines = f.read()
with open("nu2.txt","r") as f2:
    lines2 = f2.read()
    if lines != lines2 :
        print("ip发生改变.")
        lines = lines.replace(str(lines),str(lines2))
with open("nu1.txt","w") as f_w:
    f_w.write(lines)
f_w.close()
f.close()
f2.close()
