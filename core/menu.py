import json
import os
from core.banner import show_banner
from core.installer import execute_cmd
from colorama import Fore, Style

def load_tools():
    data_path = os.path.join('data', 'tools.json')
    with open(data_path, 'r') as f:
        return json.load(f)

def display_menu():
    show_banner()
    tools = load_tools()
    
    menu_list = [
        "Information Gathering", "Vulnerability Analysis", "Web Hacking",
        "Database Assessment", "Password Attacks", "Wireless Attacks",
        "Reverse Engineering", "Exploitation Tools", "Sniffing and Spoofing",
        "Reporting Tools", "Forensic Tools", "Stress Testing",
        "Install Linux Distro", "Termux Utility", "Shell Function [.bashrc]",
        "Install CLI Games", "Malware Analysis", "Compiler/Interpreter",
        "Social Engineering Tools"
    ]

    for i, name in enumerate(menu_list, 1):
        num = str(i).zfill(2)
        print(f"{Fore.GREEN}[{num}] {Fore.WHITE}{name}")

    print(f"\n{Fore.GREEN}[99] {Fore.WHITE}Update the xhackTool")
    print(f"{Fore.GREEN}[00] {Fore.WHITE}Exit the xhackTool")

def handle_choice(choice):
    tools = load_tools()
    if choice in tools:
        tool = tools[choice]
        print(f"\n{Fore.YELLOW}[*] Menjalankan instalasi: {tool['name']}...")
        execute_cmd(tool['cmd'])
        input(f"\n{Fore.GREEN}[+] Selesai. Tekan Enter untuk kembali...")
    elif choice == "00":
        print(f"{Fore.RED}Sampai jumpa, Rolandino!")
        exit()
    elif choice == "99":
        print(f"{Fore.BLUE}[*] Checking for updates...")
        execute_cmd("git pull")
    else:
        print(f"{Fore.RED}[!] Menu {choice} belum tersedia di database data/tools.json")
        input("\nTekan Enter untuk kembali...")
