n=int(input('Escribe el primer numero'))
m=int(input('Escribe el segundo numero'))
def tablamultiplicar(n,m):
    file = open('tabla-'+ str(n) + '.txt', 'w')
    for i in range(0,11):
        mult=i*n
        file.write(str(i) + "*" + str(n) + "="+ str(mult) + "\n")   

    import os
    file= 'tabla-'+ str(n) + '.txt'
    if os.path.isfile(file) :
        file = open('tabla-'+ str(n) + '.txt', 'r')
        lineas= file.read()
        separador=lineas.split()
        lista=list(separador)
        print(lista[m])
tablamultiplicar(n,m)
