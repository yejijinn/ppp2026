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
    stid = 146
    sy = 1980
    ey = 2024

    filename = f"lec/lec14/weather_jeonju_{sy}-{ey}.csv"
    download_weather(filename,stid,sy,ey)
    df = pd.read_csv(filename, skipinitialspace = True)

    fig, ax = plt.subplots(figsize=(15, 6))
    
    year = [str(x) for x in range(sy, ey + 1)]

    rain = []
    for i in range(sy,ey+1):
        total_rain = df[df["year"]== i ]["rainfall"].sum()
        rain.append(total_rain)

    ax.bar(year, rain, color="b")

    ax.set_ylabel("연간 강수량 (mm)")

    fig.savefig("./bar_rain.png")

    plt.show()

if __name__ == "__main__":
    main()