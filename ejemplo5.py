horas=float(input('¿Cuantas horas has trabajado?'))
#en caso de que haga 1h y media, si solo pudiera hacer horas enteras usariamos int
coste=float(input('¿Cual es el coste de horas?'))
sueldo = horas * coste
print('Tu sueldo es el siguiente',round(sueldo,2) ,end='€')