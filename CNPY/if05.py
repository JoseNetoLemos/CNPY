from datetime import date #IMPORTANDO A DATA DA HOJE 
from datetime import datetime
import math #IMPORTANDO UMA BIBLIOTECA MATEMÁTICA


def somarpontos():
    
    nome = str(input("Digite o seu nome: "))
    idade = str(input("Digite a sua idade: "))
    data = datetime.now()

    print("Atendimento realizado no dia", data,"para o cliente",nome,"cuja a idade é",idade,"anos.")

somarpontos()