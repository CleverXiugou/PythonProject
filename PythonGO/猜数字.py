import random
# 生成的数字在1～100之间
target_num=random.randint(1,100)
count=0
print("数字范围在1～100之间...")
while True:
    num=int(input("请输入猜的数字..."))
    count=count+1
    if num==target_num:
        print("恭喜你猜对了!")
        break
    elif num>target_num:
        print("猜的数字有点大了!")
    else:
        print("猜的数字有点小了!")

print(f"共用了{count}次猜出数字{target_num}!")