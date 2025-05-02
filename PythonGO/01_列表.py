# 列表容器
from traceback import print_tb

name_list=["Niko","Monesy","Hooxi","Hunter","JKS"]
print(name_list)
print(type(name_list))

# 容器中可以存不同类型的元素
my_list=["Niko",22,True]
print(my_list)
print(type(my_list))

# 容器中也可以嵌套容器
special_list=["Niko",["JKS","Apex",666],False]
print(special_list)
print(type(special_list))

# 从前向后取
print(my_list[0])
print(my_list[1])

# 从后向前取
print(my_list[-1])
print(my_list[-2])

# 取出嵌套元素
print(special_list[1][1])

# index方法,可以查找元素在容器中的位置,如果不存在,报错
pos=my_list.index(22)
print(pos)

# 赋值
my_list[2]=False
print(my_list)

# 插值
my_list.insert(1,"Hooxi")
print(my_list)

# 在最后位置插值,参数为元素
my_list.append("Fuck")
print(my_list)

# 把一个容器的元素全部插到另一个容器,参数为另一个容器名称
my_list.extend(special_list)
print(my_list)

# 删除元素,参数为元素下标
del my_list[5]
print(my_list)

# pop用法:在删除元素的同时,可以赋值给其他元素,参数为元素下标
factor=my_list.pop(0)
print(factor)
print(my_list)

# 在容器中删除搜索到的第一个元素,参数为元素
my_list.remove(False)
print(my_list)

# 统计元素在容器的数量
count=my_list.count(False)
print(count)

# 统计容器中所有元素的数量
total=len(my_list)
print(total)

# 使用while循环

new_list=[11,13,14,15,16]
index=0
while index<len(new_list):
    print(new_list[index],end=" ")
    index+=1
print()

# 使用for循环
for i in new_list:
    print(i,end=" ")
print()

# 清空容器
my_list.clear()
print(my_list)
