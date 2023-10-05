<<<<<<< HEAD
#Imagina que acabas de abrir una nueva cuenta 
#de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran 
#hasta finales de año, se te añaden al balance final 
#de tu cuenta de ahorros. Escribir un programa que comience 
#leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
#introducida por el usuario. Después el programa debe calcular y 
#mostrar por pantalla la cantidad de ahorros tras el primer, segundo 
#y tercer años. Redondear cada cantidad a dos decimales.
cantidad=int(input('Introduce la cantidad de dinero: '))
interes = (4/100)
for i in [1,2,3]:
    capital= cantidad  * interes
    cantidad= cantidad + capital
    print('El año',i ,'tuvo una ganancia de',round(cantidad,2),'€')




#print('El cociente de la division es: ',c)
=======
#Imagina que acabas de abrir una nueva cuenta 
#de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran 
#hasta finales de año, se te añaden al balance final 
#de tu cuenta de ahorros. Escribir un programa que comience 
#leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
#introducida por el usuario. Después el programa debe calcular y 
#mostrar por pantalla la cantidad de ahorros tras el primer, segundo 
#y tercer años. Redondear cada cantidad a dos decimales.
cantidad=int(input('Introduce la cantidad de dinero: '))
interes = (4/100)
for i in [1,2,3]:
    capital= cantidad  * interes
    cantidad= cantidad + capital
    print('El año',i ,'tuvo una ganancia de',round(cantidad,2),'€')




#print('El cociente de la division es: ',c)
>>>>>>> 190bf4af1e7df354a5c30569231a889b5d616c56
#print('El resto de la division es: ',r)