import turtle

bob = turtle.Turtle()

linha = 200
angulo = 202

while linha <=10000:
    bob.fd(linha)
    bob.lt(angulo)
    bob.fd(linha)
    bob.lt(angulo)

    bob.fd(linha)
    bob.lt(angulo)
    bob.fd(linha)
linha = linha+100

turtle.mainloop()
