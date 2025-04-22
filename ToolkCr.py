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

# Footer definition (added)
FOOTER = """
████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████
"""

def clear_screen():
    os.system('clear')

def show_banner(title=""):
    clear_screen()
    print(BANNER)
    if title:
        print(f"\n{title}\n")
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
    if pwd == "Kali linux":
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
    if pwd == "PARROT OS":
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
            termux_menu()  # Needs to be defined
        elif choice == "2":
            kali_menu()  # Needs to be defined
        elif choice == "3":
            parrot_menu()  # Needs to be defined
        elif choice == "4":
            install_packages()
        elif choice == "5":
            break
        else:
            print("Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
