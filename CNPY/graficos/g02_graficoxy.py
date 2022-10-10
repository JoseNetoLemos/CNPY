from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt

meses_x = ["JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"]
faturamento_y = [0.329,0.12,0.43,0.65,0.23,0.15,0.16,0.29,0.65,0.23,0.21,0.29]

titulo = "Gráfico mesesxfaturamento"
titulo_eixox = "meses"
titulo_eixoy = "faturamento"

plt.plot(meses_x,faturamento_y,linestyle="--", linewidth = 3, color = "blue", label = "faturamento_2022")

plt.scatter(meses_x,faturamento_y,marker="^",s=100,color="blue")