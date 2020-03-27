"""
Checkers board status

Authors: Oscar De La Garza & Yehya Albakri
"""

#Pieces defined in terms of constants (would have to be enumerated for implementation)
white = 0
black = 1
board_width = 8
white_piece = 2
black_piece = 3
white_king = 4
black_king = 5
empty_spot = 6
white_pieced = [white_piece, white_king]
black_pieces = [black_piece, black_king]

class State:
    """
    Represents the state of a checkers board and positions of pieces.
    
    Attributes:
        
    
    """
    "Create Board and status of game"
    
