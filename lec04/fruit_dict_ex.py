cal_orange = 50
cal_sb = 34
cal_banana = 70
cal_list = [50,34,70] #순서를 잘 기억해야함 
cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 70} #딕셔너리 문법 사용방법

eat_orange = 100
eat_sb = 200
eat_banana = 500
eat_list = [100,200,500]
eat_dict = {"한라봉" : 100, "딸기" : 200 , "바나나": 500}

total_cal = (cal_orange * eat_orange 
             + cal_sb * eat_sb 
             + cal_banana * eat_banana )


total_cal_list= (cal_list[0] * eat_list[0]
                 +cal_list[1]*eat_list[1]
                 +cal_list[2]*eat_list[2])

total_cal_list = 0
for i in range(3):  #3번 반복시킨다는 뜻 
    total_cal_list += cal_list[i] * eat_list[i]

print(total_cal)