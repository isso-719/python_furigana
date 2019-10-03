a, b, c, d, e = input("チーム名を連続で入力").split()

team = [a, b, c, d, e]
opps = [a, b, c, d, e]

for t1 in team:
    opps.remove(t1)
    for t2 in opps:
        print(t1, "vs", t2)
