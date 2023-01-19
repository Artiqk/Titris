from pyfiglet import Figlet
import os

def menu():
    map_choice = "circle"

    pol = "three_random"

    while 1:
        os.system("cls||clear")
        title = Figlet()
        print(title.renderText("Titris"))
        print()
        print("1. Jouer")
        print("2. Paramètres")
        print("3. Afficher les règles du jeu")
        print("4. Quitter")
        print()

        choice = -1

        while choice < 1 or choice > 4:
            choice = int(input("Que voulez-vous faire : ")) 

        if choice == 1:
            return map_choice, pol
        elif choice == 2:
            map_choice, pol= settings(map_choice)
        elif choice == 3:
            game_rules()
        elif choice == 4:
            exit(0)



settings_conf_map = {
    1: "circle",
    2: "diamond",
    3: "triangle"
}


settings_shapes = {
    1: "all",
    2: "three_random",
    3: "based_on_score"
}


def map_selection(map_choice):
    print()
    print("1. Terrain en cercle")
    print("2. Terrain en losange")
    print("3. Terrain en triangle")
    print()
    print(f"(Le terrain actuel est : {map_choice})")
    print()

    choice_map = -1

    while choice_map < 1 or choice_map > 3:
        choice_map = int(input("Quelle map choisissez-vous : "))

    return settings_conf_map[choice_map]


def shape_choice_politic():
    print()
    print("1. Afficher l'ensemble des blocs disponibles")
    print("2. Afficher 3 blocs aléatoirement")
    print("3. Afficher des blocs qui ne sont pas faciles à mettre en fonction du score")
    print()

    choice_politic = -1

    while choice_politic < 1 or choice_politic > 3:
        choice_politic = int(input("Quelle politique de choix de forme choisissez-vous : "))

    return settings_shapes[choice_politic]


def settings(map_choice):
    os.system("cls||clear")

    title = Figlet()
    print(title.renderText("Parametres"))

    map_choice = map_selection(map_choice)

    os.system("cls||clear")

    print(title.renderText("Parametres"))

    politic_choice = shape_choice_politic()
    
    return map_choice, politic_choice


def game_rules():
    os.system("cls||clear")

    title = Figlet()

    print(title.renderText("Regles du jeu"))

    print()
    print("1. Les terrains de jeu sont des plateaux de deux dimensions", end='\n\n')
    print("2. Pour placer un bloc on rentre les coordonnées de l'origine de la forme (tout en bas à gauche)", end='\n\n')
    print("3. A chaque ligne supprimer vous gagnez 100 points", end='\n\n')
    print()

    choice = ''
    while choice != "ok":
        choice = input("Veuillez valider en tapant OK : ").lower()

    return