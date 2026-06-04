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
    ey = 2024
    filename = f"lec/lec14/weather_jeonju_{sy}-{ey}.csv"
    filename_sw = f"lec/lec14/weather_suwon_{sy}-{ey}.csv"
    #변수 따로 지정 해주기
    
    download_weather(filename,146,sy,ey)
    download_weather(filename_sw,119,sy,ey)

    df = pd.read_csv(filename, skipinitialspace = True)
    df_sw = pd.read_csv(filename_sw, skipinitialspace = True)

    year = [str(x) for x in range(sy, ey + 1)]

    tavg_jj = []
    tavg_sw = []


    for i in range(sy,ey+1):
        temp_jj = df[df["year"]== i ]["tavg"].mean()
        temp_sw = df_sw[df_sw["year"]== i ]["tavg"].mean()

        tavg_jj.append(temp_jj)
        tavg_sw.append(temp_sw)


    # tavg = (df[df["year"] == 2024]["tavg"].sum())

    plt.plot(year,tavg_jj, color="r", label="전주")
    plt.plot(year,tavg_sw, color="b", label="수원")

    plt.ylabel("기온(℃)")

    plt.legend()
    plt.savefig("./line_temp_hangul.png")
    plt.show()

if __name__ == "__main__":
    main()