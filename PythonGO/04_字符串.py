# python中的字符串不支持修改
my_str="Niko hello"

# index方法,找到索引值
print(my_str.index("k"))

# replace方法,replace(str1,str2),将字符串中的str1全部换成str2
# 此操作不改变原字符串,返回值为一个新字符串
new_str=my_str.replace("l","L")
print(new_str)

# split方法,将字符串中的字符按照某种形式切分,把切分后的字符串存入列表中
the_list=my_str.split(" ")
print(the_list)

# strip方法,用于去除字符串前后的空格
test_str=" Donk is the most strongest player in CS2 "
print(test_str.strip())
# 如果传入了参数,那么会去除字符串前后指定的字符串,无论顺序如何
str1="12Donk is the most strongest player in CS212"
# 此时参数为“12”,意味着只要前后出现了“1”,或者“2”,都会去除
print(str1.strip("12"))