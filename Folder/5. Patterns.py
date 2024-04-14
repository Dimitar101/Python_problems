n = int(input())

for i in range(1, n + 1):
    for j in range(0, i):
        print('*', end='')      #We use end='' to stay on the same line.
    print()

for i in range(n - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()

