age = int(input())
drink_name = 'toddy'

if 14 < age <= 18:
    drink_name = 'coke'
elif 18 < age <= 21:
    drink_name = 'beer'
elif 21 < age:
    drink_name = 'whisky'

print(f'drink {drink_name}')
