#funciones y modularidad

def evaluar_rendimiento(nota_zona, nota_examen, asistencia_porcentaje):
    """
    Calcula el resultado académico de un estudiante
    Parámetros:
    -nota_zona: puntos obtenidos en zona, de 0 a 70.
    -nota_examen: puntos obtenidos en examen, de 0 a 100.
    -asistencia_porcentaje: porcentaje de asistencia de 0 a 100.

    Retorna: un mensaje con la nota final y el estado academico
    """
    nota_final = nota_zona + nota_examen

    if asistencia_porcentaje < 75:
        estado = "Reprobado por inasistencia"
    elif nota_final >= 61:
        estado = "Aprobado"
    elif nota_final >= 50:
        estado = "Extraordinario"
    else:
        estado: "Reprobado"

    return f"Nota final: {nota_final} puntos. Estado: {estado}"

resultado_estudiante_1 = evaluar_rendimiento(50, 20, 90)
resultado_estudiante_2 = evaluar_rendimiento(40, 40, 80)
print("Estudiante 1")
print(resultado_estudiante_1)
print("Giovanny Guerra")
print(resultado_estudiante_2)