import os
import sys
import time
import asyncio

# Import compiled modules
import rana
import master
import web2

# ===== Color =====
CYAN = "\033[96m"
RESET = "\033[0m"

# ===== Clear Screen =====
def clear():
    os.system("clear" if os.name == "posix" else "cls")

# ===== Typing Animation =====
def typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ===== Loading Animation =====
def loading():
    for i in range(3):
        sys.stdout.write(CYAN + "\rLoading" + "." * (i + 1) + RESET)
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

# ===== Banner =====
def banner():
    print(CYAN + """
███╗   ███╗ █████╗ ██████╗      ██████╗ ██████╗ 
████╗ ████║██╔══██╗██╔══██╗     ██╔══██╗██╔══██╗
██╔████╔██║███████║██████╔╝     ██████╔╝██║  ██║
██║╚██╔╝██║██╔══██║██╔══██╗     ██╔═══╝ ██║  ██║
██║ ╚═╝ ██║██║  ██║██║  ██║     ██║     ██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═════╝
""" + RESET)
    typing("Author: Rana\n")

# ===== Safe Run for both normal & async main =====
def safe_run(module):
    try:
        loading()
        # Check if main is coroutine
        if asyncio.iscoroutinefunction(module.main):
            asyncio.run(module.main())
        else:
            module.main()
    except AttributeError:
        typing("Error: main() not found inside module!")
    except Exception as e:
        typing(f"Runtime Error: {e}")

# ===== Menu =====
def menu():
    while True:
        print(CYAN + "Choose now:" + RESET)
        print("[1] Master")
        print("[2] Rana")
        print("[3] Web2")
        print("[0] Exit\n")

        choice = input(CYAN + "Enter choice: " + RESET)

        if choice == "1":
            safe_run(master)
        elif choice == "2":
            safe_run(rana)
        elif choice == "3":
            safe_run(web2)
        elif choice == "0":
            typing("Goodbye! Allah Hafez 💝")
            break
        else:
            typing("Invalid option! Try again.")

# ===== Main =====
if __name__ == "__main__":
    clear()
    banner()
    menu()
