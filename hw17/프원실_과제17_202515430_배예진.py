def str2int(text: str):
    try:
        return int(text) #자연수로 변환
    except ValueError:
        return None #배제


def main():
    values =[]
    while True: 
        x= input("X->?") #정수 or none
        x_value =str2int(x)
        
        if x_value == -1:
            break

        if x_value is not None:
            if x_value>0: #and type(x_value)==int:
                values.append(x_value)

    print(f"입력된 값 = {values}")
    print(f"입력된 값의 갯수 = {len(values)}")
    print(f"입력된 값의 평균 = {sum(values)/len(values)}")

if __name__=="__main__":
    main()