import logging
import os

# Define la ruta del archivo de log
log_directory = "/home/kali/logs"  # Cambia esta línea si deseas otra ubicación
log_file = "network_traffic.log"
log_path = os.path.join(log_directory, log_file)

# Asegúrate de que el directorio existe
os.makedirs(log_directory, exist_ok=True)

# Configura el logging
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ejemplo de uso del logging
logging.info("Inicio de la actividad de monitoreo de tráfico de red.")

try:
    # Aquí iría el código para monitorear tráfico de red
    logging.info("Monitoreando tráfico...")
    
    # Simula algún procesamiento
    for i in range(5):
        logging.info(f"Paquete {i + 1} procesado.")

except Exception as e:
    logging.error(f"Ocurrió un error: {e}")

logging.info("Finalización de la actividad de monitoreo de tráfico de red.")
