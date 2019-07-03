#Cajero Automatico
#Siempre dará la minima cantidad de billetes

class billete:
    def money(self):
        # v = valor, c = cantidad
        print("ATM")

print("ATM")

#Billete de $50
b50 = billete()
b50.v = 50
b50.c = 10

#Billete de $20
b20 = billete()
b20.v = 20
b20.c = 15

#Billete de $10
b10 = billete()
b10.v = 10
b10.c = 20



#Saldo Inicial
saldoInicial = (b50.v * b50.c) + (b20.v * b20.c) +(b10.v * b10.c)
print("Tu saldo Inicial es de $",saldoInicial,"\n")

#Datos del usuario
print("¿Cuánto dinero deseas retirar?")
R = input("")
r = int(R)
saldoFinal = saldoInicial - r

#Algoritmo ATM
if r <= saldoInicial:
    if r%10 == 0:
        print("Tu saldo Final es de $", saldoFinal)
        #Algoritmo para dar billetes de 50
        if r/b50.v <= b50.c:
            b50.c = r // b50.v
        else:
            b50.c = b50.c
        #Algoritmo para dar billetes de 20
        if (r - b50.c * b50.v) / (b20.v) <= b20.c:
            b20.c = (r - b50.v * b50.c) // b20.v
        else:
            b20.c = b20.c
        #Algoritmo para dar billetes de 50
        if ( r - (b50.c * b50.v) - (b20.c * b20.v) ) / b10.v <= b10.c:
            b10.c = ( r - (b50.c * b50.v) - (b20.c * b20.v) ) // b10.v
        else:
            print("no mames")

        #Resultado
        print(b50.c, "billetes de $", b50.v)
        print(b20.c, "billetes de $", b20.v)
        print(b10.c, "billetes de $", b10.v)
    else:
        print("Solo doy multiplos de 10, idiota")
else:
    print("No tengo tanto dinero. gei")
