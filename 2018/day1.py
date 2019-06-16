file = open("day1.txt", "r")
frequency = 0
for line in file:
    frequency = frequency + int(line)

print(frequency)
