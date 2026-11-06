num1 =  float(input("Introdueix el primer número: "))
num2 =  float(input("Introdueix el segon número: "))
num3 =  float(input("Introdueix el tercer número: "))
if num1 > num2 and num1 > num3:
    print("El majort és: ", num1 )
elif num2 > num1 and num2 > num3:
    print("El majort és: ", num2 )
else:
    print("El majort és: ", num3 )