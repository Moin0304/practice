import time

# while True:
#     print("**********")
#     print("********")
#     print("******")
#     print("***")
#     print("*")
#     for i in range(60*60*2):
#         # wait for 2 hours (60 seconds * 60 minutes * 2)
#         time.sleep(1)
while True:
    starttime= int(time.time())
    # print(starttime)
    for i in range(5,0,-1):
        print("*"*i)
    waittime= starttime+7200
    while True:
        if int(time.time())==waittime:
            break