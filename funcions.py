# ACTIVITAT PRÀCTICA - FUNCIONS EN PYTHON
# Nom: Bilal El Azouzi

# ---------- EXERCICI 1 ----------
def calcular_preu(peces, ma_obra):
    total = peces + ma_obra
    return total

preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")

# Quants paràmetres té la funció? Dos: peces i ma_obra.
# Quin valor retorna? La suma de les peces i la mà d'obra.
# Què passaria si eliminéssim el return? La funció no retornaria res
# i el print mostraria "Cost total: None".


# ---------- EXERCICI 2 ----------
# Els tipus de client s'han d'escriure en minúscules:
# particular, empresa o habitual
def aplicar_descompte(preu, tipus_client):
    if tipus_client == "particular":
        preu_final = preu
    elif tipus_client == "empresa":
        preu_final = preu - preu * 0.10
    elif tipus_client == "habitual":
        preu_final = preu - preu * 0.15
    else:
        print("Error: tipus de client no vàlid")
        preu_final = preu
    return preu_final

print(aplicar_descompte(100, "particular"))
print(aplicar_descompte(100, "empresa"))
print(aplicar_descompte(100, "habitual"))
print(aplicar_descompte(100, "estudiant"))


# ---------- EXERCICI 3 ----------
def calcular_iva(preu):
    iva = preu * 0.21
    return iva

def calcular_factura(preu, tipus_client):
    preu_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descompte)
    total = preu_descompte + iva
    return total

print("Factura:", calcular_factura(100, "empresa"), "€")


# ---------- EXERCICI 4 ----------
def mostrar_menu():
    print("===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")
    print("")

def mostrar_factura(nom, preu_inicial, tipus_client):
    preu_descompte = aplicar_descompte(preu_inicial, tipus_client)
    descompte = preu_inicial - preu_descompte
    iva = calcular_iva(preu_descompte)
    total = calcular_factura(preu_inicial, tipus_client)
    print("----- FACTURA -----")
    print("Client:", nom)
    print("Preu inicial:", preu_inicial, "€")
    print("Descompte aplicat:", descompte, "€")
    print("IVA:", iva, "€")
    print("Total a pagar:", total, "€")
    print("-------------------")

def nova_reparacio():
    nom = input("Nom del client: ")
    peces = float(input("Cost de les peces: "))
    ma_obra = float(input("Cost de la mà d'obra: "))
    tipus_client = input("Tipus de client (particular/empresa/habitual): ")
    preu_inicial = calcular_preu(peces, ma_obra)
    mostrar_factura(nom, preu_inicial, tipus_client)
    total = calcular_factura(preu_inicial, tipus_client)
    return total

# Programa principal
reparacions = 0
facturacio = 0
opcio = ""

while opcio != "4":
    mostrar_menu()
    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        total = nova_reparacio()
        reparacions = reparacions + 1
        facturacio = facturacio + total
    elif opcio == "2":
        print("Reparacions realitzades:", reparacions)
    elif opcio == "3":
        print("Facturació acumulada:", facturacio, "€")
    elif opcio == "4":
        print("Adéu!")
    else:
        print("Opció no vàlida")


# ---------- EXERCICI 5 ----------
# 1. print() mostra una cosa per pantalla. return retorna el resultat
#    per poder guardar-lo en una variable i fer-lo servir després.
# 2. Perquè el codi queda més ordenat, és més fàcil trobar errors
#    i no s'ha de repetir el mateix codi.
# 3. És una variable que es posa a la definició de la funció
#    i que rep les dades quan la cridem.
# 4. És una variable que es crea dins d'una funció i només
#    existeix allà dins. Fora de la funció no es pot utilitzar.
# 5. Escrius el codi una sola vegada i el pots fer servir moltes.
#    Si l'has de canviar, només el canvies en un lloc.