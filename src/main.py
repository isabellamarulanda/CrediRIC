# Importamos todas las listas y funciones creadas en el otro archivo
import funciones

def registrar_usuario():
    print("\nREGISTRAR NUEVO USUARIO")
    
    while True:
        nombre = input("Ingrese el Nombre --> ").strip()
        if funciones.validar_nombre_apellido(nombre):
            break
        print("Error: El nombre debe tener al menos 3 letras y no contener números.")
        
    while True:
        apellido = input("Ingrese el Apellido --> ").strip()
        if funciones.validar_nombre_apellido(apellido):
            break
        print("Error: El apellido debe tener al menos 3 letras y no contener números.")
        
    while True:
        documento = input("Ingrese el Documento --> ").strip()
        existe = False
        for u in funciones.usuarios:
            if u['documento'] == documento:
                existe = True
        if existe:
            print("Error: Este documento ya se encuentra registrado.")
            continue
        if funciones.validar_documento(documento):
            break
        print("Error: El documento debe ser numérico y tener entre 3 y 15 dígitos.")
        
    while True:
        correo = input("Ingrese el Correo Electrónico --> ").strip()
        if funciones.validar_correo(correo):
            break
        print("Error: Correo inválido. Debe contener '@' y terminar en '.com'.")
        
    while True:
        try:
            tiempo = int(input("Ingrese tiempo de préstamo permitido (5, 10, 15, 30) --> "))
            if funciones.validar_tiempo_prestamo(tiempo):
                break
            else:
                print("Error: Solo se permiten 5, 10, 15 o 30 días.")
        except ValueError:
            print("Error: Ingrese un número válido.")
            
    nuevo_usuario = {
        'nombre': nombre,
        'apellido': apellido,
        'documento': documento,
        'correo': correo,
        'tiempo_limite': tiempo
    }
    funciones.usuarios.append(nuevo_usuario)
    print(f"Cordial saludo. Usuario {nombre} {apellido} registrado con éxito en CrediRic.")

def registrar_item():
    print("\nREGISTRAR NUEVO ÍTEM AL INVENTARIO")
    
    while True:
        nombre_item = input("Nombre del artículo --> ").strip()
        if len(nombre_item) >= 3:
            break
        print("Error: El nombre debe tener al menos 3 caracteres.")
        
    print("Categorías disponibles:")
    print("1. Videojuegos")
    print("2. Libros")
    print("3. Música y video")
    print("4. Herramientas")
    print("5. Dinero")
    print("6. Misceláneo y varios")
    
    categorias = {
        "1": "Videojuegos", "2": "Libros", "3": "Música y video",
        "4": "Herramientas", "5": "Dinero", "6": "Misceláneo y varios"
    }
    
    while True:
        opc_cat = input("Seleccione el número de la categoría --> ").strip()
        if opc_cat in categorias:
            categoria_seleccionada = copy_cat = categorias[opc_cat]
            break
        print("Opción inválida.")
        
    while True:
        try:
            precio = float(input("Ingrese el precio de compra --> "))
            if precio > 0:
                break
            print("El precio debe ser mayor a 0.")
        except ValueError:
            print("Ingrese un valor numérico válido.")
            
    print("Estado del ítem (Pertenencia Lógica Difusa):")
    print("1. Excelente o Nuevo (1.0)")
    print("2. Bueno o Poco uso (0.7)")
    print("3. Regular o Desgastado (0.4)")
    while True:
        opc_estado = input("Seleccione el estado (1-3) --> ").strip()
        if opc_estado == "1":
            estado = "Excelente"
            break
        elif opc_estado == "2":
            estado = "Bueno"
            break
        elif opc_estado == "3":
            estado = "Regular"
            break
        print("Opción inválida.")
        
    prefijo = categoria_seleccionada[:3].upper()
    id_item = f"{prefijo}-{len(funciones.inventario) + 101}"
    
    nuevo_item = {
        'id': id_item,
        'nombre': nombre_item,
        'categoria': categoria_seleccionada,
        'precio': precio,
        'estado': estado,
        'disponible': True
    }
    funciones.inventario.append(nuevo_item)
    print(f"Artículo registrado correctamente. ID Asignado: {id_item}")

