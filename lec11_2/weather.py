def read_dates(weather_filename):
    dates =[]
    with open (weather_filename) as f :
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = [int(tokens[0]),int(tokens[1]),int(tokens[2])]
            dates.append(date)

    return dates


def read_weather_col(weather_filename,col_idx):
    values = []
    with open(weather_filename) as f :
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            values.append(value)

    return values

def get_max_diff(dates,tmax,tmin): #date , temp_diff
    max_diff = -999 #처음 입력값
    max_diff_date = False

    for i in range(len(dates)):
        diff = tmax[i] - tmin[i] #일교차
        
        if diff > max_diff: #계속 계산하면서 큰 값을 기억함 
            max_diff = diff
            max_diff_date = dates[i] #날짜도 기억하는 것    
            
    
    return max_diff_date, max_diff #날짜와 온도 (우리눈엔 하나 / 파이썬에서는 한덩이로 봄) / 순서주의



def gdd_season(dates,tavg):
    gdd_value = 0
    for i in range(len(dates)):
        date = dates[i]
        t = tavg[i]
        if date[1] in [5,6,7,8,9]:          #if dates[i][1] in [5,6,7,8,9]:  dates의 i 번째 로 작성가능 (동일함)        
            if t > 5:
                gdd_value += (t - 5)
    return gdd_value


def main():
    weather_filename = "lec/lec12/weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename,3)
    tmin = read_weather_col(weather_filename,5)
    tavg = read_weather_col(weather_filename,4)
    date, temp_diff = get_max_diff(dates,tmax,tmin)
    print(f"일교차가 가장 큰 날 : {date}")
    print(f"일교차가 가장 큰 날의 일교차 : {temp_diff:.1f}도")

    gdd_value = gdd_season(dates,tavg)
    print(f"GDD는 {gdd_value:.1f}도일 입니다.")

if __name__=="__main__":
    main()