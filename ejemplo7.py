 #Escribir un programa que pida al usuario su peso (en kg)
 #y estatura (en metros), calcule el índice de masa corporal y
 #lo almacene en una variable, y muestre por pantalla la frase Tu 
 #índice de masa corporal es <imc> donde <imc> es el índice de masa 
 #corporal calculado redondeado con dos decimales.

peso=float(input('Introduce tu peso en kg: '))
altura=float(input('Introduce tu altura en metros: '))
print('tu peso en kg es: ',round(peso,2))
print('Tu altura en metros es: ',round(altura,2))
IMC = round(peso/((altura)**2),2)
print('Tu indice de masa corporal es', IMC)
