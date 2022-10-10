from curses import ACS_DARROW
import math 

#FUNCAO CONVERTER DE GRAUS PARA RADIANOS

def calcula_angulos_graus_radianos():
    graus = 1 
    while graus > 0: 
        graus = float(input("Digite o valor do angulo: "))
        rad = graus * (math.pi/180)
        print(rad)

calcula_angulos_graus_radianos()

# A FUNCAO NÃO PASSA NENHUM PARÂMETRO E EXCUTA UM LAÇO DE REPETIÇÃO INTERNMENTE PARA SOLICITAR A
# DIGITAÇÃO DOS VALORES EM GRAUS.
