s = "Hola mundo, chau mundo"
s.find("mundo")  #sirve para encontrar el valor donde inicia lo buscado
s.rfind("mundo") #lo mismo de derecha a izq
s.startswith("hola") #para comprobar si es verdadero o falso que inicia con esa cadena de caracteres
s.endswith("hola") #lo mismo para finalizar
"1234".isnumeric() #para ver si es un numero
"1234".isdecimal() #para ver si es numero decimal
"1234".isdigit() #no se
"abc123".isalnum() #para ver si es alpha numerico
"abc".isupper() #para ver si es está en mayus
"abc".islower() #para ver si es minuscula
" ".isspace() #para ver si es un espacio vacio
"Hola".isprintable() #para ver si es printeable
"hola a todos".encode("utf-8") #me lo guarda como binario
"hola a todos".center(100) #no se
"hola a todos".rjust(100) #no se
"hola a todos".ljust(100,"-") #no se
"hola a todos".swapcase() #cambia mayus y minus
" Hola mundo \n".strip() #me borra los caracteres no imprimibles y los espacios vacios. Tambien existe Rtrip y Lstrip.
f = "hola mundou"
f.replace("Hola", "Chau") #me reemplaza lo primero por lo segundo. Puedo reemplazar por null para que borre.
"30°C\n".strip() #me saca el \n
"30°C\n".split("°") #me divide los caracteres en 2 a partir del lugar pactado
r = "30°C"
r.partition("°") #me lo divide pero también me guarda el simbolo en el cual lo divido entre medio
temp, grado, escala = r.partition("°") #me lo divide en las 3 partes y les asigna una variable en el orden escrito
lista = ["hola", "a", "todos"]
" ".join(lista) #me junta todos los valores de la lista en un caracter y llena los espacios entre medio con lo que ponga en las comillas
