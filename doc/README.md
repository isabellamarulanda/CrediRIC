# **Manual de Usuario**
Bienvenido al manual oficial de *CrediRic*, la solución por consola desarrollada en Python para el control de inventarios, registro de amigos y gestión estricta de préstamos personales de MJ.

Opción 1: Registrar Usuario (registrar_usuario)
Qué hace el algoritmo: Solicita y valida los datos de un nuevo prestatario antes de agregarlo a la lista en memoria.

Flujo de datos:

Ingrese el Nombre y presione Enter. El algoritmo usa un ciclo interno para verificar que tenga al menos 3 caracteres y no contenga números utilizando métodos de cadena.

Ingrese el Apellido (mismas validaciones lógicas).

Ingrese el Documento. El algoritmo recorre la lista existente para verificar que no esté repetido y que contenga únicamente caracteres numéricos.

Ingrese el Correo Electrónico. Se valida la estructura mediante condicionales que exigen la presencia del símbolo @ y la terminación .com.

Seleccione el límite de días permitidos ingresando el número exacto (5, 10, 15 o 30).

Opción 2: Registrar Artículo en Inventario (registrar_item)
Qué hace el algoritmo: Añade un objeto al inventario global y le calcula un identificador alfanumérico único.

Flujo de datos:

Ingrese el nombre del artículo.

El algoritmo mostrará una lista de categorías del 1 al 6. Digite el número asignado a la categoría del artículo. El sistema tomará las primeras tres letras en mayúsculas de esa categoría y le sumará un consecutivo para crear el ID único (Ej: VID-101).

Ingrese el valor de adquisición del objeto (el algoritmo valida mediante control de excepciones que sea un número mayor a cero).

Seleccione el estado físico según las opciones planteadas (Excelente, Bueno, Regular), mapeando el valor a los niveles correspondientes de lógica difusa.

Opción 3: Registrar Préstamo (registrar_prestamo)
Qué hace el algoritmo: Modifica la disponibilidad de un artículo y genera un registro de control de salida enlazado a un usuario.

Flujo de datos:

El algoritmo solicita el documento del amigo. Realiza una búsqueda secuencial; si no lo encuentra, interrumpe el proceso indicando que el usuario no existe.

Muestra en pantalla solo los artículos cuyo estado lógico de disponibilidad sea True.

Solicite el ID único del artículo deseado. Al procesarse, el algoritmo cambia automáticamente el estado del ítem a ocupado (False).

Opción 4: Registrar Devolución (registrar_devolucion)
Qué hace el algoritmo: Evalúa los tiempos de entrega. Determina si el artículo se reincorpora al inventario o si se ejecuta la lógica de penalización financiera por exceso de tiempo.

Flujo de datos:

Ingrese el documento del usuario para listar sus préstamos vigentes.

Seleccione el número de índice del préstamo a cerrar.

Cálculo de Condición: * Si días transcurridos <= 30: El algoritmo marca el préstamo como inactivo, vuelve a poner el artículo disponible en el inventario y genera un archivo de texto plano (Certificado_...txt) con el reporte de éxito.

Si días transcurridos > 30: El algoritmo activa la Venta Obligatoria. Toma el precio original del artículo, le aplica una multiplicación matemática para sumarle el 23% de impuesto por conchudez, bloquea el artículo para que no regrese al inventario y exporta una factura legal en formato .txt.

Opción 5: Consultar Ítems con más de 30 días (consultar_items_mas_30_dias)
Qué hace el algoritmo: Filtra de forma inmediata la lista de préstamos activos e imprime alertas directas en la pantalla de consola con los nombres y los artículos de las personas que han incumplido el tiempo estándar de devolución.

Opción 6: Consultar Artículos Prestados (consultar_articulos_prestados)
Qué hace el algoritmo: Procesa la información de préstamos mediante un método de ordenamiento y genera un reporte físico.

Funcionamiento interno: Aplica el Algoritmo de Ordenamiento de Burbuja para organizar los registros vigentes de mayor a menor tiempo de retraso. Adicionalmente, escribe de forma secuencial estas líneas en un archivo plano llamado reporte_prestamos.txt.

Opción 7: Administrador (modulo_administrador)
Qué hace el algoritmo: Ofrece un submenú restringido de analítica matemática.

Flujo de datos:

Solicita credenciales. Si el usuario ingresado coincide con admin y la contraseña con admin123, permite el ingreso.

Ejecuta contadores globales y acumuladores de sumas numéricas para desplegar en pantalla: préstamos totales, devoluciones, dinero histórico recaudado por las ventas forzadas y cálculos manuales de máximos y mínimos para hallar al amigo con mayor y menor cantidad de préstamos.

Opción 8: Salir (exportar_a_csv)
Qué hace el algoritmo: Ejecuta el volcado y la persistencia final de los datos antes de cerrar el programa.

Efecto operativo: Transforma las estructuras de listas de diccionarios internas de la memoria en archivos físicos delimitados por punto y coma (;), generando los documentos CrediRic_Usuarios.csv y CrediRic_Prestamos.csv. Acto seguido, utiliza la instrucción break para romper el ciclo principal y terminar la ejecución del script de Python de manera limpia.

