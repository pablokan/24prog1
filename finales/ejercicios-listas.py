# Ejercicio 1: Métodos básicos con lista vacía
"""
Crear una lista vacía y realizar las siguientes operaciones:
a) Agregar los números del 1 al 5 usando append
b) Insertar el número 0 al inicio de la lista
c) Eliminar el último elemento usando pop
d) Eliminar el número 3 de la lista usando remove
e) Mostrar el largo de la lista luego de cada operación

Resultado esperado final: [0, 1, 2, 4]
"""
def ejercicio1():
    # Crear lista vacía
    numeros = []
    print(f"Lista inicial: {numeros}, largo: {len(numeros)}")
    
    # a) Agregar números del 1 al 5
    for i in range(1, 6):
        numeros.append(i)
        print(f"Después de append({i}): {numeros}, largo: {len(numeros)}")
    
    # b) Insertar 0 al inicio
    numeros.insert(0, 0)
    print(f"Después de insert(0, 0): {numeros}, largo: {len(numeros)}")
    
    # c) Eliminar último elemento
    ultimo = numeros.pop()
    print(f"Después de pop(): {numeros}, largo: {len(numeros)}")
    
    # d) Eliminar el número 3
    numeros.remove(3)
    print(f"Después de remove(3): {numeros}, largo: {len(numeros)}")

# Ejercicio 2: Trabajo con listas paralelas
"""
Dadas tres listas paralelas con información de estudiantes:
- nombres: ["Ana", "Juan", "María"]
- edades: [20, 22, 19]
- notas: [6.5, 5.0, 6.8]

Realizar:
a) Agregar un nuevo estudiante al final (Pedro, 21 años, nota 5.5)
b) Eliminar al estudiante en la posición 1
c) Mostrar un resumen con nombre y nota de los estudiantes mayores de 20 años
"""
def ejercicio2():
    nombres = ["Ana", "Juan", "María"]
    edades = [20, 22, 19]
    notas = [6.5, 5.0, 6.8]
    
    # a) Agregar nuevo estudiante
    nombres.append("Pedro")
    edades.append(21)
    notas.append(5.5)
    print("Después de agregar nuevo estudiante:")
    print(f"Nombres: {nombres}")
    print(f"Edades: {edades}")
    print(f"Notas: {notas}")
    
    # b) Eliminar estudiante en posición 1
    nombres.pop(1)
    edades.pop(1)
    notas.pop(1)
    print("\nDespués de eliminar estudiante en posición 1:")
    print(f"Nombres: {nombres}")
    print(f"Edades: {edades}")
    print(f"Notas: {notas}")
    
    # c) Mostrar resumen mayores de 20
    print("\nEstudiantes mayores de 20 años:")
    for i in range(len(nombres)):
        if edades[i] > 20:
            print(f"Nombre: {nombres[i]}, Nota: {notas[i]}")

# Ejercicio 3: Recorrido por elemento
"""
Dada la lista de números: [15, 28, 36, 42, 55, 67, 73, 81, 90]
Crear nuevas listas que contengan:
a) Los números pares
b) Los números impares
c) Los números mayores a 50
Utilizar recorrido por elemento (for num in lista)
"""
def ejercicio3():
    numeros = [15, 28, 36, 42, 55, 67, 73, 81, 90]
    pares = []
    impares = []
    mayores_50 = []
    
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
            
        if num > 50:
            mayores_50.append(num)
    
    print(f"Lista original: {numeros}")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números mayores a 50: {mayores_50}")

# Ejercicio 4: Recorrido por índice
"""
Dada la lista de palabras: ["python", "java", "ruby", "javascript", "php"]
Realizar:
a) Modificar cada palabra para que inicie con mayúscula
b) Agregar la longitud de cada palabra al final entre paréntesis
Ejemplo: "Python (6)"
Utilizar recorrido por índice (for i in range(len(lista)))
"""
def ejercicio4():
    lenguajes = ["python", "java", "ruby", "javascript", "php"]
    print(f"Lista original: {lenguajes}")
    
    for i in range(len(lenguajes)):
        palabra = lenguajes[i]
        palabra_mayus = palabra.capitalize()
        palabra_con_len = f"{palabra_mayus} ({len(palabra)})"
        lenguajes[i] = palabra_con_len
    
    print(f"Lista modificada: {lenguajes}")

# Ejercicio 5: Combinación de conceptos
"""
Crear un programa que gestione una lista de tareas:
a) Comenzar con una lista vacía
b) Agregar 3 tareas con su estado (pendiente/completada)
c) Permitir marcar una tarea como completada (por índice)
d) Eliminar una tarea (por valor)
e) Mostrar solo las tareas pendientes
"""
def ejercicio5():
    tareas = []
    estados = []
    
    # b) Agregar tareas
    tareas.extend(["Estudiar Python", "Hacer ejercicios", "Repasar código"])
    estados.extend(["pendiente", "pendiente", "pendiente"])
    print("Lista inicial de tareas:")
    for i in range(len(tareas)):
        print(f"{i}: {tareas[i]} - {estados[i]}")
    
    # c) Marcar tarea como completada
    indice_completada = 1
    estados[indice_completada] = "completada"
    print(f"\nDespués de marcar tarea {indice_completada} como completada:")
    for i in range(len(tareas)):
        print(f"{i}: {tareas[i]} - {estados[i]}")
    
    # d) Eliminar una tarea
    tarea_eliminar = "Repasar código"
    indice_eliminar = tareas.index(tarea_eliminar)
    tareas.pop(indice_eliminar)
    estados.pop(indice_eliminar)
    print(f"\nDespués de eliminar '{tarea_eliminar}':")
    for i in range(len(tareas)):
        print(f"{i}: {tareas[i]} - {estados[i]}")
    
    # e) Mostrar solo tareas pendientes
    print("\nTareas pendientes:")
    for i in range(len(tareas)):
        if estados[i] == "pendiente":
            print(f"{i}: {tareas[i]}")

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("=== Ejercicio 1 ===")
    ejercicio1()
    print("\n=== Ejercicio 2 ===")
    ejercicio2()
    print("\n=== Ejercicio 3 ===")
    ejercicio3()
    print("\n=== Ejercicio 4 ===")
    ejercicio4()
    print("\n=== Ejercicio 5 ===")
    ejercicio5()
