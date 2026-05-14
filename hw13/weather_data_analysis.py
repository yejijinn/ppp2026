def read_weather_col(filename,col_idx, conv_fn):     #나중에conv_f로 인헤서 나중에 메인함수에서 int, float 결정 가능 
    dataset=[]                                      #def read_weather_col(filename,col_idx=9, conv_fn=float): 
    with open (filename) as f:
        lines = f.readlines()
        for line in lines [1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def sumifs(rainfalls, months, selected_month ):
    total_value = 0
    for i in range(len(rainfalls)): #통의 크기를 잼 ->i의 위치를 찾음
        r = rainfalls[i]
        m = months[i]
        if m in selected_month: #[6,7,8]
            total_value += r
    return total_value

# selected_rain = []
# for m, r in zip(months, rainfalls):
#     if m in selected_month:
#         selected_rain.append(r)
#     return sum ([r for m, r in zip (months, rainfalls) if m in selected_month])


def main():
    weather_filename = "lec/lec11/weather(146)_2022-2022.csv"
    rainfalls= read_weather_col(weather_filename,9,float)
    months= read_weather_col(weather_filename,1,int)
    summer_rainfall = sumifs(rainfalls, months,[6,7,8])

    # print(months)
    # print(rainfalls)
    #print(f" 여름철 총 강수량은 {sum(rainfalls)} 입니다.") 
    print(f" 여름철 강수량은 {summer_rainfall:.1f}mm 입니다.") 

if __name__=="__main__":
    main()