import time
from google import genai
import os

# 1. CONFIGURACIÓN
client = genai.Client(api_key="Your_Key")
MODEL_ID = "gemini-3-flash-preview"

# Función genérica para manejar los reintentos por saturación (Error 503)
def llamar_ia_con_reintento(prompt):
    for intento in range(3):
        try:
            response = client.models.generate_content(model=MODEL_ID, contents=prompt)
            return response.text
        except Exception as e:
            if "503" in str(e):
                print(f"⚠️ Servidor ocupado, reintentando en 5 segundos... (Intento {intento+1}/3)")
                time.sleep(5)
            else:
                raise e
    return "Error: El servidor de IA no está disponible tras varios intentos."

# --- AGENTES SEGÚN TU INFORME  ---

def agente_1_especialista_parseo(log_sucio):
    """Limpia los datos y extrae la línea técnica del fallo crítico[cite: 8, 9]."""
    prompt = f"Eres un Especialista en Parseo de Logs. Limpia estos datos crudos: '{log_sucio}'. Extrae solo la línea técnica del fallo crítico."
    return llamar_ia_con_reintento(prompt)

def agente_2_analista_causa_raiz(error_puro):
    """Explica claramente por qué se rompió el sistema[cite: 10]."""
    prompt = f"Eres un Analista de Causa Raíz (SRE). Explica en lenguaje humano por qué falló el sistema basándote en: '{error_puro}'."
    return llamar_ia_con_reintento(prompt)

def agente_3_ingeniero_resoluciones(diagnostico):
    """Propone acciones correctivas y comandos exactos para restaurar el servicio[cite: 11]."""
    prompt = f"Eres un Ingeniero de Resoluciones. Proporciona comandos de consola y pasos técnicos para solucionar: '{diagnostico}'."
    return llamar_ia_con_reintento(prompt)

def agente_4_coordinador_soporte(data_parseo, data_analisis, data_solucion):
    """Redacta un ticket estructurado y profesional[cite: 12]."""
    prompt = f"Eres un Coordinador de Soporte IT. Redacta un ticket profesional con estos datos: Error: {data_parseo}, Análisis: {data_analisis}, Solución: {data_solucion}."
    return llamar_ia_con_reintento(prompt)

# 2. EJECUCIÓN DEL FLUJO [cite: 13, 30]
if __name__ == "__main__":
    log_entrada = "3:00 AM - INFO: Booting... 3:02 AM - FATAL: password authentication failed for user 'postgres'"
    
    print("🚀 INICIANDO SISTEMA MULTI-AGENTE: RESPUESTA A INCIDENTES\n")
    
    # Paso 1: Parseo [cite: 17, 18]
    error_extraido = agente_1_especialista_parseo(log_entrada)
    print(f"✅ Agente 1 (Parseo): {error_extraido}\n")
    
    # Paso 2: Análisis [cite: 19, 21]
    analisis = agente_2_analista_causa_raiz(error_extraido)
    print(f"✅ Agente 2 (Analista): {analisis}\n")
    
    # Paso 3: Solución [cite: 22, 25]
    solucion = agente_3_ingeniero_resoluciones(analisis)
    print(f"✅ Agente 3 (Ingeniero): {solucion}\n")
    
    # Paso 4: Coordinación y Ticket Final [cite: 26, 30]
    ticket_final = agente_4_coordinador_soporte(error_extraido, analisis, solucion)
    print("📝 TICKET DE SOPORTE SRE GENERADO:\n")
    print(ticket_final)
