A_class = [
"김민수", "이서연", "박지훈", "최유진", "정하준",
"김민수", # 중복
 "한지민", "윤도현", "이서연" # 중복
]
B_class = [
"박지훈", "최유진", "강다은", "오세훈", "윤도현",
"강다은", # 중복
 "김민수", "배수지"
]
#print(type(A_class)) - 타입을 알 수 있음
print(A_class)
print(set(A_class)) #중복 값 제거
print(set(B_class)) #중복 값 제거
print(set(A_class) - set(B_class))
print(set(A_class) | set(B_class)) # |는 or이랑 같음
print(set(A_class) & set(B_class)) # &는 and와 같음

#for = 갯수를 알때 사용 / 주머니에서 하나하나 꺼낼때 / 괄호 안에 지정한 숫자만큼 반복
#while = 어느 조건일때 계속 진행 while ture- 계속 돌다가 특정한 상황 발생 - 그만
# while문 중단시키는 방법 - break - 뒤에꺼 실행 x 반복문 끝나는 다음 줄 부터 시작
# while문 continue - 뒤에껀 실행하지 않지만, 맨 처음으로 다시 돌아감
#i 는 0부터 시작
