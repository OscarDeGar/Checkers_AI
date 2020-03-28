""""""""""""""""""""""""""""

MP4: Checkers_AI

By: Oscar De La Garza & Yehya Albakri

""""""""""""""""""""""""""""

import os, sys
import pygame
from pygame.locals import*
import CheckersView
import CheckersState


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

    def event_loop(self):
        """Here the actual actions/events occur, such as
        selecting pieces and the resulting effect"""

        pass

    def update(self):
        "Updates the appearence of the board"

        pass

    def end_game(self):
        "Quits program to end the game"
        pygame.quit()
        sys.exit
        pass

    def main_loop(self):
        """Executes game and searches for endgame
        occurrence to intialize end_game"""

        pass

    def end_turn(self):
        "Ends turn of the player and switches player"

        pass


if __name__ == "__main__":
    MainWindow = CheckersMain()
    MainWindow.MainLoop()
