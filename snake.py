n = 15
res = [[0 for i in range(n)] for j in range(n)]
current = 1
dir = 1
x = 0
y = -1
while current <= n*n:
	if dir == 1 and y + 1 < n and res[x][y + 1] == 0:
		y += 1
	elif dir == 2 and x + 1 < n and res[x + 1][y] == 0:
		x += 1
	elif dir == 3 and y - 1 >= 0 and res[x][y - 1] == 0:
		y -= 1
	elif dir == 0 and x - 1 >= 0 and res[x - 1][y] == 0:
		x -= 1
	else:
		dir = (dir + 1) % 4
		continue
	res[x][y] = current
	current += 1

for line in res:
	for element in line:
		print("%3i " % element,' ', end='')
	print()