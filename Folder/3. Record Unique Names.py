n = int(input())
unique = {input() for _ in range(n)}
for name in unique:
    print(name)


# def unique(a, seq):
#     for name in seq:
#         print(name)
#
# n = int(input())
# unique(n, {input() for _ in range(n)})



# n = int(input())
# result = []
# for _ in range(n):
#     name = input()
#     if name not in result:
#         result.append(name)
# for element in result:
#     print(element)
