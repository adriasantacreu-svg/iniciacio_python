estat = "AUTORITZAT"
estat_bateria = "OK"
estat_vent = "ESTABLE"

bateria = int(input("Quin és el nivell de bateria del dron? "))
velocitat = float(input("Quina velocitat té el vent avui? "))
urgencia = input("Quin tipus d'urgència té aquest enviament? ")

if bateria < 20:
    estat = "DENEGAT"
    estat_bateria = "BAIX"

if velocitat > 50 and not urgencia.lower() == "medic":
    estat = "DENEGAT"
    estat_vent = "INESTABLE"

print("========================================")
print("[+] ECODRONE FLIGHT CONTROL v2.0")
print("========================================")
print("> DADES DE TELEMETRIA:")
print(f"Nivell Bateria: [ {bateria} % ] {estat_bateria}")
print(f"Velocitat Vent: [ {velocitat} km/h ] {estat_vent}")
print("—————————————-")
print("> ANALITZANT SISTEMES...")
print(f"»> ESTAT FINAL: [ {estat} ]")
print("========================================")
