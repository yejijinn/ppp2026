for i in range(20):         #i는 0부터 시작 
    print (i+1)

for n in range(1,10+1) : #i 는 0부터 시작하기 때문에, +1해줘야함. / n은 구분하기 쉽게 표시를 다르게 진행한 것입.
    print(n)

# "+=" 누적 

total = 0
for n in range(1,10+1) : 
    total += n
print(total)

total = 0
for n in range(1,100+1) : 
    total += n
print(total)
