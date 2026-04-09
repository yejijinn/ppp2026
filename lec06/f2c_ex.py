#def f2c(temp_f):
#    temp_c = (temp_f-32)*5/9
#    return temp_c
#f2c(78)
#print(f"{temp_f:.1f}F는 {temp_c:.1f}C 입니다.") (내가 짠 코드 왜 안되누ㅜ)





def f2c(tf):
    temp_c = (tf-32)*5/9
    return temp_c

# 호출
print(f2c(78))
print(f"{78}F => {f2c(78):.1f}C")