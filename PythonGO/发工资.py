import random
sum = 10000
for i in range(1,21):
    score = random.randint(1,10)
    if score >= 5:
        if sum <1000:
            print("奖金已经发完，下个月再来领取吧！")
            break
        sum -= 1000
        print(f"员工{i}绩效为{score},发放奖金1000元")
    else:
        print(f"员工{i}绩效为{score},未达到标准，扣除奖金")
