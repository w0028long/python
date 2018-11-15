#!/usr/bin/python3
import time, subprocess
timelef = 60
while timelef > 0 :
    print(timelef, end=' ')
    time.sleep(1)
    timelef -= 1
subprocess.Popen(['open', ' '])
