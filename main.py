import os
import time
import schedule
import requests
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
from cerebro import create_chatbot # Reutilizamos nuestro cerebro

# --- 1. CONFIGURACIÓN INICIAL ---
load_dotenv()
print(">>> INICIANDO AGENTE DE TIKTOK <<<")

# --- Variables de Entorno (las obtendremos del portal de TikTok) ---
TIKTOK_CLIENT_ID = os.environ.get('TIKTOK_CLIENT_ID')
TIKTOK_CLIENT_SECRET = os.environ.get('TIKTOK_CLIENT_SECRET')
TIKTOK_ACCESS_TOKEN = os.environ.get('TIKTOK_ACCESS_TOKEN') # Este lo guardaremos y refrescaremos

# --- Variables Globales ---
# Guardaremos el ID de los comentarios ya respondidos para no repetir.
# En el futuro, esto vivirá en nuestra base de datos PostgreSQL.
comentarios_respondidos = set()

# Inicializamos nuestro cerebro de IA una sola vez
cerebro_ia = create_chatbot(session_id="tiktok_agent_global")

# --- 2. LA FUNCIÓN PRINCIPAL DEL VIGILANTE ---
def revisar_comentarios_tiktok():
    """
    Esta es la función principal. Se conecta a TikTok, busca comentarios nuevos,
    los procesa con la IA y publica las respuestas.
    """
    print("\n--- [CICLO INICIADO] Buscando nuevos comentarios... ---")
    
    # --- AQUÍ IRÁ LA LÓGICA PARA CONECTARSE A TIKTOK ---
    # Por ahora, simularemos que encontramos un comentario.
    
    simular_comentario_nuevo() # Esta es una función de prueba temporal

    print("--- [CICLO FINALIZADO] Esperando al siguiente intervalo. ---")


# --- 3. FUNCIÓN DE SIMULACIÓN (PARA PRUEBAS) ---
def simular_comentario_nuevo():
    """
    Esta función temporal simula la llegada de un nuevo comentario
    para que podamos probar que el cerebro funciona.
    """
    id_comentario_simulado = "12345"
    texto_comentario_simulado = "¿Cuánto cuesta el plan básico?"

    if id_comentario_simulado not in comentarios_respondidos:
        print(f"  [!] Nuevo comentario encontrado (ID: {id_comentario_simulado}): '{texto_comentario_simulado}'")
        
        # Pasamos el comentario al cerebro de IA
        respuesta_ia = cerebro_ia.invoke({"question": texto_comentario_simulado})
        
        print(f"  [->] Respuesta generada por la IA: '{respuesta_ia}'")
        
        # --- AQUÍ IRÁ EL CÓDIGO PARA PUBLICAR LA RESPUESTA EN TIKTOK ---
        print("  [OK] (Simulación) Respuesta publicada en TikTok.")

        # Añadimos el ID a nuestra lista para no volver a responderlo
        comentarios_respondidos.add(id_comentario_simulado)
    else:
        print("  [-] No hay comentarios nuevos.")


# --- 4. EL BUCLE INFINITO DEL VIGILANTE ---
if __name__ == '__main__':
    # Le decimos a 'schedule' que ejecute nuestra función 'revisar_comentarios_tiktok'
    # cada 60 segundos.
    schedule.every(60).seconds.do(revisar_comentarios_tiktok)
    
    print(">>> Agente configurado. El primer ciclo comenzará en 60 segundos. <<<")

    # Bucle principal que mantiene el script vivo y ejecutando las tareas programadas.
    while True:
        schedule.run_pending()
        time.sleep(1)
