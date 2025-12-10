fuel_type = input()
fuel_quantity = float(input())
discount_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_price = 0

if fuel_type == "Gasoline":
    if discount_card == "Yes":
        new_gasoline_price = gasoline_price - 0.18
        total_price = fuel_quantity * new_gasoline_price
    else:
        total_price = fuel_quantity * gasoline_price
elif fuel_type == "Diesel":
    if discount_card == "Yes":
        new_diesel_price = diesel_price - 0.12
        total_price = fuel_quantity * new_diesel_price
    else:
        total_price = fuel_quantity * diesel_price
elif fuel_type == "Gas":
    if discount_card == "Yes":
        new_gas_price = gas_price - 0.08
        total_price = fuel_quantity * new_gas_price
    else:
        total_price = fuel_quantity * gas_price

if 20 <= fuel_quantity <= 25:
    total_price *= 0.92
elif fuel_quantity > 26:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")