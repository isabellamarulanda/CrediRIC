![imagen del proyecto](Img/imagenproyecto.jpeg)
# CrediRIC 📊
El proyecto desarrolla un software en Python para gestionar préstamos de artículos, registrando usuarios y operaciones de préstamo/retorno. Usa clases y menú en consola, y genera facturas si no se devuelve en 30 días. Incluye exportación a CSV y trabajo colaborativo en grupos con actas y seguimiento.
 # *Integrantes*
 ## **Raquel Morillo Caicedo** 
> Estoy en el programa de Ingenieria Industrial, dentro de mis habilidades y fortalezas estan la creatividad y pensamiento visual, mis ganas de aprender que van de la mano con querer mejorar constamente, y tambien me considero una persona muy organizada que tiene claridad en sus objetivos teniendo a su vez responsabilidad y empatia. 
## **Isabella Marulanda Uribe**
> Estoy en el programa de Ingeniería Industrial. Dentro de mis habilidades y fortalezas se destacan mi creatividad y capacidad para resolver problemas, así como mi facilidad para trabajar en equipo. Me considero una persona organizada, responsable y con muchas ganas de aprender y mejorar constantemente, siempre buscando cumplir mis objetivos con compromiso y buena actitud.

## **Descripción del Proyecto** 

**CrediRIC** es una solución tecnológica desarrollada en Python, diseñada para resolver la pérdida de control sobre préstamos personales. 

El software funciona como un sistema de gestión integral que permite:

- Registrar amigos (clientes)  
- Inventariar objetos de diversas categorías y dinero  
- Realizar un seguimiento riguroso de las fechas de entrega  

El sistema opera mediante una interfaz de consola amigable y utiliza archivos planos para garantizar que la información sea persistente y exportable a formatos como CSV.

##  Objetivos

- **Gestión Centralizada:**  
  Crear un programa de consola que permita administrar el flujo completo de préstamos y devoluciones de artículos y dinero.

- **Control de Tiempos:**  
  Implementar alertas automáticas para solicitar devoluciones después de 20 días y procesar ventas obligatorias tras 30 días de mora.

- **Formalización de Procesos:**  
  Generar documentos técnicos (certificados de devolución y facturas de venta) que den soporte legal y administrativo a cada transacción.

- **Seguridad y Reportes:**  
  Proveer un módulo de administrador protegido por contraseña para visualizar estadísticas críticas como el total de ventas, pagos realizados y comportamiento de los usuarios.

##  Beneficios

- **Eliminación del Olvido:**  
  Resuelve el problema de la "memoria de pollo" al mantener un registro exacto de qué se prestó, a quién y en qué fecha.

- **Protección del Patrimonio:**  
  Asegura que el dueño no pierda dinero; si un objeto no regresa en un mes, el sistema genera una factura por el valor de adquisición más un 23% de "impuesto por conchudez".

- **Organización del Inventario:**  
  Clasifica los bienes en categorías específicas (Videojuegos, Herramientas, Dinero, etc.), asignando identificadores únicos para una búsqueda rápida.

- **Transparencia:**  
  Al generar certificados de devolución y reportes de estado, tanto el prestamista como el deudor tienen claridad sobre sus compromisos activos.

##  Requisitos

### ✔️ Requisitos Funcionales (RF)

Los requisitos funcionales definen las acciones y comportamientos que CrediRIC debe ejecutar para satisfacer al usuario:

- **RF01 - Gestión de Usuarios:**  
  El sistema debe permitir registrar amigos con nombre (mínimo 3 letras, sin números), apellido (mínimo 3 letras, sin números), documento (3-15 dígitos numéricos) y correo electrónico válido (con "@", "." y "com").

- **RF02 - Definición de Tiempos:**  
  Al crear un usuario, se debe asignar un tiempo de préstamo permitido de 5, 10, 15 o 30 días únicamente.

- **RF03 - Registro de Inventario:**  
  El sistema debe permitir registrar ítems categorizados en: Videojuegos, Libros, Música/Video, Herramientas, Dinero o Misceláneo.

