###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF968 -- Programacao 1
#
# Autor:    Bianca Moura
#           Jean Pierre
#
# Email:   bfmm@cin.ufpe.br
#          jpos2@cin.ufpe.br
#
# Data:        2015-12-13
#
# Descricao:  Este e' um modelo de arquivo para ser utilizado para a implementacao
#             do projeto pratico da disciplina de Programacao 1. 
#             A descricao do projeto encontra-se no site da disciplina e trata-se
#             de uma adaptacao do projeto disponivel em 
#             http://nifty.stanford.edu/2013/craig-authorship-detection/handout/index.shtml
#             O objetivo deste projeto e' implementar um sistema de atribuicao
#             automatica da autoria de textos.
#             Este arquivo e a modificacao do projeto foram permitidas
#             pela autora do projeto original, Dr. Michelle Craig (Uni of Toronto).
#             As docstrings foram traduzidas para o portugues, enquanto a maior
#             parte do codigo foi preservada em ingles. O arquivo tambem foi alterado
#             para acomodar as mudancas no enunciado do problema feitas pelo professor
#             da disciplina, Dr. Renato Vimieiro (CIn - UFPE).
#
# Licenca: The MIT License (MIT)
#            Copyright(c) 2015 Bianca Moura, Jean Pierre
#
###############################################################################

import numpy as np
import sys
import re

################################################
############## FUNCOES AUXILIARES ##############
################################################

def clean_up(s):                  #1
    ''' Retorna uma versao da string 's' na qual todas as letras sao
        convertidas para minusculas e caracteres de pontuacao sao removidos
        de ambos os extremos. A pontuacao presente no interior da string
        e' mantida intacta.
    '''    
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result



def append_on_list(s):             #2

    '''Retorna um vetor de strings onde cada palavra estara' em uma posicao numa lista
        sem caracteres justapostos (caso haja)
        '''

    lista = []
    lista = s.split()

    for i in range(len(lista)):
        lista [i] = clean_up(lista[i])

    return lista
    
def quantity_words(text):                  #3
    '''Retorna a quantidade de palavras presentes no texto; o calculo e'
    feito com base no tamanho da lista em que as palavras foram inseridas
    '''
    text = append_on_list(text)
    return len(text)    


def quantity_single_words(text):       #4

    '''Retorna a quantidade de palavras unicas presentes no texto.
    O calculo e' feito com a funcao count, que retorna quantas vezes
    determinado elemento aparece no texto. Caso seja 1, acrescenta no somatorio
        '''

    main_list = []    #criacao de lista
    main_list = append_on_list(text) #split na lista (transforma o txt em lista)
    clone_list = main_list[:]    #clone da lista
    without_duplicate = list(set(main_list))    #retorna a lista sem duplicadas
    for i in range(len(without_duplicate)):
        clone_list.remove(without_duplicate[i])    #remove a lista sem duplicadas da lista completa, ou seja, sobra so as repetidas
    
    return len(list(set(main_list) - set(clone_list)))  #set do texto principal (sem duplicados) menos set da lista de repetidas (sem duplicados)
    
def quantity_different_words(text):    #5

    '''Retorna a quantidade de palavras distintas presentes no texto.
    O calculo e' feito com a funcao set, que retorna uma lista sem elementos
    repetidos
        '''
    lista = set(append_on_list(text))
    return len(lista)


def quantity_sentence(text):               #6

    '''Retorna a quantidade de sentencas que aparecerem no texto
    usando a funcao split_on_separators
        '''

    text = split_on_separators(text, ".!?")
    return len(text)



def quantity_phrase(text):                #7
    '''Retorna a quantidade de frases que aparecerem no texto
    usando a funcao split_on_separators
    '''
    
    text = split_on_separators(text, ",:;.!?")
    return len(text)



def quantity_characters(s):        #8

    '''Retorna a quantidade de caracteres presentes no texto, sem
        os caracteres especiais. Para isso, foi criado um replace para
        substituir os caracteres especiais por vazio.
        '''

    lista = append_on_list(s)
    punctuation = '''!"',; :.?)([]<>*#\n\t\r'''
    for i in punctuation:
        s = s.replace(i, "")
    return len(s) 



################################################
############## FUNCOES PRINCIPAIS ##############
################################################


def average_word_length(text):
    ''' Retorna o tamanho medio das palavras em 'text' 
        recebida como parametro. Caracteres de pontuacao justapostos `as palavras
        nao devem ser contados.
    '''
    
    return float(quantity_characters(text)) / quantity_words(text)
    
    


def type_token_ratio(text):
    ''' Retorna a razao vocabulo/ocorrencia para text.
        Esta razao e' o numero de palavras distintas sobre
        o total de palavras no texto.
    '''

    return float(quantity_different_words(text)) / quantity_words(text)
    
    
                
def hapax_legomana_ratio(text):
    '''    Retorna a razao Hapax Legomena para text.
        Esta razao e' o numero de palavras que ocorrem
        uma unica vez no texto sobre o total de palavras.
    '''

    return float(quantity_single_words(text)) / quantity_words(text)



def split_on_separators(original, separators):
    '''    Retorna um vetor de strings nao vazias obtido a partir da quebra
        da string original em qualquer dos caracteres contidos em 'separators'.
        'separtors' e' uma string formada com caracteres unicos a serem usados
        como separadores. Por exemplo, '^$' e' uma string valida, indicando que
        a string original sera quebrada em '^' e '$'.
    '''            
    return np.array(filter(lambda x: x != '',re.split('[{0}]'.format(separators),original)),\
                    dtype="object")
  
    
    
