# Ejercicio 1: Función con parámetros posicionales obligatorios
def calcular_promedio(nota1, nota2, nota3):
    """
    Calcula el promedio de tres notas.
    Todos los parámetros son posicionales obligatorios.
    """
    return (nota1 + nota2 + nota3) / 3

# Ejercicio 2: Función con parámetros posicionales variables
def encontrar_nota_maxima(*notas):
    """
    Encuentra la nota más alta de un conjunto variable de notas.
    Utiliza *args para recibir cantidad variable de notas.
    """
    if not notas:
        raise ValueError("Debe proporcionar al menos una nota")
    return max(notas)

# Ejercicio 3: Función con parámetros nombrados específicos
def registrar_estudiante(nombre, apellido, edad=18, carrera="Informática"):
    """
    Registra un estudiante con parámetros nombrados, algunos con valores por defecto.
    """
    return {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carrera
    }

# Ejercicio 4: Función con parámetros nombrados variables
def crear_perfil_estudiante(**datos):
    """
    Crea un perfil de estudiante con datos variables.
    Utiliza **kwargs para permitir cualquier cantidad de datos.
    """
    perfil = {}
    campos_requeridos = {"nombre", "apellido"}
    
    if not all(campo in datos for campo in campos_requeridos):
        raise ValueError("Faltan campos requeridos: nombre y apellido")
    
    for clave, valor in datos.items():
        perfil[clave] = valor
    return perfil

# Ejercicio 5: Función que combina todos los tipos de parámetros
def registrar_curso(nombre_curso, profesor, *estudiantes, cupo_maximo=30, **metadata):
    """
    Registra un curso combinando todos los tipos de parámetros:
    - nombre_curso: posicional obligatorio
    - profesor: posicional obligatorio
    - estudiantes: posicional variable (*args)
    - cupo_maximo: nombrado con valor por defecto
    - metadata: nombrado variable (**kwargs)
    """
    return {
        "curso": nombre_curso,
        "profesor": profesor,
        "estudiantes": list(estudiantes),
        "cupo_maximo": cupo_maximo,
        "metadata": metadata
    }

# Ejercicio 6: Procedimiento (función sin retorno) que utiliza otras funciones
def imprimir_reporte_curso(nombre_curso, profesor, *estudiantes, **metadata):
    """
    Procedimiento que imprime un reporte de curso utilizando otras funciones.
    No retorna nada, solo imprime información.
    """
    curso = registrar_curso(nombre_curso, profesor, *estudiantes, **metadata)
    print(f"\nReporte de Curso: {curso['curso']}")
    print(f"Profesor: {curso['profesor']}")
    print(f"Número de estudiantes: {len(curso['estudiantes'])}")
    print("Metadata adicional:")
    for clave, valor in curso['metadata'].items():
        print(f"  - {clave}: {valor}")

# Ejercicio 7: Función que utiliza parámetros posicionales y retorna una función
def crear_calculadora_ponderada(*ponderaciones):
    """
    Crea una función calculadora con ponderaciones específicas.
    Retorna una función que puede ser utilizada posteriormente.
    """
    def calcular(*notas):
        if len(notas) != len(ponderaciones):
            raise ValueError("El número de notas debe coincidir con el número de ponderaciones")
        return sum(nota * pond for nota, pond in zip(notas, ponderaciones))
    return calcular

# Ejercicio 8: Función que combina kwargs con validación
def actualizar_estudiante(id_estudiante, **actualizaciones):
    """
    Actualiza los datos de un estudiante permitiendo solo ciertos campos.
    """
    campos_permitidos = {"nombre", "apellido", "edad", "carrera", "semestre"}
    campos_invalidos = set(actualizaciones.keys()) - campos_permitidos
    
    if campos_invalidos:
        raise ValueError(f"Campos no permitidos: {campos_invalidos}")
    
    print(f"Actualizando estudiante {id_estudiante} con:")
    for campo, valor in actualizaciones.items():
        print(f"  {campo}: {valor}")

# Ejercicio 9: Procedimiento que utiliza args para registro de eventos
def registrar_eventos_estudiante(id_estudiante, *eventos):
    """
    Registra múltiples eventos para un estudiante.
    No retorna nada, solo imprime los eventos registrados.
    """
    print(f"\nRegistrando eventos para estudiante {id_estudiante}:")
    for i, evento in enumerate(eventos, 1):
        print(f"Evento {i}: {evento}")

# Ejercicio 10: Función que combina todo lo anterior
def gestionar_clase(nombre_clase, profesor, 
                   *estudiantes, 
                   notas_requeridas=3,
                   ponderaciones=(0.3, 0.3, 0.4),
                   **configuracion):
    """
    Función compleja que utiliza todas las características anteriores.
    """
    # Usar función de registro
    clase = registrar_curso(nombre_clase, profesor, *estudiantes, **configuracion)
    
    # Crear calculadora de notas
    calculadora = crear_calculadora_ponderada(*ponderaciones)
    
    # Registrar eventos
    registrar_eventos_estudiante(nombre_clase, 
                               f"Clase iniciada por {profesor}",
                               f"Registrados {len(estudiantes)} estudiantes")
    
    return {
        "informacion_clase": clase,
        "calculadora_notas": calculadora,
        "configuracion": configuracion
    }
