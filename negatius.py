hi_ha_negatiu = False

for i in range(10):
    numero = float(input("Introdueix un número: "))
    if numero < 0:
        hi_ha_negatiu = True

if hi_ha_negatiu:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")