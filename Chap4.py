import Chap4func

data = [{"name": "山本", "bill": 40000, "crg": True},
        {"name": "吉田", "bill": 25000, "crg": False}]

for rec in data:
    bill = rec["bill"]
    if rec["crg"]:
        bill = Chap4func.add_charge(bill)

    Chap4func.create_mail(rec["name"], bill)
