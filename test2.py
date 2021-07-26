#你们公司每月的净利润计算公式如下
#( 总收入 -  会计小王薪资  - 餐饮费 - 交通费 ) * 80%税费剩余
#请大家写Python程序，合理的使用变量 和注释 ，计算 并 打印出 每月的净利润。
#具体的 收入和支出 数值，使用input函数，让用户输入。
def fun1(total,wang,food,bus):
    return (total-wang-food-bus) * 0.8
total = input("请输入总收入：")
wang = input("请输入小王薪资:")
food = input("请输入餐饮费:")
bus = input("请输入交通费:")
str = fun1(int(total),int(wang),int(food),int(bus))
print(str)

#请定义一个函数printlen, 该函数中让用户输入一个字符串， 该函数打印出用户输入的这个字符串的 长度
#比如 用户输入 123456789， 该函数应该打印出：长度为9
def printlen():
    shuru = input("请输入一个字符串")
    print(len(shuru))

printlen()