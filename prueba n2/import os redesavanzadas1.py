import os
import ipaddress
import json

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
        dispositivos = dispositivos_por_sector[sector]['dispositivos']
        for i, dispositivo in enumerate(dispositivos, 1):
            print(f"{i} - {dispositivo['nombre']}")
        dispositivo_elegido = int(input("Elija un dispositivo para ver más detalles: "))
        if 1 <= dispositivo_elegido <= len(dispositivos):
            dispositivo = dispositivos[dispositivo_elegido - 1]
            print(f"Detalles del dispositivo: {json.dumps(dispositivo, indent=4)}")
            if 'archivo' in dispositivo:
                leer_archivo(dispositivo['archivo'])
        else:
            print("Dispositivo no válido.")
    else:
        print("Sector no válido.")

# Función para validar una dirección IP
def validar_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Función para leer archivos específicos
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as file:
            contenido = file.read()
            print(f"Contenido de {nombre_archivo}:")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")

# Función para generar los archivos solicitados
def generar_archivos_txt():
    archivos_contenidos = {
        "internet.txt": "Contenido del archivo internet.txt",
        "oficina remota 5-6.txt": "Contenido del archivo oficina remota 5-6.txt",
        "oficina remota 3-4.txt": "Contenido del archivo oficina remota 3-4.txt"
    }
    
    for nombre_archivo, contenido in archivos_contenidos.items():
        with open(nombre_archivo, "w") as file:
            file.write(contenido)
        print(f"Archivo {nombre_archivo} generado con éxito.")

# Función para borrar dispositivos de un sector
def borrar_dispositivo(sector, dispositivos_por_sector):
    if sector in dispositivos_por_sector:
        print("Dispositivos en el sector seleccionado:")
        dispositivos = dispositivos_por_sector[sector]['dispositivos']
        for i, dispositivo in enumerate(dispositivos, 1):
            print(f"{i} - {dispositivo['nombre']}")
        dispositivo_elegido = int(input("Elija el número del dispositivo a borrar: "))
        if 1 <= dispositivo_elegido <= len(dispositivos):
            dispositivo_borrado = dispositivos.pop(dispositivo_elegido - 1)
            print(f"Dispositivo '{dispositivo_borrado['nombre']}' borrado con éxito.")
        else:
            print("Número de dispositivo no válido.")
    else:
        print("Sector no válido.")

# Función para añadir dispositivos a un sector
def añadir_dispositivo(sector, dispositivos_por_sector):
    if sector in dispositivos_por_sector:
        nombre = input("Ingrese el nombre del nuevo dispositivo: ")
        ip = input("Ingrese la IP del nuevo dispositivo: ")
        while not validar_ip(ip):
            print("IP no válida. Intente de nuevo.")
            ip = input("Ingrese la IP del nuevo dispositivo: ")
        vlan = input("Ingrese la VLAN del nuevo dispositivo: ")
        modelo = input("Ingrese el modelo jerárquico del nuevo dispositivo (Núcleo, Distribución, Acceso): ")
        while modelo not in ["Núcleo", "Distribución", "Acceso"]:
            print("Modelo jerárquico no válido. Intente de nuevo.")
            modelo = input("Ingrese el modelo jerárquico del nuevo dispositivo (Núcleo, Distribución, Acceso): ")
        servicios = input("Ingrese los servicios del nuevo dispositivo: ")
        archivo = input("Ingrese el nombre del archivo asociado (opcional): ")

        nuevo_dispositivo = {
            'nombre': nombre,
            'ip': ip,
            'vlan': vlan,
            'modelo': modelo,
            'servicios': servicios
        }
        if archivo:
            nuevo_dispositivo['archivo'] = archivo

        dispositivos_por_sector[sector]['dispositivos'].append(nuevo_dispositivo)
        print(f"Dispositivo '{nombre}' añadido con éxito al sector {sector}.")
    else:
        print("Sector no válido.")

# Función para borrar sectores
def borrar_sector(dispositivos_por_sector):
    print("Sectores disponibles:")
    for sector, detalles in dispositivos_por_sector.items():
        print(f"{sector} - {detalles['nombre']}")
    sector_elegido = int(input("Elija el número del sector a borrar: "))
    if sector_elegido in dispositivos_por_sector:
        del dispositivos_por_sector[sector_elegido]
        print(f"Sector {sector_elegido} borrado con éxito.")
    else:
        print("Número de sector no válido.")

