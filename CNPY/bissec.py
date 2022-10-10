a = float(input('Digite o valor de A:'))
b = float(input("Digite o valor de B:"))
p = int(input("Digite o valor da Precisão:"))
nmax = int(input("Digite o número máximo de iterações:"))

cont = 0
x = a
er = 1

while ((er > p) and (cont <= nmax)):
    a = x 
    x = (a+b)/2
    if f(x) * f(a) <= 0:
        b = x
    else:
        a = x 
    er = (abs(x - a))/abs(x)
    cont = cont + 1
print (x, cont)