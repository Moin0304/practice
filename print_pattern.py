import time

while True:
    starttime= int(time.time())
    # print(starttime)
    for i in range(5,0,-1):
        print("*"*i)
    waittime= starttime+7200
    while True:
        if int(time.time())==waittime:
            break