x = float(input("x1 좌표 입력 = "))
y = float(input("y1 좌표 입력 = "))

if x>0 and y>0:
    print(f"입력한 좌표 {x},{y}는 1사분면에 있습니다.")
elif x<0 and y>0:
    print(f"입력한 좌표 {x},{y}는 2사분면에 있습니다.")
elif x<0 and y<0:
    print(f"입력한 좌표 {x},{y}는 3사분면에 있습니다.")
elif x>0 and y<0:
    print(f"입력한 좌표 {x},{y}는 4사분면에 있습니다.")
