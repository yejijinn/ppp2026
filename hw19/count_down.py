import time

for i in range(10,0,-1):
    #print(i) 그대로 순서대로 진행
    print(f"{i:3d}", end= "\r")
    time.sleep(1) # 쉬게 할 수 있음  