# Importar las bibliotecas necesarias
from scapy.all import sniff, IP, TCP
import logging

# Configurar el archivo de logs donde se guardará el tráfico capturado
logging.basicConfig(filename="C:/Users/Brais/Desktop/network_traffic.log", level=logging.INFO, 
                    format="%(asctime)s - %(message)s")


# Solicitar la dirección IP a monitorear
ip_to_monitor = input("Introduce la dirección IP que deseas monitorear: ")

# Función que procesa cada paquete capturado
def packet_callback(packet):
    # Verificar si el paquete tiene capa IP y TCP (para analizar tráfico TCP)
    if IP in packet and TCP in packet:
        ip_src = packet[IP].src  #https://nmap.org/npcap/ Dirección IP de origen
        ip_dst = packet[IP].dst  # Dirección IP de destino
        port_src = packet[TCP].sport  # Puerto de origen
        port_dst = packet[TCP].dport  # Puerto de destino

        # Filtrar solo los paquetes que involucran la IP a monitorear
        if ip_src == ip_to_monitor or ip_dst == ip_to_monitor:
            # Mostrar información relevante del paquete en pantalla
            print(f"[+] Paquete capturado: {ip_src}:{port_src} -> {ip_dst}:{port_dst}")

            # Registrar la información del tráfico en el archivo de logs
            logging.info(f"IP Origen: {ip_src}:{port_src} -> IP Destino: {ip_dst}:{port_dst}")

# Capturar tráfico en tiempo real, aplicando un filtro para paquetes IP
print(f"Monitoreando tráfico de red para la IP {ip_to_monitor}...")
sniff(prn=packet_callback, filter=f"ip host {ip_to_monitor}", store=0)
