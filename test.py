def make_great(names):
    # 对原列表进行遍历
    while names:
        # 对每一个列表元素进行出栈操作，并在前面添加字符串，并保存在当前变量中
        new = '0000'
        current_name = int(new) + names.pop()
        # 把当前变量保存在新列表中
        b.append(current_name)

    return b  # 返回新列表


b = []
for i in range(1,5):
    b.append(i)
a = make_great(b)
print(b)