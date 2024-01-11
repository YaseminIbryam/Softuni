name = input()
adult_tickets = int(input())
child_tickets = int(input())
price_adult_ticket = float(input())
price_service = float(input())
price_child_ticket = price_adult_ticket - 70/100 * price_adult_ticket + price_service
price_adult_ticket = price_adult_ticket + price_service
price = adult_tickets * price_adult_ticket + child_tickets * price_child_ticket
profit = price * 20/100
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")
