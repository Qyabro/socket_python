import socket
import serial, time
import os #para poder enviar comandos de la consola

PUERTO_SERVIDOR = 1421

#======================== FUNCIONES =======================================
# Funcion para limpiar la consola de acuerdo al sistema operativo
def clear(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#============================================================================

def abrir_socket(ip):

	#try:

	global mi_socket
	# Se crea nuestro socket
	mi_socket = socket.socket()
	mi_socket.settimeout(15) #En segundos
	# Se establece conexion con el servidor
	mi_socket.connect((ip,PUERTO_SERVIDOR))	
	return mi_socket

	#except socket.timeout:
	#	input("\n  No se logra alcanzar el phobos!!! ... Pressione una tecla.")
	#except :
	#	input("\n  Error Inesperado Apertura Socket!!! ... Pressione una tecla.")

#============================================================================

def consulta_phobos(consulta):
	

	mi_socket.send(consulta)
	#print("Enviado  -->", consulta.decode())
	mi_socket.settimeout(5) #En segundos
	# Se espera una respuesta desde el servidor
	# con un limite de 1024 Bytes en el buffer
	# se usa decode para convertir los Bytes a ASCCI
	#respuesta = mi_socket.recv(1024).decode()
	respuesta = mi_socket.recv(17).decode()

	# Se muestra la respuesta por la consola
	return respuesta
	
#============================================================================

#========================== PRINCIPAL =======================================
while True:
	try:			
		clear()
		fecha = [str(time.strftime("%d-%m-%y"))]
		fecha = fecha[0]
		print("\n ================================================")
		print(" %\t     Consultas Socket v1.0	\t%")	
		print(" %\t\t   "+fecha+"\t\t\t%")	
		print(" ================================================\n")
		
		archivo = open("listado.txt","r")
		listado = archivo.read()
		archivo.close()		

		listado_ip=listado.split('\n')

		for ip in listado_ip:
			print(ip)
			mi_socket = abrir_socket(ip)
			time.sleep(2)
			resp=consulta_phobos(b'FIR')
			print("FIR:\t\t\t" + resp)	
					

			mi_socket.close()

			#---- Guarda en archivo General --------
			f = open("pruebas.txt","a")
			f.write(fecha)
			f.write("|") # Separador
			f.write(ip)
			f.write("|") # Separador
			f.write(resp)
			f.write("\n")
			f.close()

			
		#-----------------------------
		input("\n FINALIZADO. Presione ENTER para realizar otra prueba.")

	except socket.timeout:
		input("\n  Sin respuesta!!! ... Pressione una tecla.")
	#except :
	#	input("\n  Error Inesperado Apertura Socket!!! ... Pressione una tecla.")

	except :
	    input("\n Error Inesperado!!! ... Pressione una tecla.")
	    puerto.close()

