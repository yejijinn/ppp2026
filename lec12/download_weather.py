import requests
import os

def main():
    year =2023
    url = f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"

    filename = f"lec/lec12/weather_{year}.csv"


    if not os.path.exists(filename): #파일이 있을 ㄸ떄

        resp =requests.get(url)
        with open(filename,"w") as fout:
            fout.write(resp.text)
        
    else:
        print(f"ㅇㅣ미 {filename}이 있습니다.")


if __name__=="__main__":
    main()