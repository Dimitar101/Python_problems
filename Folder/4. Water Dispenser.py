from collections import deque


def water_dispenser():
    quantity = int(input())
    names = deque()
    while True:
        name = input()
        if name == "Start":
            while True:
                command = input()
                if command == "End":
                    break
                if command.isdigit():
                    water_current_wants = int(command)
                    if water_current_wants <= quantity:
                        print(f"{names.popleft()} got water")
                        quantity -= water_current_wants
                    else:
                        print(f"{names.popleft()} must wait")
                else:
                    command = command.split()
                    if command[0] == "refill":
                        quantity += int(command[1])
            break
        names.append(name)
    print(f"{quantity} liters left")


water_dispenser()
