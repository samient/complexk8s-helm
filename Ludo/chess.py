import tkinter as tk


class ChessGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess Game")
        self.board_size = 8
        self.colors = ["white", "black"]
        self.pieces = {
            "rook": "♜",
            "knight": "♞",
            "bishop": "♝",
            "queen": "♛",
            "king": "♚",
            "pawn": "♟",
        }
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.tiles = []
        self.selected_piece = None
        self.selected_tile = None
        self.create_board()
        self.place_pieces()

    def create_board(self):
        """Draw the chessboard."""
        for row in range(self.board_size):
            tile_row = []
            for col in range(self.board_size):
                color = self.colors[(row + col) % 2]
                tile = tk.Frame(self.window, width=60, height=60, bg=color)
                tile.grid(row=row, column=col)
                tile.bind("<Button-1>", lambda event, r=row, c=col: self.on_tile_click(r, c))
                tile_row.append(tile)
            self.tiles.append(tile_row)

    def place_pieces(self):
        """Place all chess pieces on the board."""
        # Place pawns
        for col in range(self.board_size):
            self.add_piece(1, col, "pawn", "black")
            self.add_piece(6, col, "pawn", "white")

        # Place rooks
        self.add_piece(0, 0, "rook", "black")
        self.add_piece(0, 7, "rook", "black")
        self.add_piece(7, 0, "rook", "white")
        self.add_piece(7, 7, "rook", "white")

        # Place knights
        self.add_piece(0, 1, "knight", "black")
        self.add_piece(0, 6, "knight", "black")
        self.add_piece(7, 1, "knight", "white")
        self.add_piece(7, 6, "knight", "white")

        # Place bishops
        self.add_piece(0, 2, "bishop", "black")
        self.add_piece(0, 5, "bishop", "black")
        self.add_piece(7, 2, "bishop", "white")
        self.add_piece(7, 5, "bishop", "white")

        # Place queens
        self.add_piece(0, 3, "queen", "black")
        self.add_piece(7, 3, "queen", "white")

        # Place kings
        self.add_piece(0, 4, "king", "black")
        self.add_piece(7, 4, "king", "white")

    def add_piece(self, row, col, piece, color):
        """Add a piece to the board."""
        label = tk.Label(
            self.tiles[row][col],
            text=self.pieces[piece],
            font=("Arial", 24),
            fg=color,
            bg=self.tiles[row][col].cget("bg"),
        )
        label.pack()
        self.board[row][col] = {"type": piece, "color": color, "widget": label}

    def on_tile_click(self, row, col):
        """Handle tile click events."""
        if self.selected_piece:
            # Move the selected piece to the new tile if valid
            self.move_piece(row, col)
        elif self.board[row][col]:
            # Select a piece if one exists on the clicked tile
            self.selected_piece = self.board[row][col]
            self.selected_tile = (row, col)
            self.highlight_moves(row, col)

    def move_piece(self, row, col):
        """Move the selected piece to the specified tile."""
        start_row, start_col = self.selected_tile

        # Remove the piece from the starting position
        self.board[start_row][start_col] = None
        self.tiles[start_row][start_col].config(bg=self.colors[(start_row + start_col) % 2])
        self.selected_piece["widget"].pack_forget()

        # Place the piece in the new position
        self.board[row][col] = self.selected_piece
        self.selected_piece["widget"].pack()
        self.tiles[row][col].config(bg=self.colors[(row + col) % 2])

        # Clear selection
        self.selected_piece = None
        self.selected_tile = None
        self.clear_highlights()

    def highlight_moves(self, row, col):
        """Highlight possible moves for the selected piece."""
        self.clear_highlights()
        piece = self.board[row][col]["type"]
        color = self.board[row][col]["color"]

        if piece == "bishop":
            # Highlight diagonal moves
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < self.board_size and 0 <= c < self.board_size:
                    if self.board[r][c] is None or self.board[r][c]["color"] != color:
                        self.tiles[r][c].config(bg="green")
                    if self.board[r][c] is not None:
                        break
                    r += dr
                    c += dc

        # Add logic for other pieces as needed (rook, knight, etc.)

    def clear_highlights(self):
        """Clear all highlighted tiles."""
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.tiles[row][col].config(bg=self.colors[(row + col) % 2])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = ChessGame()
    game.run()