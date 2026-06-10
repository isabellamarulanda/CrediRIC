# BASES DE DATOS EN MEMORIA (LISTAS DE DICCIONARIOS)
usuarios = []
inventario = []
prestamos = []

# Datos del Administrador
CONTRASENA_ADMIN = "admin123"
USUARIO_ADMIN = "admin"

# FUNCIONES DE VALIDACIÓN
# ==========================================
def validar_nombre_apellido(texto):
    if len(texto) < 3:
        return False
    for caracter in texto:
        if caracter.isdigit():
            return False
    return True

def validar_documento(doc):
    if len(doc) < 3 or len(doc) > 15:
        return False
    if not doc.isdigit():
        return False
    return True

def validar_correo(correo):
    if "@" in correo and correo.endswith(".com"):
        return True
    return False

def validar_tiempo_prestamo(tiempo):
    if tiempo in [5, 10, 15, 30]:
        return True
    return False

# ==========================================
# FUNCIONES OPERATIVAS
# ==========================================
def generar_factura_venta(prestamo_sel):
    subtotal = prestamo_sel['item_precio']
    impuesto_conchudez = subtotal * 0.23
    total = subtotal + impuesto_conchudez
    
    prestamo_sel['activo'] = False
    
    nombre_factura = f"Factura_Venta_{prestamo_sel['usuario_doc']}_{prestamo_sel['item_id']}.txt"
    with open(nombre_factura, "w", encoding="utf-8") as archivo:
        archivo.write("FACTURA DE VENTA - CREDIRIC\n")
        archivo.write(f"Cliente: {prestamo_sel['usuario_nombre']}\n")
        archivo.write(f"Documento: {prestamo_sel['usuario_doc']}\n")
        archivo.write(f"Artículo: {prestamo_sel['item_nombre']}\n")
        archivo.write(f"ID Artículo: {prestamo_sel['item_id']}\n")
        archivo.write("Motivo: Superó los 30 días permitidos.\n")
        archivo.write(f"Subtotal: ${subtotal:.2f}\n")
        archivo.write(f"Impuesto por Conchudez (23%): ${impuesto_conchudez:.2f}\n")
        archivo.write(f"TOTAL RECAUDADO: ${total:.2f}\n")
        
    prestamo_sel['tipo_cierre'] = 'Venta'
    prestamo_sel['total_pago'] = total
    print(f"Factura de venta generada en archivo plano: {nombre_factura}")

def calcular_mayor_menor_prestador():
    if not usuarios or not prestamos:
        print("Datos insuficientes para estadísticas.")
        return
        
    conteo = {}
    for u in usuarios:
        conteo[u['documento']] = 0
    for p in prestamos:
        if p['usuario_doc'] in conteo:
            conteo[p['usuario_doc']] += 1
            
    max_doc = min_doc = usuarios[0]['documento']
    max_cant = min_cant = conteo[max_doc]
    
    for doc, cant in conteo.items():
        if cant > max_cant:
            max_cant = cant
            max_doc = doc
        if cant < min_cant:
            min_cant = cant
            min_doc = doc
            
    nombre_max = nombre_min = ""
    for u in usuarios:
        if u['documento'] == max_doc:
            nombre_max = f"{u['nombre']} {u['apellido']}"
        if u['documento'] == min_doc:
            nombre_min = f"{u['nombre']} {u['apellido']}"
            
    print(f"Mayor cantidad de préstamos: {nombre_max} ({max_cant})")
    print(f"Menor cantidad de préstamos: {nombre_min} ({min_cant})")

def exportar_a_csv():
    with open("CrediRic_Usuarios.csv", "w", encoding="utf-8") as f:
        f.write("Documento;Nombre;Apellido;Correo;Tiempo_Limite\n")
        for u in usuarios:
            f.write(f"{u['documento']};{u['nombre']};{u['apellido']};{u['correo']};{u['tiempo_limite']}\n")
            
    with open("CrediRic_Prestamos.csv", "w", encoding="utf-8") as f:
        f.write("Usuario_Doc;Usuario_Nombre;Item_ID;Item_Nombre;Dias;Activo\n")
        for p in prestamos:
            f.write(f"{p['usuario_doc']};{p['usuario_nombre']};{p['item_id']};{p['item_nombre']};{p['dias_transcurridos']};{p['activo']}\n")

