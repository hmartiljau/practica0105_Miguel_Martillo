#Escribir un programa que pida al usuario dos números enteros 
#y muestre por pantalla la <n> entre <m> da un cociente <c> y 
#un resto <r> donde <n> y <m> son los números introducidos por 
#el usuario, y <c> y <r> son el cociente y el resto de la división 
#entera respectivamente.
n=int(input('Introduce un numero: '))
m=int(input('Introduce un numero: '))
c= n // m
r= n % m
print('El cociente de la division es: ',c)
print('El resto de la division es: ',r)

