ganador = ""
mayor = 0
votos = int(input())
while votos < 1 or votos > 100:
    print("error")
    votos = int(input())
lista = {}
while votos !=0:
    nombres = input()
    if nombres in lista:
        lista[nombres] +=1 
    else:
        lista.update({nombres:1})
    votos -=1
for x, y in lista.items():
    if y > mayor:
        mayor = y       
        ganador = x
print(ganador)