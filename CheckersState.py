"""
Checkers Board Class

Authors: Oscar De La Garza & Yehya Albakri
"""

#Pieces defined in terms of constants (would have to be enumerated for implementation)
red = 0
black = 1
board_width = 8
board_height = 8
red_piece = 2
black_piece = 3
red_king = 4
black_king = 5
empty_spot = 6
red_pieces = [red_piece, red_king]
black_pieces = [black_piece, black_king]

class Board:
        """
        Represents the state of a checkers board and positions of pieces.
        
        Checks if the piece you selected is your piece. If it is, it will compare your move
        attempt to the legal spaces you can move to. After a turn, it will allow you to move the 
        same piece a second turn (by showing a message) if you have the ability to capture a 
        second piece. Clicking on an empty part of the board will skip this bonus turn. If your move
        attempt is not legal, the game will not move the piece and show a message indicating the reason.

        Attributes:
            turns: indidcate what players turn it is
            spaces: 2-dimensional list of all the spaces on the board
            black_piece_moved: show if a black piece moved
            red_piece_moved: show if a red piece moved
            black_king_moved: show if a black king moved
            red_king_moved: show if a red king moved
        """

        def __init__(self):
            """
            Create and setup board
            """

            # Set it to black's turn, black goes first

            # Define the board as a list of arrays with values from 0-6
            # Define the initial values for setup

            # Place pieces into corresponding black squares for the end_game

            # Create Textbox/area for messages and information to be displayed
            pass

        def possible_moves(self, row, column):
            """
            Show possible moves on the board

            Args:
                row: which row is the piece located(0-7)
                column: which column is the piece located(0-7)
            Returns:
                A list of possible moves available to the selected piece
            """

            # Selects piece and decide what possible moves are available

            # Check for whose turn it is and if an opponents piece is selected
            # return "Not your piece, please select a one of your pieces"

            # Check for if the square is empty or outside the 8x8 range and
            # return "No piece or outside of the board, please select on of your pieces"

            # Check to see if a normal checker piece or a king for possible movements

            # Differneiate whether a capture or movement solely

            # Add a form to check for double+ jumps from capturing multiple Pieces
            pass

        def captured_pieces(self):
            """
            Create a callable list to keep track of how many captured pieces each player has
            """
            pass 
        
        def move(self, start_row, start_column, end_row, end_column):
            """
            Compares the inputted moves to the legal moves of the selected piece

            Args:
                start_row: indicate starting row of the piece(0-7)
                start_column: indicate starting column of the piece(0-7)
                end_row: indicate ending row of the piece piece(0-7)
                end_column: indicate ending column of the piece(0-7)
            Returns:
                if a valid move return "move completed, (start_row,start_column) to (end_row, end_column)"
                if a piece is captured also return "piece captured at (c_piece_row,c_piece_column)"
                if an invalid move return "invalid move"
            """
            # Check first to see if a valid move is being presented

            # If valid move is presented move piece to final location

            # Check if in that movement a piece was captured by using
            # nature od 2 diagonal spaces were hopped to checker

            # If piece was captured make space empty and add to counter of captured pieces
            pass
