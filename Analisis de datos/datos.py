import pandas as pd

datos2 = pd.read_excel("Datos2.xlsx")
data = datos2.to_dict("records") 
print("Datos:\n")
print(datos2)

for i in data:
    print("vamos por: ", i["Nombre"])
    Quimi = i["Quimica"]
    Mate = i["Matematica"]
    Fisi = i["Fisica"]
    if isinstance(Quimi,int) == False:
        Quimi = 0
        print("Reescribi quimi de:", i["Nombre"])
    if isinstance(Mate,int) == False:
        Mate = 0
        print("Reescribi mate de:", i["Nombre"])
    if isinstance(Fisi,float) == False:
        Fisi = 0
        print("Reescribi fisi de:", i["Nombre"])
    if (Mate < 11 and Mate > 4):
        total = (Quimi + Mate + Fisi)/3
        print(f"El promedio de {i['Nombre']}  es: {total}")