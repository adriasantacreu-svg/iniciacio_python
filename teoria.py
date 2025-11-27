# Operadors condicionals
# Operadors de comparació: ==, !=, <, >, <=, >=
print(type(1 == 2))

# Comparem nombres
comparacio = (2 == 3)
print(comparacio)

# Comparacio strings
comparacio_str = ("hola" == "hola")
print(comparacio_str)

# Operadors lògics
# and, or, not
print(True and False)
print((1==2) and (1==1))
print((1==2) or (1==1))
print(not (1 == 2) and (1==1))

control_flux = 4
if (control_flux == 1):
    print('hola')
elif not (control_flux == 3):
    print("adeu")
elif (control_flux == 3):
    print("aquest sí")
else:
    print("bvhteivreo")

comptador = 1
while (comptador < 10):
    print("hola")
    comptador += 1

print(38875755 % 23)
