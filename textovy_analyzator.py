"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Michal Kubín
email: kubin.michal@gmail.com
discord: Michal Kubín #0577
"""

import task_template as tt
import users

separator = "-" * 10

# Vyžádá si od uživatele přihlašovací jméno a heslo

login = input("Please insert your login: ")

# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,

if str(login) in users.logins:
    password = input("Please insert your password: ")

    # pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,

    if str(password) in users.users[str(login)]:

        print("Hi! Welcome in Text Analyser!")
        print(f"For a text analysis you can choose from these text:\n")
        print(f"No. 1: {tt.TEXTS[0]}")
        print(f"No. 2: {tt.TEXTS[1]}")
        print(f"No. 3: {tt.TEXTS[2]}")
        print(separator)
        chosen_text = input("Please choose one of these texts for follow-up "
                            "analysis (use numbers 1/2/3): ")

        # pokud uživatel zadal špatný vstup nebo číslo mimo hranici,
        # upozorni ho a ukonči program

        if str(chosen_text).isdecimal() is False or int(chosen_text) < 1 or \
                int(chosen_text) > 3:
            print("Wrong value entered. Terminating the program..")

        # pokud vybral správně, zahaj analýzu textu

        else:
            print(f"Your choice: text No. {chosen_text}. Initiating "
                  f"analysis..")
            print(separator)

        # Pro vybraný text spočítá následující statistiky:

            analyzed_text = tt.TEXTS[int(chosen_text)-1]

            # odstraní tečky, čárky a pomlčky

            for forbidden_character in analyzed_text:
                if forbidden_character == "." or forbidden_character == ",":
                    analyzed_text = str(analyzed_text).replace(
                        forbidden_character, "")
                elif forbidden_character == "-":
                    analyzed_text = str(analyzed_text).replace(
                        forbidden_character, " ")
                elif forbidden_character == "\n":
                    analyzed_text = str(analyzed_text).replace(
                        forbidden_character, " ")

            analyzed_text = analyzed_text.rsplit(" ")

            # odstraní uvozovky na začátku a na konci textu, které po
            # rozdělení vytvoří samostatné znaky

            for forbidden_space in analyzed_text:
                if forbidden_space == '':
                    analyzed_text.remove('')

            # počet slov,

            word_count = len(analyzed_text)
            print(f"There are {word_count} words in the selected text.")

            # počet slov začínajících velkým písmenem,

            print(analyzed_text)

            # počet slov psaných velkými písmeny,

            # počet slov psaných malými písmeny,

            # počet čísel (ne cifer),

            # sumu všech čísel (ne cifer) v textu.


    # pokud nesedí login a heslo, upozorni uživatele a ukonči program

    else:
        print("Login details do not match. Terminating the program..")

# pokud není registrovaný, upozorni jej a ukonči program.

else:
    print("Unregistered user, terminating the program..")