- **RF04 - Identificación Única:**  
  Cada ítem debe poseer un ID único alfanumérico asociado a su categoría y registrar su precio de compra original.

- **RF05 - Valoración del Estado:**  
  Se debe registrar el estado físico del objeto utilizando lógica difusa para determinar su calidad.

- **RF06 - Control de Préstamos:**  
  Solo se pueden realizar préstamos a usuarios previamente registrados en la plataforma.

- **RF07 - Certificación de Devolución:**  
  Si la devolución es exitosa y a tiempo, el sistema generará un archivo de texto plano con el nombre del prestador, fecha e ID.

- **RF08 - Generación de Facturas (Venta):**  
  Para ítems con más de 30 días de préstamo, el sistema debe generar automáticamente una factura de venta que incluya el precio base más un 23% de impuesto.

- **RF09 - Módulo Administrativo:**  
  Debe existir un submenú protegido por usuario y contraseña que muestre reportes de ventas, préstamos totales y estadísticas de usuarios.

### ✔️ Requisitos No Funcionales (RNF)

Estos especifican criterios sobre la operación y calidad del sistema más allá de su comportamiento específico:

- **RNF01 - Usabilidad:**  
  El programa debe contar con un menú amigable basado en consola para facilitar la navegación del usuario.

- **RNF02 - Persistencia de Datos:**  
  Toda la información debe ser gestionada mediante archivos planos y ser capaz de exportarse a formato CSV usando Python.

- **RNF03 - Lenguaje de Desarrollo:**  
  El software debe estar escrito estrictamente en el lenguaje de programación Python.

- **RNF04 - Gestión de Versiones:**  
  El código debe estar alojado en un repositorio de GitHub bajo una estructura de carpetas específica (src para código y doc para manuales).

- **RNF05 - Seguridad:**  
  El acceso a los reportes sensibles (Administrador) debe estar restringido mediante validación de credenciales almacenadas en una lista.

##  Descripcion de Actividades

Para el desarrollo de **CrediRIC**, el equipo ha definido un conjunto de actividades críticas divididas en fases, asegurando el cumplimiento de los entregables en el repositorio de GitHub:

### ✔️ Fase 1: Formalización y Alianzas (Semanas 3-4)

- **Elaboración de Actas de Entendimiento y Compromiso:**  
  Reunión inicial para definir las expectativas de cada miembro y los objetivos comunes del proyecto.

- **Definición de Protocolos de Colaboración:**  
  Redacción del acta que especifica la metodología de trabajo, canales de comunicación y mecanismos para la resolución de conflictos.

- **Asignación de Responsabilidades:**  
  Creación del acta de responsabilidad donde se delegan tareas específicas y se establecen los plazos de entrega internos.

### ✔️ Fase 2: Ingeniería de Requisitos y Diseño (Semanas 5-8)

- **Entrevista con el Product Owner (PO):**  
  Sesión de recolección de requisitos con el docente para entender las necesidades de gestión de préstamos.

- **Redacción del Reporte de Visión:**  
  Descripción general del software CrediRIC, detallando sus beneficios y objetivos principales.

- **Especificación de Requisitos:**  
  Definición técnica de los requisitos funcionales (como validaciones de nombre y cálculos de impuestos) y no funcionales (seguridad y persistencia en archivos planos).

- **Planificación y Presupuesto:**  
  Elaboración del cronograma y cálculo del presupuesto basado en 50 horas de práctica profesional.

### ✔️ Fase 3: Desarrollo del Algoritmo (Semanas 9-14)

- **Configuración del Entorno (Carpeta `src`):**  
  Inicialización del repositorio en GitHub utilizando credenciales institucionales.

- **Implementación de Módulos Core:**  
  Programación en Python de las funciones de registro de usuarios, inventario de ítems y lógica de préstamos.

- **Lógica de Negocio y Automatización:**  
  Desarrollo del sistema de alertas para préstamos mayores a 20 días y el motor de facturación automática para ventas tras 30 días, incluyendo el impuesto del 23%.

