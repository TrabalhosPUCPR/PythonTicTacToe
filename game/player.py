import abc

from game.tictactoecore import TicTacToe, SquareState


class Player:
    def __init__(self, name, square_symbol):
        self.name = name
        self.square_symbol = square_symbol

    @abc.abstractmethod
    def act(self, current_board: TicTacToe) -> (int, int):
        while True:
            col = int(input(f"{self.name}'s turn, type the column of your next move\ncolumn: "))
            line = int(input(f"line: "))
            if 0 < col < current_board.x_size and 0 < line < current_board.y_size and \
                    current_board.get_square(col, line) == SquareState(None):
                print("Invalid column or line number")
                continue
            break
        return col, line
