annual_fee = int(input())

sneakers = annual_fee * (1 - 0.40)
clothes = sneakers * (1 - 0.20)
ball = clothes / 4
accessories = ball / 5

total = sneakers + clothes + ball + accessories + annual_fee

print(total)