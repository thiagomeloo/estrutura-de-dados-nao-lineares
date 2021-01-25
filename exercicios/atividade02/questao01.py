# Dado o seguinte código para os nós:

# -[ok] Crie uma função chamada valor_folhas(no)
# que me informe quais são os valores das folhas.

# -[ok] Crie uma função chamada altura(no)
# que me informe qual a altura da árvore.

# -[ok] Crie uma função chamada quantidade_nos(no)
# que me informe a quantidade de nós de uma árvore.

# - Crie uma função chamada buscar(no,x)
# que encontre qual é o nó que possui o valor X
# e retorne o Nó encontrado, deve retornar None se não encontrar.

class No:

    valor = None
    f_esq = None
    f_dir = None

    def __init__(self, valor, f_esq=None, f_dir=None):
        self.valor = valor
        self.f_esq = f_esq
        self.f_dir = f_dir

    def __str__(self):
        return str(self.valor)


class Arvore:
    raiz = None

    # construtor da arvore
    def __init__(self, no):
        self.raiz = no

    # percorre toda a arvore e imprime o valor
    def varredura(self, raiz):
        if not raiz:
            return
        self.varredura(raiz.f_esq)
        print(raiz.valor),
        self.varredura(raiz.f_dir)

    # funcao auxiliar para imprimir os elementos da raiz da arvore instanciada
    def printElements(self):
        self.varredura(self.raiz)

    # retorna o valor das folhas de um no
    def valor_folhas(self, no):
        if not no:
            return
        print(no.f_esq.valor)
        print(no.f_dir.valor)

    # retorna a quantidade de nos de uma arvore
    def quantidade_nos(self, no):
        if not no:
            return 0
        Esq = self.quantidade_nos(no.f_esq)
        Dir = self.quantidade_nos(no.f_dir)
        return Esq + Dir + 1

     # funcao auxiliar para imprimir a quantidade de nos da arvore instanciada
    def print_quantidade_nos(self):
        print(self.quantidade_nos(self.raiz))

    # funcao que retorna a altura da arvore
    def altura(self, no):
        if not no:
            return 0
        Esq = self.altura(no.f_esq)
        Dir = self.altura(no.f_dir)
        if (Esq > Dir):
            return Esq + 1
        else:
            return Dir + 1

    # funcao auxiliar para imprimir o valor da arvore
    def print_altura(self):
        print(self.altura(self.raiz))

    # funcao que retorna a busca de um elemento
    def busca(self, no, x):
        if not no:
             return

        self.busca(no.f_esq, x)
        self.busca(no.f_dir, x)

        if(no.valor == x):
            return print (x)
 


    # funcao auxiliar que imprime a busca de um elemento da arvore instanciada
    def print_busca(self, x):
        self.busca(self.raiz, x)




raiz = No(1)
raiz.f_esq = No(2)
raiz.f_dir = No(3)

raiz.f_esq.f_esq = No(4)
raiz.f_esq.f_dir = No(5)
raiz.f_esq.f_esq.f_esq = No(6)

arv = Arvore(raiz)
#arv.valor_folhas(raiz)
#arv.print_altura()
#arv.print_quantidade_nos()
#arv.print_busca(4)
