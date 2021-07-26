def func1(tep1,pa1):
    if tep1 > 30 or tep1 < -8:
        print("bushushi")
    if pa1 >300 or pa1<20:
        print("bushushi")
    if 25 < tep1 <= 30 and 200 < pa1 <= 300:
        print("bijiaoshushi")
    elif 10 < tep1 <= 25 and 100 < pa1 <= 200:
        print("tebieshushi")
    elif -8 <= tep1 <=10 and 20 <= pa1 <= 100:
        print("bijiaoshushi")
    else:print("wufapanduan")

tep = input("请输入今天德温度")
pa = input("请输入今天的气压")
tep1 = int(tep)
pa1 = int(pa)
func1(tep1,pa1)

