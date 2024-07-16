n = int(input())
record = dict()

for i in range(n):
    info = input().split()
    student = info[0]
    grade = info[1]

    if student not in record:
        record[student] = []
    record[student].append(grade)

from statistics import mean
for key, value in record.items():
    print(f"{key} -> {' '.join(map(str, value))} (avg: {mean(float(x) for x in value):.2f})")
