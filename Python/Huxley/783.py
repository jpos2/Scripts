entrada = "11 2 13 4 15"
entrada = entrada.split()

entrada = [ int(x) for x in entrada ]  

class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


root = BSTNode(entrada[0])
x = root
for i in (1, len(entrada)-1):
    if entrada[i] < x.key:
        x.left = BSTNode(entrada[i])
        x = x.left
    elif entrada[i] >= x.key:
        x.right = BSTNode(entrada[i])
        x = x.right

print (root.left.left.key)