def average_sentence_length(text):
    '''    Retorna o numero medio de palavras por sentenca.
        Uma sentenca e' uma sequencia nao vazia de caracteres
        terminada por '.', '!', '?' ou fim de arquivo.
    '''
    
    return float(quantity_words(text)) / quantity_sentence(text)
    

def avg_sentence_complexity(text):
    '''    Retorna o numero medio de frases por sentenca.
        Uma sentenca e' uma sequencia nao vazia de caracteres
        terminada por '.', '!', '?' ou fim de arquivo.
        Frases sao subsequencias de caracteres de uma sentenca
        separadas pelos seguintes delimitadores ,;:        
    '''
    
    return float(quantity_phrase(text)) / quantity_sentence(text)
        
    
def compare_signatures(sig1, sig2, weight):
    '''    Retona um vetor numpy de floats com o resultado da comparacao
        entre a assinatura no primeiro vetor e as assinaturas na matriz (segundo
        parametro). O terceiro parametro e' um vetor de pesos, determinando
        a significancia de cada caracteristica para a similaridade.
        O vetor sig1 e a matriz sig2 contem as seguintes colunas:
        0  : tamanho medio das palavras
        1  : razao vocabulo/ocorrencia
        2  : razao Hapax Legomena
        3  : tamanho medio de sentenca
        4  : complexidade media de sentenca
    '''
    result = np.zeros(len(sig2),dtype="float128")
    
    for line in xrange(len(sig2)):
        for col in xrange(len(sig1)):
            result[line] = result[line] + (abs((sig1[col]) - (sig2[line,col])) * weight[col])
    
    return result
    
# Lendo nomes e assinaturas
   # authors, features = read_signatures(sys.argv[1])
def read_signatures(filename):
    ''' Le um conjunto de assinaturas linguisticas de um arquivo CSV cujo
        caminho e' contido no parametro 'filename'. Retorna uma tupla contendo
        um vetor numpy com os nomes dos autores e uma matriz com as assinaturas
        linguisticas de cada autor (autores em linhas). 
    '''
    
    # TODO: Essa funcao deve ser implementada para ler as assinaturas linguisticas
    #        do arquivo CSV (formatado conforme especificacao) e retornar uma tupla
    #        contendo dois itens: o primeiro e' o vetor de nomes dos autores; e o
    #        segundo a matriz de dados com os valores das 5 caracteristicas para
    #        cada assinatura/autor.
    #        Nao e' permitido usar a funcao de leitura de arquivos CSV de numpy.
    #        O numero de colunas da matriz ja e' conhecido. Conte o numero de
    #        linhas usando readlines e, em seguida, reposicione o arquivo no
    #        comeco usando seek(0).
    
    arq = open(filename,'r')
    text = arq.readlines()
    
    
    qt_lines = 0
    
    for line in text:
        qt_lines = qt_lines + 1

    author = np.empty(len(text),dtype="object")
    feature = np.empty((qt_lines,5), dtype="float128")
                       
    count = 0
    for i in text:
        author[count] = i[:(i.find(','))]
        count = count + 1
    
    start = i.find(",")
    end = 0
    count2 = 0
    count3 = 0

    for i in text:
        start = i.find(",")+1
        for j in xrange(5):
            end = i.find(",",start)
            feature[count3,j] = i[start:end]
            start = end + 1
            count2 = count2 + 1    
        count3 = count3 + 1
        
    return (author,feature)
    
def compute_signature(filename):
    ''' Computa a assinatura linguistica do arquivo misterioso 'filename'.
        Retorna um vetor numpy de float com o valor das 5 caracteristicas
        conforme ordem descrita em compare_signatures.
    '''
    signature = np.empty(5,dtype="float128")
    
    mistery_file = open(filename)
    text = mistery_file.read()
    mistery_file.close()
    
    signature[0] = average_word_length(text)
    signature[1] = type_token_ratio(text)
    signature[2] = hapax_legomana_ratio(text)
    signature[3] = average_sentence_length(text)
    signature[4] = avg_sentence_complexity(text)
    
    return signature


def main():
    
    
    # Os arquivos sao passados como argumentos da linha de comando para o programa
    # Voce deve buscar mais informacoes sobre o funcionamento disso (e' parte do
    # projeto).
    
    # A ordem dos parametros e' a seguinte: o primeiro e' o nome do arquivo
    # com assinaturas linguisticas, em seguida os arquivos misteriosos.
    # Devem ser informados, no minimo, dois arquivos na entrada.
    
    if len(sys.argv) < 3:
        print 'Numero invalido de argumentos'
        print 'O programa deve ser executado como python find_author.py <arq-ass> <arqs-misteriosos>'
        sys.exit(0)

    # Lendo nomes e assinaturas
    authors, features = read_signatures(sys.argv[1])

    # Para cada arquivo misterioso
    for filename in sys.argv[2:]:
        global filename
        signature = compute_signature(filename)

        
        # computar similaridade com outras assinaturas e determinar autoria
            
        weights = np.array([11, 33, 50, 0.4, 4],dtype="float128")
        scores = compare_signatures(signature, features, weights)
        
        
        
        # TODO: scores contem o valor de todas as comparacoes entre as assinaturas conhecidas
        #        e a do arquivo misteriosos. Voce deve descobrir qual e' a mais proxima
        #        e mostrar exibir o autor dessa assinatura como o provavel autor do arquivo
        #        misterioso.
    
        minScore = min(scores)
    
        for i in xrange(len(scores)):
            if scores[i] == minScore:
                print "O livro foi escrito por:", authors[i]

        

if __name__ == '__main__':
    main()
    
    