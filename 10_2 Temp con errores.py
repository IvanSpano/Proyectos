# Programa que pide una temperatura y la convierte de ºC a ºF o viceversa

def inicio():
	print("Programa de conversión de temperaturas")
	print("=========================================")

def menu():
	print("\n********** Menu de opciones ************")
	print("\t1. Conversión de ºC a ºF")
	print("\t2. Conversión de ºF a ºC")
	print("\t3. Salir")
	
def ingresar_temperatura():
	while True:
		try:	
			temp = float(input("Ingrese la temperatura: "))
		except ValueError:
			print("Error, debe ingresar un nro")
		else:
			return temp


def celsius_a_farenheit(temp):
	return temp * 1.8 + 32
	

def farenheit_a_celsius(temp):
	return (temp - 32) / 1.8
	
	
#############################################

inicio()

while True:
	
	menu()

	opcion = input("Seleccione una opción: ")

	if opcion == "1":
		temp = ingresar_temperatura()
		print("La temperatura convertida es {:.1f}ºF".format(celsius_a_farenheit(temp)))
	
	elif opcion == "2":
		temp = ingresar_temperatura()
		print("La temperatura convertida es {:.1f}ºC".format(farenheit_a_celsius(temp)))
		
	elif opcion == "3":
		print("Gracias por utilizar este programa...")
		break
		
	else:
		print("Opción incorrecta")
