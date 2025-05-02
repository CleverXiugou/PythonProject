# 打开指定文件,统计文件中"Niko"的数量
from itertools import count

# 方法一,直接读取整个文件中Niko字符的数量
with open("/Users/mendacityyep/Documents/word.md","r") as f:
     res=f.read().count("Niko")
     print(res)

# 方法二,
with open("/Users/mendacityyep/Documents/word.md","r") as f2:
    res=0
    # 逐行读取文件
    for line in f2:
        # 去除文件前后的空格和换行符
        line=line.strip()
        # 将每个单词存入列表
        words=line.split(" ")
        # 遍历列表,遇到Niko时,计数器加一
        for word in words:
            if word=="Niko":
                res+=1
    print(res)