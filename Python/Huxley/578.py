#entrada = input()

class Heap:
  def __init__(self, tamanho):
    self.elementos = [None] * tamanho
    self.tamanho = tamanho
  
  def __getitem__(self,indice):
    if indice> 0 and indice <= self.tamanho:
      return self.elementos[indice-1]
    raise IndexError("Tentando acessar elemento fora do intervalo")
  
  def __setitem__(self,indice,valor):
    if indice > 0 and indice <= self.tamanho:
      self.elementos[indice-1] = valor
      return 
    raise IndexError("Tentando setar elemento fora do intervalo")

  def __eq__(self,outro):
    if (type(outro) != type(self)):
      return False
    for i in range(tamanho):
      if self.elementos[i] != outro.elementos[i]:
        return False
    return True

  def __len__(self):
    return self.tamanho

  def __iter__(self):
    for i in range(len(self.elementos)):
      yield self.elementos[i]
  
  def __contains__(self,elemento):
    for i in range(len(self.elementos)):
      if self.elementos[i] == elemento:
        return True
    return False

  def __str__(self):
    return str(self.elementos)

  def troca(self,i,j):
    tmp = self.__getitem__(i)
    self.__setitem__(i, self.__getitem__(j))
    self.__setitem__(j, tmp)

  def buildMaxHeap(self):
    for i in range(self.tamanho//2,0,-1):
        self.maxHeapify(i)
        
  def left(self,i):
    return i*2
  def right(self,i):
    return (i*2)+1        
  def parent(self,i):
    return i//2
  
  
  def maxHeapify(self,i):
       l = self.left(i)
       r = self.right(i)
       if (l<=self.heapsize and self.elemento.__getitem__(l)):
        largest = l
       else:
        largest = i

       if (r<=self.heapsize and self.elemento.__getitem__(largest)):
        largest = r
       else:
        largest = i
        
       if largest != i:
        self.troca(i,largest)
        self.maxHeapify(largest)
        
       
entrada = "10 20 7 12 18 6 8 401 42"
entrada = [x for x in entrada.split()]
print (entrada.join(" | "))
