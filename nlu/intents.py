def detectar_intencion(texto):
    texto = texto.lower()

    if "comparar" in texto and "matricula" in texto:
        return "comparar_matricula"
    
    if "matricula" in texto and "comparar" not in texto:
        return "matricula_sexo"
    
    if texto.strip() in ["hola", "buenos dias", "buenos días", "buenas tardes", "buenas noches"]:
        return "saludo"

    mapa_intenciones = {
        "docentes_consulta": ["docente", "docentes", "profesor", "profesores", "maestro", "maestros", "cantidad de docentes"],
        "matricula_sexo": ["matricula", "matrícula", "inscritos", "alumnos", "estudiantes", "cantidad de estudiantes"],
        "egresados_consulta": ["egresado", "egresados", "graduado", "graduados"],
        "titulados_consulta": ["titulado", "titulados", "titulo", "título"],
        "edificios_consulta": ["edificio", "infraestructura", "nomenclatura", "fundacion", "niveles del edificio"],
        "administrativos_consulta": ["administrativos", "personal administrativo", "personal de oficina", "cantidad de administrativos", "no docentes"],
        "comparar_matricula": ["comparar", "compara"]
    }

    for intent, palabras_clave in mapa_intenciones.items():
        for palabra in palabras_clave:
            if palabra in texto:
                return intent  
              
    return None

def responder_intencion_no_detectada():
    """
    Mensaje estándar cuando no se reconoce la intención.
    """

    return (
            f"No entendí tu consulta 🤔\n\n"
            f"Puedes preguntar sobre:\n"
            f"- Matrícula\n"
            f"- Egresados\n"
            f"- Titulados\n"
            f"- Docentes\n\n"
            f"Ejemplo: 'Matrícula en sistemas 2024 semestre 1'"
        )