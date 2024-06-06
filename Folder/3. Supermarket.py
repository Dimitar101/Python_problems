from collections import deque


def solve_supermarket():
    names = deque()
    while True:
        command = input()
        if command == "End":
            print(f"{len(names)} people remaining.")
            break
        if command == "Paid":
            for i in range(len(names)):
                print(names.popleft())
        else:
            name = command
            names.append(name)


solve_supermarket()