- **Módulo de Administración:**  
  Programación del acceso restringido para la consulta de estadísticas generales y reportes financieros.
  
### ✔️ Fase 4: Documentación y Cierre (Semanas 15-16)

- **Creación del Manual de Usuario (Carpeta `doc`):**  
  Redacción de instrucciones detalladas para el uso del sistema.

- **Plan de Versionado Final:**  
  Documentación del historial de versiones y avances del software.

- **Sustentación y Entrega:**  
  Presentación del software ante el docente, incluyendo explicación técnica del funcionamiento.

## **Plan del proyecto**
##  **Cronograma**

| Fase | Actividad Principal     | Sem 3-4  | Sem 5-6 | Sem 8 | Sem 9-10 | Sem 11-12 | Sem 13-14 | Sem 15 | Sem 16 
|------|-------------------------|----------|---------|-------|----------|-----------|-----------|--------|--------|
| Fase 1: Definición | Actas           | ████ |        |      |          |           |           |        |        |
| Fase 2: Requisitos | Product Owner   |      | ████   |      |          |           |           |        |        |
| Fase 3: Diseño     | Plan proyecto   |      |        | ████ |          |           |           |        |        |
| Fase 4: Desarrollo | Programación    |      |        |      | ████     | ████      | ████      |        |        |
| Fase 5: Documenta  | Manual usuario  |      |        |      |          |           |           | ████   |        |
| Fase 6: Cierre     | Sustentación    |      |        |      |          |           |           |        | ████   |

##  **Presupuesto**

El presupuesto del proyecto **CrediRIC** se calcula con base en una dedicación parcial durante el desarrollo.

###  Detalle del Cálculo

|  Concepto              |       Valor     |
|--------------------------|---------------|
|  Horas semanales       | 5 horas       |
|  Semanas por mes       | 4             |
|  Duración del proyecto | 3,5 meses     |
|  **Total de horas**    | **70 horas**  |
|  Valor por hora        | $10.943       |

|  Operación             | Resultado   |
|--------------------------|--------------|
| 5 × 4 × 3,5              | 70 horas     |
| 70 × $10.943             | $766.010     |

###  Presupuesto Total

# 💰 **$766.010 COP**
- Este valor representa el costo estimado del desarrollo del proyecto, considerando la dedicación parcial durante el tiempo establecido.
## **Plan de versionado**
El plan de versionado describe la evolución técnica del código fuente del software *CrediRic*:

| Versión | Día del Proyecto | Semana Académica | Procedimiento Relevante / Hito de Desarrollo |
| :---: | :---: | :---: | :--- |
| *v0.1* | Día 1 | Semana 3 | *Inicialización del Repositorio:* Creación de la estructura del proyecto en GitHub con la carpeta obligatoria src. Configuración del archivo base de Python. |
| *v0.2* | Día 14 | Semana 5 | *Estructura de Datos Base:* Definición de los diccionarios y listas en memoria (usuarios, inventario, prestamos) para simular la persistencia temporal. |
| *v0.3* | Día 28 | Semana 7 | *Módulo de Usuarios:* Implementación de la función registrar_usuario() y sus validaciones estrictas (nombres sin números, documento numérico, correo con @ y .com). |
| *v0.4* | Día 42 | Semana 9 | *Módulo de Inventario:* Codificación de la función registrar_item(), asignación del menú de categorías y lógica para generar códigos ID automáticos (ej. VID-101). |
| *v0.5* | Día 56 | Semana 11 | *Módulo de Control de Préstamos:* Programación de la función registrar_prestamo() con validación cruzada (verificar si el amigo existe y si el artículo está disponible). |
| *v0.6* | Día 70 | Semana 13 | *Lógica de Devolución y Conchudez:* Creación de registrar_devolucion(). Integración del condicional para detectar más de 30 días, cálculo del *23% de impuesto* y generación de facturas .txt. |
| *v0.7* | Día 77 | Semana 14 | *Algoritmo de Ordenamiento:* Incorporación del algoritmo de ordenamiento por el *Método Burbuja* para listar los préstamos activos de mayor a menor tiempo transcurrido. |
| *v0.8* | Día 84 | Semana 15 | *Módulo de Administración:* Creación del submenú protegido por contraseña (admin / admin123) y funciones de cálculo matemático para las estadísticas e históricos. |
| *v0.9* | Día 91 | Semana 16 | *Persistencia Final y Limpieza:* Implementación de la función exportar_a_csv() al salir del programa. Ajuste de la interfaz visual con flechas --> limpias según el estilo del docente. |
| *v1.0* | Día 95 | Semana 16 | *Versión de Producción:* Pruebas finales de caja negra libres de errores. Creación de la carpeta doc en GitHub con el Manual de Usuario definitivo. |
| *v1.1* | Día 98 | Semana 16 | *Cierre del Proyecto:* Congelamiento del código en GitHub listo para la sustentación presencial de 5 minutos ante el profesor Julián Andrés Castillo. |

