# 自定义统计字符串长度函数
def str_len(str):
    count = 0
    for i in str:
        count += 1
    return count
str1 = "Hello Python!"
print(f"字符串长度是{str_len(str1)}")
