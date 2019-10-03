def create_mail(recv, bill):
    tmp = '''{}様
磯貝です。
今月の請求額は{}円です。'''
    msg = tmp.format(recv, bill)
    print(msg)


def add_charge(bill):
    return int(bill * 1.07)
