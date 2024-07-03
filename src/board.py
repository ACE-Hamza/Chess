from const import *
from square import Square

class Board:

    def __init__(self) -> None:
        self.squares = [[0 for row in range(ROWS)] for col in range(COLS)] # 0's are just placeholders here
        self._create()

    def _create(self): # _ at the start denotes that the method is private
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col) # replacing each element of square by a square object

    def _add_pieces(self, color):
        pass

