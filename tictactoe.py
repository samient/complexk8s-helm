import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x350")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        # Create the game board's buttons
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 20), height=2, width=5,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        # Create a reset button
        reset_button = tk.Button(self.window, text="Reset", font=("Arial", 14), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for a winner
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
                return

            # Check for a draw
            if self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return

            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

    def run(self):
        self.window.mainloop()


# Run the game
if __name__ == "__main__":
    game = TicTacToeGame()
    game.run()
