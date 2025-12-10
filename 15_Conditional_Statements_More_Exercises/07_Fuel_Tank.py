type_fuel = input()
fuel_in = float(input()) # литри гориво, които има в резервоара

if type_fuel == "Diesel":
    type_fuel = "diesel"
    if fuel_in >= 25:
        print(f"You have enough {type_fuel}.")
    elif fuel_in < 25:
        print(f"Fill your tank with {type_fuel}!")

elif type_fuel == "Gasoline":
    type_fuel = "gasoline"
    if fuel_in >= 25:
        print(f"You have enough {type_fuel}.")
    elif fuel_in < 25:
        print(f"Fill your tank with {type_fuel}!")

elif type_fuel == "Gas":
    type_fuel = "gas"
    if fuel_in >= 25:
        print(f"You have enough {type_fuel}.")
    elif fuel_in < 25:
        print(f"Fill your tank with {type_fuel}!")

else:
    print("Invalid fuel!")