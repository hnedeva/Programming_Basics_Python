pens = int(input())
markers = int(input())
litres_cleaning_liquid = int(input())
discount = int(input())

total_price = pens * 5.80 + markers * 7.20 + litres_cleaning_liquid * 1.20
total_price_after_discount = (total_price * (1 - discount / 100))

print(total_price_after_discount)
