def user_info(name,age,gender):
    print(f"名字是{name},年龄为{age},性别为{gender}")

# 位置传参
user_info("Hooxi","26","Male")

# 关键字传参
user_info(name="Hooxi",age=26,gender="Male")
# 位置可以颠倒
user_info(age=26,name="Hooxi",gender="Male")
# 可以和位置传参混用,当混用的时候,必须把位置参数放在最前面
user_info("Hooxi",age=26,gender="Male")

# 缺省传参
def user_info(name,age,gender="男"):
    print(f"名字是{name},年龄为{age},性别为{gender}")

# 如果没有给出参数,那么就使用默认参数
user_info("Niko",28)
# 可以覆盖默认参数
user_info("憨憨",age=27,gender="女")

# 不定常传参,传入的参数长度任意
# 1.位置传参:agrs作为一个元组传入,
def user_info(*args):
    print(f"args参数的类型为{type(args)},值为{args}")
user_info(1,2,3,"Niko")

# 2.关键字传参:
def user_info(**kwargs):
    print(f"kwargs参数的类型为{type(kwargs)},值为{kwargs}")
user_info(name="Niko",age=28,gender="男")

# 函数传参--函数嵌套
def add(a,b):
    return a+b

def fuc():
    print(add(1,2))

fuc()



