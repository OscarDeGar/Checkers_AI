"""
Checkers Board Class

Authors: Oscar De La Garza & Yehya Albakri
"""

#Pieces defined in terms of constants (would have to be enumerated for implementation)
white = 0
black = 1
board_width = 8
board_height = 8
white_piece = 2
black_piece = 3
white_king = 4
black_king = 5
empty_spot = 6
white_pieces = [white_piece, white_king]
black_pieces = [black_piece, black_king]

class Board:
        """
        Represents the state of a checkers board and positions of pieces.

        Attributes:
            turns: indidcate what players turn it is
            spaces: 2-dimensional list of all the spaces on the board
            black_piece_moved: show if a black piece moved
            white_piece_moved: show if a white piece moved
            black_king_moved: show if a black king moved
            white_king_moved: show if a white kind moved
        """

        def __init__(self):
            "Create and setup board"

            #Set it to black's turn, black goes first

            #Made from an array with empty spaces for the board

            #Place pieces into corresponding black squares for the end_game

            #Create Textbox/area for messages and information to be displayed
            pass

        def possible_moves(self, row, column):
            """Show possible moves on the board

            Args:
                row: which row is the piece located(0-7)
                column: which column is the piece located(0-7)
            Returns:
                A list of possible moves available to the selected piece
            """

            #Selects piece and decide what possible moves are available

            #Check for whose turn it is and if an opponents piece is selected
            #return "Not your piece, please select a one of your pieces"

            #Check for if the square is empty or outside the 8x8 range and
            #return "No piece or outside of the board, please select on of your pieces"

            #Check to see if a normal checker piece or a queen for possible movements

            #Differneiate whether a capture or movement solely

            #Add a form to check for double+ jumps from capturing multiple Pieces
            pass

        def captured_pieces(self):
            "Create a callable list to keep track of captured pieces"
            pass

        def move(self, start_row, start_column, end_row, end_column):
            """Intiate possible moves

            Args:
                start_row: indicate starting row of the piece(0-7)
                start_column: indicate starting column of the piece(0-7)
                end_row: indicate ending row of the piece piece(0-7)
                end_column: indicate ending column of the piece(0-7)
            Returns:
                if a valid move return "move completed, (start_row,start_column) to (end_row, end_column)"
                if a piece is captured also return "Piece captured at (c_piece_row,c_piece_column)"
                if an invalid move return "move cannot be completed, invalid"
            """
            #Check first to see if a valid move is being presented

            #If valid move is presented move piece to final location

            #Check if in that movement a piece was captured by using
            #nature od 2 diagonal spaces were hopped to checker

            #If piece was captured make space empty and add to counter of captured pieces
