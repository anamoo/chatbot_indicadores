import re

def extraer_entidades(texto, intent):

    texto = texto.lower()
    entidades = {}

    mapa_departamentos = {
        "administracion": "Ciencias Económico-Administrativas",
        "gestion": "Ciencias Económico-Administrativas",
        "industrial": "Ingeniería Industrial",
        "logistica": "Ingeniería Industrial",
        "arquitectura": "Ciencias de la Tierra",
        "civil": "Ciencias de la Tierra",
        "quimica": "Química-Bioquímica",
        "bioquimica": "Química-Bioquímica",
        "electrica": "Eléctrica-Electrónica",
        "electronica": "Eléctrica-Electrónica",
        "biomedica": "Eléctrica-Electrónica",
        "semiconductores": "Eleéctrica-Electrónica",
        "mecanica": "Metal-Mecánica",
        "mecatronica": "Metal-Mecánica",
        "sistemas": "Sistemas y Computación",
        "informatica": "Sistemas y Computación",
        "tics": "Sistemas y Computación"
    }

    mapa_carreras = {
        "arquitectura": "Arquitectura",
        "civil": "Ingeniería Civil",
        "sistemas": "Ingeniería en Sistemas Computacionales",
        "industrial": "Ingeniería Industrial",
        "logistica": "Ingeniería en Logística",
        "informatica": "Ingeniería Informática",
        "tics": "Ingeniería en Tecnologías de la Información y Comunicaciones",
        "administracion": "Licenciatura en Administración",
        "gestion": "Ingeniería en Gestión Empresarial",
        "quimica": "Ingeniería Química",
        "bioquimica": "Ingeniería Bioquímica",
        "mecanica": "Ingeniería Mecánica",
        "mecatronica": "Ingeniería Mecatrónica",
        "electronica": "Ingeniería Electrónica",
        "electrica": "Ingeniería Eléctrica",
        "semiconductores": "Ingeniería en Semiconductores",
        "biomedica": "Ingeniería Biomédica",
        "licinformatica": "Licenciatura en Informática"
    }

    # ---------------- DOCENTES ----------------
    if intent == "docentes_consulta":

        for palabra, nombre_real in mapa_departamentos.items():
            if palabra in texto:
                entidades["departamento"] = nombre_real
                break

    # ---------------- CARRERAS ----------------
    elif intent in ["egresados_consulta", "titulados_consulta", "matricula_sexo", "comparar_matricula"]:

        for palabra, nombre_real in mapa_carreras.items():
            if palabra in texto:
                entidades["carrera"] = nombre_real
                break

    # ---------------- EDIFICIOS ----------------
    elif intent == "edificios_consulta":

        # detectar edificio específico
        match = re.search(r"\bedificio\s+([a-zA-Z]'?)", texto)

        if match:
            entidades["nomenclatura"] = match.group(1).upper()

        mapa_alberga = {
            "laboratorio": "lab",
            "laboratorios": "lab",
            "lab": "lab",

            "aula": "aulas",
            "aulas": "aulas",
            "salon": "aulas",
            "salones": "aulas",

            "oficina": "oficinas",
            "oficinas": "oficinas",
            "administrativo": "oficinas",
            "administracion": "oficinas",

            "taller": "taller",
            "talleres": "taller"
        }

        for palabra, valor in mapa_alberga.items():
            if palabra in texto:
                entidades["alberga"] = valor
                break

# ---------------- AÑOS ----------------

    anios = re.findall(r"(19\d{2}|20\d{2})", texto)

    # Si hay más de un año → es comparativa
    if len(anios) > 1:
        entidades["anios"] = [int(a) for a in anios]

    # Si solo hay un año → consulta normal
    elif len(anios) == 1:
        
        valor_anio = int(anios[0])

        if intent == "edificios_consulta":
            entidades["fundacion"] = valor_anio
        else:
            entidades["anio"] = valor_anio

        
        # ---------------- SEMESTRE ----------------
    mapa_semestres = {

        "semestre 1": 1,
        "semestre 2": 2,

        "enero junio": 1,
        "enero-junio": 1,

        "agosto diciembre": 2,
        "agosto-diciembre": 2,

        "enero": 1,
        "junio": 1,

        "agosto": 2,
        "diciembre": 2,

        "ene-jun": 1,
        "ago-dic": 2
    }

    for clave, valor in mapa_semestres.items():
        if clave in texto:
            entidades["semestre"] = valor
            break

    return entidades