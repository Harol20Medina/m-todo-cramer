import numpy as np
#NumPy, una biblioteca esencial para el cómputo científico en Python, proporciona estructuras de datos eficientes, 
# como los arreglos multidimensionales, junto con un conjunto amplio de funciones matemáticas de alto nivel. 
# Este soporte especializado permite realizar operaciones numéricas de manera rápida y concisa, facilitando el 
# desarrollo de código eficiente en tareas relacionadas con matemáticas y ciencia de datos.

# Definir una función para resolver un sistema de ecuaciones lineales usando la Regla de Cramer
def cramer_solver(A, b):
    n = A.shape[0]  # Obtener el tamaño del sistema de ecuaciones (número de ecuaciones/incógnitas)
    solutions = np.zeros(n)  # Inicializar un array para almacenar las soluciones

    det_A = np.linalg.det(A)  # Calcular el determinante de la matriz de coeficientes A

    # Verificar si el determinante es cero (si es así, el sistema no tiene una solución única)
    if det_A == 0:
        print("El sistema no tiene solución única (determinante de A = 0)")
        return None

    # Calcular las soluciones utilizando la Regla de Cramer
    for i in range(n):
        Ai = A.copy()  # Crear una copia de la matriz A
        Ai[:, i] = b  # Reemplazar la columna i con el vector de términos independientes b
        det_Ai = np.linalg.det(Ai)  # Calcular el determinante de la matriz modificada
        solutions[i] = det_Ai / det_A  # Almacenar la solución para la variable correspondiente

    return solutions  # Devolver el array de soluciones

# Solicitar al usuario ingresar el número de ecuaciones/incógnitas
n = int(input("Ingrese el número de ecuaciones/incógnitas: "))

# Inicializar matrices para los coeficientes y el vector de términos independientes
A = np.zeros((n, n))
b = np.zeros(n)

# Solicitar al usuario ingresar los coeficientes de la matriz A
print("Ingrese los coeficientes de la matriz A:")
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"Ingrese el coeficiente A[{chr(120+i)}][{chr(120+j)}]: "))

# Solicitar al usuario ingresar el vector de términos independientes b
print("Ingrese el vector de términos independientes b:")
for i in range(n):
    b[i] = float(input(f"Ingrese el término independiente B[{chr(120+i)}]: "))

# Imprimir la matriz A
print("\nMatriz A:")
for i in range(n):
    row = [f"A[{chr(120+i)}][{chr(120+j)}]: {A[i][j]}" for j in range(n)]
    print(" | ".join(row))

# Calcular el determinante de la matriz A
det_A = np.linalg.det(A)

# Verificar si el sistema tiene una solución única o no
if det_A == 0:
    print("El sistema no tiene solución única (determinante de A = 0)")
else:
    # Calcular y mostrar las soluciones utilizando la Regla de Cramer
    solutions = cramer_solver(A, b)
    print("\nSoluciones finales:")
    for i in range(n):
        print(f"{chr(120+i)} = {solutions[i]}")
