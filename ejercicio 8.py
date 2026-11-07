# ==============================================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1
# Estudiante: Alonso Lopez Quesada
# Fecha: 08/11/2026
# Versión: 1.0
# Descripción: Evalúa la factibilidad del viaje de regreso a la Tierra. Si hay 
#              combustible, simula el viaje día a día (Caso A). Si no alcanza,
#              determina los días de supervivencia de la tripulación varada (Caso B).
# ==============================================================================


CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_PERSONA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_PERSONA = 1



tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))



combustible_necesario = dias_viaje * CONSUMO_COMBUSTIBLE_DIA


# ==============================================================================

# ==============================================================================
if combustible >= combustible_necesario:
    dia_actual = 1
    regreso_exitoso = True
    
    # Simulación día por día del viaje de regreso
    while dia_actual <= dias_viaje and regreso_exitoso:
        # 1. Calcular consumos requeridos para el día actual
        c_combustible = CONSUMO_COMBUSTIBLE_DIA
        c_oxigeno = tripulantes * CONSUMO_OXIGENO_PERSONA
        c_energia = CONSUMO_ENERGIA_DIA
        c_provisiones = tripulantes * CONSUMO_PROVISIONES_PERSONA
        
        # 2. Verificar disponibilidad de los cuatro recursos
        if combustible >= c_combustible and oxigeno >= c_oxigeno and energia >= c_energia and provisiones >= c_provisiones:
            # Descontar consumos del día
            combustible = combustible - c_combustible
            oxigeno = oxigeno - c_oxigeno
            energia = energia - c_energia
            provisiones = provisiones - c_provisiones
            
            # Mostrar estado del día completado
            print("Día", dia_actual, "| Combustible:", combustible, "| Oxígeno:", oxigeno, "| Energía:", energia, "| Provisiones:", provisiones)
            
            dia_actual = dia_actual + 1
        else:
            # Al menos un recurso falló: no se descuentan consumos y se interrumpe
            regreso_exitoso = False

    # Evaluación del resultado final del viaje (Caso A)
    if regreso_exitoso:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible, "unidades")
        print("Oxígeno restante:", oxigeno, "unidades")
        print("Energía restante:", energia, "unidades")
        print("Provisiones restantes:", provisiones, "unidades")
    else:
        print("El regreso se interrumpió en el día", dia_actual, ".")
        
        # Reportar recursos insuficientes (en el orden: oxígeno, energía, provisiones)
        if oxigeno < tripulantes * CONSUMO_OXIGENO_PERSONA:
            print("Recurso insuficiente: oxigeno")
        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energia")
        if provisiones < tripulantes * CONSUMO_PROVISIONES_PERSONA:
            print("Recurso insuficiente: provisiones")
            
        print("La tripulación no completó el regreso.")


# ==============================================================================
# CASO B: TRIPULACIÓN VARADA (NO INICIA EL REGRESO)
# ==============================================================================
else:
    print("La tripulación quedó varada en el destino.")
    
    # Cálculo de días de supervivencia por recurso
    dias_oxigeno = oxigeno // (tripulantes * CONSUMO_OXIGENO_PERSONA)
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // (tripulantes * CONSUMO_PROVISIONES_PERSONA)
    
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)
    
    # Obtención del menor valor sin usar min()
    supervivencia_minima = dias_oxigeno
    if dias_energia < supervivencia_minima:
        supervivencia_minima = dias_energia
    if dias_provisiones < supervivencia_minima:
        supervivencia_minima = dias_provisiones
        
    print("Supervivencia estimada:", supervivencia_minima, "días")
    
    # Identificación de recursos limitantes (manejando empates)
    recursos_limitantes = ""
    
    if dias_oxigeno == supervivencia_minima:
        recursos_limitantes = "oxigeno"
        
    if dias_energia == supervivencia_minima:
        if recursos_limitantes == "":
            recursos_limitantes = "energia"
        else:
            recursos_limitantes = recursos_limitantes + ", energia"
            
    if dias_provisiones == supervivencia_minima:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"
            
    print("Recurso(s) limitante(s):", recursos_limitantes)