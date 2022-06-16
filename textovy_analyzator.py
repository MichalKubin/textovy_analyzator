"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Michal Kubín
email: kubin.michal@gmail.com
discord: Michal Kubín#0577
"""

import task_template as tt
import users

# Vyžádá si od uživatele přihlašovací jméno a heslo

login = input("Please insert your login: ")

# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
if str(login) in users.logins:
    password = input("Please insert your password: ")

    # pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
    if str(password) in users.users[str(login)]:

        print("Hi! Welcome in Text Analyser!")
        chosen_text = input("Please choose one of three text for follow-up "
                            "analysis (use numbers 1/2/3): ")

        # pokud uživatel zadal špatný vstup nebo číslo mimo hranici,
        # upozorni ho a ukonči program
        if str(chosen_text).isdecimal() is False or int(chosen_text) < 1 or \
                int(chosen_text) > 3:
            print("Wrong value entered. Terminating the program..")

        # pokud vybral správně, zahaj analázu textu
        else:
            print(f"Your choice: text No. {chosen_text}. Initiating "
                  f"analysis..")


    # pokud nesedí login a heslo, upozorni uživatele a ukonči program
    else:
        print("Login details do not match. Terminating the program..")

# pokud není registrovaný, upozorni jej a ukonči program.
else:
    terminate_txt = "Unregistered user, terminating the program.."
    print(terminate_txt)