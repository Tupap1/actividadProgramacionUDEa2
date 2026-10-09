"""  Determine el precio del servicio de agua potable para una casa, de acuerdo a las
tarifas que establece la empresa de servicios públicos de acuerdo a la cantidad de
metros cúbicos (𝑚³) consumidos.
● 0-9 𝑚 - $6/𝑚³
● 10-13 𝑚³ - $5/𝑚³
● >13 𝑚 - $9/𝑚³
Además, a todos los usuarios se les cobra una tarifa base de $50. Por último, si el
usuario pertenece al estrato 1 o 2, se realiza un descuento del 20% del total. Realice un
programa que determine el valor a pagar.
 """
 
 
 
usedWater = input('Ingresa la cantida de m3 consumidos: ')
economicTier = input('Ingresa el estrato: ')

total = 0
usedWater = float(usedWater)
if usedWater  > 0 or usedWater <= 9:
    total = usedWater * 6
elif usedWater >= 10 or usedWater >=  13:
    total = usedWater * 5
elif usedWater > 13:
    total = usedWater * 9


if economicTier in '12':
    total = total* 0.80
    
print('El total a pagar es de: ', total)
