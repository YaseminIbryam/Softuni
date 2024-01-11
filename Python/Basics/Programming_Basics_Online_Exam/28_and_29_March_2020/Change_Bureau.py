bitcoins = int(input())
CNYs = float(input())
commission = float(input())
dollar = CNYs * 0.15
leva = bitcoins * 1168 + dollar * 1.76
euro = leva / 1.95
total = euro * (1-commission/100)
print(f"{total:.2f}")
