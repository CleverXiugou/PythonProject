# 用写入方法打开文件,如果文件存在,会将原文件清空后写入,文件不存在会创建新的文件进行操作
f=open('/Users/mendacityyep/Documents/Hello Python!.md','w')

# 将内容写入内存中
f.write("The extra content !")

# 将内存中的内容写入到硬盘中
f.flush()

# 在关闭文件时,会自动把内存中的文件写入硬盘
f.close()