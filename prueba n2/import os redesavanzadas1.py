import os

# Función para limpiar la pantalla de manera compatible con diferentes sistemas operativos
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Función para mostrar dispositivos de un sector
def mostrar_dispositivos(sector, dispositivos_por_sector):
    if sector in dispositivos_por_sector:
        print("Dispositivos en el sector seleccionado:")
        dispositivos = dispositivos_por_sector[sector]
        for i, dispositivo in enumerate(dispositivos, 1):
            print(f"{i} - {dispositivo}")
        dispositivo_elegido = int(input("Elija un dispositivo para ver más detalles: "))
        if 1 <= dispositivo_elegido <= len(dispositivos):
            if sector == 1:  # Sucursal Principal
                if dispositivo_elegido == 1:  # Router seleccionado
                    leer_archivo_routersucursal()
                elif dispositivo_elegido == 2:  # Switch Multicapa seleccionado
                    leer_archivo_switchmulticapa()
                elif dispositivo_elegido == 3:  # Dispositivos Finales seleccionado
                    leer_archivo_dispositivofinal()
                else:
                    print(f"Detalles del dispositivo: {dispositivos[dispositivo_elegido - 1]}")
            else:
                print(f"Detalles del dispositivo: {dispositivos[dispositivo_elegido - 1]}")
        else:
            print("Dispositivo no válido.")
    else:
        print("Sector no válido.")

# Función para leer el archivo Routersucursal.txt
def leer_archivo_routersucursal():
    try:
        with open("Routersucursal.txt", "r") as file:
            contenido = file.read()
            print("Contenido de Routersucursal.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo Routersucursal.txt no se encuentra.")

# Función para leer el archivo switchmulticapa.txt
def leer_archivo_switchmulticapa():
    try:
        with open("switchmulticapa.txt", "r") as file:
            contenido = file.read()
            print("Contenido de switchmulticapa.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo switchmulticapa.txt no se encuentra.")

# Función para leer el archivo dispositivofinal.txt
def leer_archivo_dispositivofinal():
    try:
        with open("dispositivofinal.txt", "r") as file:
            contenido = file.read()
            print("Contenido de dispositivofinal.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo dispositivofinal.txt no se encuentra.")

# Diccionario para almacenar los dispositivos por sector
dispositivos_por_sector = {
    1: ["Router", "Switch Multicapa", "Dispositivos Finales"],
    2: ["Router", "Switch Multicapa", "Dispositivos Finales"],
    3: ["Router", "Switch Multicapa", "Dispositivos Finales"],
    4: ["Router", "Switch Multicapa", "Dispositivos Finales"]
}

sectores = (
    "1-sucursal principal\n"
    "2-blackbone\n"
    "3-core empresa\n"
    "4-oficina remota"
)

while True:
    clear_screen()
    print("Bienvenido, ¿qué desea hacer?")
    print("1-ver sectores\n2-ver dispositivos\n3-borrar dispositivos\n4-borrar sectores\n5-añadir sectores\n6-añadir dispositivos\n7-salir")
    opciones = int(input("Elija una opción: "))
    clear_screen()

    if opciones == 1:
        print("Sectores disponibles:")
        print(sectores)
        sector = int(input("Elija un sector: "))
        clear_screen()
        mostrar_dispositivos(sector, dispositivos_por_sector)
    elif opciones == 2:
        print("Sectores disponibles:")
        print(sectores)
        sector = int(input("Elija un sector: "))
        clear_screen()
        mostrar_dispositivos(sector, dispositivos_por_sector)
    elif opciones == 3:
        print("Función para borrar dispositivos aún no implementada.")
    elif opciones == 4:
        print("Función para borrar sectores aún no implementada.")
    elif opciones == 5:
        print("Función para añadir sectores aún no implementada.")
    elif opciones == 6:
        print("Función para añadir dispositivos aún no implementada.")
    elif opciones == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")

    input("\nPresione Enter para continuar...")

