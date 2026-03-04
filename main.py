import os
import sys
import time

# Import compiled modules
import rana
import master
import web2

CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def typing(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading():
    for i in range(3):
        sys.stdout.write(CYAN + "\rLoading" + "." * (i + 1) + RESET)
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

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

def safe_run(module):
    try:
        loading()
        module.main()
    except AttributeError:
        typing("Error: main() not found inside .so file!")
    except Exception as e:
        typing(f"Runtime Error: {e}")

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
            typing("Goodbye Master 💝 Allah Hafez")
            break
        else:
            typing("Invalid option!")

if __name__ == "__main__":
    clear()
    banner()
    menu()
