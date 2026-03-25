![Imagen del proyecto](https://raw.githubusercontent.com/isabellamarulanda/CrediRIC/refs/heads/main/img/Imagen%20crediRIC.jpeg)
# CrediRIC
El proyecto desarrolla un software en Python para gestionar préstamos de artículos, registrando usuarios y operaciones de préstamo/retorno. Usa clases y menú en consola, y genera facturas si no se devuelve en 30 días. Incluye exportación a CSV y trabajo colaborativo en grupos con actas y seguimiento.
 # *Integrantes*
 ## **Raquel Morillo Caicedo**
> Estoy en el programa de Ingenieria Industrial, dentro de mis habilidades y fortalezas estan la creatividad y pensamiento visual, mis ganas de aprender que van de la mano con querer mejorar constamente, y tambien me considero una persona muy organizada que tiene claridad en sus objetivos teniendo a su vez responsabilidad y empatia. 
## **Maria Camila Osorio Tuberquia**
> Soy una persona resiliente, adaptable y con pensamiento crítico, capaz de gestionar mi tiempo de manera efectiva y mantener una actitud positiva ante los retos. Pertenezco al programa de Ingeniería Industrial y me caracterizo por mi responsabilidad, compromiso y disciplina, actuando siempre con determinación y apertura al aprendizaje continuo.
## **Isabella Marulanda Uribe**
> Estoy en el programa de Ingeniería Industrial. Dentro de mis habilidades y fortalezas se destacan mi creatividad y capacidad para resolver problemas, así como mi facilidad para trabajar en equipo. Me considero una persona organizada, responsable y con muchas ganas de aprender y mejorar constantemente, siempre buscando cumplir mis objetivos con compromiso y buena actitud.

## 📌 **Descripción del Proyecto**

**CrediRIC** es una solución tecnológica desarrollada en Python, diseñada para resolver la pérdida de control sobre préstamos personales.  

El software funciona como un sistema de gestión integral que permite:

- Registrar amigos (clientes)  
- Inventariar objetos de diversas categorías y dinero  
- Realizar un seguimiento riguroso de las fechas de entrega  

El sistema opera mediante una interfaz de consola amigable y utiliza archivos planos para garantizar que la información sea persistente y exportable a formatos como CSV.

## 🎯 Objetivos

- **Gestión Centralizada:**  
  Crear un programa de consola que permita administrar el flujo completo de préstamos y devoluciones de artículos y dinero.

- **Control de Tiempos:**  
  Implementar alertas automáticas para solicitar devoluciones después de 20 días y procesar ventas obligatorias tras 30 días de mora.

- **Formalización de Procesos:**  
  Generar documentos técnicos (certificados de devolución y facturas de venta) que den soporte legal y administrativo a cada transacción.

- **Seguridad y Reportes:**  
  Proveer un módulo de administrador protegido por contraseña para visualizar estadísticas críticas como el total de ventas, pagos realizados y comportamiento de los usuarios.

  ## ✅ Beneficios

- **Eliminación del Olvido:**  
  Resuelve el problema de la "memoria de pollo" al mantener un registro exacto de qué se prestó, a quién y en qué fecha.

- **Protección del Patrimonio:**  
  Asegura que el dueño no pierda dinero; si un objeto no regresa en un mes, el sistema genera una factura por el valor de adquisición más un 23% de "impuesto por conchudez".

- **Organización del Inventario:**  
  Clasifica los bienes en categorías específicas (Videojuegos, Herramientas, Dinero, etc.), asignando identificadores únicos para una búsqueda rápida.

- **Transparencia:**  
  Al generar certificados de devolución y reportes de estado, tanto el prestamista como el deudor tienen claridad sobre sus compromisos activos.

## 📋 Requisitos

### 🔹 Requisitos Funcionales (RF)

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

### 🔸 Requisitos No Funcionales (RNF)

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

# Licencia
<a href="https://github.com/isabellamarulanda/CrediRIC">CrediRIC</a> © 2026 by <a href="https://github.com/isabellamarulanda">Isabella Marulanda Uribe</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
