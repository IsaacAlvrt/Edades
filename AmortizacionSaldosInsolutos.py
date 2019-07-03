#Tabla de amortizacion sobre saldos insoluto
#Interes Simple
print("TABLA DE AMOTTIZACIÓN SOBRE SALDOS INSOLUTOS \n")

#Tiempo
print("¿De cuantos meses es tu deuda?")
t = int(input("")) #Tiempo en meses

#Tasa de interes
print("¿Qué porcentaje es tu tasa de interes anual?")
iAnual = int( input("") )
i = (float(iAnual) / 1200)

#Capital
print("¿Cuánto es tu capital (Valor presente)")
cap = input("")
c = float(cap)
print("Tu tasa de interes es de: ", iAnual, "% Anual \n"
    "Tu capital es de: $", c)

#amortizacion sobre saldo insoluto
R = (c*i) / (1-(1+i)**-t) #Pago mensual
total = R *t
print("Tu deuda total es de: ", round(total,2), "\n" )

#Tabla de deuda
x = 1
for x in range(1, t + 1):
    m = c - ( R - (c * i) )
    print("El saldo de tu deuda el ", x, "Mes es: ", round(m,2),
     "Tu pago mensual es de: ",round(R,2))
    c = m
