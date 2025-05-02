# 打开文件,参数:地址,方法
import time

f=open('/Users/mendacityyep/Documents/Hello Python!.md','r')
print(type(f))

# 读取文件,参数为读取字节长度,如果没有参数,默认读取所有字节
print(f.read(2))
# 同一程序中多次使用read,会在下次会在上次结尾处接着读
print(f.read())


# readlines 读取文件全部行,封装到列表中
the_list=f.readlines()

# readline 读取一行,封装到列表中
list2=f.readline()

# for循环逐行读入数据
for line in f:
    print(line)

# 关闭文件
f.close()

# 在执行完操作后自动关闭程序
with open('/Users/mendacityyep/Documents/Hello Python!.md','r') as f:
    for line in f:
        print(line)