def registrar_prestamo():
    print("\nREGISTRAR PRÉSTAMO")
    if not funciones.usuarios:
        print("No hay usuarios registrados en el sistema.")
        return
    if not funciones.inventario:
        print("El inventario se encuentra vacío.")
        return
        
    doc_usuario = input("Ingrese el documento del amigo --> ").strip()
    
    usuario_encontrado = None
    for u in funciones.usuarios:
        if u['documento'] == doc_usuario:
            usuario_encontrado = u
            break
            
    if usuario_encontrado is None:
        print("El usuario no existe. Debe registrar al nuevo amigo primero.")
        return
        
    print("ARTÍCULOS DISPONIBLES")
    hay_disponibles = False
    for item in funciones.inventario:
        if item['disponible']:
            print(f"ID: {item['id']} | Nombre: {item['nombre']} | Categoría: {item['categoria']}")
            hay_disponibles = True
            
    if not hay_disponibles:
        print("No hay artículos disponibles para préstamo.")
        return
        
    id_solicitado = input("Ingrese el ID del ítem a prestar --> ").strip().upper()
    
    item_encontrado = None
    for item in funciones.inventario:
        if item['id'] == id_solicitado and item['disponible']:
            item_encontrado = item
            break
            
    if item_encontrado is None:
        print("ID incorrecto o el artículo ya está prestado.")
        return
        
    while True:
        try:
            dias_prestado = int(input(f"¿Por cuántos días se prestará? (Límite: {usuario_encontrado['tiempo_limite']}) --> "))
            if dias_prestado <= 0:
                print("Los días deben ser mayores a cero.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido.")
            
    nuevo_prestamo = {
        'usuario_doc': doc_usuario,
        'usuario_nombre': f"{usuario_encontrado['nombre']} {usuario_encontrado['apellido']}",
        'item_id': item_encontrado['id'],
        'item_nombre': item_encontrado['nombre'],
        'item_precio': item_encontrado['precio'],
        'dias_transcurridos': dias_prestado,
        'activo': True
    }
    
    item_encontrado['disponible'] = False
    funciones.prestamos.append(nuevo_prestamo)
    print(f"Préstamo registrado. El ítem {item_encontrado['nombre']} fue entregado.")

def registrar_devolucion():
    print("\nREGISTRAR DEVOLUCIÓN Y CERTIFICADO")
    doc_usuario = input("Ingrese el documento del usuario --> ").strip()
    
    prestamos_usuario = []
    for p in funciones.prestamos:
        if p['usuario_doc'] == doc_usuario and p['activo']:
            prestamos_usuario.append(p)
            
    if not prestamos_usuario:
        print("El usuario no tiene préstamos activos.")
        return
        
    print("Préstamos activos de este usuario:")
    for i, p in enumerate(prestamos_usuario):
        print(f"{i+1}. Ítem: {p['item_nombre']} (ID: {p['item_id']}) | Días acumulados: {p['dias_transcurridos']}")
        
    while True:
        try:
            opc = int(input("Seleccione el número del préstamo a devolver --> ")) - 1
            if 0 <= opc < len(prestamos_usuario):
                prestamo_sel = prestamos_usuario[opc]
                break
            print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")
            
    if prestamo_sel['dias_transcurridos'] > 30:
        print("Alerta: El préstamo superó los 30 días.")
        print("Generando factura de venta obligatoria por cobro de conchudez.")
        funciones.generar_factura_venta(prestamo_sel)
        return
        
    prestamo_sel['activo'] = False
    for item in funciones.inventario:
        if item['id'] == prestamo_sel['item_id']:
            item['disponible'] = True
            break
            
    nombre_archivo = f"Certificado_{prestamo_sel['usuario_doc']}_{prestamo_sel['item_id']}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("CERTIFICADO DE DEVOLUCIÓN - CREDIRIC\n")
        archivo.write(f"Prestador: {prestamo_sel['usuario_nombre']}\n")
        archivo.write(f"Documento: {prestamo_sel['usuario_doc']}\n")
        archivo.write(f"Artículo: {prestamo_sel['item_nombre']}\n")
        archivo.write(f"ID Artículo: {prestamo_sel['item_id']}\n")
        archivo.write(f"Días utilizados: {prestamo_sel['dias_transcurridos']}\n")
        archivo.write("Estado: Devuelto a tiempo.\n")
        
    print(f"Devolución procesada. Archivo plano generado: {nombre_archivo}")

