def read_weather(filename):
    dataset=[]
    with open (filename) as f:
        lines = f.readlines()
        for line in lines [1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset


def read_rainfall(filename):
    dataset=[]
    with open (filename) as f:
        lines = f.readlines()
        for line in lines [1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset


def read_tmax(filename):
    dataset=[]
    with open (filename) as f:
        lines = f.readlines()
        for line in lines [1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[3]))
    return dataset

def get_days_over_5mm(rainfall):
    count_5mm = 0
    for r in rainfall:
        if r >= 5:
            count_5mm += 1
    return count_5mm
    #return sum([1 for x in rainfall if x >=5]) 한줄로도 가능 

def get_rain_event_days(rainfall):
    dataset_rainfall = [] #비가 오면 1 , 안오면 0
    for m in rainfall:
        if m >0: #m==1
            dataset_rainfall.append(1)
        else: #m==0
            dataset_rainfall.append(0)
    
    dataset_rain_event = []
    for i in range(len(dataset_rainfall)):
        m = dataset_rainfall[i] #for m in rainfall: 와 같음 / 0 or 1
        if m == 0:
            dataset_rain_event.append(0)
        
        else : #m==1
            if i == 0:
                dataset_rain_event.append(1)
            else :
                dataset_rain_event.append(dataset_rain_event[i-1]+1) # 직전값에 +1

    print(dataset_rain_event)
    return max(dataset_rain_event)


def get_rain_event_days(rainfall):
    datasets =[]
    rainfall_event = []
    for r in rainfall:
        if r > 0 :
            if rainfall_event != None:
                rainfall_event.append(r) #전날에 비가 옴 (연속)
            else :
                rainfall_event = [r] #비가 온 첫날
        else :
            if rainfall_event != None: #비가 안옴
                datasets.append(rainfall_event) #전체 데이터 셋에 넣어줌
            rainfall_event = None #바구니를 없애줌
    #print(datasets)
    #print(max([len(x) for x in datasets])) #7일 확인  / 4번 답
    return (max([sum(x) for x in datasets])) # 5번 답



def get_top3 (list_values):
    return sorted(list_values) [-3:]

def main():
    weather_filename = "lec/lec10/weather(146)_2022-2022.csv"
    rainfall= read_rainfall(weather_filename)
    tmax = read_tmax(weather_filename)

    days_over_5mm = get_days_over_5mm(rainfall) #=값이 있다 -> return값 존재
    print(f" 5mm 이상인 총 강우일수는 {days_over_5mm}일 입니다.")

    max_rainy_days = get_rain_event_days(rainfall)
    print(f" 최장연속 강우일수는 {max_rainy_days}일 입니다.") 

    max_rainfall_event = get_rain_event_days(rainfall)
    print(f" 최대 강우량은 {max_rainfall_event}mm 입니다.") 

    tmax_top3 = get_top3(tmax)
    print(f" tmax 최대값 3개는 {tmax_top3} 입니다.") 
    
if __name__=="__main__":
    main()