# ** Codigo***
import os

# BASES DE DATOS EN MEMORIA (LISTAS DE DICCIONARIOS)
usuarios = []
inventario = []
prestamos = []

# Datos del Administrador
CONTRASENA_ADMIN = "admin123"
USUARIO_ADMIN = "admin"

# FUNCIONES DE VALIDACIÓN
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

# FUNCIONES DEL MENÚ PRINCIPAL
def registrar_usuario():
    print("\nREGISTRAR NUEVO USUARIO")

    while True:
        nombre = input("Ingrese el Nombre --> ").strip()
        if validar_nombre_apellido(nombre):
            break
        print("Error: El nombre debe tener al menos 3 letras y no contener números.")

    while True:
        apellido = input("Ingrese el Apellido --> ").strip()
        if validar_nombre_apellido(apellido):
            break
        print("Error: El apellido debe tener al menos 3 letras y no contener números.")

    while True:
        documento = input("Ingrese el Documento --> ").strip()
        existe = False
        for u in usuarios:
            if u['documento'] == documento:
                existe = True
        if existe:
            print("Error: Este documento ya se encuentra registrado.")
            continue
        if validar_documento(documento):
            break
        print("Error: El documento debe ser numérico y tener entre 3 and 15 dígitos.")

    while True:
        correo = input("Ingrese el Correo Electrónico --> ").strip()
        if validar_correo(correo):
            break
        print("Error: Correo inválido. Debe contener '@' y terminar en '.com'.")

    while True:
        try:
            tiempo = int(input("Ingrese tiempo de préstamo permitido (5, 10, 15, 30) --> "))
            if validar_tiempo_prestamo(tiempo):
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
    usuarios.append(nuevo_usuario)
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
            categoria_seleccionada = categorias[opc_cat]
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
    id_item = f"{prefijo}-{len(inventario) + 101}"

    nuevo_item = {
        'id': id_item,
        'nombre': nombre_item,
        'categoria': categoria_seleccionada,
        'precio': precio,
        'estado': estado,
        'disponible': True
    }
    inventario.append(nuevo_item)
    print(f"Artículo registrado correctamente. ID Asignado: {id_item}")

def registrar_prestamo():
    print("\nREGISTRAR PRÉSTAMO")
    if not usuarios:
        print("No hay usuarios registrados en el sistema.")
        return
    if not inventario:
        print("El inventario se encuentra vacío.")
        return

    doc_usuario = input("Ingrese el documento del amigo --> ").strip()

    usuario_encontrado = None
    for u in usuarios:
        if u['documento'] == doc_usuario:
            usuario_encontrado = u
            break

    if usuario_encontrado is None:
        print("El usuario no existe. Debe registrar al nuevo amigo primero.")
        return

    print("ARTÍCULOS DISPONIBLES")
    hay_disponibles = False
    for item in inventario:
        if item['disponible']:
            print(f"ID: {item['id']} | Nombre: {item['nombre']} | Categoría: {item['categoria']}")
            hay_disponibles = True

    if not hay_disponibles:
        print("No hay artículos disponibles para préstamo.")
        return

    id_solicitado = input("Ingrese el ID del ítem a prestar --> ").strip().upper()

    item_encontrado = None
    for item in inventario:
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
    prestamos.append(nuevo_prestamo)
    print(f"Préstamo registrado. El ítem {item_encontrado['nombre']} fue entregado.")

