""""""""""""""""""""""""""""

MP4: Checkers_AI

By: Oscar De La Garza & Yehya Albakri

""""""""""""""""""""""""""""

import os, sys
import pygame
from pygame.locals import*

if not pygame.font: print("Warning, fonts disabled")
if not pygame.mixer: print("Warning, sound disabled")


class CheckersMain:
    "Runs the game and intializes it"
    def __init__(self, width = 640, height = 480):
        "intialize"
        "intialize pygame"
        pygame.init()
        "Set window size"
        self.width = width
        self.height = height
        "Create the Screen"
        self.screen = pygame.display.set_mode((self.width, self.height))


class BlackPiece(pygame.sprite.Sprite):
    "BlackPiece and its movements"

class WhitePiece(pygame.sprite.Sprite):
    "WhitePiece and its movements"

class WhiteQueenPiece(pygame.sprit.Sprite):
    "QueenWP and its movements"

class BlackQueenPiece(pygame.sprite.Sprite):
    "QueenBP and its movements"

class State:
    "Create Board and status of game"

if __name__ == "__main__":
    MainWindow = CheckersMain()
    MainWindow.MainLoop()
