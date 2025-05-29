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