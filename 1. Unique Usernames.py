# n = int(input())
# result = []                     # Make result a set  result = set()
# for _ in range(n):
#     username = input()
#     if username not in result:  # use  result.add(username)  to add to the set
#         result.append(username)
# for element in result:
#     print(element)




result = set()
for _ in range(int(input())):
    username = input()
    result.add(username)
[print(element) for element in result]
