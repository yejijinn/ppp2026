def gugudan(num):
    for cri in range(1,11):
        print(f"{num} X {cri} = {num*cri}")   
    

def main ():
    num = int(input("구구단을 생성하고 싶은 숫자를 입력해주세요. = "))
    gugudan(num)

if __name__=="__main__":
    main()