def consultar_items_mas_30_dias():
    print("\nÍTEMS CON MÁS DE 30 DÍAS DE PRÉSTAMO")
    conteo = 0
    for p in funciones.prestamos:
        if p['activo'] and p['dias_transcurridos'] > 30:
            print(f"Alerta: Amigo: {p['usuario_nombre']} | Ítem: {p['item_nombre']} | Días: {p['dias_transcurridos']}")
            conteo += 1
    if conteo == 0:
        print("No se registran artículos que superen los 30 días.")

def consultar_articulos_prestados():
    print("\nLISTADO GENERAL DE ARTÍCULOS PRESTADOS")
    
    prestamos_activos = [p for p in funciones.prestamos if p['activo']]
    
    # Algoritmo de ordenamiento de burbuja simple
    for i in range(len(prestamos_activos)):
        for j in range(0, len(prestamos_activos) - i - 1):
            if prestamos_activos[j]['dias_transcurridos'] < prestamos_activos[j+1]['dias_transcurridos']:
                prestamos_activos[j], prestamos_activos[j+1] = prestamos_activos[j+1], prestamos_activos[j]
                
    if not prestamos_activos:
        print("No hay artículos prestados actualmente.")
        return
        
    with open("reporte_prestamos.txt", "w", encoding="utf-8") as arch:
        arch.write("REPORTE GENERAL DE PRÉSTAMOS ACTIVOS\n")
        for p in prestamos_activos:
            linea = f"Días: {p['dias_transcurridos']} -> Ítem: {p['item_nombre']} ({p['item_id']}) | Amigo: {p['usuario_nombre']}\n"
            print(linea.strip())
            arch.write(linea)
            
    print("\nInformación exportada a reporte_prestamos.txt")

def modulo_administrador():
    print("\nACCESO RESTRINGIDO ADMINISTRADOR")
    usuario = input("Usuario --> ").strip()
    contrasena = input("Contraseña --> ").strip()
    
    if usuario == funciones.USUARIO_ADMIN and contrasena == funciones.CONTRASENA_ADMIN:
        print("Acceso concedido.")
        while True:
            print("\nSUBMENÚ ADMINISTRADOR")
            print("1. Total de préstamos registrados")
            print("2. Total de ítems devueltos")
            print("3. Total de ventas realizadas y dinero recaudado")
            print("4. Lista completa de usuarios")
            print("5. Usuario con mayor y menor cantidad de préstamos")
            print("6. Volver al menú principal")
            
            opc_admin = input("Seleccione una opción --> ").strip()
            
            if opc_admin == "1":
                print(f"Total préstamos históricos: {len(funciones.prestamos)}")
            elif opc_admin == "2":
                devueltos = len([p for p in funciones.prestamos if not p['activo'] and 'tipo_cierre' not in p])
                print(f"Total ítems devueltos: {devueltos}")
            elif opc_admin == "3":
                ventas = [p for p in funciones.prestamos if 'tipo_cierre' in p and p['tipo_cierre'] == 'Venta']
                total_dinero = sum([v['total_pago'] for v in ventas])
                print(f"Total ventas forzadas: {len(ventas)}")
                print(f"Dinero recaudado: ${total_dinero:.2f}")
            elif opc_admin == "4":
                print("LISTA DE USUARIOS:")
                for u in funciones.usuarios:
                    print(f"Doc: {u['documento']} | {u['nombre']} {u['apellido']}")
            elif opc_admin == "5":
                funciones.calcular_mayor_menor_prestador()
            elif opc_admin == "6":
                break
            else:
                print("Opción inválida.")
    else:
        print("Acceso denegado.")

def menu_principal():
    while True:
        print("\nBIENVENIDO A CREDIRIC")
        print("1. Registrar Usuario")
        print("2. Registrar Artículo en Inventario")
        print("3. Registrar Préstamo")
        print("4. Registrar Devolución")
        print("5. Consultar Ítems con más de 30 días")
        print("6. Consultar Artículos Prestados")
        print("7. Administrador")
        print("8. Salir")
        
        opcion = input("Seleccione una opción (1-8) --> ").strip()
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_item()
        elif opcion == "3":
            registrar_prestamo()
        elif opcion == "4":
            registrar_devolucion()
        elif opcion == "5":
            consultar_items_mas_30_dias()
        elif opcion == "6":
            consultar_articulos_prestados()
        elif opcion == "7":
            modulo_administrador()
        elif opcion == "8":
            funciones.exportar_a_csv()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
