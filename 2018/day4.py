file = open('day3.txt', 'r')

fabricMatrix = [[0 for x in range(1000)] for y in range(1000)]

counter = 0

for line in file:
    lineArray = line.split(' ')
    coordinates = lineArray[2][:-1].split(',')
    area = lineArray[3].split('x')

    for x in range(int(area[0])):
        for y in range(int(area[1])):
            if fabricMatrix[int(coordinates[0]) + x][int(coordinates[1]) + y] != 0:
                if fabricMatrix[int(coordinates[0]) + x][int(coordinates[1]) + y] != 'X':
                    fabricMatrix[int(coordinates[0]) + x][int(coordinates[1]) + y] = 'X'
                    counter += 1
            else:
                fabricMatrix[int(coordinates[0]) + x][int(coordinates[1]) + y] = lineArray[0][1:]

print(counter)