# Función para añadir sectores
def añadir_sector(dispositivos_por_sector):
    nuevo_sector = int(input("Ingrese el número del nuevo sector: "))
    if nuevo_sector not in dispositivos_por_sector:
        nombre_sector = input("Ingrese el nombre del nuevo sector: ")
        dispositivos_por_sector[nuevo_sector] = {
            'nombre': nombre_sector,
            'dispositivos': []
        }
        print(f"Sector {nuevo_sector} ('{nombre_sector}') añadido con éxito.")
    else:
        print(f"El sector {nuevo_sector} ya existe.")

# Función para mostrar sectores
def mostrar_sectores(dispositivos_por_sector):
    print("Sectores disponibles:")
    for sector, detalles in dispositivos_por_sector.items():
        print(f"{sector} - {detalles['nombre']}")

# Diccionario para almacenar los dispositivos por sector
dispositivos_por_sector = {
    1: {
        'nombre': "Sucursal Principal",
        'dispositivos': [
            {'nombre': "Router", 'ip': "192.168.1.1", 'vlan': "10", 'modelo': "Núcleo", 'servicios': "Enrutamiento, Firewall", 'archivo': "Routersucursal.txt"},
            {'nombre': "Switch Multicapa", 'ip': "192.168.1.2", 'vlan': "20", 'modelo': "Distribución", 'servicios': "Conmutación", 'archivo': "switchmulticapa.txt"},
            {'nombre': "Dispositivos Finales", 'ip': "192.168.1.3", 'vlan': "30", 'modelo': "Acceso", 'servicios': "Acceso a red", 'archivo': "dispositivofinal.txt"}
        ]
    },
    2: {
        'nombre': "Backbone",
        'dispositivos': [
            {'nombre': "Router", 'ip': "10.0.0.1", 'vlan': "40", 'modelo': "Núcleo", 'servicios': "Enrutamiento", 'archivo': "Routerblackbone.txt"}
        ]
    },
    3: {
        'nombre': "BGP 2345",
        'dispositivos': [
            {'nombre': "Router BGP 2345", 'ip': "10.1.0.1", 'vlan': "50", 'modelo': "Núcleo", 'servicios': "Enrutamiento", 'archivo': "RouterBGP2345.txt"}
        ]
    },
    4: {
        'nombre': "Oficina Remota",
        'dispositivos': [
            {'nombre': "Oficina Remota 1", 'ip': "172.16.0.1", 'vlan': "60", 'modelo': "Distribución", 'servicios': "Conmutación", 'archivo': "oficina remota 1.txt"},
            {'nombre': "Oficina Remota 2", 'ip': "172.16.0.2", 'vlan': "70", 'modelo': "Distribución", 'servicios': "Conmutación", 'archivo': "oficina remota 2.txt"}
        ]
    },
    5: {
        'nombre': "OSPF Area 123",
        'dispositivos': [
            {'nombre': "OSPF Area 123", 'ip': "10.2.0.1", 'vlan': "80", 'modelo': "Distribución", 'servicios': "Enrutamiento", 'archivo': "OSPF Area 123.txt"}
        ]
    }
}

# Generar los archivos solicitados al inicio del programa
generar_archivos_txt()

while True:
    clear_screen()
    print("Bienvenido, ¿qué desea hacer?")
    print("1-ver sectores\n2-ver dispositivos\n3-borrar dispositivos\n4-borrar sectores\n5-añadir sectores\n6-añadir dispositivos\n7-salir")
    opciones = int(input("Elija una opción: "))
    clear_screen()

    if opciones == 1:
        mostrar_sectores(dispositivos_por_sector)
    elif opciones == 2:
        mostrar_sectores(dispositivos_por_sector)
        sector = int(input("Elija un sector: "))
        clear_screen()
        mostrar_dispositivos(sector, dispositivos_por_sector)
    elif opciones == 3:
        mostrar_sectores(dispositivos_por_sector)
        sector = int(input("Elija un sector: "))
        clear_screen()
        borrar_dispositivo(sector, dispositivos_por_sector)
    elif opciones == 4:
        borrar_sector(dispositivos_por_sector)
    elif opciones == 5:
        añadir_sector(dispositivos_por_sector)
    elif opciones == 6:
        mostrar_sectores(dispositivos_por_sector)
        sector = int(input("Elija un sector: "))
        clear_screen()
        añadir_dispositivo(sector, dispositivos_por_sector)
    elif opciones == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")

    input("\nPresione Enter para continuar...")
