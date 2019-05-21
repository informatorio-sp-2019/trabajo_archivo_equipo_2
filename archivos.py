"""
"""
def guarda_usuario(usuario,clave)
	import os

	if  not os.path.exists('usuarios.txt'):
		archivo = open('usuarios.txt', 'w')
	else:
		archivo = open('usuarios.txt', 'r+')

	archivo.write(usuario+'#'+clave+\n')
