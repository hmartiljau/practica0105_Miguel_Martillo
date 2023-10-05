#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número 
#de barras vendidas que no son del día. Después el programa debe 
#mostrar el precio habitual de una barra de pan, el descuento que 
#se le hace por no ser fresca y la ganancia final total.
preciopan = 3.49
descuento = (60/100)
vendidas = int(input('¿Cuantas barras de pan vendidas no son del dia?: '))
print('El precio habitual de una barra de pan es: ',preciopan ,'€')
preciopanmalo = preciopan * descuento
print('El descuento que se hace por no ser fresca es de: ',preciopanmalo ,'€')
gananciadelpanmalo = vendidas*preciopanmalo
print('La ganancia del pan vendido que no esta fresco es de: ',gananciadelpanmalo,'€')
