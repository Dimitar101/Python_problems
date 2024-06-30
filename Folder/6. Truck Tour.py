N = int(input())
path = []

for i in range(N):
    info = input().split()
    petrol_x, distance_x = int(info[0]), int(info[1])
    path.append([petrol_x, distance_x])

original_path = []
[original_path.append(petrol_distance_pair) for petrol_distance_pair in path]

for q in range(len(path)):
    total_petrol = 0
    for j in range(len(path)):
        petrol = path[j][0]
        distance = path[j][1]
        #---------------------
        total_petrol += petrol
        if total_petrol < distance:
            path.append(path.pop(0))
            break
        total_petrol -= distance

print(original_path.index(path[0]))
