import datetime as dt


def day_calculator(str: str):
    dates = str.split('-')
    year, month, days = int(dates[0]), int(dates[1]), int(dates[2])  # date = datetime.strptime(date_str,'%Y-%m-%d')
    born = dt.date(1999, 1, 14) # sajjad_bdate = datetime.strptime("1999-01-14",'%Y-%m-%d')
    d2 = dt.date(year, month, days)
    delta = (d2 - born).days # return days of years 
    if delta < 0:
        return 'Not yet born'
    else:
        return delta
