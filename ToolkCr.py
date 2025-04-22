import os
import subprocess
import time
from termcolor import colored

FOOTER = "║ Select an option and press Enter"
def clear_screen(): os.system("clear")
def show_banner(title): 
    clear_screen()
    print(f"""
╔════════════════════════════════════╗
║          TOOLKIT CROW              ║
║         {title.center(30)}         ║
╚════════════════════════════════════╝
""")

def ask_continue_or_back():
    c = input("Continue? (Y/n): ").lower()
    return c in ["", "y", "yes"]

def install_all_packages():
    show_banner("INSTALLATION")
    print("Warning: Mass installation of packages (T/K/P). This will install every available package in Termux. Some may be unnecessary or redundant.")
    
    confirm = input("Are you sure you want to install ALL packages? (Y/n): ").lower()
    if confirm not in ["", "y", "yes"]:
        print("Installation aborted.")
        return
    
    # Actual mass installation of packages
    subprocess.run("pkg update && pkg upgrade -y", shell=True)
    print("Starting installation of all available packages...")
    
    # List all available packages in Termux and install them
    packages = subprocess.run("pkg list-all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if packages.returncode == 0:
        all_pkgs = packages.stdout.decode("utf-8").splitlines()
        for pkg in all_pkgs:
            subprocess.run(f"pkg install {pkg} -y", shell=True)
    
    print("All available packages have been installed.")
    input("Press Enter to return to menu...")

def send_ddos_request(target, bot_number):
    """Función que simula el envío de un paquete de DDoS y devuelve si fue exitoso o no."""
    try:
        # Realiza la solicitud HTTP para el bot (simulación)
        result = subprocess.run(f"curl {target} --silent --max-time 5", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            # Si no hubo error, mostrar en verde
            print(colored(f"Bot {bot_number}: Envío exitoso a {target}", "green"))
        else:
            # Si hubo error (protección o fallo), mostrar en rojo
            print(colored(f"Bot {bot_number}: ERROR al enviar a {target}. Posible protección activa.", "red"))
    
    except Exception as e:
        # En caso de error inesperado, también mostramos en rojo
        print(colored(f"Bot {bot_number}: ERROR inesperado: {str(e)}", "red"))

def ddos_attack():
    """Función principal para iniciar el DDoS y registrar cada bot."""
    target = input("Ingresa la URL o IP objetivo: ")
    bots = input("Número de bots (escribe 'inf' para infinito): ")

    if bots == "inf":
        print("Presiona Enter para iniciar el ataque (Ctrl+C para detenerse)...")
        bot_number = 1
        while True:
            send_ddos_request(target, bot_number)
            bot_number += 1
            time.sleep(1)  # Intervalo de 1 segundo entre cada bot
    else:
        for bot_number in range(1, int(bots) + 1):
            send_ddos_request(target, bot_number)
            time.sleep(1)  # Intervalo de 1 segundo entre cada bot

def termux_menu():
    while True:
        show_banner("TERMUX")
        print("""\
║ (1) Sniffer 🕵️‍♂️
║ (2) Check web/IP status 🌐
║ (3) HTTP requests 🔗
║ (4) Secret 🔒
║ (5) DDoS ⚡
║ (6) DoS 🔥
║ (7) Anti‑DDoS check 🛡️
║ (8) Vulnerability scan 🕵️‍♀️
║ (9) Port scan 🌍
║ (10) Show my IP 🌐
║ (11) Danger ☠️
║ (12) Install Packages 📦
║ (13) Install All Packages (Mass Installation) 💣
║ (14) Back ⇦""")
        print(FOOTER)
        choice = input("Select an option: ")
        
        if choice == "1" and ask_continue_or_back():
            os.system("tcpdump -c 100")
        elif choice == "2" and ask_continue_or_back():
            url = input("Enter URL: ")
            os.system(f"curl -Is {url} | head -n1")
        elif choice == "3" and ask_continue_or_back():
            url = input("Enter URL: ")
            os.system(f"httpie {url}")
        elif choice == "5" and ask_continue_or_back():
            ddos_attack()  # Inicia el ataque DDoS con la función que registrará los bots y sus estados
        elif choice == "12":
            install_packages()  # Instalar todos los paquetes necesarios básicos
        elif choice == "13":
            install_all_packages()  # Instalar todos los paquetes disponibles en Termux
        elif choice == "14":
            break
        time.sleep(1)

def kali_menu():
    while True:
        show_banner("KALI LINUX")
        print("""\
║ (1) Nmap 🔍
║ (2) Metasploit ⚔️
║ (3) DDoS ⚡
║ (4) DoS 🔥
║ (5) Aircrack-ng 📶
║ (6) Hydra 🔐
║ (7) OSINT 🕵️
║ (8) Credits 🏷️
║ (9) Scan IP 🌐
║ (10) Web status 🌐
║ (11) Anti‑DDoS check 🛡️
║ (12) Vuln scan 🕵️‍♂️
║ (13) Sniffer 👻
║ (14) HTTPS requests 🔗
║ (15) Danger ☠️
║ (16) Install Packages 📦
║ (17) Back ⇦""")
        print(FOOTER)
        choice = input("Select an option: ")
        
        if choice == "3" and ask_continue_or_back():
            ddos_attack()  # Inicia el ataque DDoS en Kali
        elif choice == "16":
            install_packages()  # Instalar todos los paquetes masivos en Kali
        elif choice == "17":
            break
        time.sleep(1)

def parrot_menu():
    while True:
        show_banner("PARROT OS")
        print("""\
║ (1) Nmap 🔍
║ (2) Metasploit ⚔️
║ (3) DDoS ⚡
║ (4) DoS 🔥
║ (5) Aircrack-ng 📶
║ (6) Hydra 🔐
║ (7) TheHarvester 🕵️
║ (8) OSRFramework 👣
║ (9) Sherlock 🧠
║ (10) Nikto 🧰
║ (11) Exploit DB 🧨
║ (12) WAFW00F 🦺
║ (13) Tor 👻
║ (14) SQLMap 🐍
║ (15) Sniffer 🕳️
║ (16) HTTPie 🔗
║ (17) Danger ☠️
║ (18) Install Packages 📦
║ (19) Back ⇦""")
        print(FOOTER)
        choice = input("Select an option: ")
        
        if choice == "3" and ask_continue_or_back():
            ddos_attack()  # Inicia el ataque DDoS en Parrot
        elif choice == "18":
            install_packages()  # Instalar todos los paquetes masivos en Parrot
        elif choice == "19":
            break
        time.sleep(1)
