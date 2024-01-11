import math

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.5
cacti_price = 8
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
price_gift = float(input())
total = (magnolias * magnolias_price + hyacinths * hyacinths_price + roses * roses_price + cacti * cacti_price)
income = total - 5/100 * total
if price_gift <= income:
    left_money = income - price_gift
    print(f"She is left with {math.floor(left_money)} leva.")
else:
    borrowed_money = price_gift - income
    print(f"She will have to borrow {math.ceil(borrowed_money)} leva.")
