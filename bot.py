from nlu.intents import detectar_intencion, responder_intencion_no_detectada
from nlu.entities import extraer_entidades
from validaciones import validar_datos, generar_pregunta_faltante
from services.api_client import llamar_backend
from responses.formatter import generar_respuesta

contexto_actual = None

def procesar_mensaje(texto):
    
    global contexto_actual

    if contexto_actual and contexto_actual.get("faltantes"):
         
        # intent = detectar_intencion(texto)
        intent = contexto_actual["intent"]
        entities = contexto_actual["entities"]

        new_entities = extraer_entidades(texto, intent)
        entities.update(new_entities)

        faltantes = validar_datos(intent, entities)

        if not faltantes:
            data = llamar_backend(intent, entities)

            if data is None:
                contexto_actual = None
                return {"respuesta": "No se pudo obtener información, contactar al DEPARTAMENTO DE PLANEACIÓN."}
            
            respuesta = generar_respuesta(intent, data)

            contexto_actual = None

            return respuesta
        
        contexto_actual["faltantes"]= faltantes
        return generar_pregunta_faltante(intent, faltantes)
    
    intent = detectar_intencion(texto)

    #print("INTENCION DETECTADA:", intent)
    #entities = extraer_entidades(texto, intent)

    #print("ENTIDADES EXTRAIDAS:", entities)

    if not intent:
        return responder_intencion_no_detectada()
    
    if intent == "saludo":
        respuesta = generar_respuesta(intent, None)
        return respuesta
    
    entities = extraer_entidades(texto, intent)

    print("ENTIDADES EXTRAIDAS:", entities)

    faltantes = validar_datos(intent, entities)

    if faltantes:
        contexto_actual = {
            "intent": intent,
            "entities": entities,
            "faltantes": faltantes
        }
        return generar_pregunta_faltante(intent, faltantes)

    data = llamar_backend(intent, entities)

    if data is None:
        return {"respuesta": "No se pudo obtener información del servidor"}

    #print("RESPUESTA BACKEND:", data)

    respuesta = generar_respuesta(intent, data)

    return respuesta

    #if not data:
     #   return "No se encontraron datos."

    #return generar_respuesta(intent, data)
