# __author: Administrator
# date:  2020/7/14

product_list = [
    ('Mac', 9000),
    ('kindle', 800),
    ('tesla', 900000),
    ('python book', 105),
    ('bike', 2000)
]
shopping_car = []

saving = input("please input your money:")

if saving.isdigit():
    saving = int(saving)
    while True:

        for i, (v, j) in enumerate(product_list, 1):
            print(i, ">>>>>", v, j)
        choice = input('选择购买商品编号[退出：q]：')

        if choice.isdigit():
            choice = int(choice)
            if 0 < choice < len(product_list) + 1:
                p_item = product_list[choice - 1]
                if p_item[1] <= saving:
                    if p_item not in shopping_car:
                        saving -= p_item[1]
                        shopping_car.append(p_item)
                        print(p_item[0], "已加入购物车，当前余额剩余：%d" % saving)
                    else:
                        print(p_item[0], "已加入购物车，请误重复添加")
                else:
                    print("余额不足，剩余%d元" % saving)
            else:
                print('编码不存在')
        elif choice.lower() == "q":
            print("*" * 10, "您已经购买以下商品", "*" * 10)
            for i, v in shopping_car:
                print(i, v)

            print("当前余额为：%d元" % saving)
            print("欢迎下次光临")

            break
        else:
            print('invalid input')


