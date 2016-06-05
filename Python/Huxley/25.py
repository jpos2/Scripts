ent = input()
ent = ent.split()
n = int(ent[0])
m = int(ent[1])
A = []
A = [int(x) for x in range(n,m+1) if (x % 10 != 0 and (x % int((str(x)[:1])) == 0))
for i in A:
	print (i)