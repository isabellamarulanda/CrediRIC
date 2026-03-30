![imagen del proyecto](Img/imagenproyecto.jpeg)
# CrediRIC 📊💰💵
El proyecto desarrolla un software en Python para gestionar préstamos de artículos, registrando usuarios y operaciones de préstamo/retorno. Usa clases y menú en consola, y genera facturas si no se devuelve en 30 días. Incluye exportación a CSV y trabajo colaborativo en grupos con actas y seguimiento.
 # *Integrantes*
 ## **Raquel Morillo Caicedo** 
> Estoy en el programa de Ingenieria Industrial, dentro de mis habilidades y fortalezas estan la creatividad y pensamiento visual, mis ganas de aprender que van de la mano con querer mejorar constamente, y tambien me considero una persona muy organizada que tiene claridad en sus objetivos teniendo a su vez responsabilidad y empatia. 
## **Maria Camila Osorio Tuberquia**
> Soy una persona resiliente, adaptable y con pensamiento crítico, capaz de gestionar mi tiempo de manera efectiva y mantener una actitud positiva ante los retos. Pertenezco al programa de Ingeniería Industrial y me caracterizo por mi responsabilidad, compromiso y disciplina, actuando siempre con determinación y apertura al aprendizaje continuo.
## **Isabella Marulanda Uribe**
> Estoy en el programa de Ingeniería Industrial. Dentro de mis habilidades y fortalezas se destacan mi creatividad y capacidad para resolver problemas, así como mi facilidad para trabajar en equipo. Me considero una persona organizada, responsable y con muchas ganas de aprender y mejorar constantemente, siempre buscando cumplir mis objetivos con compromiso y buena actitud.

## 💡📚 **Descripción del Proyecto** 

**CrediRIC** es una solución tecnológica desarrollada en Python, diseñada para resolver la pérdida de control sobre préstamos personales. 

El software funciona como un sistema de gestión integral que permite:

- Registrar amigos (clientes)  
- Inventariar objetos de diversas categorías y dinero  
- Realizar un seguimiento riguroso de las fechas de entrega  

El sistema opera mediante una interfaz de consola amigable y utiliza archivos planos para garantizar que la información sea persistente y exportable a formatos como CSV.

## 🎯📈 Objetivos

- **Gestión Centralizada:**  
  Crear un programa de consola que permita administrar el flujo completo de préstamos y devoluciones de artículos y dinero.

- **Control de Tiempos:**  
  Implementar alertas automáticas para solicitar devoluciones después de 20 días y procesar ventas obligatorias tras 30 días de mora.

- **Formalización de Procesos:**  
  Generar documentos técnicos (certificados de devolución y facturas de venta) que den soporte legal y administrativo a cada transacción.

- **Seguridad y Reportes:**  
  Proveer un módulo de administrador protegido por contraseña para visualizar estadísticas críticas como el total de ventas, pagos realizados y comportamiento de los usuarios.

## 🌟🔥 Beneficios

- **Eliminación del Olvido:**  
  Resuelve el problema de la "memoria de pollo" al mantener un registro exacto de qué se prestó, a quién y en qué fecha.

- **Protección del Patrimonio:**  
  Asegura que el dueño no pierda dinero; si un objeto no regresa en un mes, el sistema genera una factura por el valor de adquisición más un 23% de "impuesto por conchudez".

- **Organización del Inventario:**  
  Clasifica los bienes en categorías específicas (Videojuegos, Herramientas, Dinero, etc.), asignando identificadores únicos para una búsqueda rápida.

- **Transparencia:**  
  Al generar certificados de devolución y reportes de estado, tanto el prestamista como el deudor tienen claridad sobre sus compromisos activos.

## 📋🚫 Requisitos

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

## 📝🔎 Descrpcion de Actividades

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

## 🧩📈 **Diagrama de Gantt**

| Fase | Actividad Principal     | Sem 3-4  | Sem 5-6 | Sem 8 | Sem 9-10 | Sem 11-12 | Sem 13-14 | Sem 15 | Sem 16 
|------|-------------------------|----------|---------|-------|----------|-----------|-----------|--------|--------|
| Fase 1: Definición | Actas           | ████ |        |      |          |           |           |        |        |
| Fase 2: Requisitos | Entrevista      |      | ████   |      |          |           |           |        |        |
| Fase 3: Diseño     | Plan proyecto   |      |        | ████ |          |           |           |        |        |
| Fase 4: Desarrollo | Programación    |      |        |      | ████     | ████      | ████      |        |        |
| Fase 5: Documenta  | Manual usuario  |      |        |      |          |           |           | ████   |        |
| Fase 6: Cierre     | Sustentación    |      |        |      |          |           |           |        | ████   |

## 🪙🧾 **Presupuesto**

El presupuesto del proyecto **CrediRIC** se calcula con base en una dedicación parcial durante el desarrollo.

### 📊 Detalle del Cálculo

|  Concepto              |       Valor     |
|--------------------------|---------------|
| 🕒 Horas semanales       | 5 horas       |
| 📅 Semanas por mes       | 4             |
| ⏳ Duración del proyecto | 3,5 meses     |
| 🌟 **Total de horas**    | **70 horas**  |
| 💵 Valor por hora        | $10.943       |

### 🧮 Cálculo Final

| ✨ Operación             | Resultado   |
|--------------------------|--------------|
| 5 × 4 × 3,5              | 70 horas     |
| 70 × $10.943             | $766.010     |

### ✨ Presupuesto Total

# 💰 **$766.010 COP**
- Este valor representa el costo estimado del desarrollo del proyecto, considerando la dedicación parcial durante el tiempo establecido.

# Licencia
<a href="https://github.com/isabellamarulanda/CrediRIC">CrediRIC</a> © 2026 by <a href="https://github.com/isabellamarulanda">Isabella Marulanda Uribe</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
