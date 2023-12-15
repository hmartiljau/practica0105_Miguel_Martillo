file = open('sdg_08_10 - sdg_08_10.tsv', 'r')
texto = file.read()
separador=texto.split("\n")
pais=input('introduce las iniciales del pais')
pais=pais.upper()
print(pais)
ejey=(F"CLV10_EUR_HAB,B1GQ.{pais}")
tabla=[]
año=2000
for i in separador:
    z = i.split()
    if z[0] == ejey:
        x=(z[1:])
    print(tabla)