import os

def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    año = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2024-año-1

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def obtener_pais():
    pais = input("Indica tu país de nacimiento: ")
    return pais

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
    return amigos

def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    return (n,e,em,ec,na)

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "metro y ", estatura_cm, "centímetros")
    print("Sexo:     ", sexo)
    print("País:     ", pais)
    print("Amigos:   ", num_amigos)
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

def leer_datos_usuario(nombre):
    if os.path.isfile(nombre + ".user"):
        print("Leyendo datos de usuario", nombre, "desde archivo.")
        with open(nombre + ".user", "r") as archivo_usuario:
            nombre = archivo_usuario.readline().strip()
            edad = int(archivo_usuario.readline().strip())
            estatura = float(archivo_usuario.readline().strip())
            estatura_m = int(estatura)
            estatura_cm = int((estatura - estatura_m) * 100)
            sexo = archivo_usuario.readline().strip()
            pais = archivo_usuario.readline().strip()
            num_amigos = int(archivo_usuario.readline().strip())
            estado = archivo_usuario.readline().strip()
        return nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado
    else:
        return None

def escribir_datos_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado):
    with open(nombre + ".user", "w") as archivo_usuario:
        archivo_usuario.write(nombre + "\n")
        archivo_usuario.write(str(edad) + "\n")
        archivo_usuario.write(str(estatura_m + estatura_cm/100) + "\n")
        archivo_usuario.write(sexo + "\n")
        archivo_usuario.write(pais + "\n")
        archivo_usuario.write(str(num_amigos) + "\n")
        archivo_usuario.write(estado + "\n")

