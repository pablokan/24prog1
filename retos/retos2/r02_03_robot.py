"""
Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se
encuentra en una cuadrícula representada por los ejes "x" e "y".
- El robot comienza en la coordenada (0, 0).
- Para indicarle que se mueva, le enviamos una lista formado por enteros 
  (positivos o negativos) que indican la secuencia de pasos a dar.
- Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
  luego 5, se detiene, y finalmente 2. 
  El resultado en este caso sería (x: -5, y: 12)
- Si el número de pasos es negativo, se desplazaría en sentido contrario al
  que está mirando (camina hacia atrás)
- Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
  hacia la parte positiva del eje "y".
- El robot tiene un fallo en su programación: cada vez que finaliza una
  secuencia de pasos gira 90 grados en el sentido contrario a las agujas
  del reloj.
"""
pi = [0, 0]
direcciones = ['arriba', 'izquierda', 'abajo', 'derecha']
i = 0
ordenes = [10, 5, -2]
for o in ordenes:
    if direcciones[i] == 'arriba':
        pi[1] += o
    elif direcciones[i] == 'izquierda':
        pi[0] -= o
    elif direcciones[i] == 'abajo':
        pi[1] -= o
    elif direcciones[i] == 'derecha':
        pi[0] += o  
    i = i + 1 if i < 3 else 0
print(pi)
