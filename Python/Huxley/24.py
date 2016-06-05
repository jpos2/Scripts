n = int(input())
while not n < 0:
	fat = 1
	for i in range(1,n+1):
		fat = fat*i
	print(fat)
	n = int(input())