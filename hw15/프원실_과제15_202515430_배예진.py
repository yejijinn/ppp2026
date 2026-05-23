import requests
import os

def read_weather_col(filename,col_idx):
    values = []
    with open(filename) as f :
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            values.append(value)

    return values


def get_days_over_5mm(rainfall):
    count_5mm = 0
    for r in rainfall:
        if r >= 5:
            count_5mm += 1
    return count_5mm


# def every_rain(rainfall):
#     sum (rainfall)

def main():
    year =2023
    url = f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"

    filename = f"lec/lec12/weather_{year}.csv"


    if not os.path.exists(filename): #파일이 있을 ㄸ떄

        resp =requests.get(url)
        with open(filename,"w") as fout:
            fout.write(resp.text)
        
    else:
        print(f"이미 {filename}이 있습니다!!!!!!!!!!!!!")

    tavg = read_weather_col(filename,4)
    annual_tavg = sum(tavg)/len(tavg)

    rainfall = read_weather_col(filename,9)
    days_over_5mm = get_days_over_5mm(rainfall) 
    all_rain = sum(rainfall)
    
    print(f"연 평균 기온 = {annual_tavg:.2f}")
    print(f"5mm 이상인 총 강우일수는 {days_over_5mm}일 입니다.")
    print(f"총 강우량은 {all_rain}mm입니다. ")


if __name__=="__main__":
    main()