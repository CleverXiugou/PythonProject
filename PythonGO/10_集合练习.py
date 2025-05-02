# 将列表中的元素去重
my_list=[1,2,3,3,2,4,5,7]

my_set=set()

for element in my_list:
    my_set.add(element)

print(my_set)