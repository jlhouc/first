'''
有如下的代码，定义了一个Python列表 变量
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
请接下来写一行代码，打印出var1这个列表变量里面的 字符串 hello world!
'''
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1[2])
print(var1[1][1])
var1[2]="oh my god"
var1[1][1]="stones"
print(var1)


def func(arg):
    arg[0] = 'hello'

var = ['ok']
func(var)
print(var)