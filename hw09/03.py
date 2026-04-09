def is_leap_year(y):
    if y%4 ==0 and y%100!=0:
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")
    return y

def main ():
    y=int(input("윤년을 확인하고 싶은 년도를 입력해주세요. ="))
    is_leap_year(y)
if __name__=="__main__":
    main()