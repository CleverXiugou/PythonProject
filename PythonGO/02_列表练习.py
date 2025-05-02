# 定义列表
the_list= [21, 25, 21, 23, 22, 20]
print(the_list)
# 追加一个数字33到末尾
the_list.append(31)
print(the_list)
# 追加一个新列表到末尾
new_list=[29,33,30]
the_list.extend(new_list)
print(the_list)
# 从列表中取出第一个元素
the_first=the_list[0]
print(the_first)

# 取出最后一个元素
the_last=the_list[-1]
print(the_last)

# 查找元素31,返回其位置
print(the_list.index(31))