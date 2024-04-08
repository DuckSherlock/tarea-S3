def obtener_calificacion(calificacion):
    if calificacion >= 9.1 and calificacion <= 10:
        return 'A'
    elif calificacion >= 8.1 and calificacion <= 9.0:
        return 'B'
    elif calificacion >= 7.5 and calificacion <= 8.0:
        return 'C'
    else:
        return 'R'

# Ejemplo de uso
calificacion = float(input("Ingrese la calificación: "))
print("La calificación es:", obtener_calificacion(calificacion))

    