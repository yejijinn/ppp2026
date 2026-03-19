temp_c = (input("온도를 입력하시오."))
temp_c = float(temp_c)
# temp_c = int(input("온도를 입력하시오")) 로 두개 합친 한줄 이용가능
#정수 = int / 실수 = float

temp_f = temp_c * 9 / 5 + 32
print(f"{temp_c}C=> {temp_f}F ")
