#imports and variables
import random
import time
game_status = True
hp_player = 30
victory = 0
lost = 0
winstreak = 0
boss_slain = 0
boss_round = 0
rules = False

#main loop du jeux pour que le jeux peut se faire répeter
while game_status:
    #un bug avec le programe sans le if est de skip le mob sans perdre de points de vies
    #si il n'avait pas affiché les règles du jeux dans le tour prédédent
    if rules == False:
        strength_opponent = random.randint(2, 10)
    #si il avait affiché les règles dans le tour précédent et la force de l'adversaire reste le même
    elif rules == True:
        rules = False
    #si le joueur arrive à trois victoires consécutifs et il face un boss
    if winstreak % 3 == 0 and winstreak != 0:
        boss_status = True
        hp_boss = hp_player
        print(f"Vous tombez face à face avec un boss avec {hp_boss} points de vie.")
        print("Vous ne pouvez pas contourner cet adversaire. \n")
        time.sleep(2)
        #main loop pour que le joueur et le boss se bat (le joueur ne touche rien)
        while boss_status:
            # si le joueur est mort
            if hp_player <= 0:
                print(f"Vous êtes mort avec {victory} victoires, {lost} défaites et {boss_slain} boss batue.")
                boss_status = False
                winstreak = 0
            #si il est pas mort, il continue avec le boss fight
            else:
                boss_round += 1
                dmg_player = random.randint(2, 12)
                if boss_round % 5 == 0:
                    dmg_boss = 15
                elif boss_slain >= 3:
                    dmg_boss = random.randint(5,10)
                else:
                    dmg_boss = random.randint(1,6)
                print(f"Lancer du dé: {dmg_player} \n")
                time.sleep(2)
                print(f"Vous inflictez {dmg_player} dégats.\n")
                hp_boss -= dmg_player
                #differents chemins que la bataille peut aller
                #le boss est battue
                if hp_boss <= 0:
                    boss_slain += 1
                    print(f"Le boss est vaincu en {boss_round} tours. \n")
                    print(f"Vous avez tué {boss_slain} boss en tout.")
                    print("Vous avez gagné 25 points de vie pour avoir tué un boss.")
                    hp_player += 25
                    print(f"Vous avez maintenant {hp_player} points de vie \n")
                    boss_round = 0
                    boss_status = False
                    winstreak += 1
                #le joueur et le boss est toujours vivants et ils se battent
                else:
                    print(f"Le boss vous a inflicté {dmg_boss} point de vie. \n")
                    hp_player -= dmg_boss
                    print(f"Le boss a {hp_boss} points de vie.")
                    print(f"Vous avez {hp_player} points de vie \n")
                    time.sleep(3)
    #si le joueur meurt
    elif hp_player <= 0:
        game_status = False
    #le choix principale (combat avec mob, skip le mob, afficher les règles, quitter le jeux)
    else:
        print(f"Vous tombez face à face avec un adversaire de difficulté : {strength_opponent} \n")
        choice_player = int(input("Que voulez-vous faire ?\n1- Combattre cet adversaire \n2- Contourner cet adversaire et aller ouvrir une autre porte \n3- Afficher les règles du jeu \n4- Quitter la partie \n"))
        #si le choix du joueur est de combattre le mob
        if choice_player == 1:
            dice_player1 = random.randint(1, 6)
            dice_player2 = random.randint(1, 6)
            print(f"Adversaire : {victory + lost + 1} \nForce de l’adversaire : {strength_opponent} \nNiveau de vie de l’usager : {hp_player} \nCombat {victory + lost + 1} : {victory} vs {lost} \n")

            print(f"Lancer du premier dé : {dice_player1} \n")
            print(f"Lancer du deuxième dé : {dice_player2} \n")
            #combat entre joueur et le mob
            #si le joueur a un nb plus petit ou égal au mob(défaite)
            if strength_opponent >= dice_player1 + dice_player2:
                print("Dernier combat = défaite \n")
                hp_player -= strength_opponent
                lost += 1
                winstreak = 0
                print(f"Niveau de vie : {hp_player} \n")
            #si le joueur a un nb plus grand que le mob(victoire)
            else:
                print("Dernier combat = victoire \n")
                hp_player += 4
                victory += 1
                winstreak += 1
                print(f"Niveau de vie : {hp_player} \nNombre de victoires consécutives : {winstreak} \n")
            print(f"La partie est terminée, vous avez vaincu {victory} monstre(s). \n \n \n \n \n")
        #si le joueur choisit de skip le mob
        elif choice_player == 2:
            hp_player -= 1
            print("\nVous avez perdu un point de vie.")
            print(f"Vous avez {hp_player} point de vie. \n")
        #si le joueur décide de regarder les règles du jeux
        elif choice_player == 3:
            print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
            print("\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.")
            print("\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. \n \n \n \n \n")
            rules = True
        #si le jouveur décide de quitter le jeux
        else:
            print("Merci et au revoir...")
            game_status = False



