#대괄호 안에 다 넣을 수 있음.
numbers=[10,90,20,30,40,50]
print(numbers)
numbers.append(100) #100추가 하는 방법 / 하나의 덩어리로 인식
print(numbers)
numbers.extend([101,102,103]) # 숫자를 하나하나로 인식
print(numbers)
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
numbers.sort() #정렬
print(numbers)
print(numbers[0])
print(numbers[9])  #9 아니면 -1 가능
print(numbers[len(numbers)//2]) # 몫이 나오는 나누기기 / 중앙값 (전체의 길이를 모를때)
