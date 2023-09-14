n = int(input())

for _ in range(n):
    line = input()
    if ',' in line or '.' in line or '_' in line:
        print(f'{line} is not pure!')
    else:
        print(f'{line} is pure.')
