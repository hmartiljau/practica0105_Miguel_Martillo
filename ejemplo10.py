#Una juguetería tiene mucho éxito en dos de sus productos:
#payasos y muñecas. Suele hacer venta por correo y la empresa
#de logística les cobra por peso de cada paquete así que deben 
#calcular el peso de los payasos y muñecas que saldrán en cada 
#paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
#Escribir un programa que lea el número de payasos y muñecas vendidos
#en el último pedido y calcule el peso total del paquete que será enviado.
cantmuñeca = int(input('Introduce la cantidad de muñecas en la caja: '))
cantpayaso = int(input('Introduce la cantidad de payasos en la caja: '))
pesomuñeca = int(75)
pesopayaso = int(112)
mu = cantmuñeca * pesomuñeca
pa = cantpayaso * pesopayaso
sumatotal = mu + pa
print('El peso total de la caja es de: ',sumatotal ,end=' gr')