# Solution assumes input is always valid.
first = input().split()
N, S, X = int(first[0]), int(first[1]), int(first[2])
if S != 0:
    second = list(map(lambda x: int(x), input().split()))[S:]
else:
    second = list(map(lambda x: int(x), input().split()))
    #second = list(map(int, input().split()))

if second:
    if X in second:
        print(True)
    else:
        print(min(second))
else:
    print(0)


# # Some notes.
# numbers = [int(x) for x in input().split()]
#                # -> 1 2 66
# print(numbers) # -> [1, 2, 66]
# a, b, c = numbers
# print(a)       # -> 1
# print(b)       # -> 2
# print(c)       # -> 66
