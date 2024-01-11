city = input()
sales_volume = float(input())
commission = 0
if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commission = 5
    elif 500 < sales_volume <= 1000:
        commission = 7
    elif 1000 < sales_volume <= 10000:
        commission = 8
    elif sales_volume > 10000:
        commission = 12
elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commission = 4.5
    elif 500 < sales_volume <= 1000:
        commission = 7.5
    elif 1000 < sales_volume <= 10000:
        commission = 10
    elif sales_volume > 10000:
        commission = 13
elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission = 5.5
    elif 500 < sales_volume <= 1000:
        commission = 8
    elif 1000 < sales_volume <= 10000:
        commission = 12
    elif sales_volume > 10000:
        commission = 14.5
if commission == 0:
    print("error")
else:
    commission_of_sales = sales_volume * commission/100
    print(f"{commission_of_sales:.2f}")


