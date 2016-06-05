n = int(input())
words = ""
aux = ""
while n != 0:
	aux = input()
	words = words+aux[::-1]
	n = int(input())
	if n != 0:
		words = words+"\n"

print (words)
