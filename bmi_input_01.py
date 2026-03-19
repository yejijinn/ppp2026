weight = float(input("몸무게(kg)를 입력해주세요 = "))
height = float(input("키(cm)를 입력해주세요 ="))

#  command+슬래쉬 = 주석처리

BMI = (weight)/(height/100)**2


print(f"키가 {height}cm이고, 몸무게가 {weight}kg이라면, BMI는 {BMI} 입니다.")

if  23<BMI<24.9 :
    print ("비만 전단계 입니다.")
elif 25<BMI<29.9 :
    print ("1단계 비만입니다.")
elif 30<BMI<34.9 :
    print ("2단계 비만입니다.")
elif BMI>=35 :
    print ("3단계 비만입니다.")
