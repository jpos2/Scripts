
mval = 9999
n = 0
s = 0

def selection_sort(n, L, s, mval):
        
        for i in range(len(L)):
            if L[i] <= mval:
                    mval = L[i]
                    s = i
                    
        aux = L[n]
        L[n] = mval    
        L[s] = aux
        print(L)
        n = n + 1
        print(n)
        selection_sort(n+1,L[n:],s, L[n])

    
L = input("Insira uma lista: ")

L = [int(x) for x in L.split()]
#print (L)
print (type(L[n]))    
print(selection_sort(n, L, s, mval))
