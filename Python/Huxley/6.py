from math import sqrt
a = float(input())
b = float(input())
c = float(input())

if a == 0:
	print("NEESG")
else:
	delta = ((b**2) - (4*a*c))
	if delta < 0:
		print("NRR")
	else:
		#print("Delta: %f" %delta)
		x1 = ((b*-1) + sqrt(delta))/(2.0*a)
		x2 = ((b*-1) - sqrt(delta))/(2.0*a)
		print("%.2f\n%.2f" %(x1, x2))