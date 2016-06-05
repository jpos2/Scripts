n = int(input())
h = n // (60**2)
m = (n % (60**2))//60
s = n % 60
print ("%d h %d m %d s" %(h, m, s))