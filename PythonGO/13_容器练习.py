my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str="abcdefg"
my_set={1,2,3,4,5}
my_dict={
    "key1":1,
    "key2":2,
    "key3":3,
    "key4":4,
    "key5":5,
}

# 找出最大最小元素使用max和min函数
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))

print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))

# 通用转换
# 转列表
print(list(my_list))
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict))

# 转元组
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_str))
print(tuple(my_set))
# 此时value会丢失
print(tuple(my_dict))

# 转字符串,尽管输出没什么变化,实际上已经成了字符串,省略了双引号
print(str(my_list))
print(str(my_tuple))
print(str(my_str))
print(str(my_set))
print(str(my_dict))

# 转集合
print(set(my_list))
print(set(my_tuple))
# 由于集合数据无序,此时字符串不一定按照原来的顺序
print(set(my_str))
print(set(my_set))
# value值丢失
print(set(my_dict))

# 无法转字典,因为字典中存储的数据是键值对

my_list=[3,1,2,5,4]
my_tuple=(3,1,2,5,4)
my_str="agbfced"
my_set={3,1,2,5,4}
my_dict={
    "key3":3,
    "key1":1,
    "key2":2,
    "key5":5,
    "key4":4,
}

# 对容器排序,默认从小到大,使用reverse=True参数可从大到小排序
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))

print(sorted(my_list,reverse=True))
print(sorted(my_tuple,reverse=True))
print(sorted(my_str,reverse=True))
print(sorted(my_set,reverse=True))
print(sorted(my_dict,reverse=True))



