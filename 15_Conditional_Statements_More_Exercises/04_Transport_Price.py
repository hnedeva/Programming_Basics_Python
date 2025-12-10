n = int(input())
time_of_day = input()

# Taxi price (always available)
if time_of_day == "day":
    taxi = 0.70 + 0.79 * n
else:
    taxi = 0.70 + 0.90 * n

# Define bus and train only when allowed
if n >= 20:
    bus = 0.09 * n
else:
    bus = 999999999  # very large number so it never becomes the cheapest

if n >= 100:
    train = 0.06 * n
else:
    train = 999999999  # same trick

# Find the cheapest of the three
cheapest = taxi

if bus < cheapest:
    cheapest = bus

if train < cheapest:
    cheapest = train

print(f"{cheapest:.2f}")
