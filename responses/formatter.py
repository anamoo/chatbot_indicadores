from utils.graficas import grafica_genero
from utils.graficas import grafica_comparativa

def generar_respuesta(intent, data):
    if intent == "docentes_consulta":

        if not data:
            return {
                "respuesta": "No encontré información del personal docente."
            }

        return {
            "respuesta": f"En el departamento de {data.get('departamento')} "
            f"durante {data.get('semestre')}-{data.get('anio')} "
            f"hay 👨‍🏫 {data.get('total_docentes')} docentes.\n"
            f"•Tiempo completo: {data.get('tiempo_completo')}.\n"
            f"•3/4 de Tiempo: {data.get('tres_cuartos_tiempo')}.\n"
            f"•1/2 Tiempo: {data.get('medio_tiempo')}.\n"
            f"•Horas asignatura: {data.get('horas_asignatura')}."
        }
    
    if intent == "administrativos_consulta":
        if not data:
            return {
                "respuesta": "No encontré información del personal administrativo."
            }

        total = data.get('total_adm')
        hombres = data.get('hombres_adm')
        mujeres = data.get('mujeres_adm')

        archivo = grafica_genero(
            hombres,
            mujeres,
            f"Personal administrativo {data.get('semestre')} {data.get('anio')}"
        )

        p_hombres = round((hombres / total) * 100, 1)
        p_mujeres = round((mujeres / total) * 100, 1)

        return {
            "respuesta": f"En el semestre {data.get('semestre')} del {data.get('anio')} hubo:\n\n"
            f"👨 Hombres: {hombres} ({p_hombres}%)\n"
            f"👩 Mujeres: {mujeres} ({p_mujeres}%)\n"
            f"👥 Total: {total} administrativos\n"
            #f"📊 Gráfica generada: {archivo}"
        }
    
    if intent == "comparar_matricula":

        if not data:
            return {
                "respuesta": "No se encontraron datos para realizar la comparación."
            }

        anios = data.get("anios", [])
        valores = data.get("valores", [])
        carrera = data.get("carrera", "la carrera")

        if not anios or not valores:
            return {
                "respuesta": "No hay datos suficientes para generar la gráfica."
            }

        inicio = valores[0]
        fin = valores[-1]

        variacion = round(((fin - inicio) / inicio) * 100, 1) if inicio != 0 else 0

        tendencia = "crecido 📈" if fin > inicio else "disminuido 📉"

        texto = f"Comparativa de matrícula en {carrera}:\n\n"

        for a, v in zip(anios, valores):
            texto += f"{a}: {v} estudiantes\n"

        texto += f"\nLa matrícula ha {tendencia} {abs(variacion)}% entre {anios[0]} y {anios[-1]}."

        return {
            "respuesta": texto,
            "grafica": {
                "tipo": "bar",
                "anios": anios,
                "valores": valores
            }
    }
         

    if intent == "matricula_sexo":

        if not data:
         return {
            "respuesta": "No se encontró información de matrícula."
        }

         # 🔵 MATRÍCULA TOTAL
        if data.get("tipo") == "total":
            return {
            "respuesta": f"Matrícula total del periodo {data.get('semestre')} {data.get('anio')}:\n\n"
                         f"👨 Hombres: {data.get('hombres')}\n"
                         f"👩 Mujeres: {data.get('mujeres')}\n"
                         f"👥 Total: {data.get('total')} estudiantes."
        }

        # 🟢 MATRÍCULA POR CARRERA
        if data.get("tipo") == "carrera":
            return {
            "respuesta": f"Matrícula en {data.get('carrera')}: {data.get('semestre')} {data.get('anio')}:\n\n"
                         f"• Nuevo ingreso → 👨 {data.get('nuevo_ingreso', {}).get('hombres')} | "
                         f"👩 {data.get('nuevo_ingreso', {}).get('mujeres')} = {data.get('totales', {}).get('total_nuevo_ingreso')}\n"
                         f"• Reingreso → 👨 {data.get('reingreso', {}).get('hombres')} | "
                         f"👩 {data.get('reingreso', {}).get('mujeres')} = {data.get('totales', {}).get('total_reingreso')}\n\n"
                         f"👥 Total: {data.get('totales', {}).get('Matricula TOTAL')} estudiantes."
        }
    
    if intent == "egresados_consulta":

        if not data:
            return {
                "respuesta": "No se encontró información de egresados para ese criterio."
            }
        
        cantidad = data.get("cantidad_egresados", 0)
        total = data.get("total_institucional", 0)

        porcentaje = 0
        if total > 0:
            porcentaje = round((cantidad / total) * 100, 1)
        
        return {
            "respuesta": f"En {data.get('carrera')} "
            f"durante {data.get('semestre')} {data.get('anio')} "
            f"hubo en total: 🎓 {data.get('cantidad_egresados')} egresados.\n\n"

            f"🏫 Total institucional en este periodo: "
            f"🎓 {data.get('total_institucional')} egresados.\n\n"

            f"📊 Esta carrera representa el {porcentaje}% del total institucional."
        }
    
    if intent == "titulados_consulta":
        if not data:
            return {
                "respuesta": "No se encontró información de titulados para este criterio"
            }
        cantidad = data.get("cantidad_titulados", 0)
        total = data.get("total_institucional", 0)

        porcentaje = 0
        if total > 0:
            porcentaje = round((cantidad / total) * 100, 1)

        return {
            "respuesta": f"En {data.get('carrera')} "
            f"durante {data.get('semestre')} {data.get('anio')} "
            f"hubo en total: 🏅 {data.get('cantidad_titulados')} titulados.\n\n"

            f"🏫 Total institucional en este periodo: "
            f"🏅 {data.get('total_institucional')} titulados. \n\n"
            
            f"📊 Esta carrera representa el {porcentaje}% del total institucional."
        }
    
    if intent == "edificios_consulta":
        return formatear_edificios(data)
    
    if intent == "saludo":
        return {
            "respuesta": f"Hola 👋\n"

            f"Soy el chatbot de indicadores institucionales del Instituto Tecnológico de Durango\n"

            f"Puedes consultarme sobre:\n"

            f"📊 Matrícula\n"  
            f"🎓 Egresados\n"  
            f"🏅 Titulados\n"  
            f"👨‍🏫 Docentes\n"
            f"👤 Administrativos\n"
            f"🏫 Edificios\n" 
    
            f"Ejemplos:\n"
            f"- matrícula sistemas 2024 semestre 1\n"
            f"- egresados sistemas 2023\n"
            f"- docentes en industrial 2025\n"
            f"- admnistrativos en junio 2022\n"
            f"- comparar matrícula sistemas 2023 2024 2025\n"
            f"- información del edificio A\n"
        }
    
def formatear_edificios(data):

    if not data:
        return {
            "respuesta": "No encontré edificios con ese criterio."
        }

    respuesta = f"Se encontraron 🏫 {len(data)} edificios:\n\n"

    for e in data:
        respuesta += (
            f"• Edificio {e.get('nomenclatura')} (fundado en {int(e.get('fundacion'))})\n"
            f"  Área: {e.get('area')} m²\n"
            f"  Niveles: {e.get('niveles')}\n"
            f"  Alberga: {e.get('alberga')}\n\n"
        )

    return {
        "respuesta": respuesta
    }