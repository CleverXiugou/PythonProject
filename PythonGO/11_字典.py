# 定义空字典
from 列表练习 import the_first

empty_dict=dict()
print(empty_dict)

# 定义字典变量
my_dict={
    "Niko":92,
    "Donk":100,
    "Monesy":98,
    "Hunter":67
}
print(my_dict)

# 字典不允许key值重复,新数据会覆盖旧数据
the_dict={
    "Niko":100,
    "Niko":32
}
print(the_dict)

# 取出字典的值
print(my_dict["Donk"])

# 字典可以嵌套,案例:学生成绩单
the_player={
    "Donk":{
        "ADR":96.1,
        "SURVIVING":0.32,
        "RATING":1.34
    },
    "Monesy":{
        "ADR":89,
        "SURVIVING":0.38,
        "RATING":1.29
    },
    "zywoo":{
        "ADR":92.1,
        "SURVIVING":0.37,
        "RATING":1.32
    }
}
print(the_player)

# 获奖某人的具体信息
print(the_player["Donk"]["ADR"])

# 新增元素或修改元素
my_dict["Niko"]=99
my_dict["bit"]=92
print(my_dict)

# 删除元素,同时获得删除元素的值
value=my_dict.pop("bit")
print(my_dict)
print(value)

# 获取全部的key值
keys=my_dict.keys()
print(keys)

# 使用keys遍历字典
for key in keys:
    print(my_dict[key],end=" ")
print()

# 直接遍历字典
for value in my_dict:
    # 这样是遍历key值
    print(value,end=" ")
    # 这样是遍历value值
    print(my_dict[value],end=" ")
    print()

# 统计字典元素数量
print(len(my_dict))

# 清空字典
my_dict.clear()
print(my_dict)