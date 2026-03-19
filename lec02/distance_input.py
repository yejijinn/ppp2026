x1 = float(input("x1 좌표 입력 = "))
y1 = float(input("y1 좌표 입력 = "))
x2 = float(input("x2 좌표 입력 = "))
y2 = float(input("y2 좌표 입력 = "))

x_d = x2 - x1
y_d = y2 - y1

import math
distance = math.sqrt(x_d**2 + y_d**2)

print(f"점{x1},{y1}과 점 {x2},{y2}사이의 거리는 {distance}입니다.")
