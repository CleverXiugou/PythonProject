# lambda匿名函数

# 定义一个函数,接受其他函数的输入
def fuc(compute):
    value=compute(1,2)
    print(value)

# 匿名函数格式: lambda 参数 : 逻辑
# 逻辑只能一行
fuc(lambda x,y:x+y)