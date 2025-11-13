print("Taxa de canvi fixa: 1 EUR = 1.10 USD\n")

# Factors de conversió necessaris
factor_euro_dolar = 1. / 1.10 # factor de conversió per passar d'euros a dolars
factor_dolar_euro = 1. / factor_euro_dolar # factor de conversió per passar de dolars a euros

# Demanem les dades a l'usuari
import_ = float(input("Introdueix l'import en euros: "))

# Mostrem els resultats per pantalla
print(f"\n{import_:.2f} € equivalen a {(import_*factor_dolar_euro):.2f} $ (tipo entrada: {type(import_)}, tipo resultat: {type(import_*factor_dolar_euro)})")

