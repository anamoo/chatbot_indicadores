def validar_datos(intent, entidades):

    if intent == "edificios_consulta":
        if not any(k in entidades for k in ["nomenclatura", "fundacion", "alberga"]):
            return ["criterio_edificio"]

    requeridos = {
        "matricula_sexo": ["anio", "semestre"],
        "egresados_consulta": ["carrera", "anio", "semestre"],
        "titulados_consulta": ["carrera", "anio", "semestre"],
        "docentes_consulta": ["departamento", "anio", "semestre"],
        "administrativos_consulta": ["anio", "semestre"],
        "comparar_matricula": ["carrera", "anios"]
    }

    faltantes = []

    if intent in requeridos:
        for campo in requeridos[intent]:
            if campo not in entidades:
                faltantes.append(campo)

    return faltantes

def generar_pregunta_faltante(intent, faltantes):
    campo = faltantes[0]

    if intent == "edificios_consulta" and campo == "criterio_edificio":
        return {
            "respuesta": "¿Cómo deseas consultar los edificios? 🏫\n\n"
            "Puedes buscar por: \n"
            "• Nomenclatura → 'edificio A'\n"
            "• Año → 'edificios 1977'\n"
            "• Uso → 'edificios con laboratorios'"
        }

    if intent == "comparar_matricula" and campo == "anios":
        return {
            "respuesta": "Indícame los años que deseas comparar 📊 (ejemplo: 2022 2023 2024)"
        }

    preguntas = {
        "carrera": "¿De qué carrera necesitas la información?",
        "departamento": "¿De qué departamento deseas consultar los docentes?",
        "anio": "¿De qué año necesitas la información?",
        "semestre": "¿De qué semestre? (Enero-Junio o Agosto-Diciembre)"
    }

    return {
        "respuesta": preguntas.get(campo, "Necesito más información para continuar.")
    }