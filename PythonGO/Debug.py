money=50000
name=None

name=input("该死,快给自己起个好听的名字吧:")

# 查询
def fuc():
    print("欢迎进入查询余额系统!")
    print(f"你好{name},你的账户还有{money}元!")

# 存款
def save(num):
    global money # 把money设定为全局变量
    money+=num
