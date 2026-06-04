import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib
import os
import requests 
import pandas as pd

def download_weather(filename, stid, sy, ey):
    url = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"

    if not os.path.exists(filename): 

        resp =requests.get(url)
        with open(filename,"w") as fout:
            fout.write(resp.text)
        
    else:
        print(f"이미 {filename}이 있습니다.")

def main():
    sy = 1980
    ey = 2014
    filename = f"lec/lec14/weather_jeonju_{sy}-{ey}.csv"
    download_weather(filename,146,sy,ey)

    df = pd.read_csv(filename, skipinitialspace = True)

    byear = 2006
    bmonth = 6
    bday =28

    df_birth = df[(df["month"] == bmonth) & (df["day"] == bday)]
#최고최저ㅏ기온있는 열 추출 -> 년도 추출위해서
    max =df_birth[df_birth["tavg"] == df_birth["tavg"].max()] 
    min=df_birth[df_birth["tavg"] == df_birth["tavg"].min()]

    max_year = int(list(max["year"])[0])
    min_year = int(list(min["year"])[0])

    #2006년 뽑긱
    year_in_chart = df_birth[df_birth["year"] == byear]
    temp_in_chart = float(list(year_in_chart["tavg"])[0])

    h_2006 = df_birth[df_birth["tavg"] > temp_in_chart]# 나보다 기온이 더 높음
    rank = len(h_2006) + 1     #기온높은 날짜 +1

    # print(f"내가 태어난 해{byear}년의 기온 = {temp_in_chart:.1f}℃ ")
    print(f"{byear}은 1980-2024 사이에 몇{rank}번째로 온도가 높았습니다.")
    print(f"가장 온도가 높았던 해: {max_year}년 ")
    print(f"가장 온도가 낮았던 해: {min_year}년 ")

    year = [str(x) for x in df_birth["year"]]
    temp = list(df_birth["tavg"])
    plt.plot(year,temp, color="r", label="전주") #순서대로x,y 데이터로 들어감...

    plt.xlabel("연도")
    plt.ylabel("기온(℃)")

    plt.legend()
    plt.savefig("./line_temp_hangul.png")
    plt.show()

if __name__ == "__main__":
    main()