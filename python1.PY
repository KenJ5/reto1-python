costo = float()
horas = 100

print("escriba el dia en minusculas y sin tildes")
dia = str(input(""))
dia1 = dia.casefold()
while True:
    if dia1 == "lunes" or dia1 == "martes" or dia1 == "miercoles":
        costo = 2.00
        break
    elif dia1 == "jueves" or dia1 == "viernes":
        costo = 2.50
        break
    elif dia1 == "sabado" or dia1 == "domingo":
        costo = 3.00
        break
    else:
        print("error==> escriba bien")
        dia1 = str(input(""))

while horas > 24 :
    horas = int(input("digite la cantidad de horas\n"))
    minutos = int(input("digite la cantidad de minutos\n"))
    while minutos > 60:
        if minutos > 60:
            minutos = int(input("error==> no se puede pasar de 60 minutos, escriba de nuevo\n"))
        elif minutos < 5:
            print("")
        else:
            horas = horas + 1
    
    if horas > 24:
        print("error==> no se puede estimar un valor pasadas las 24 horas")


valorT = float(costo * horas)
print("el precio a pagar por el estacionamiento en el día " , dia1 , "es de: " , str(valorT), "dolares")
