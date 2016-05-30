
#L = input("")
L = "1 8 9 2 0 4 5 12 5 3 2 1"
L = [int(x) for x in L.split()]
maxint = 2149000000
def selection(L, a, maxint):
    global SL
    if len(L) == a+1:
        return (L)
    else:
        mval = maxint
        a = a
        s = 0
        for i in range(a,len(L)):
            if L[i] < mval:
                mval = L[i]
                s = i
        aux  = L[a]
        L[a] = mval
        L[s] = aux
        print ("Menor elemento neste passo:", L[a])
        #print (L)
        SL = str(L[0])
        for e in range(1,len(L)):
            SL = SL+" | "+str(L[e].strip())
        print ("Estado Atual:", SL,"'","\n")
        selection(L, a+1, maxint)
        return(SL)
x=selection(L, 0, maxint)
x
print("Resultado Final:", SL)
