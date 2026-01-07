'''
This program is currently in development but will eventually (hopefully) be an all-inclusive tool to solve RSA encyption CTF challenges
'''

#!/usr/bin/env python3
####################################################
## Authors: GGMONEYFACE                           ##
## Purpose: An RSA program for training/CTFs      ##
####################################################

#Imports and globals
import argparse, hashlib, random, sys, os, shutil, Helpful, mymath, crack

REDTEXT = Helpful.REDTEXT
GREENTEXT = Helpful.GREENTEXT
YELLOWTEXT = Helpful.YELLOWTEXT
BLUETEXT = Helpful.BLUETEXT
RETURNDEFAULTCOLOR = Helpful.RETURNDEFAULTCOLOR
block = Helpful.block

FILEPATH = "./resources/helppage.txt" #Path to help page




# Helper to read an integer from input with validation
def read_int_prompt(prompt):
    while True:
        try:
            val = input(prompt)
        except KeyboardInterrupt:
            print()  # move to next line
            print(REDTEXT + "[!] Input cancelled. Returning to menu..." + RETURNDEFAULTCOLOR)
            quit_to_menu()

        try:
            return int(val)
        except ValueError:
            print(REDTEXT + "Invalid input. Please enter an integer value." + RETURNDEFAULTCOLOR)





def main_crack():
    block("Crack RSA")
    crack.pick_mode()




def create():
    block("Create RSA")
    print(GREENTEXT + "Choose two prime numbers. 'q' should be larger than 'p'." + RETURNDEFAULTCOLOR)
    p = read_int_prompt("p: ")
    q = read_int_prompt("q: ")
    while q <= p:
        print(REDTEXT + "'q' must be larger than 'p'." + RETURNDEFAULTCOLOR)
        q = read_int_prompt("q: ")
    n = p * q
    ϕ = (p - 1) * (q - 1)
    print(f"n: {n}")
    print(f"ϕ: {ϕ}")
    while True:
        e = read_int_prompt("Choose a public exponent e (1 < e < ϕ and gcd(e, ϕ) = 1): ")
        if not (1 < e < ϕ):
            print(REDTEXT + "e must satisfy 1 < e < ϕ." + RETURNDEFAULTCOLOR)
            continue
        d = mymath.findModInverse(e, ϕ)
        if d is None:
            print(REDTEXT + "Invalid choice of e. It must be coprime to ϕ." + RETURNDEFAULTCOLOR)
            continue
        break
    block(f"Public key: (e={e}, n={n})\nPrivate key: (d={d}, n={n})")
    

    #print("This module is still in development, but will eventually be able to create RSA encyption using various methods.")
    quit_to_menu()



#Function for showing the help page
def helppage():
    # Displays the content of a file one screen at a time.
    if not os.path.exists(FILEPATH):
        print(f"Error: The file '{FILEPATH}' does not exist.")
        return

    # Get the terminal size (rows). Fallback to 12 rows if detection fails.
    try:
        rows = shutil.get_terminal_size(fallback=(80, 24)).lines
        # keep a conservative page size so prompt fits
        rows = max(6, rows)  # at least 6 lines
    except Exception:
        rows = 12

    with open(FILEPATH, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        current_line = 0
        while current_line < len(lines):
            # Print a page of lines (use write+flush so we control output)
            for i in range(rows - 1):  # reserve one line for the prompt
                idx = current_line + i
                if idx < len(lines):
                    sys.stdout.write(lines[idx])
            sys.stdout.flush()

            # If we've reached the end of the file, show message and exit
            if current_line + (rows - 1) >= len(lines):
                print("\nEnd of file. Press ENTER to exit.")
                input()
                break

            # Build prompt and show it (no newline)
            pct = int((current_line / max(1, len(lines))) * 100)
            prompt = f"--More-- ({pct}%) -- press ENTER to continue, 'q' to quit --"
            sys.stdout.write(prompt)
            sys.stdout.flush()

            user_input = input()  # user types, cursor moves to new line

            # Move cursor up one line and clear that line so prompt disappears
            # \x1b[1A -> move cursor up 1 line
            # \x1b[2K -> clear entire line
            sys.stdout.write('\x1b[1A' + '\x1b[2K')
            sys.stdout.flush()

            if user_input.lower() == 'q':
                break

            current_line += (rows - 1)

#Function for quitting the program (just for organizational / readability)
def quitter():
    print(REDTEXT + "[!] Quitting..." + RETURNDEFAULTCOLOR)
    print("Feel free to reachout if you have any suggestions! email:gspris5694@ung.edu")
    sys.exit(0)

#Quits from module back to main menu
def quit_to_menu():
    print(REDTEXT + "[!] Quitting to Menu..." + RETURNDEFAULTCOLOR)
    pick_module()

#Menu to pick what you want to work on.
def pick_module():
    #finished = check_modules()
    #while finished == False: #tracks total points until all modules are complete. 
        block("Pick a Mode")
        print("  [1] Crack RSA\n  [2] Create RSA\n  [H] Help Page\n  [Q] Quit Program")
        answer = str(input("Module: ")).upper()
        while answer not in menu_handlers:
            print(f"{REDTEXT}THAT IS NOT A VALID ANSWER >:[{RETURNDEFAULTCOLOR}")
            answer = str(input("Module: ")).upper()
        handler = menu_handlers[answer]
        handler() 

#Defines handlers to make menu... better?
menu_handlers = {
    "1": main_crack,
    "2": create,
    "Q": quitter,
    "H": helppage
}

#Main...
def main():
    block("Preparing the RSA Solver")
    while True:
        pick_module()


if __name__ == '__main__':
    main()

