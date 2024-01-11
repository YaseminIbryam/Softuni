budget = float(input())
video_cards = int(input())
processors = float(input())
rams = float(input())
price_video_card = 250
price_video_cards = price_video_card * video_cards
price_processor = 35/100 * price_video_cards
price_processors = price_processor * processors
price_ram = 10/100 * price_video_cards
price_rams = price_ram * rams
total = price_rams + price_processors + price_video_cards
if video_cards > processors:
    total *= (1-15/100)
if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
