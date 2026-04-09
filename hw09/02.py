def get_range_list(n):
    result = [] #list
    for i in range(1,n+1):
        result.append(i)
    print(result)
    return(result)

    
    
def main ():
    n = int(input("숫자를 입력해주세요.= "))
    get_range_list(n) 
if __name__=="__main__":
    main()
