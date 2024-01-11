price_processor_dollar = float(input())
price_video_card_dollar = float(input())
price_RAM_memory_dollar = float(input())
number_RAM_memory_dollar = int(input())
discount_percent = float(input())
RAM_memory_cards_price = price_RAM_memory_dollar * number_RAM_memory_dollar
price_processor_discount = price_processor_dollar * (1-discount_percent)
price_video_card_discount = price_video_card_dollar * (1-discount_percent)
price_dollars = RAM_memory_cards_price + price_processor_discount + price_video_card_discount
price = price_dollars * 1.57
print(f"Money needed - {price:.2f} leva.")
