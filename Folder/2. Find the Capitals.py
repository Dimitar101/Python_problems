input_str = input()
capital_letters_indices = []

for i in range(len(input_str)):
    if input_str[i].isupper():
        capital_letters_indices.append(i)

print(capital_letters_indices)
