initial_budget = float(input())
category = input()
people = int(input())

vip_price = 499.99
normal_price = 249.99

# Calculate transport cost
if people <= 4:
    transport_cost = initial_budget * 0.75
elif 5 <= people <= 9:
    transport_cost = initial_budget * 0.60
elif 10 <= people <= 24:
    transport_cost = initial_budget * 0.50
elif 25 <= people <= 49:
    transport_cost = initial_budget * 0.40
else:  # people >= 50
    transport_cost = initial_budget * 0.25

money_left_for_tickets = initial_budget - transport_cost

# Calculate ticket total
if category == "VIP":
    ticket_cost = people * vip_price
else:  # Normal
    ticket_cost = people * normal_price

# Compare
if ticket_cost <= money_left_for_tickets:
    money_left = money_left_for_tickets - ticket_cost
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = ticket_cost - money_left_for_tickets
    print(f"Not enough money! You need {money_needed:.2f} leva.")
