clothes =  list(map(lambda x: int(x), input().split()))
capacity = int(input())
rack = 0

temp = 0
for i in range(len(clothes)):
    temp += clothes[i]
    if temp > capacity:
        temp = clothes[i]
        rack += 1

print(rack + 1)
