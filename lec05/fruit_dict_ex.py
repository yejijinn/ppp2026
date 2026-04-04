cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 70} #딕셔너리 문법 사용방법

eat_dict = {"한라봉" : 100, "딸기" : 200 , "바나나": 500} # "망고" : 200

# for key in eat_dict:                 #for key in eat_dict:
#     print(key)

total_cal = 0
for key, val in eat_dict.items():
    if key in cal_dict: # print(key,val) #key - 한라봉 val - 몇그람
        total_cal +=val * cal_dict[key] #cal_dict["한라봉"] = 50
print(total_cal)
