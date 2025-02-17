chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

order_price = chicken_menu * 10.35 + fish_menu * 12.40 + veggie_menu * 8.15
dessert_price = order_price * 0.20
price = order_price + dessert_price + 2.50

print(price)
