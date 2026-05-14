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


def get_max_diff_by_year(dates, tmax, tmin, start_year=2001, end_year=2021):
    result = {}

    for i in range(len(dates)):
        y, m, d = dates[i]
        if y < start_year or y > end_year:
            continue

        diff = tmax[i] - tmin[i]

        if y not in result or diff > result[y][0]:
            result[y] = (diff , dates[i])
     
    return result


def gdd_by_year(dates, tavg, start_year=2001, end_year=2021):
    gdd_value = {}
    for i in range(len(dates)):
        y, m, d = dates[i]
        t = tavg[i]
        if m in [5, 6, 7, 8, 9]:
            continue

        if t > 5:
            if y not in gdd_value:
                gdd_value[y] = 0
            gdd_value[y] += (t - 5)

    return gdd_value


def main():
    weather_filename = "lec/lec12/hw14/weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename,3)
    tmin = read_weather_col(weather_filename,5)
    tavg = read_weather_col(weather_filename,4)

    max_diff_by_year = get_max_diff_by_year(dates, tmax, tmin, start_year=2001, end_year=2021)
    for year in sorted(max_diff_by_year):
        diff, date = max_diff_by_year[year]
        print(f"일교차 최대 날짜 : {date}, 일교차 : {diff:.1f}도")
        
    gdd_year = gdd_by_year(dates, tavg, 2001, 2021)
    for year in sorted(gdd_year):
        print(f"{year}년 5~9월 적산온도: {gdd_year[year]:.1f}도/일")
   

if __name__=="__main__":
    main()