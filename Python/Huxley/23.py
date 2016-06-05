entrada = input()
entrada = entrada.split()
n = int(entrada[0])
m = int(entrada[1])
A = ""
for i in range(n,m+1):
	if i % 5 == 0:
		A = A+str(i)+"|"
A = A.strip("|")
print(A)
		