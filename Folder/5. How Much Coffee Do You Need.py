coffee = counter = 0

while True:
    event = input()
    if event == "END":
        break
    counter += 1

    if event == "dog" or event == "cat" or event == "movie" or event == "coding":
        coffee += 1
    elif event == "DOG" or event == "CAT" or event == "MOVIE" or event == "CODING":
        coffee += 2

if counter < 5:
    print(coffee)
else:
    print("You need extra sleep")

