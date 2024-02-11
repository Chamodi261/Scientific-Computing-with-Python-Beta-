class Board:
    def __init__(self, board):
        """
        Initializes the Sudoku board.

        Parameters:
        - board (list): 2D list representing the initial Sudoku board.
        """
        self.board = board

    def __str__(self):
        """
        Returns a string representation of the Sudoku board for printing.
        """
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            row_list = []
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append('║')

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty

            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    def find_empty_cell(self):
        """
        Finds the first empty cell (cell with value 0) in the board.

        Returns:
        - tuple: (row, col) of the empty cell, or None if not found.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        """
        Checks if 'num' is valid to be placed in the specified row.

        Parameters:
        - row (int): Row index.
        - num (int): Number to check.

        Returns:
        - bool: True if valid, False otherwise.
        """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Checks if 'num' is valid to be placed in the specified column.

        Parameters:
        - col (int): Column index.
        - num (int): Number to check.

        Returns:
        - bool: True if valid, False otherwise.
        """
        return all(
            self.board[row][col] != num
            for row in range(9)
        )

    def valid_in_square(self, row, col, num):
        """
        Checks if 'num' is valid to be placed in the specified 3x3 square.

        Parameters:
        - row (int): Row index.
        - col (int): Column index.
        - num (int): Number to check.

        Returns:
        - bool: True if valid, False otherwise.
        """
        row_start = (row // 3) * 3
        col_start=(col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        """
        Checks if placing 'num' in the empty cell at the specified position is valid.

        Parameters:
        - empty (tuple): (row, col) of the empty cell.
        - num (int): Number to check.

        Returns:
        - bool: True if valid, False otherwise.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
         """
        Recursive backtracking algorithm to solve the Sudoku puzzle.

        Returns:
        - bool: True if a solution is found, False otherwise.
        """
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0

        return False

def solve_sudoku(board):
    """
    Solves the given Sudoku puzzle and prints the result.

    Parameters:
    - board (list): 2D list representing the Sudoku puzzle.

    Returns:
    - Board: Gameboard object after solving the puzzle.
    """

    # Create a Sudoku board object
    gameboard = Board(board)

    # Print the original puzzle
    print(f'\nPuzzle to solve:\n{gameboard}')

    # Attempt to solve the puzzle using the solver method
    if gameboard.solver():
        # If a solution is found, print the solved puzzle
        print('\nSolved puzzle:')
        print(gameboard)

    else:
        # If no solution is found, print a message
        print('\nThe provided puzzle is unsolvable.')

    # Return the gameboard object for further analysis or use
    return gameboard
# Example Sudoku puzzle
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Solve the Sudoku puzzle and get the resulting gameboard
solve_sudoku(puzzle)