def registrar_devolucion():
    print("\nREGISTRAR DEVOLUCIÓN Y CERTIFICADO")
    doc_usuario = input("Ingrese el documento del usuario --> ").strip()

    prestamos_usuario = []
    for p in prestamos:
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
        generar_factura_venta(prestamo_sel)
        return

    prestamo_sel['activo'] = False
    for item in inventario:
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

def consultar_items_mas_30_dias():
    print("\nÍTEMS CON MÁS DE 30 DÍAS DE PRÉSTAMO")
    conteo = 0
    for p in prestamos:
        if p['activo'] and p['dias_transcurridos'] > 30:
            print(f"Alerta: Amigo: {p['usuario_nombre']} | Ítem: {p['item_nombre']} | Días: {p['dias_transcurridos']}")
            conteo += 1
    if conteo == 0:
        print("No se registran artículos que superen los 30 días.")

def consultar_articulos_prestados():
    print("\nLISTADO GENERAL DE ARTÍCULOS PRESTADOS")

    prestamos_activos = [p for p in prestamos if p['activo']]

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

# MÓDULO ADMINISTRADOR
def modulo_administrador():
    print("\nACCESO RESTRINGIDO ADMINISTRADOR")
    usuario = input("Usuario --> ").strip()
    contrasena = input("Contraseña --> ").strip()

    if usuario == USUARIO_ADMIN and contrasena == CONTRASENA_ADMIN:
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
                print(f"Total préstamos históricos: {len(prestamos)}")
            elif opc_admin == "2":
                devueltos = len([p for p in prestamos if not p['activo'] and 'tipo_cierre' not in p])
                print(f"Total ítems devueltos: {devueltos}")
            elif opc_admin == "3":
                ventas = [p for p in prestamos if 'tipo_cierre' in p and p['tipo_cierre'] == 'Venta']
                total_dinero = sum([v['total_pago'] for v in ventas])
                print(f"Total ventas forzadas: {len(ventas)}")
                print(f"Dinero recaudado: ${total_dinero:.2f}")
            elif opc_admin == "4":
                print("LISTA DE USUARIOS:")
                for u in usuarios:
                    print(f"Doc: {u['documento']} | {u['nombre']} {u['apellido']}")
            elif opc_admin == "5":
                calcular_mayor_menor_prestador()
            elif opc_admin == "6":
                break
            else:
                print("Opción inválida.")
    else:
        print("Acceso denegado.")

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

# EXPORTACIÓN FINAL A CSV
def exportar_a_csv():
    with open("CrediRic_Usuarios.csv", "w", encoding="utf-8") as f:
        f.write("Documento;Nombre;Apellido;Correo;Tiempo_Limite\n")
        for u in usuarios:
            f.write(f"{u['documento']};{u['nombre']};{u['apellido']};{u['correo']};{u['tiempo_limite']}\n")

    with open("CrediRic_Prestamos.csv", "w", encoding="utf-8") as f:
        f.write("Usuario_Doc;Usuario_Nombre;Item_ID;Item_Nombre;Dias;Activo\n")
        for p in prestamos:
            f.write(f"{p['usuario_doc']};{p['usuario_nombre']};{p['item_id']};{p['item_nombre']};{p['dias_transcurridos']};{p['activo']}\n")

# MENÚ PRINCIPAL
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
            exportar_a_csv()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()

# Licencia
<a href="https://github.com/isabellamarulanda/CrediRIC">CrediRIC</a> © 2026 by <a href="https://github.com/isabellamarulanda">Isabella Marulanda Uribe</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
