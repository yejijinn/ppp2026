mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}

cart=["우유","우유","계란","계란","계란"]
# cart=["빵","계란"]
total_cost = 0
for item in cart:
    total_cost+=mart[item] #mart라는 집합 (사전)에서 item(우유,계란,빵... )같은걸 뺴냄
print(f" 총 구매금액은 {total_cost:,}입니다.") #:, = 100단위에서 , 찍음