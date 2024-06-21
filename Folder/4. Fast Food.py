quantity = int(input())
orders = list(map(lambda x: int(x), input().split()))
print(max(orders))

for i in range(len(orders)):
    if quantity >= orders[i]:
        if i + 1 == len(orders):
            print("Orders complete")
            break
        quantity -= orders[i]
    else:
        print(f"Orders left: ", end='')
        for j in range(i, len(orders)):
            print(f"{orders[j]} ", end='')
        break
