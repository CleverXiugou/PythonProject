# 分割字符串
str1="itheima itcast boxuegu"
# 1.统计有多少个"it"字符
print(f"一共有{str1.count("it")}个it字符")

# 2.将字符串中的空格使用"|"代替
str2=str1.replace(" ","|")
print(str2)

# 3.将字符串以"|"为分割符,存入到列表中
the_list=str2.split("|")
print(the_list)