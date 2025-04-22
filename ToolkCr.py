import os
import subprocess
import time
from termcolor import colored

FOOTER = "║ Select an option and press Enter"

# Limpia la pantalla
def clear_screen():
    os.system("clear")

# Muestra el banner de la herramienta
def show_banner(title):
    clear_screen()
    print(f"""
╔════════════════════════════════════╗
║          TOOLKIT CROW              ║
║         {title.center(30)}         ║
╚════════════════════════════════════╝
""")

# Pregunta si continuar o regresar al menú
def ask_continue_or_back():
    c = input("Continue? (Y/n): ").lower()
    return c in ["", "y", "yes"]

# Instalación masiva de paquetes en Termux
def install_all_packages():
    show_banner("INSTALLATION")
    print("Warning: Mass installation of all packages (T/K/P). This will attempt to install every available package in Termux. Some packages may not be useful and could take up significant storage space.")
    
    confirm = input("Are you sure you want to install ALL packages, including unnecessary ones? (Y/n): ").lower()
    if confirm not in ["", "y", "yes"]:
        print("Installation aborted.")
        return
    
    # Actualiza los paquetes primero
    subprocess.run("pkg update && pkg upgrade -y", shell=True)
    print("Starting installation of all available packages...")
    
    # Lista todos los paquetes disponibles en Termux
    packages = subprocess.run("pkg list-all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if packages.returncode == 0:
        all_pkgs = packages.stdout.decode("utf-8").splitlines()
        for pkg in all_pkgs:
            subprocess.run(f"pkg install {pkg} -y", shell=True)
    
    print("All available packages have been installed.")
    input("Press Enter to return to menu...")

# Funciones de cada herramienta de Termux
def nmap_scan():
    print("Iniciando Nmap... Nmap es una herramienta de escaneo de redes que detecta dispositivos y servicios en una red.")
    print("Funciona enviando paquetes a una IP y analizando las respuestas para determinar qué puertos están abiertos y qué servicios están activos.")
    os.system("nmap -v")

def metasploit_console():
    print("Iniciando Metasploit... Metasploit es un framework para pruebas de penetración y explotación de vulnerabilidades.")
    print("Permite a los usuarios buscar vulnerabilidades, explotarlas y generar payloads para obtener acceso no autorizado a un sistema.")
    os.system("msfconsole")

def ddos_attack():
    print("Iniciando ataque DDoS... El ataque DDoS intenta sobrecargar un servidor o red enviando tráfico masivo para que el servidor quede fuera de servicio.")
    print("Esta herramienta genera un gran volumen de solicitudes para agotar los recursos de un servidor.")
    os.system("ddos-attack")

def dos_attack():
    print("Iniciando ataque DoS... Un ataque de denegación de servicio intenta hacer que un servicio sea inaccesible mediante el envío de tráfico excesivo.")
    print("A diferencia del DDoS, DoS es un ataque de un solo origen, pero igualmente busca interrumpir la disponibilidad del servicio.")
    os.system("dos")

def aircrack_ng():
    print("Iniciando Aircrack-ng... Aircrack-ng es una suite de herramientas para auditoría de redes Wi-Fi.")
    print("Permite capturar paquetes de redes Wi-Fi, realizar ataques de fuerza bruta sobre contraseñas WPA y WEP, y comprobar la seguridad de las redes inalámbricas.")
    os.system("aircrack-ng")

def hydra_attack():
    print("Iniciando Hydra... Hydra es una herramienta de fuerza bruta que permite probar múltiples contraseñas en diferentes protocolos.")
    print("Utiliza un diccionario de contraseñas para intentar acceder a servicios como SSH, FTP, HTTP, y otros protocolos de red.")
    os.system("hydra")

def osint_tools():
    print("Iniciando OSINT... Herramientas para recolección de información pública en línea.")
    print("OSINT (Open Source Intelligence) utiliza fuentes abiertas como redes sociales, bases de datos públicas y otros recursos accesibles para recopilar información sobre un objetivo.")
    os.system("osint")

def credits_info():
    print("Mostrando créditos... Aquí se muestra la información sobre los creadores y colaboradores del proyecto.")
    print("Este proyecto fue creado para fines educativos y de pruebas en entornos controlados.")
    os.system("credits")

def scan_ip():
    print("Escaneando IP... Usamos herramientas para verificar la disponibilidad de una IP en la red.")
    print("Este escaneo verifica si una dirección IP está activa y qué servicios están corriendo en ella, útil para mapear redes locales.")
    os.system("scan-ip")

def web_status():
    print("Comprobando el estado web... Usamos herramientas como `curl` para verificar si un sitio web está activo.")
    print("La herramienta realiza una solicitud HTTP a la URL y verifica si la respuesta es exitosa (200 OK) o si hay algún error (404, 500, etc.).")
    os.system("web-status")

def anti_ddos_check():
    print("Verificando protección anti-DDoS... Se revisan configuraciones para mitigar ataques DDoS.")
    print("Esta herramienta verifica la existencia de mecanismos como firewalls y servidores proxy que ayudan a proteger a un sitio web de ataques de denegación de servicio distribuidos.")
    os.system("anti-ddos")

def vuln_scan():
    print("Escaneando vulnerabilidades... Buscando posibles vulnerabilidades de seguridad en sistemas y servicios.")
    print("Esta herramienta realiza un análisis de seguridad para encontrar puntos débiles en sistemas informáticos y redes, ayudando a mejorar la seguridad.")
    os.system("vuln-scan")

def sniffer_tool():
    print("Iniciando Sniffer... Usamos Wireshark o tcpdump para capturar paquetes de red y analizarlos.")
    print("Un 'sniffer' captura y analiza paquetes de datos que viajan por una red. Esto puede ayudar a entender el tráfico o detectar actividades sospechosas.")
    os.system("sniffer")

def https_requests():
    print("Realizando solicitudes HTTPS... Herramienta para analizar y realizar solicitudes HTTPS.")
    print("Esta herramienta permite verificar la seguridad de las comunicaciones HTTPS entre el cliente y el servidor, y realizar pruebas de rendimiento.")
    os.system("https-requests")

def install_packages():
    print("Instalando paquetes... Instalando los paquetes esenciales para herramientas de pruebas de penetración.")
    install_all_packages()

def install_all_termux_packages():
    print("Instalando todos los paquetes de Termux... Instalación masiva de todos los paquetes disponibles.")
    install_all_packages()

# Menú de Termux
def termux_menu():
    while True:
        show_banner("Termux")
        print("""\
║ (1) Nmap 🔍: Escaneo de red
║ (2) Metasploit ⚔️: Framework de explotación
║ (3) DDoS ⚡: Ataque de denegación de servicio distribuido
║ (4) DoS 🔥: Ataque de denegación de servicio
║ (5) Aircrack-ng 📶: Auditoría de redes Wi-Fi
║ (6) Hydra 🔐: Ataque de fuerza bruta
║ (7) OSINT 🕵️: Recolección de información pública
║ (8) Credits 🏷️: Información de créditos
║ (9) Scan IP 🌐: Escaneo de IPs
║ (10) Web status 🌐: Comprobar si un sitio web está activo
║ (11) Anti‑DDoS check 🛡️: Comprobación de protección contra DDoS
║ (12) Sniffer 👻: Captura de paquetes de red
║ (13) Install All Packages 💣: Instalación masiva de paquetes
║ (14) Back ⇦: Volver al menú principal""")
        print(FOOTER)
        choice = input("Select an option: ").strip()  # Eliminar espacios extra
        
        # Ejecutar opciones de menú
        if choice == "1" and ask_continue_or_back():
            nmap_scan()
        elif choice == "2" and ask_continue_or_back():
            metasploit_console()
        elif choice == "3" and ask_continue_or_back():
            ddos_attack()  # Inicia el ataque DDoS en Termux
        elif choice == "4" and ask_continue_or_back():
            dos_attack()  # Inicia el ataque DoS
        elif choice == "5" and ask_continue_or_back():
            aircrack_ng()  # Inicia Aircrack-ng
        elif choice == "6" and ask_continue_or_back():
            hydra_attack()  # Inicia el ataque Hydra
        elif choice == "7" and ask_continue_or_back():
            osint_tools()  # Inicia herramientas OSINT
        elif choice == "8" and ask_continue_or_back():
            credits_info()  # Muestra información de créditos
        elif choice == "9" and ask_continue_or_back():
            scan_ip()  # Escanea IP
        elif choice == "10" and ask_continue_or_back():
            web_status()  # Verifica el estado de un sitio web
        elif choice == "11" and ask_continue_or_back():
            anti_ddos_check()  # Verifica protección contra DDoS
        elif choice == "12" and ask_continue_or_back():
            sniffer_tool()  # Inicia el sniffer de red
        elif choice == "13" and ask_continue_or_back():
            install_all_termux_packages()  # Instalar todos los paquetes disponibles en Termux
        elif choice == "14":
            break  # Regresar al menú principal
        time.sleep(1)

# Menú de Kali Linux (funciones similares a las de Termux)
def kali_menu():
    while True:
        show_banner("Kali Linux")
        print("""\
║ (1) Nmap 🔍: Escaneo de red
║ (2) Metasploit ⚔️: Framework de explotación
║ (3) DDoS ⚡: Ataque de denegación de servicio distribuido
║ (4) DoS 🔥: Ataque de denegación de servicio
║ (5) Aircrack-ng 📶: Auditoría de redes Wi-Fi
║ (6) Hydra 🔐: Ataque de fuerza bruta
║ (7) OSINT 🕵️: Recolección de información pública
║ (8) Credits 🏷️: Información de créditos
║ (9) Scan IP 🌐: Escaneo de IPs
║ (10) Web status 🌐: Comprobar si un sitio web está activo
║ (11) Anti‑DDoS check 🛡️: Comprobación de protección contra DDoS
║ (12) Sniffer 👻: Captura de paquetes de red
║ (13) Install All Packages 💣: Instalación masiva de paquetes
║ (14) Back ⇦: Volver al menú principal""")
        print(FOOTER)
        choice = input("Select an option: ").strip()  # Eliminar espacios extra
        
        # Ejecutar opciones de menú
        if choice == "1" and ask_continue_or_back():
            nmap_scan()
        elif choice == "2" and ask_continue_or_back():
            metasploit_console()
        elif choice == "3" and ask_continue_or_back():
            ddos_attack()  # Inicia el ataque DDoS en Kali
        elif choice == "4" and ask_continue_or_back():
            dos_attack()  # Inicia el ataque DoS
        elif choice == "5" and ask_continue_or_back():
            aircrack_ng()  # Inicia Aircrack-ng
        elif choice == "6" and ask_continue_or_back():
            hydra_attack()  # Inicia el ataque Hydra
        elif choice == "7" and ask_continue_or_back():
            osint_tools()  # Inicia herramientas OSINT
        elif choice == "8" and ask_continue_or_back():
            credits_info()  # Muestra información de créditos
        elif choice == "9" and ask_continue_or_back():
            scan_ip()  # Escanea IP
        elif choice == "10" and ask_continue_or_back():
            web_status()  # Verifica el estado de un sitio web
        elif choice == "11" and ask_continue_or_back():
            anti_ddos_check()  # Verifica protección contra DDoS
        elif choice == "12" and ask_continue_or_back():
            sniffer_tool()  # Inicia el sniffer de red
        elif choice == "13" and ask_continue_or_back():
            install_all_termux_packages()  # Instalar todos los paquetes disponibles
        elif choice == "14":
            break  # Regresar al menú principal
        time.sleep(1)

# Menú de Parrot OS (funciones similares)
def parrot_menu():
    while True:
        show_banner("Parrot OS")
        print("""\
║ (1) Nmap 🔍: Escaneo de red
║ (2) Metasploit ⚔️: Framework de explotación
║ (3) DDoS ⚡: Ataque de denegación de servicio distribuido
║ (4) DoS 🔥: Ataque de denegación de servicio
║ (5) Aircrack-ng 📶: Auditoría de redes Wi-Fi
║ (6) Hydra 🔐: Ataque de fuerza bruta
║ (7) OSINT 🕵️: Recolección de información pública
║ (8) Credits 🏷️: Información de créditos
║ (9) Scan IP 🌐: Escaneo de IPs
║ (10) Web status 🌐: Comprobar si un sitio web está activo
║ (11) Anti‑DDoS check 🛡️: Comprobación de protección contra DDoS
║ (12) Sniffer 👻: Captura de paquetes de red
║ (13) Install All Packages 💣: Instalación masiva de paquetes
║ (14) Back ⇦: Volver al menú principal""")
        print(FOOTER)
        choice = input("Select an option: ").strip()  # Eliminar espacios extra
        
        # Ejecutar opciones de menú
        if choice == "1" and ask_continue_or_back():
            nmap_scan()
        elif choice == "2" and ask_continue_or_back():
            metasploit_console()
        elif choice == "3" and ask_continue_or_back():
            ddos_attack()  # Inicia el ataque DDoS en Parrot
        elif choice == "4" and ask_continue_or_back():
            dos_attack()  # Inicia el ataque DoS
        elif choice == "5" and ask_continue_or_back():
            aircrack_ng()  # Inicia Aircrack-ng
        elif choice == "6" and ask_continue_or_back():
            hydra_attack()  # Inicia el ataque Hydra
        elif choice == "7" and ask_continue_or_back():
            osint_tools()  # Inicia herramientas OSINT
        elif choice == "8" and ask_continue_or_back():
            credits_info()  # Muestra información de créditos
        elif choice == "9" and ask_continue_or_back():
            scan_ip()  # Escanea IP
        elif choice == "10" and ask_continue_or_back():
            web_status()  # Verifica el estado de un sitio web
        elif choice == "11" and ask_continue_or_back():
            anti_ddos_check()  # Verifica protección contra DDoS
        elif choice == "12" and ask_continue_or_back():
            sniffer_tool()  # Inicia el sniffer de red
        elif choice == "13" and ask_continue_or_back():
            install_all_termux_packages()  # Instalar todos los paquetes disponibles en Parrot
        elif choice == "14":
            break  # Regresar al menú principal
        time.sleep(1)

# Llamar al menú de Termux, Kali o Parrot según la selección inicial
def main_menu():
    while True:
        print("""\
(1) Termux
(2) Kali Linux
(3) Parrot OS
(4) Exit""")
        choice = input("Select the environment: ").strip()
        if choice == "1":
            termux_menu()
        elif choice == "2":
            kali_menu()
        elif choice == "3":
            parrot_menu()
        elif choice == "4":
            break

if __name__ == "__main__":
    main_menu()
