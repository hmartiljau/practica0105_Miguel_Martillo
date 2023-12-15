num=int(input('introduce un numero entre 1 y 10'))
def tabla(num):
    import os
    file= 'tabla-'+ str(num) + '.txt'
    if os.path.isfile(file) :
        file = open('tabla-'+ str(num) + '.txt', 'r')
        lineas= file.read()
        print(lineas)
    else :
        print('el fichero no existe')
tabla(num)





