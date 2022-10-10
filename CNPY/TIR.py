def fluxodecaixa():
    n = int(input("número de períodos: "))
    i = 0
    somar = 0 
    somad = 0

    tma = float(input("Digite a Taxa Mínima de Atratividade (TMA) em %: "))

    while i < n:
        r = float(input("Digite a receita do mês: "))
        vpl = somar+r-(r*tma/100)
        somar = somar + r
        i = i + 1
    print("O receita total foi: ", somar)
    print("O VPL total foi: ", vpl)
    

    print("Calcular despesas: ")
    i = 0
    somard = 0 

    while i < n:
        d = float(input("Digite a despesa do mês: "))
        somad = somad + d
        i = i + 1
    montante = somar - somad


    print("A despesa total foi: ", somad)
    print("O montante é: ", montante)


    
    
fluxodecaixa()
