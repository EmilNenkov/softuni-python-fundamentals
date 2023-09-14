while True:
    command = input()
    if command == 'End!':
        break
    elif command != "SoftUni":
        res = ""
        for i in command:
            res += i * 2
        print(res)
