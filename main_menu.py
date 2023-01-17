from pyfiglet import Figlet
import os

def menu():
    map = "circle"
    while 1:
        os.system("cls||clear")
        title = Figlet()
        print(title.renderText("Titris"))
        print()
        print("1. Jouer")
        print("2. Paramètres")
        print("3. Quitter")
        print()

        choice = -1

        while choice < 1 or choice > 3:
            choice = int(input("Que voulez-vous faire : ")) 

        if choice == 1:
            return map
        elif choice == 2:
            map = settings(map)
        elif choice == 3:
            exit(0)



settings_conf = {
    1: "circle",
    2: "diamond",
    3: "triangle"
}

def settings(map):
    os.system("cls||clear")
    title = Figlet()
    print(title.renderText("Parametres"))
    print()
    print("1. Terrain en cercle")
    print("2. Terrain en losange")
    print("3. Terrain en triangle")
    print()
    print(f"(Le terrain actuel est : {map})")
    print()

    choice = -1

    while choice < 1 or choice > 3:
        choice = int(input("Quelle map choisissez-vous : "))
    
    return settings_conf[choice]