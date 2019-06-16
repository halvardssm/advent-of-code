file = open('day2.txt', 'r')

counterTwo = 0
counterThree = 0

for line in file:
    hasTwo = False
    hasThree = False

    for letter in line:
        counter = line.count(letter)

        if counter == 3:
            hasThree = True
        elif counter == 2:
            hasTwo = True

    if hasThree:
        counterThree += 1
    if hasTwo:
        counterTwo += 1

checkSum = counterTwo * counterThree

print(checkSum)
