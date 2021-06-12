class SudokuSolver:
    def __init__(self, board_string):
        self.board_string = board_string
        self.board_array = self.string_to_grid()

    # This logic converts the input 81 character string to a 2d array:
    # where the first [] = the row (0-8), and the second [] indicates column.
    def string_to_grid(self):
        lst = []
        for i, _ in enumerate(self.board_string):
            if i % 9 == 0:
                sub = self.board_string[i:i+9:1]
                lst.append(sub)
        return(lst)

    def check_column(self, index):
        if board_string[index] != 0:
            return
        

    def solve(self):
        # To make the logic more clear,
        # convert the input string to a list of
        # 9 sub lists, so [row][column] becomes the addresses in question
            
        # Looks up and down the column while removing possible options for non 0 values at indices.

        # Check row
        # Check box

        # Working with a string we need an answer key for index values
        # in relative positioning:
        # Row 1 i : 0-8     Column 1: i: 0, 9,18,27,36,45,54,63,72
        # Row 2 i : 9-17    Column 2: i: 1,10,19,28,37,46,55,64,73
        # Row 3 i : 18-26   Column 3: i: 2,11,20,29,38,47,56,65,74
        # Row 4 i : 27:35   Column 4: i: 3,12,21,30,39,48,57,66,75
        # Row 5 i : 36:44   Column 5: i: 4,13,22,31,40,49,58,67,76
        # Row 6 i : 45:53   Column 6: i: 5,14,23,32,41,50,59,68,77
        # Row 7 i : 54:62   Column 7: i: 6,15,24,33,42,51,60,69,78
        # Row 8 i : 63:71   Column 8: i: 7,16,25,34,43,52,61,70,79
        # Row 9 i : 72:80   Column 9: i: 8,17,26,35,44,53,62,71,80
        pass

    def board(self):
        box_format_string = "----------------------\n"
        formatted_board = box_format_string
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
print(game.board_array)
# The file has newlines at the end of each line, so we call
# String#chomp to remove them.
# game = SudokuSolver(board_string)
# # Remember: this will just fill out what it can and not "guess"
# game.solve

# print(game.board)
