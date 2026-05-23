def read_weather_col(filename,col_idx, conv_fn):    
    dataset=[]                                     
    with open (filename) as f:
        lines = f.readlines()
        for line in lines [1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def sumifs(rainfalls, years, selected_years ):
    total_value = 0
    for i in range(len(rainfalls)): #통의 크기를 잼 ->i의 위치를 찾음
        r = rainfalls[i]
        m = years[i]
        if m in selected_years: #[6,7,8]
            total_value += r
    return total_value


def sum_annual (rainfalls,years):
    dataset = {}
    for y in range(2001,2003):
        dataset[y] = sumifs(rainfalls,years, [y])
    return dataset


import os
import requests 

def download_weather(weather_filename,sy,ey):
    year =2023
    url = f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"

    filename = f"lec/lec12/weather_{year}.csv"

    if not os.path.exists(filename): #파일이 있을 ㄸ떄

        resp =requests.get(url)
        with open(filename,"w") as fout:
            fout.write(resp.text)
        
    else:
        print(f"ㅇㅣ미 {filename}이 있습니다.")

def main():
    weather_filename = "lec/lec12/weather(146)_2001-2022.csv"

    
    if not os.path.exists(weather_filename):
        download_weather(weather_filename,2021,2022)

    rainfalls= read_weather_col(weather_filename,9,float)
    years= read_weather_col(weather_filename,0,int)
    rainfall_2021 = sumifs(rainfalls, years,[2021])
    rainfall_2022 = sumifs(rainfalls, years,[2022])

    # print(months)
    # print(rainfalls)
    #print(f" 여름철 총 강수량은 {sum(rainfalls)} 입니다.") 
    print(f" 2021년 강수량은 {rainfall_2021:.1f}mm 입니다.") #1496
    print(f" 2022년 강수량은 {rainfall_2022:.1f}mm 입니다.") #1071

    for y in range(2001,2003):
        rainfall_y = sumifs(rainfalls,years, [y])
        print(f"{y}년 강수량은 {rainfall_y:.1f}입니다.")

    # rainfall_annual = sum_annual (rainfalls,years)
    # print(rainfall_annual[2006])


if __name__=="__main__":
    main()