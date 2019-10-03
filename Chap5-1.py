from datetime import date, timedelta
start = date(2019, 5, 8)
youbi = "月火水木金土日"

for d in range(14):
    cur = start + timedelta(days=d)
    wd = cur.weekday()
    print(cur, youbi[wd])
