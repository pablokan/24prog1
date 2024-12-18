# Ejercicios de evaluación: Manipulación de Strings en Python

def ejercicio1():
    """
    Ejercicio 1: Validador de direcciones de correo electrónico
    Escribe una función que verifique si una dirección de correo electrónico es válida.
    Debe contener un '@' y al menos un '.' después del '@'.
    
    Ejemplo:
    verificar_email("usuario@dominio.com") -> True
    verificar_email("usuariodominio.com") -> False
    """
    def verificar_email(email):
        if '@' not in email:
            return False
        
        # Encontrar la posición del @
        pos_arroba = email.find('@')
        
        # Verificar si hay un punto después del @
        dominio = email[pos_arroba:]
        return '.' in dominio
    
    # Casos de prueba
    tests = [
        "usuario@dominio.com",
        "usuario.nombre@subdominio.dominio.com",
        "usuario@dominio",
        "usuario.dominio.com",
        "@dominio.com"
    ]
    
    for email in tests:
        print(f"Email: {email} -> {'Válido' if verificar_email(email) else 'Inválido'}")

def ejercicio2():
    """
    Ejercicio 2: Formateo de nombres
    Escribe una función que tome un nombre completo en cualquier formato y lo devuelva
    en el formato "Apellido, Nombre" con la primera letra de cada palabra en mayúscula.
    
    Ejemplo:
    formatear_nombre("juan carlos PEREZ") -> "Perez, Juan Carlos"
    """
    def formatear_nombre(nombre_completo):
        # Dividir el nombre en palabras
        palabras = nombre_completo.lower().split()
        
        # Separar el apellido (última palabra) y el resto del nombre
        apellido = palabras[-1].capitalize()
        nombres = ' '.join(palabra.capitalize() for palabra in palabras[:-1])
        
        return f"{apellido}, {nombres}"
    
    # Casos de prueba
    nombres = [
        "juan carlos PEREZ",
        "MARIA JOSE rodriguez",
        "pedro SANCHEZ",
        "ANA MARIA LOPEZ GARCIA"
    ]
    
    for nombre in nombres:
        print(f"Original: {nombre}")
        print(f"Formateado: {formatear_nombre(nombre)}\n")

def ejercicio3():
    """
    Ejercicio 3: Extractor de información
    Dada una cadena con información personal en formato "Nombre:Edad:Ciudad",
    crear un diccionario con esta información y presentarla de manera formateada.
    
    Ejemplo:
    procesar_informacion("Ana:25:Madrid") -> 
    {
        'nombre': 'Ana',
        'edad': 25,
        'ciudad': 'Madrid'
    }
    """
    def procesar_informacion(info_string):
        nombre, edad, ciudad = info_string.split(':')
        
        persona = {
            'nombre': nombre,
            'edad': int(edad),
            'ciudad': ciudad
        }
        
        # Crear un resumen formateado
        resumen = f"Nombre: {persona['nombre']}\n" \
                 f"Edad: {persona['edad']} años\n" \
                 f"Ciudad: {persona['ciudad']}"
        
        return persona, resumen
    
    # Casos de prueba
    datos = [
        "Ana:25:Madrid",
        "Carlos:30:Barcelona",
        "María:22:Valencia"
    ]
    
    for dato in datos:
        persona, resumen = procesar_informacion(dato)
        print(f"Datos originales: {dato}")
        print("Información procesada:")
        print(resumen)
        print()

def ejercicio4():
    """
    Ejercicio 4: Generador de hashtags
    Crear una función que tome una frase y genere hashtags válidos:
    - Eliminar espacios
    - Agregar # al inicio
    - Capitalizar cada palabra
    - Limitar a 20 caracteres
    
    Ejemplo:
    generar_hashtag("python es genial") -> "#PythonEsGenial"
    """
    def generar_hashtag(frase):
        if not frase.strip():
            return ""
        
        # Capitalizar cada palabra y unir
        palabras = frase.split()
        hashtag = ''.join(palabra.capitalize() for palabra in palabras)
        
        # Agregar # y limitar longitud
        hashtag = f"#{hashtag}"
        return hashtag[:20]
    
    # Casos de prueba
    frases = [
        "python es genial",
        "programación orientada a objetos",
        "desarrollo web",
        "inteligencia artificial y machine learning"
    ]
    
    for frase in frases:
        print(f"Frase original: {frase}")
        print(f"Hashtag: {generar_hashtag(frase)}\n")

def ejercicio5():
    """
    Ejercicio 5: Detector de palíndromos
    Crear una función que determine si una frase es un palíndromo,
    ignorando espacios, puntuación y mayúsculas/minúsculas.
    
    Ejemplo:
    es_palindromo("Anita lava la tina") -> True
    """
    def es_palindromo(frase):
        # Limpiar la frase: convertir a minúsculas y eliminar espacios/puntuación
        caracteres_validos = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
        frase_limpia = ''.join(c for c in frase.lower() if c in caracteres_validos)
        
        # Comparar la cadena con su reverso
        return frase_limpia == frase_limpia[::-1]
    
    # Casos de prueba
    frases = [
        "Anita lava la tina",
        "A man, a plan, a canal: Panama",
        "No es palíndromo",
        "Dábale arroz a la zorra el abad"
    ]
    
    for frase in frases:
        es_pal = es_palindromo(frase)
        print(f"Frase: {frase}")
        print(f"{'Es palíndromo' if es_pal else 'No es palíndromo'}\n")

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("=== Ejercicio 1: Validador de Email ===")
    ejercicio1()
    print("\n=== Ejercicio 2: Formateo de Nombres ===")
    ejercicio2()
    print("\n=== Ejercicio 3: Extractor de Información ===")
    ejercicio3()
    print("\n=== Ejercicio 4: Generador de Hashtags ===")
    ejercicio4()
    print("\n=== Ejercicio 5: Detector de Palíndromos ===")
    ejercicio5()
