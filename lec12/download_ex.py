import requests
def main():
    url = "https://www.jbnu.ac.kr/web/unvrslife/campuslife/cafeteria/dataAjax.do?type=day"

    resp = requests.get(url)
    print(resp.text)

    with open("lec/lec12/cafe.html","w") as fout:
        fout.write(resp.text)

if __name__=="__main__":
    main()