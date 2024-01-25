
print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

#Primera interacción. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas.\n")
print()
print("Hola ", nombre, ", bienvenido/a a Mi Red")
print()

#Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
#¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente lí­nea?
años = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2024-años-1
print()

#Tercera interacción. Solicitamos la estatura, medida en metros.
#Utilizamos la conversión a 'int', y una expresión para convertir esto
#a una medida en metros y centÃ­metros
estatura = float(input("Cuentame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros.\n"))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interacción. Consultamos cuÃ¡ntos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes.\n"))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Ahora puedes practicar solicitando más datos al usuario. Solo tienes que usar apropiadamente input() y print()
#1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escríbelos en pantalla
#   utilizando print. Puedes agregar todas las líneas que necesites.

sexo = input("¿Cuál es tu sexo?\n")
print()
print("--------------------------------------------------")

telefono = str(input("¿Cuál es tu número de teléfono?\n"))
print()
print("--------------------------------------------------")

ciudad = input("¿En qué ciudad vives?\n")
print()


print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("Tu sexo es: ", sexo)
print("Tu número de teléfono es: ", telefono)
print("Tu ciudad es: ", ciudad)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acción de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar más acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafíos:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opción al usuario.
#
#2. Modifica este menú para que le permita el usuario realizar más de una acción.
#   Por ejemplo, puedes agregar una acción que permita al usuario modificar su nombre.

continuar = True
while continuar:
    # Solicitamos opción al usuario
    opcion = input("¿Qué acción deseas realizar?\n1. Escribir un mensaje (1)\n2. Modificar nombre (2)\n3. Salir (3)\n")

    if opcion == "1" or opcion == "Escribir un mensaje" or opcion == "mensaje":
        mensaje = input("Perfecto. ¿En qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    elif opcion == "2" or opcion == "Modificar nombre" or opcion == "nombre":
        nuevo_nombre = input("Ingresa tu nuevo nombre: ")
        nombre = nuevo_nombre
        print("Nombre modificado exitosamente.")
    elif opcion == "3" or opcion == "Salir" or opcion == "salir":
        continuar = False
        print("Gracias por usar Mi Red. ¡Hasta pronto!")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
