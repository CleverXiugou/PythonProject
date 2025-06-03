# i表示在输出第i行
# j表示在输出这一行的第j个式子
i=1
# 一共需要输入9行
while i<=9:
    # 每行都要从第一个式子开始输出
    j=1
    while j<=i:
        print(f"{j} * {i} = {j*i}\t",end=' ')
        j+=1
    i+=1
    print()

# 使用for循环完成九九乘法表
# x表明现在在输出第几行，范围是从第一行到第九行
for x in range(1,10):
    # y表明在输入该行的第几个式子，范围是从第一行到第x行
    for y in range(1,x+1):
        print(f"{y} * {x} = {x*y}",end='\t')
    print()
