# 定义集合
my_set={"Niko","JKS","Hooxi","Monesy","Hunter"}
# 定义空集合
empty_set=set()

# 集合是无序的,不支持下标访问

# 集合添加元素
my_set.add("Fuck")
print(my_set)

# 移除元素
my_set.remove("JKS")
print(my_set)

# 随机取出一个元素,取出后,集合将删除这个元素
value=my_set.pop()
print(f"取出的元素是{value},集合中还剩下{my_set}")

# 清空集合
my_set.clear()
print(my_set)

# 取出集合1和集合2的差集:set1中有且set2中没有的元素
set1={1,2,3}
set2={2,4,6}
print(set1.difference(set2))

# 删除差集,删除set1中和set2中相同的元素,会改变set1的内容,set2中不会发生变化
set1.difference_update(set2)
print(set1)
print(set2)

# 合并差集,将set1和set2中元素合并,返回值为合并的新集合,原集合不变
set1={2,4,5}
set2={5,3,7}
set3=set1.union(set2)
print(set1)
print(set2)
print(set3)

# 统计集合中元素的数量
print(len(set3))

# 集合遍历
for element in set3:
    print(element,end=" ")
