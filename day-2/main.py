inputFile = open('input.txt', 'r')
x = 0
y = 0
for line in inputFile.read().splitlines():
	a, b = line.split()
	if a == 'forward':
		x += int(b)
	elif a == 'up':
		y -= int(b)
	elif a == 'down':
		y += int(b)
print(x * y)
inputFile.close()