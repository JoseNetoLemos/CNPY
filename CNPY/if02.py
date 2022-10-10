import math 

def soma(n1, n2):
    soma=n1+n2
    print("A soma dos valores é:",soma)

def subtacao(n1,n2):
    subtacao=n1-n2
    print("A subtacao dos valores é:",subtacao)

def multiplica(n1,n2):
    multiplica=n1*n2
    print("A multiplicação dos valores é:",multiplica)

def divisao(n1,n2):
    divisao=n1/n2
    print("A divisao dos valores é:",divisao)

def operacoes (n1,n2):
    soma(n1,n2)

    subtacao(n1,n2)

    multiplica(n1,n2)

    divisao(n1,n2)

       
n1 = int(input("Digite n1:"))
n2 = int(input("Digite n2:"))

operacoes(n1,n2)
