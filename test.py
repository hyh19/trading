# 浮盈加仓

from decimal import *
import math

getcontext().prec = 7

coin = "ETH"
print("交易币种 {}".format(coin))

# 实际杠杆倍数
leverage = Decimal(2)
# 开仓杠杆倍数
leverage_100x = Decimal(100)
# 仓位比例
position = leverage / leverage_100x
print("实际杠杆倍数 {:.2f} = 开仓杠杆倍数 {:.2f} X 仓位比例 {:.2%}".format(
    leverage, leverage_100x, position))

total_balance = init_balance = Decimal(17000)
print("初始资金总额 {:.2f} USDT".format(total_balance))

margin = init_balance * leverage / leverage_100x
print("初始保证金 {:.2f} USDT".format(margin))

open_price = Decimal(1000)
print("开仓价格 {:.2f} USDT".format(open_price))

close_price = Decimal(3000)
print("平仓价格 {:.2f} USDT".format(close_price))

interval = Decimal(0.1)
print("加仓间隔 {:.2%}".format(interval))

n = math.ceil(math.log(close_price/open_price, Decimal(1)+interval))
print("加仓次数 {} 次".format(n))

print("-" * 24)

for i in range(n):

    print("第 {} 次加仓".format(i+1))

    open_price += open_price * interval
    print("加仓价格 {:.2f} USDT".format(open_price))

    print("上次保证金 {:.2f} USDT".format(margin))

    profit = margin * leverage_100x * interval
    print("上次盈利金额 {:.2f} USDT".format(profit))

    total_balance += profit
    print("当前资金总额 {:.2f} USDT".format(total_balance))

    new_margin = total_balance * leverage / leverage_100x
    print("本次保证金 {:.2f} USDT".format(new_margin))

    call_margin = new_margin - margin * (Decimal(1) + interval)
    print("追加保证金 {:.2f} USDT".format(call_margin))

    margin = new_margin

    print("-" * 24)

print("最终收益 {:.2%}".format(total_balance/init_balance-Decimal(1)))
