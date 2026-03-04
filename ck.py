import os
import sys
import time
import rana
import master

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

# ===== Menu =====
def menu():
    while True:
        print(CYAN + "Choose now:" + RESET)
        print(CYAN + "[1] Master")
        print("[2] Run (Rana)")
        print("[0] Exit\n" + RESET)

        choice = input(CYAN + "Enter your choice: " + RESET)

        if choice == "1":
            loading()
            master.main()
        elif choice == "2":
            loading()
            rana.main()
        elif choice == "0":
            typing("Goodbye Master allah hafez 💝")
            break
        else:
            typing("Invalid choice! Try again.")

# ===== Main =====
if __name__ == "__main__":
    clear()
    banner()
    menu()
