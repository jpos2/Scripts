#Exemplos de objeto em python

class aluno:
    def __init__(self, nome):
        self.nome = nome
        self.idade = None
        self.cpf = None
        self.rg = None
        self.endereco = None
    def exibir(self, obj):
        print (self.nome)
        print (self.idade)
        print (self.cpf)
        
def main():
    entradas()
    
def entradas():
    nome = input("Informe o nome do aluno: ")
    Aluno = aluno(nome)
    idade = int(input("Informe a idade do aluno: "))
    Aluno.idade = idade
    cpf = int(input("Informe o CPF do aluno: "))
    Aluno.cpf = cpf
    Aluno.exibir(Aluno)
    
    
main()
