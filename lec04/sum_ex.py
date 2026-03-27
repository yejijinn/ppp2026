#for n in range (250): #0-249 -for문에서 보정해줘야함  => total +=(i+1)
#for n in range (251): #문제가 됨

total = 0
for n in range (1,251): #1-250
    if n %2 ==0:
        total += n
print(total)

print(sum([x for x in range(1,251) if x %2==0]))