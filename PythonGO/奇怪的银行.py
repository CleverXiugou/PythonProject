from random import choice

money = 50000
name = input("该死,快给自己起个好听的名字吧:\n")


# 查询
def check():
    print(f"你好{name},你的账户还有{money}元!")


# 存款
def save(num):
    global money  # 把money设定为全局变量
    money += num
    print(f"你已经成功存入{num}元,账户还剩{money}元!")


# 取款
def cost(num):
    global money
    money-=num
    print(f"你已经成功取出{num}元,账户还剩{money}元")



print("你好,欢迎来到奇怪的银行系统!")
print("查看余额请按\t1")
print("存款请按\t2")
print("取款请按\t3")
print("退出系统请按\t4")
while True:
    choice = int(input())
    if choice==4:
        print("即将退出系统")
        break
    elif choice==1:
        check()
    elif choice==2:
        num=int(input("你想存多少钱:"))
        save(num)
    else:
        num=int(input("你想取多少钱:"))
        cost(num)

