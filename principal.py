# Ejercicio 2
# Utilizando los módulos 1 y 2 del ejercicio de ‘módulos’, validación de usuario y contraseña:
# •	Implemente un módulo que importe los dos módulos del ejercicio de ‘módulos’.
# •	Guardar nombre de usuario y contraseña en un archivo plano.
# •	Controlar que no se registren nombres de usuarios repetidos.
# •	Implementar algún método de cifrado para registrar la contraseña.
# •	Realizar un menú para poder seleccionar la acción a realizar. (registrar usuario, ingresar al sistema, y salir).
# •	Al ingresar al sistema debe mostrar el mensaje: ‘Ingreso Exitoso!’

from validacion.valida_usu import *
from validacion.valida_usu import valida_long_min as valida_long_min_usu
from validacion.valida_clave import *
from os import system



#Menú
def menu():
	while True:

			print('¿Qué acción desea realizar?')
			opc =int(input('1-Registrar usuario, 2-Ingresar al sistema, 3-Salir: '))
			if opc > 4 or opc < 1:
				print('Error. Opción inválida')
				continue
			break
	if opc == 1:

		while True:
			system('cls')
			usuario = input('Usuario: ')
			if not valida_long_min_usu(usuario):
				print('\n Debe ingresar un mínimo de 6 caracteres!')
				input()			
			continue

			if not valida_long_max(usuario):
				print('\n Debe ingresar un máximo de 12 caracteres!')
				input()			
			continue

			if not valida_alfanum(usuario):
				print('\n El nombre de usuario sólo puede estar compuesto por letras y números!')
				input()			
			continue

			
			print('\n ¡Usuario validado!')
			break

		while True:
			system('cls')
			print('Nombre de usuario: ',usuario)
			print()
			import getpass
	 
			password = getpass.getpass("Contraseña: ",stream=None)
			# clave = input('Clave: ')
			if not valida_long_min(password):
				print('\n Debe ingresar un mínimo de 8 caracteres!')
						
				continue

			if valida_espacios(password):
				print('\n La contraseña no puede contener espacios en blanco!')
				input()			
				continue

			# import ipdb
			# ipdb.set_trace()
			if valida_minuscula(password) or valida_mayuscula(password) :
				print('\n La contraseña debe estár compuesta por, al menos, una minúscula y una mayúscula!')
				input()			
				continue

			if not valida_caracter_numerico(password):
				print('\n La clave debe contener, al menos, un caracter numérico!')
				input()			
				continue

			if not valida_caracter_no_alfanum(password):
				print('\n La clave debe contener, al menos, un símbolo!')
				input()			
				continue

			print('\n ¡Clave validada!')
			break
		system('cls')
		
		archivo.guardar_usuario(usuario, password)



menu()




	

