import os
from core.menu import display_menu, handle_choice
from colorama import init, Fore

# Inisialisasi warna untuk Windows/Linux/Termux
init(autoreset=True)

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        display_menu()
        
        print(f"\n{Fore.GREEN}123Tool {Fore.WHITE}> {Fore.YELLOW}", end="")
        user_input = input().strip()
        
        if user_input.startswith("set_install"):
            parts = user_input.split()
            if len(parts) > 1:
                handle_choice(parts[1])
            else:
                print(f"{Fore.RED}[!] Gunakan format: set_install [nomor]")
                import time; time.sleep(2)
        else:
            handle_choice(user_input)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Berhenti paksa.")
        exit()
