# Finds the biggest int you can form out of the digits of the input int.
num_str = input()
list_1 = []
result_str = ""

for i in range(len(num_str)):
    list_1.append(num_str[i])

list_1.sort(reverse = True)

for i in range(len(list_1)):
    result_str += list_1[i]

print(result_str)

