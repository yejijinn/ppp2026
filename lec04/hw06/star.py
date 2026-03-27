num = int(input("삼각형으로 제작할 별 개수를 입력해 주세요."))

star = "*"
for result in range(1,num+1):
    print(result * star)