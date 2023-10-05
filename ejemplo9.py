#Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, 
#y muestre por pantalla el capital obtenido en la inversión.
cantidad=int(input('Introduce la cantidad a invertir: '))
#la variable cantidad la dejo como un numero entero porque de normal se suele invertir 1000, 10000, 1000000 ...
interes=int(input('Introduce el interes anual: '))
interes= interes / 100
años=int(input('Introduce el numero de años: '))
beneficio= cantidad * (interes)
beneficiototal= beneficio * años
capitalfinal= cantidad + beneficiototal
#print(beneficio)
print('La ganancia de la inversion es: ',beneficiototal ,'€')
print('Has terminado la inversion con un capital final de : ',capitalfinal ,'€')
