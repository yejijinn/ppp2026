h=float(input("한라봉 섭취 무게 ="))
s=float(input("딸기 섭취 무게 ="))
b=float(input("바나나 섭취 무게 ="))

h_cal = h*0.5
s_cal = s*0.34
b_cal = b*0.77

total = h_cal + s_cal + b_cal

print(f"한라봉 섭취무게 {h}g, 딸기 섭취 무게{s}g, 바나나 섭취 무게 {b}g 라면, 총 섭취 칼로리는 {total}kcal 입니다.")