#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 08:19:54 2018.

@author: jim
"""
# ---------------------------- Imports ----------------------------------------

import os
import random

# ---------------------------- Classes ----------------------------------------


class Grid():
    """Grille du jeu."""

    def __init__(self):
        """Initialise le plateau de jeu.

        Les blancs sont O et les noirs sont X.
        """
        self.board = [['-'] * 8 for _ in range(0, 8)]
        self.board[3][3] = 'O'
        self.board[4][4] = 'O'
        self.board[3][4] = 'X'
        self.board[4][3] = 'X'

        self.counter = 4  # Nombes de cases utilisées

    def affiche(self):
        """Affiche le plateau de jeu."""
        lettre = '   A  B  C  D  E  F  G  H\n'

        print(lettre)

        for i, sublist in enumerate(self.board):
            print(f'{i + 1}  {"  ".join(sublist)}  {i + 1}')

        print(lettre)

    def playable(self, color):
        """Cherche un pion de la couleur opposé.

        Si on en trouve, cherche une case vide contigue.
        Si on en trouve, cherche un pion retournable.
        """
        count_playable = 0

        for irow, row in enumerate(self.board):
            for icol, col in enumerate(row):
                if col == color:
                    count_playable += 1
                    print(icol, irow)
        print(count_playable)


class Player():
    """Crée le joueur ou AI."""

    def __init__(self, name):
        """Configure joueurs."""
        self.name = name
        self.score = 2
        self.color = None
        self.can_play = True

# ---------------------------- Fonctions --------------------------------------


def clear():
    """Effancemenr de l'écran."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu(title, liste):
    """Gestion des menus."""
    clear()
    print(title)
    print('-' * len(title) + '\n')

    for count, item in enumerate(liste, 1):
        print(count, item)
        print('\n')

    result = 0

    while result not in range(1, len(liste) + 1):
        result = input('Votre choix :')
        if result.isdigit():
            result = int(result)

    return result


def menu_intro():
    """Menu de départ."""
    title = 'Welcome to PyOthello !'
    liste = ['Jouer', 'Quitter']

    option = menu(title, liste)

    if option == 2:
        print('Ok Bye !')
        exit()


def menu_b_or_w():
    """Choisir noir ou blanc ou aléatoire."""
    title = (f'Quelle couleur choisissez vous {player1.name} ?')
    liste = ['Blancs (O)', 'Noirs (X)', 'Au hasard']

    option = menu(title, liste)

    if option == 3:
        player1.color = random.choice('OX')

    elif option == 2:
        player1.color = 'X'

    else:
        player1.color = 'O'

    if player1.color == 'X':
        player2.color = 'O'

    else:
        player2.color = 'X'


def get_player():
    """Création des joueurs."""
    player1 = input('Entrez votre nom :')
    return player1


def score():
    """Affichage du score."""
    print('---------- Scores ----------\n')
    p1 = (f'{player1.name} ({player1.color})').ljust(24, '.') + ' :'
    p1 = p1 + (f'{player1.score}').rjust(2)
    p2 = (f'{player2.name} ({player2.color})').ljust(24, '.') + ' :'
    p2 = p2 + (f'{player2.score}').rjust(2)

    print(p1)
    print(p2)
    print('----------------------------\n')


def in_board():
    """Conformité de la saisie."""
    ok = False
    while not ok:

        entree = input("Quelle case jouez vous (exemple A4) ?")
        entree = entree.upper()

        if len(entree) > 2:
            print('Pas plus de 2 caractéres !\n')

        elif ord(entree[0]) not in range(65, 73):
            print('La colonne doit être une lettre entre A et H')

        elif not entree[1].isdigit() or int(entree[1]) not in range(1, 9):
            print('La rangée doit être un chiffre entre 1 et 8')

        else:
            ok = True

            col = ord(entree[0]) - 65  # Coordonnées valide pour les listes.
            row = int(entree[1]) - 1  # Coordonnées valide pour les listes.

    return col, row

# ---------------------------- Start ------------------------------------------


menu_intro()
print('\n\n')

player1 = Player(get_player())
player2 = Player('Computer')
print('\n\n')

menu_b_or_w()
print('\n\n')

print(f'{player1.name} joue avec les {player1.color}, \
{player2.name} joue avec les {player2.color}.\n')

score()

game = Grid()
game.affiche()
game.playable('O')


coup = in_board()
print(coup)
