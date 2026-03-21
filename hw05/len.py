choice = input("1: (ft->cm ), 2:(cm->ft) 변환을 선택하세요. = ")
put = float(input("변환할 값을 입력해주세요. ="))

if choice =="1" :
    cal = put*30.48
    print(f"{cal:.1f}cm 입니다. ")

elif choice =="2" :
    cal = put/30.48
    print(f"{cal:.1f}ft 입니다. ")
