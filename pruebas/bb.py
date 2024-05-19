import random
def adivinar_numero():
    print("Piensa en un número entre 1 y 1000, yo intentaré adivinarlo.")
    input("Presiona Enter cuando estés listo...")

    limite_inferior = 1
    limite_superior = 1000
    intentos = 0

    while True:
        intento = (limite_inferior + limite_superior) // 2
        print("¿Es tu número {}?".format(intento))
        respuesta = input("Ingresa 's' si es correcto, 'm' si mi número es demasiado bajo, 'a' si es demasiado alto: ").lower()

        if respuesta == 's':
            print("¡Genial! ¡Adiviné tu número en {} intentos!".format(intentos))
            break
        elif respuesta == 'm':
            limite_inferior = intento + 1
        elif respuesta == 'a':
            limite_superior = intento - 1
        else:
            print("Respuesta inválida. Por favor, ingresa 's', 'm' o 'a'.")

        intentos += 1

adivinar_numero()
