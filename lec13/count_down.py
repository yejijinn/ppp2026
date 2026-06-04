import time

for i in range(10,0,-1):
    # print(i)
    # print(i,end= "\r") 줄바꿈 하지 않음
    print(f"{i:3d}", end= "\r")
    time.sleep(1) # 쉬게 할 수 있음  