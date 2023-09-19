coffee = 0

while True:
    command = input()
    if command == 'END':
        break
    elif command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        coffee += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        coffee += 2

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")
