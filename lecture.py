## EJERCICIOS INTERACTIVOS:

# 1.- Calculadora de promedio:Escribe un programa que solicite al usuario una serie de números separados por espacios y calcule
# su promedio. Utiliza el operador walrus para leer la entrada del usuario en una sola línea.

numeros = input("Ingresa una serie de números separados por espacios: ")
numeros = [float(num) for num in numeros.split()]
promedio = sum(numeros) / len(numeros) if (numeros := numeros) else 0
print("El promedio de los números es:", promedio)

# 2.- Generador de contraseñas seguras:Crea un programa que genere contraseñas seguras de longitud especificada por el usuario. 
# Utiliza el operador walrus para leer la longitud deseada de la contraseña en una sola línea.

import random
import string

longitud = int(input("Longitud de la contraseña: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
print("Contraseña generada:", contraseña)

# 3.- Buscador de archivos en un directorio:Escribe un programa que solicite al usuario un directorio y una extensión de archivo,
# luego liste todos los archivos con esa extensión en ese directorio. Utiliza el operador walrus para leer la entrada del usuario en una sola línea.

import os

directorio = input("Directorio a buscar: ")
extension = input("Extensión de archivo a buscar: ")
archivos = [archivo for archivo in os.listdir(directorio) if archivo.endswith(extension)] if (directorio := os.path.abspath(directorio)) else []
print("Archivos encontrados:", archivos)

# 4.- Calculadora de factorial recursivo:Escribe una función recursiva para calcular el factorial de un número dado. Utiliza el operador walrus para 
# mostrar el número de iteraciones realizadas durante el cálculo.

def factorial(n, iteraciones=0):
    if n == 0:
        return 1, iteraciones
    else:
        resultado, iteraciones = factorial(n - 1, iteraciones)
        iteraciones += 1
        return n * resultado, iteraciones

numero = int(input("Ingrese un número para calcular su factorial: "))
resultado, iteraciones = factorial(numero)
print(f"El factorial de {numero} es {resultado}. Se realizaron {iteraciones} iteraciones.")

# 5.- Contador de palabras en un texto:Escribe un programa que cuente el número de palabras en un texto ingresado por el usuario. Utiliza el operador 
# walrus para leer la entrada del usuario en una sola línea.

texto = input("Ingrese un texto: ")
palabras = texto.split()
cantidad_palabras = len(palabras) if (palabras := palabras) else 0
print("Número de palabras en el texto:", cantidad_palabras)
