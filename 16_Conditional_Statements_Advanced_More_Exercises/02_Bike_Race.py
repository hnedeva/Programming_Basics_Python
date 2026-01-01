junior_bikers = int(input())
senior_bikers = int(input())
trace_type = input()

price = 0
junior_price = 0
senior_price = 0

if trace_type == "trail":
    junior_price = 5.50
    senior_price = 7
elif trace_type == "cross-country":
    junior_price = 8
    senior_price = 9.50
    total_count = junior_bikers + senior_bikers
    if total_count >= 50:
        junior_price = 8 * 0.75
        senior_price = 9.50 * 0.75
elif trace_type == "downhill":
    junior_price = 12.25
    senior_price = 13.75
elif trace_type == "road":
    junior_price = 20
    senior_price = 21.50

money_donated = (junior_bikers * junior_price + senior_bikers * senior_price) * 0.95

print(f"{money_donated:.2f}")