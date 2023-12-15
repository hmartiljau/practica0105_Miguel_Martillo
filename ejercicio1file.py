num=int(input('introduce un numero entre 1 y 10'))
def tabla (num):
    file = open('tabla-'+ str(num) + '.txt', 'w')
    for i in range(0,11):
        mult=i*num
        file.write(str(i) + "*" + str(num) + "="+ str(mult) + "\n")   
tabla(num)    
