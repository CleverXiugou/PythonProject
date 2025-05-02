# 对级别为1对员工加薪1000元,且级别升为2级

# 初始数据
the_employee={
    "Niko":{
        "角色":"步枪手",
        "工资":8000,
        "级别":1
    },
    "Donk":{
        "角色":"步枪手",
        "工资":9000,
        "级别":2
    },
    "Monesy":{
        "角色":"狙击手",
        "工资":8800,
        "级别":2
    },
    "zywoo":{
        "角色":"狙击手",
        "工资":9000,
        "级别":3
    },
    "Hooxi":{
        "角色":"指挥",
        "工资":6000,
        "级别":1
    }
}

# 遍历涨薪
for value in the_employee:
    if the_employee[value]["级别"]==1:
        the_employee[value]["级别"] =2
        the_employee[value]["工资"] +=1000

# 输出最终结果
for value in the_employee:
    print(value,end=":")
    print(the_employee[value])
