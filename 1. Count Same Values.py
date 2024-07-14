# seq = input().split()
# unique = []
#
# for i in range(len(seq)):
#     if seq[i] not in unique:
#         unique.append(seq[i])
#
# for j in range(len(unique)):
#     if "." in unique[j]:
#         print(f"{unique[j]} - {seq.count(unique[j])} times")
#     else:
#         print(f"{unique[j]}.0 - {seq.count(unique[j])} times")


# seq = [float(x) for x in input().split()]
# unique = []
#
# for i in range(len(seq)):
#     if seq[i] not in unique:
#         unique.append(seq[i])
#
# for j in range(len(unique)):
#     print(f"{unique[j]} - {seq.count(unique[j])} times")


# seq = [float(x) for x in input().split()]
# occurrences = dict()
# for el in seq:
#     if el not in occurrences:
#         occurrences[el] = 0
#     occurrences[el] += 1
#
# for key, value in occurrences.items():
#     print(f"{key} - {value} times")


def solve(seq):
    occurrences = dict()
    for el in seq:
        if el not in occurrences:
            occurrences[el] = 0
        occurrences[el] += 1

    for key, value in occurrences.items():
        print(f"{key} - {value} times")

a = [float(x) for x in input().split()]
solve(a)
