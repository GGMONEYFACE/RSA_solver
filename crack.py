import RSA_script, Helpful, helppage, mymath

#Quits from module back to main menu
def quit_to_menu():
    print(Helpful.REDTEXT + "[!] Quitting to Menu..." + Helpful.RETURNDEFAULTCOLOR)
    RSA_script.pick_module()




def find_q():
    N = int(input("Please provide N: "))
    yes_no = input("Do you know either p or q? (y/n) ").lower()
    if yes_no == "y":
        p = int(input("Please provide the prime: "))
        print(f"Calculating q using N/p...")
        q = mymath.find_q(N, p)
        print(f"q = {q}")


def find_d():
    print("This module is still in development, but will eventually be able to find the private exponent d using various methods.")
    RSA_script.quit_to_menu()

#Menu to pick what you want to crack.
def pick_mode():
    Helpful.block("Pick a Mode")
    print("  [1] Find q\n  [2] Find d\n  [H] Help Page\n  [Q] Quit Program")
    answer = str(input("Module: ")).upper()
    while answer not in crack_handlers:
        print(f"{Helpful.REDTEXT}THAT IS NOT A VALID ANSWER >:[{Helpful.RETURNDEFAULTCOLOR}")
        answer = str(input("Module: ")).upper()
    handler = crack_handlers[answer]
    handler()

crack_handlers = {
    "1": find_q,
    "2": find_d,
    "Q": quit_to_menu,
#    "H": helppage.helppage
}

