#Recordemos que en este mÃ³dulo estÃ¡n todos las funciones adicionales que hemos creado.
import S5Red as Red
#El mÃ³dulo 'os' nos permitirÃ¡ consultar si un archivo existe.
import os

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

datos_usuario = Red.leer_datos_usuario(nombre)
if datos_usuario:
    nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado = datos_usuario
else:
    # En caso que el usuario no exista, consultamos por sus datos tal como lo hacíamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""

#En ambos casos, al llegar aquí­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
Red.mostrar_mensaje(nombre, None, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)
    elif opcion == 2:
        estado = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, estado)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre + ".user")
        Red.escribir_datos_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)
        print("Archivo", nombre + ".user", "guardado")

print("Gracias por usar Mi Red. ¡Hasta pronto!")
