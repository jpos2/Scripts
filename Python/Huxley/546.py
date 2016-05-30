A = "12 4 19 5 13 6 9 77"
A = [int(x) for x in A.split()]
print (A)

class Tree:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        
T = Tree(A[0])

def ins(T, x):
    if T.key == None:
        T = Tree(x)
        
    elif x > T.key:
        ins(T.right, x)
    else:
        ins(T.left, x)
        
print (type(T.right))

for i in range(len(A)):
    ins(T, A[i])
    #print(A[i])
