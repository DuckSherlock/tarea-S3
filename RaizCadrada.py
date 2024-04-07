def CalcularRaizCuadrada(numero):
    if numero >= 0:
        return numero ** 0.5
    else:
        return "No se puede calcular la raíz cuadrada de un número negativo"


numero = int(input("Ingrese un número para calcular su raíz cuadrada: "))
raiz_cuadrada = CalcularRaizCuadrada(numero)
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
