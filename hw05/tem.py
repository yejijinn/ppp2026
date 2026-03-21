choice = input("1 : ( 화씨->섭씨) , 2: ( 섭씨->화씨) 변환을 선택하세요.")
put = float(input("변환할 값을 입력하세요.: "))

if choice == "1" :
    result = (put-32)*5/9
    print (f"{result:.1f}섭씨 입니다.")

elif choice == "2" :
    result = put*9/5 +32
    print (f"{result:.1f}화씨 입니다.")