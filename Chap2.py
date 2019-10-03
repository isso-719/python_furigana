text = input("年齢入力")

if text.isdigit():

    age = int(text)

    if age < 20:

        if age < 6:
            print("幼児")
        elif 6 <= age <= 18:
            print("未成年(義務教育期間)")
        else:
            print("未成年")
    elif age < 65:
        print("成人")
    else:
        print("高齢者")
else:
    print("数字を入力してください")
