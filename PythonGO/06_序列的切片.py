# 从一个序列中取出子序列
# 语法:序列[起始下标:结束下标:步长]
# 起始下标:左闭,留空时为从头开始
# 结束下标:右开,留空时为取到最后
# 步长:取元素的间隔,参数为1时为依次取出,参数为2为间隔取出
my_list=[1,2,3,4,5,6]

# 从头取到下标为2的前一位,间隔为1
print(my_list[0:2:1])

# 从下标为1开始取到最后一位,间隔为2
print(my_list[1::2])

# 从后向前取,间隔为1
print(my_list[::-1])

# 从下标3开始,取到下标为1,间隔为1
print(my_list[3:1:-1])