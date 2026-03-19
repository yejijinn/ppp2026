r = float(input("반지름을 입력하십시오 = "))

import math
c_area= math.pi*r**2
c_measure = 2*math.pi*r
print(f"반지름 = {r}, 넓이 = {c_area:.2f}, 둘레 = {c_measure:.1f}")

#.1f는 소수점 첫째자리 
