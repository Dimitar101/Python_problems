# def get_matching(a_expression):
#     brackets = []
#     a_sub_expressions = []
#     for i in range(len(a_expression)):
#         ch = a_expression[i]
#         if ch == "(":
#             brackets.append(i)
#         elif ch == ")":
#             start_index = brackets.pop()
#             end_index = i
#             a_sub_expressions.append(a_expression[start_index:end_index + 1])
#     return a_sub_expressions
#
# expression = input()
# sub_expressions = get_matching(expression)
# [print(exp) for exp in sub_expressions]


seq = input()
indexes = []
subs = []

for i in range(len(seq)):
    char = seq[i]

    if char == "(":
        indexes.append(i)
    elif char == ")":
        start_idx = indexes.pop()
        end_idx = i + 1
        subs.append(seq[start_idx:end_idx])

[print(sub) for sub in subs]
