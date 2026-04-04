mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}

cart=["우유","우유","계란","계란","계란"]

total_cost = 0
for item in cart:
    total_cost+=mart[item] 
print(f" 총 구매금액은 {total_cost:,}입니다.") 