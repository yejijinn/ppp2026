import os
import requests 
import pandas as pd

def download_weather(filename, stid, sy, ey):
    url = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"

    if not os.path.exists(filename): #파일이 있을 ㄸ떄

        resp =requests.get(url)
        with open(filename,"w") as fout:
            fout.write(resp.text)
        
    else:
        print(f"이미 {filename}이 있습니다.")

def main(): #수원 부분 다시 해보기
   sy = 1980
   ey = 2024
   filename = f"lec/lec14/weather_jeonju_{sy}-{ey}.csv"
   filename_sw= f"lec/lec14/weather_suwon_{sy}-{ey}.csv"
    #변수 따로 지정 해주기
   download_weather("lec/lec14/weather_jeonju_1980-2024.csv",146,sy,ey)
   download_weather("lec/lec14/weather_suwon_1980-2024.csv",119,sy,ey)

   df = pd.read_csv(filename, skipinitialspace = True)
   df_sw = pd.read_csv(filename_sw, skipinitialspace = True)

   #print(df.head())

   print(df[df["year"] == 2012]["rainfall"].sum()) # 1번  
   print(df[df["year"] == 2024]["tavg"].max()) # 2번

   df["tdiff"] = df["tmax"] - df ["tmin"]
   print(df[df["year"] == 2020]["tdiff"].max()) #3번

   prec_jj = df[df["year"] == 2019]["rainfall"].sum()
   prec_sw = df_sw[df_sw["year"] == 2019]["rainfall"].sum()
   print(abs(prec_jj - prec_sw)) #4번

if __name__=="__main__":
    main()