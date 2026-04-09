def sum_n(n):
    total = 0
    for n in range(0,n+1):
        total += n
    print(total)

def main():
    n = int(input("숫자를 입력해주세요. = "))
    sum_n(n)

if __name__=="__main__":
    main()