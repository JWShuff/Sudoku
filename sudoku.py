class SudokuSolver:
    def __init__(self, board_string):
        self.board_string = board_string

    def solve(self):
        pass


    def board(self):
        formatted_board = "----------------------\n"
        box_format_string = "----------------------\n"
        # Prints the board string in the appropriate format:
        for i, value in enumerate(self.board_string):
            if i % 9 == 0:
                formatted_board += "\n"
                if i % 27 == 0:
                    formatted_board += box_format_string
            elif i % 3 == 0:
                formatted_board += " |"
            formatted_board += (" " + value)

        formatted_board += "\n" +box_format_string
        return formatted_board

        """
        ---------------------
        4 8 3 | 9 2 1 | 6 5 7
        9 6 7 | 3 4 5 | 8 2 1
        2 5 1 | 8 7 6 | 4 9 3
        ---------------------
        5 4 8 | 1 3 2 | 9 7 6
        7 2 9 | 5 6 4 | 1 3 8
        1 3 6 | 7 9 8 | 2 4 5
        ---------------------
        3 7 2 | 6 8 9 | 5 1 4
        8 1 4 | 2 5 3 | 7 6 9
        6 9 5 | 4 1 7 | 3 8 2
        ---------------------
        """ 
  
game = SudokuSolver("619030040270061008000047621486302079000014580031009060005720806320106057160400030")
print(game.board())

# The file has newlines at the end of each line, so we call
# String#chomp to remove them.
# game = SudokuSolver(board_string)
# # Remember: this will just fill out what it can and not "guess"
# game.solve

# print(game.board)
