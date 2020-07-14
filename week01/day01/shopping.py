
iphone_price = 5800
mac_price = 9000
coffee_price = 32
python_price = 80
bicyle_price = 1500

list = []
salary = int(input("Please input your salary:"))
print("**********欢迎来到购物车系统**********")

while True:
    print("1. iPhone 11   ————%d元" % iphone_price)
    print("2. Mac book   ————%d" % mac_price)
    print("3. coffee   ————%d元" % coffee_price)
    print("4. python book   ————%d元" % python_price)
    print("5. bicyle   ————%d元" % bicyle_price)
    print("0. 退出")

    operator = int(input("Please input your choose:"))

    if operator == 1:
        if salary >= iphone_price:

            list.append(["iPhone", iphone_price])
            salary -= iphone_price
            print("iPhone 11已加入到你的购物车，当前余额剩余：%d" % salary)
        else:
            print("余额不足，剩余 %d" % salary)
    elif operator == 2:
        if salary >= mac_price:
            list.append(["Mac Book", mac_price])
            salary -= mac_price
            print("Mac Book已加入到你的购物车，当前余额剩余：%d" % salary)
        else:
            print("余额不足，剩余 %d" % salary)
    elif operator == 3:
        if salary >= coffee_price:
            list.append(["Coffee", coffee_price])
            salary -= coffee_price
            print("Coffee已加入到你的购物车，当前余额剩余：%d" % salary)
        else:
            print("余额不足，剩余 %d" % salary)
    elif operator == 4:
        if salary >= python_price:
            list.append(["Python Book", python_price])
            salary -= python_price
            print("Python Book已加入到你的购物车，当前余额剩余：%d" % salary)
        else:
            print("余额不足，剩余 %d" % salary)
    elif operator == 5:
        if salary >= bicyle_price:
            list.append(["Bicyle", bicyle_price])
            salary -= bicyle_price
            print("Mac Book已加入到你的购物车，当前余额剩余：%d" % salary)
        else:
            print("余额不足，剩余 %d" % salary)
    elif operator == 0:
        break
        exit()
    else:
        print("输入错误，请重新输入")


if list is not None:
    print("您已购买以下商品：")
    for i in list:
        print("%s %d" % (i[0], i[1]))

print("您的余额为：%d" % salary)
print("欢迎下次光临")