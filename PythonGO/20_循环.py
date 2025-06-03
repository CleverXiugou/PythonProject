# for循环
name = "Where are you from?"

for x in name:
    print(x,end=' ')
print()
count = 0
for x in name:
    if x == "e":
        count+=1
print(f"name中e出现了{count}次")

# range语句
# range(num)表示从0到num，不包含num
for x in range(10):
    print(x,end=' ')
print()

# range(num1,num2)表示从num1到num2，左闭右开
for x in range(14,20):
    print(x,end=' ')
print()

# range(num1,num2,num3)表示从num1到num2，步数为num3，左闭右开
for x in range(2,20,2):
    print(x,end=' ')
print()

# 可以借用range来确定for循环的次数
for x in range(10):
    print("I love python!")

# 我们可以在外部访问到for循环里面的局部变量，虽然我们不建议这么做
# 如果想要访问它，可以再循环前定义它
num = 0
for num in range(5):
    print(num,end=' ')
print(num)

# 嵌套循环
for i in range(10):
    for j in range(10):
        print(i*j,end='\t')
    print()

# 中断循环，continue和 break
for i in range(1,6):
    if i % 2 == 0:
        continue
    print(i,end=' ')
print()

for i in range(1,6):
    if i == 4:
        break
    print(i,end=' ')
print()
