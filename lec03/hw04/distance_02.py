x = int(input("x 좌표 입력 = "))
y = int(input("y 좌표 입력 = "))

if x>0 and y>0:
    print(f"입력한 좌표 {x},{y}는 1사분면에 있습니다.")
elif x<0 and y>0:
    print(f"입력한 좌표 {x},{y}는 2사분면에 있습니다.")
elif x<0 and y<0:
    print(f"입력한 좌표 {x},{y}는 3사분면에 있습니다.")
elif x>0 and y<0 :
    print(f"입력한 좌표 {x},{y}는 4사분면에 있습니다.")
elif x==0 and y>0 or y<0 :
    print (f"입력한 좌표 {x},{y}는 y축에 있습니다.")
elif y==0 and x>0 or x<0 :
    print (f"입력한 좌표 {x},{y}는 x축에 있습니다.")
elif x==0 and y==0 :
    print (f"입력한 좌표{x},{y}는 원점에 있습니다.")