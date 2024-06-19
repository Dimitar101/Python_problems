# Solution assumes input is always valid.
first = input().split()
N, S, X = int(first[0]), int(first[1]), int(first[2])
second = list(map(lambda x: int(x), input().split()))[S:]

if second:
    if X in second:
        print(True)
    else:
        print(min(second))
else:
    print(0)
