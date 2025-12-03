# llistes i diccionaris
llista_buida = []
diccionari_buit = {}

# creem una llista plena de coses
llista = ["Adrià", 33, 168., "Institut Escola Sant Pol de Mar"]

print(type(llista))
print(type(llista[2])) # float
print(type(llista[0])) # str

# Accedir a subllistes
# Mostrem els elements llista[M:N]
print(llista[0:3]) # Mostrarà els elements compresos en l'interval M:(N-1)

# Accedim a l'ultim element:
print(llista[-1])

# Mètodes importants de les llistes:
# omplim la llista buida:
llista_buida.append("Prova")
print(llista_buida)

llista_buida.append(["hola", "adeu"])
print(llista_buida)

print(llista_buida[1]) # ÉS UNA LLISTA
print(llista_buida[1][0][2])

# Inserim contingut en una posició determinada
llista.insert(1, "Santacreu")
print(llista)

# Eliminem elements
llista.pop() # Si no especifico posició elimina el darrer element
print(llista)

# Eliminem per valor
llista.remove(33) # Només elimina la primera vegada que el troba
print(llista)

# Podem assignar SUBLLISTES a noves variables:
subllista = llista[0:2]
print(subllista)

# Longitud de la llista / string
print(len(llista))
print(len("Hola, em dic Adrià"))

# Invertir la llista
print(llista[::-1]) 

"""
DICCIONARIS :)
"""
dades_formulari = {
    "nom": "Adrià",
    "cognom": "Santacreu",
    "edat": 33,
    "alcada": 168.,
    "feina": "Institut Escola Sant Pol de Mar" 
}

print(type(dades_formulari)) # tipus DICT

# Accedim a les dades:
print(dades_formulari["nom"])

# Canviar dades d'una variable del diccionari
dades_formulari["nom"] = "Gerard"

print(dades_formulari)

# Claus del diccionari
print(dades_formulari.keys())

for clau in dades_formulari.keys():
    print(clau)

print("\nLes dades introduïdes per l'usuari, són:")
for clau, item in dades_formulari.items():
    print(f"* {clau.capitalize()}: {item}")
    


