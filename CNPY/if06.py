import math 
from datetime import datetime

#testes de if.

print("Esse programa foi criado em: ", datetime.now())

def sinal(): 

    cor = "st"
    while cor != "stop":
        cor = str(input("Digite uma cor:"))
        if cor == "vermelho":
            print("Parar")
        elif cor == "amarelo":
                print("atenção")
        elif cor == "verde":
                print("Avançar!")
        else:
            print("Opção inválida.")

sinal()