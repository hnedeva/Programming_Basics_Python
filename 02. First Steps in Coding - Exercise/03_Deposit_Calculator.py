deposit_amount = float(input())
deposit_months = int(input())
annual_interest_rate = float(input())
annual_interest_rate_percentage = annual_interest_rate / 100
result = deposit_amount + deposit_months * ((deposit_amount * annual_interest_rate_percentage) / 12)
print(result)