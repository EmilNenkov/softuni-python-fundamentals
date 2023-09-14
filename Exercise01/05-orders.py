n = int(input())
total = 0

for _ in range(n):
    price_sum = 0
    
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (price_per_capsule < 0.01 or price_per_capsule > 100.00) or (days < 1 or days > 31) or (capsules_per_day < 1 or capsules_per_day > 2_000):
        continue
    
    price_sum += price_per_capsule * capsules_per_day * days
    total += price_sum
    
    print(f"The price for the coffee is: ${price_sum:.2f}")
print(f"Total: ${total:.2f}")
