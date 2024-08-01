# e = input().split()
# n = int(e[0]); m = int(e[1])
# container = []
#
# for _ in range(n + m):
#     container.append(int(input()))
#
# set_1 = set(container[:n])
# set_2 = set(container[n:])
#
# for element in (set_1 & set_2):
#     print(element)




e = input().split()
n = int(e[0]); m = int(e[1])
set_1 = set(); set_2 = set()

[set_1.add(int(input())) for _ in range(n)]
[set_2.add(int(input())) for _ in range(m)]
[print(element) for element in (set_1 & set_2)]
