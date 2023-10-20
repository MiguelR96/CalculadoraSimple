# Función Suma
def suma(a, b):
    return a + b
# Función Resta
def resta(a, b):
    return a - b
# Función Multiplicación
def multiplicacion(a, b):
    return a * b
# Función División
def division(a, b):
    if b == 0:
        return "Error: Imposible dividir por cero."
    else:
        return a / b

# Función principal Calculadora
def calculadora():
    print("Selecciona operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

while True:
    operacion = input("Ingresa el número de la operación que deseas realizar (1/2/3/4): ")

    valor1 = float(input("Ingresa el primer número: "))
    valor2 = float(input("Ingresa el segundo número: "))
    
    if operacion == '1':
        print("Resultado:", suma(valor1, valor2))
    elif operacion == '2':
        print("Resultado:", resta(valor1, valor2))
    elif operacion == '3':
        print("Resultado:", multiplicacion(valor1, valor2))
    elif operacion == '4':
        print("Resultado:", division(valor1, valor2))
    else:
        print("Operación no válida, seleccione una válida")
            
calculadora()
