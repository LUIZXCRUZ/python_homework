class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message 
        super().__init__(message)

class Board: 
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right", 
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [
            [" "," ", " "],
            [" "," ", " "],
            [" "," ", " "]
        ]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")    

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That position is already taken.")

        self.board_array[row][column] = self.turn

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        for row in self.board_array:
            if row == ["X", "X", "X"]:
                return (True, "X wins!")
            if row == ["O", "O", "O"]:
                return (True, "O wins!")

        for col in range(3):
            if (
                self.board_array[0][col] == "X" and
                self.board_array[1][col] == "X" and
                self.board_array[2][col] == "X"
            ):
                return (True, "X wins!")

            if (
                self.board_array[0][col] == "O" and
                self.board_array[1][col] == "O" and
                self.board_array[2][col] == "O"
            ):
                return (True, "O wins!")

        for player in ["X", "O"]:
            if (
                self.board_array[0][0] == player and
                self.board_array[1][1] == player and
                self.board_array[2][2] == player
            ):
                return (True, f"{player} wins!")

            if (
                self.board_array[0][2] == player and
                self.board_array[1][1] == player and
                self.board_array[2][0] == player
            ):
                return (True, f"{player} wins!")

        if all(" " not in row for row in self.board_array):
            return (True, "Cat's Game!")

        return (False, f"{self.turn}'s turn.")
    
board = Board()
while True:
    print(board)

    game_over, message = board.whats_next()
    print(message)

    if game_over:
        break

    move = input(f"{board.turn}, enter your move: ").strip().lower()

    try:
        board.move(move)
    except TictactoeException as error:
        print(error.message)
