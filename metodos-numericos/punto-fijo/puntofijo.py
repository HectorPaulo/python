import numpy as np

# Coeficientes de la ecuación cúbica: ax^3 + bx^2 + cx + d = 0
a = 1
b = -6.543
c = -31.975266
d = 179.65217
coeficientes = [a, b, c, d]  # Coeficientes de la ecuación

# Método de punto fijo
def punto_fijo(g, x0, max_iter=100, max_value=1e10):
    for i in range(max_iter):
        x1 = g(x0)  # Función iterativa g(x)
        if abs(x1) > max_value:  # Evita valores excesivos
            print(f"Valor excesivo alcanzado: x = {x1}. Abandonando la iteración.")
            return None, i+1
        if abs(x1 - x0) < 1e-6:  # Criterio de convergencia
            return x1, i+1
        x0 = x1  # Actualiza x0 para la siguiente iteración
    return None, max_iter  # No se encontró solución en max_iter iteraciones

# Función generadora de g(x) basada en la ecuación cúbica
def g_cubica(a, b, c, d):
    # Retorna la función iterativa g(x)
    return lambda x: x - (a*x**3 + b*x**2 + c*x + d) / (3*a*x**2 + 2*b*x + c)

# Función principal que ejecuta el método de punto fijo
def main():
    # Genera la función iterativa g(x) a partir de los coeficientes de la ecuación cúbica
    g = g_cubica(a, b, c, d)
    
    soluciones = []  # Lista para almacenar las soluciones
    valores_iniciales = [-5, 7, 4]  # Valores iniciales de prueba (basados en las soluciones esperadas)

    # Itera sobre los valores iniciales y busca soluciones
    for x0 in valores_iniciales:
        sol, iteraciones = punto_fijo(g, x0)
        if sol is not None:
            soluciones.append(sol)
            # print(f"Solución: {sol} : {iteraciones} iteraciones")
        else:
            print(f"El método no convergió para el valor inicial {x0}.")

    if len(soluciones) > 0:
        print(f"Raíces aproximadas: {soluciones}")
    else:
        print("No se encontraron raíces.")

# Ejecuta la función principal
if __name__ == "__main__":
    main()
