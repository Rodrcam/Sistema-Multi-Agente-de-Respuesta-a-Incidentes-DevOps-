# 🚀 Sistema Multi-Agente de Respuesta a Incidentes (SRE-AI)

- Este proyecto es un sistema **Multi-Agente** diseñado para automatizar la fase de investigación y diagnóstico de errores en entornos DevOps. Utilizando la potencia de **Gemini 3 Flash**, el sistema ingiere logs técnicos complejos, aísla el fallo crítico, traduce el problema a lenguaje humano y genera un ticket de soporte con soluciones técnicas inmediatas.

## 📋 Descripción del Sistema
- El sistema transforma registros de sistema "sucios" en reportes estructurados en cuestión de segundos, reduciendo drásticamente el tiempo de reparación (MTTR).

## 🤖 Los 4 Agentes (Pipeline de Inteligencia)
- ]Siguiendo el flujo de trabajo definido en el manual de **Respuesta a Incidentes**:

1.  **Especialista en Parseo de Logs**: Limpia los datos crudos, descarta mensajes informativos (INFO/DEBUG) y extrae la línea técnica del fallo crítico.
2.  **Analista de Causa Raíz (SRE)**: Traduce el código de error a lenguaje humano y explica por qué colapsó el sistema.
3.  **Ingeniero de Resoluciones**: Propone las acciones correctivas y los comandos de consola exactos (Linux, Docker, Kubernetes) para restaurar el servicio.
4.  **Coordinador de Soporte IT**: Recopila el trabajo de los agentes anteriores y redacta un ticket de incidencia profesional y estructurado.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje**: Python 3.13
* **IA**: Google Gemini 3 Flash Preview
* **SDK**: `google-genai` (Versión 2026)

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
   cd nombre-del-repo

2. **Instalar dependencias:**
   ```bash
   pip install -U google-genai
3. **Configurar API Key:**
   Crea un archivo .env o configura tu variable de entorno:
   ```bash
   export GOOGLE_API_KEY='TU_CLAVE_DE_API'
4. **Ejecutar:**
   ```bash
   python main.py
   
