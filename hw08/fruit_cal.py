def cal(cal_dict,eat_dict):
    total_cal = 0
    for word, eat in eat_dict.items():
        if word in cal_dict: 
            total_cal +=eat * cal_dict[word] 
        print(total_cal)

def main ():
    cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 70} 
    eat_dict = {"한라봉" : 100, "딸기" : 200 , "바나나": 500} 
    cal(cal_dict,eat_dict)

if __name__=="__main__":
    main()