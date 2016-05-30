
def mh(l,x,tam):
    
    left = 2*x+1
    right = 2*x+2
    if (left <= tam and l[x] < l[left]):
        larg = left
    else:
        larg = x
    if (right <= tam and l[larg] < l[right]):
        larg = right
    if (larg != x):
        l[x],l[larg] = l[larg],l[x]
        mh(l,larg,tam)

l = [5,9,4,6,3,7,2,8,1]

print(l)        
mh(l,0,len(l)-1)
print (l)
