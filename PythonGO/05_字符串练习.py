# 分割字符串
str1="itheima itcast boxuegu"
# 1.统计有多少个"it"字符
print(f"一共有{str1.count("it")}个it字符")

# 2.将字符串中的空格使用"|"代替
str2=str1.replace(" ","|")
print(str2)

# 3.将字符串以"|"为分割符,存入到列表中
the_list=str2.split("|")
print(the_list)

# 股价计算小程序
company_name="Wine"
stock_price=15
stock_code="021120110"
stock_price_daily_growth_factor=1.2
growth_day=7

message=(f"公司名:{company_name},股票代码:{stock_code},当前股价:{stock_price}\n"
         f"每日增长系数:{stock_price_daily_growth_factor},经过{growth_day}天的增长后,"
         f"股价为:%.2f!" % (stock_price * stock_price_daily_growth_factor ** growth_day))
print(message)