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

    if str(password) in users.users[str(login)]:
        print("Yes")
    else:
        print("Login details do not match. Terminating the program..")


# pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,

# pokud není registrovaný, upozorni jej a ukonči program.
else:
    terminate_txt = "Unregistered user, terminating the program.."
    print(terminate_txt)


