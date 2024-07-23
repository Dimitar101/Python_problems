register = []
while True:
    info = input()
    if info == "END":
        break
    info = info.split(", ")
    command = info[0]
    car_plate = info[1]

    if command == "IN":
        register.append(car_plate)
    elif command == "OUT":
        register.remove(car_plate)

register = set(register)

if register:
    for element in register:
        print(element)
else:
    print("Parking Lot is Empty")
