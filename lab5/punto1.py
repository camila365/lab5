
#PASO1
print("¡Hola, mundo!")

#declaracion variables
int_var = 10
float_var = 3.14
str_var = "El resultado es"

resultado = int_var + float_var
print(f"{str_var} {resultado}")

#concatenar
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}!")

#PASO 2
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#Bucle for para iterar sobre una lista e imprimir cuadrados

numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

#Bucle while para solicitar entrada hasta cumplir una condición

while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("¡Adiós!")
        break
#PASO 3

estudiantes = ["Ana", "Luis", "Sofía"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")

#Diccionario de información de contacto

contactos = {"Ana": "ana@example.com", "Luis": "luis@example.com"}
for nombre, correo in contactos.items():
    print(f"{nombre}: {correo}")

#Agregar elementos a una lista o diccionario:

lista = []
while True:
    elemento = input("Agrega un elemento a la lista (o escribe 'salir'): ")
    if elemento.lower() == "salir":
        break
    lista.append(elemento)
print(f"Lista final: {lista}")

#PASO 4

while True:
    print("Selecciona una operación: (+, -, *, /) o 'salir'")
    operacion = input()
    if operacion.lower() == "salir":
        break
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    if operacion == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "/":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: división entre cero.")
    else:
        print("Operación no válida.")

# adivinanza

import random
numero_secreto = random.randint(1, 100)
print("Adivina el número entre 1 y 100")

while True:
    intento = int(input("Introduce tu número: "))
    if intento < numero_secreto:
        print("Es mayor.")
    elif intento > numero_secreto:
        print("Es menor.")
    else:
        print("¡Adivinaste!")
        break





