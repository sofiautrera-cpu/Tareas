# bucle_for_basico1.py — Código completo
# 1. Básico: imprime todos los números enteros del 0 al 100.
print("=== Ejercicio 1: Básico ===")
for i in range(0, 101):
    print(i)
# 2. Múltiples de 2: imprime todos los múltiplos de 2 entre 2 y 500.
print("\n=== Ejercicio 2: Múltiplos de 2 ===")
for i in range(2, 501, 2):
    print(i)
# 3. Contando Vanilla Ice:
# - Si es divisible por 5 → "ice ice"
# - Si es divisible por 10 → "baby"
print("\n=== Ejercicio 3: Contando Vanilla Ice ===")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
# 4. Wow. Número gigante a la vista:
# Suma los números pares del 0 al 500,000.
print("\n=== Ejercicio 4: Wow. Número gigante a la vista ===")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("La suma total es:", suma)
# 5. Regrésame al 3:
# Imprime números positivos desde 2024, regresando de 3 en 3.
print("\n=== Ejercicio 5: Regrésame al 3 ===")
for i in range(2024, 0, -3):
    print(i)
# 6. Contador dinámico:
# Imprime los números entre numInicial y numFinal que sean múltiplos de 'multiplo'.
print("\n=== Ejercicio 6: Contador dinámico ===")

numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
