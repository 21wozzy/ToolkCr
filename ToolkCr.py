import os
import subprocess
import time

FOOTER = "║ Select an option and press Enter"

def clear_screen():
    os.system("clear")

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

def install_packages():
    show_banner("INSTALLATION")
    print("Installing required packages for Termux, Kali, Parrot...")
    
    # Termux
    subprocess.run("pkg update && pkg upgrade -y", shell=True)
    termux_pkgs = ["sudo", "nmap", "aircrack-ng", "python", "python3-pip", "git", "curl", "wget", "vim", "openssh", "tsu", "net-tools", "unzip", "zip", "htop"]
    for pkg in termux_pkgs:
        subprocess.run(f"pkg install {pkg} -y", shell=True)
    
    # Kali
    subprocess.run("apt update && apt upgrade -y", shell=True)
    kali_pkgs = ["sudo", "nmap", "aircrack-ng", "metasploit-framework", "python3-pip", "git", "curl", "wget", "vim", "net-tools", "unzip", "zip", "htop"]
    for pkg in kali_pkgs:
        subprocess.run(f"apt install {pkg} -y", shell=True)
    
    # Parrot
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
    parrot_pkgs = ["sudo", "nmap", "aircrack-ng", "metasploit-framework", "python3-pip", "git", "curl", "wget", "vim", "net-tools", "unzip", "zip", "htop"]
    subprocess.run("sudo apt install " + " ".join(parrot_pkgs) + " -y", shell=True)

    print("All packages installed.")
    input("Press Enter to return to menu...")

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
║ (13) Back ⇦""")
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
        elif choice == "4":
            if ask_continue_or_back():
                print("Secret option (protected)")  # Aquí va el módulo secreto
        elif choice == "5" and ask_continue_or_back():
            target = input("Target URL/IP: ")
            bots = input("Number of bots (inf for infinite): ")
            if bots == "inf":
                input("Press Enter to start (Ctrl+C to stop)...")
                while True:
                    os.system(f"curl {target} --silent > /dev/null")
            else:
                for _ in range(int(bots)):
                    os.system(f"curl {target}")
        elif choice == "6" and ask_continue_or_back():
            target = input("Target IP: ")
            os.system(f"hping3 --flood --udp {target}")
        elif choice == "7" and ask_continue_or_back():
            url = input("Enter URL: ")
            os.system(f"whatweb {url}")
        elif choice == "8" and ask_continue_or_back():
            target = input("Target IP/Domain: ")
            os.system(f"nmap --script vuln {target}")
        elif choice == "9" and ask_continue_or_back():
            target = input("Target IP/Domain: ")
            os.system(f"nmap -p- {target}")
        elif choice == "10" and ask_continue_or_back():
            os.system("curl ifconfig.me")
        elif choice == "11" and ask_continue_or_back():
            print("Modo peligroso")
            os.system("echo Danger mode activated!")  # Sustituir por módulo real
        elif choice == "12":
            install_packages()
        elif choice == "13":
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
        
        if choice == "1" and ask_continue_or_back():
            os.system("nmap -h")
        elif choice == "2" and ask_continue_or_back():
            os.system("msfconsole")
        elif choice == "3" and ask_continue_or_back():
            target = input("Target URL/IP: ")
            bots = input("Bots (inf): ")
            if bots == "inf":
                input("Enter→start, Ctrl+C→stop")
                while True:
                    os.system(f"curl {target}")
            else:
                for _ in range(int(bots)):
                    os.system(f"curl {target}")
        elif choice == "4" and ask_continue_or_back():
            ip = input("Enter IP: ")
            os.system(f"hping3 --flood --udp {ip}")
        elif choice == "5" and ask_continue_or_back():
            os.system("aircrack-ng --help")
        elif choice == "6" and ask_continue_or_back():
            os.system("hydra -h")
        elif choice == "7" and ask_continue_or_back():
            os.system("theHarvester -h")
        elif choice == "8":
            clear_screen()
            print("Created by crowley and szkryy")
            input("Press Enter to go back...")
        elif choice == "9" and ask_continue_or_back():
            ip = input("Enter IP: ")
            os.system(f"nmap {ip}")
        elif choice == "10" and ask_continue_or_back():
            web = input("Enter URL: ")
            os.system(f"curl -I {web}")
        elif choice == "11" and ask_continue_or_back():
            web = input("Enter URL: ")
            os.system(f"whatweb {web}")
        elif choice == "12" and ask_continue_or_back():
            dom = input("Enter IP/Domain: ")
            os.system(f"nmap --script vuln {dom}")
        elif choice == "13" and ask_continue_or_back():
            os.system("tcpdump -c 100")
        elif choice == "14" and ask_continue_or_back():
            url = input("Enter URL: ")
            os.system(f"httpie {url}")
        elif choice == "15" and ask_continue_or_back():
            print("Modo peligroso")
        elif choice == "16":
            install_packages()
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
        
        if choice == "17" and ask_continue_or_back():
            print("Modo peligroso")
        elif choice == "18":
            install_packages()
        elif choice == "19":
            break
        else:
            print("Option under development...")
        time.sleep(1)

def main_menu():
    while True:
        show_banner("MAIN MENU")
        print("""\
║ (1) Termux 📱
║ (2) Kali Linux 🐉
║ (3) Parrot OS 🦜
║ (4) Install All Packages 📦
║ (5) Exit ❌""")
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
            print("Goodbye, hackercito hermoso!")
            break
        time.sleep(1)

if __name__ == "__main__":
    main_menu()
