# ============================================
#   QUIZ SMX - El joc del curs
#   Autor: Bilal El Azouzi
# ============================================

print("=======================================")
print("      BENVINGUT AL QUIZ D'SMX 💻")
print("=======================================")

nom = input("Com et dius? ")
print("Molt bé,", nom + "! Respon amb el número de l'opció.")
print("Cada encert val 1 punt. Som-hi!")

punts = 0

# ---------- Pregunta 1: Git ----------
print("\n--- Pregunta 1: Git ---")
print("Quina comanda puja els canvis a GitHub?")
print("1) git add")
print("2) git commit")
print("3) git push")
resposta = int(input("La teva resposta: "))

if resposta == 3:
    print("✅ Correcte! git push puja els commits al repositori remot.")
    punts = punts + 1
else:
    print("❌ Incorrecte. La bona era git push.")

# ---------- Pregunta 2: Python ----------
print("\n--- Pregunta 2: Python ---")
print("Què fa la funció int()?")
print("1) Mostra un text per pantalla")
print("2) Converteix un valor a nombre enter")
print("3) Demana un valor per teclat")
resposta = int(input("La teva resposta: "))

if resposta == 2:
    print("✅ Correcte! Això és el casting.")
    punts = punts + 1
else:
    print("❌ Incorrecte. int() converteix a enter.")

# ---------- Pregunta 3: Xarxes ----------
print("\n--- Pregunta 3: Xarxes ---")
print("Quin servei dona adreces IP automàticament?")
print("1) DNS")
print("2) DHCP")
print("3) SSH")
resposta = int(input("La teva resposta: "))

if resposta == 2:
    print("✅ Correcte! El DHCP reparteix les IPs.")
    punts = punts + 1
else:
    print("❌ Incorrecte. És el DHCP.")

# ---------- Pregunta 4: Linux ----------
print("\n--- Pregunta 4: Linux ---")
print("Quina comanda crea una carpeta?")
print("1) mkdir")
print("2) cd")
print("3) ls")
resposta = int(input("La teva resposta: "))

if resposta == 1:
    print("✅ Correcte! mkdir = make directory.")
    punts = punts + 1
else:
    print("❌ Incorrecte. És mkdir.")

# ---------- Pregunta 5: Seguretat ----------
print("\n--- Pregunta 5: Seguretat ---")
print("Quina clau SSH NO s'ha de compartir mai?")
print("1) La pública (.pub)")
print("2) La privada")
print("3) Totes dues es poden compartir")
resposta = int(input("La teva resposta: "))

if resposta == 2:
    print("✅ Correcte! La privada es queda sempre al teu ordinador.")
    punts = punts + 1
else:
    print("❌ Incorrecte. La privada no es comparteix mai.")

# ---------- Resultat final ----------
print("\n=======================================")
print("RESULTAT FINAL DE", nom.upper())
print("Has fet", punts, "de 5 punts")

nota = punts * 2
print("La teva nota és:", nota)

if nota == 10:
    print("🏆 Perfecte! Ets un crack de l'SMX!")
elif nota >= 8:
    print("🔥 Molt bé! Gairebé perfecte.")
elif nota >= 5:
    print("👍 Aprovat! Però encara pots millorar.")
else:
    print("📚 Suspès... toca repassar una mica!")
print("=======================================")