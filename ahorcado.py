texto = ""
texto = input(texto)
texto.upper()
intentos = 0

vidas = 0
vidas = int(input()) + 1

while vidas>100 or vidas<1:
    vidas= int(input()) + 1

while len(texto) != 0 and vidas != 0:
    letra = ""
    letra = input()
    letra.upper()
    if letra in texto:
        texto = texto.replace(letra, "")
    else:    
        vidas -= 1
    intentos += 1

if vidas == 0:
    print(0)
else:
    print(intentos)