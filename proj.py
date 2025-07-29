import tkinter as tk
import random
from tkinter import messagebox

COLUMNS = 7
ROWS = 6
PLAYER = 1
COMPUTER = 2
SCORE_PART = 50


class GameC4:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect 4")
        self.menu_frame = tk.Frame(self.window)
        self.player_score = 0
        self.computer_score = 0
        self.menu_title = tk.Label(
            self.menu_frame, text="Connect 4", font=("Impact", 100)
        )
        self.play_button = tk.Button(
            self.menu_frame,
            text="Play Game",
            font=("Impact", 15),
            command=self.start_game,
        )
        self.quit_button = tk.Button(
            self.menu_frame,
            text="Quit",
            font=("Impact", 13),
            command=self.window.quit,
        )
        self.menu_title.pack(pady=30)
        self.play_button.pack(pady=15)
        self.quit_button.pack(pady=10)
        self.menu_frame.pack()
        self.game_frame = tk.Frame(self.window)
        self.canvas = tk.Canvas(self.window, width=700, height=650, bg="blue")
        self.canvas.pack()

        self.window.mainloop()

    def draw_score(self):
        self.canvas.create_rectangle(0, 0, 700, 50, fill="lightgrey", outline="black")
        score_text = (
            f"Player: {self.player_score}        Computer: {self.computer_score}"
        )
        self.canvas.create_text(
            350, 30, text=score_text, font=("Impact", 25), fill="black"
        )

    def build_board(self):
        self.canvas.delete("all")  # reputs board after every move for updated piece
        self.draw_score()
        for row in range(ROWS):
            for column in range(COLUMNS):
                x1 = column * 100 + 10  # 100 = cell size & 10 = padding, for space
                y1 = row * 100 + 10 + SCORE_PART
                x2 = x1 + 80
                y2 = y1 + 80

                if self.board[row][column] == PLAYER:  # Game piece colors
                    color = "red"
                elif self.board[row][column] == COMPUTER:
                    color = "yellow"
                else:
                    color = "white"

                self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def start_game(self):
        self.menu_frame.pack_forget()
        self.game_frame.pack()
        self.board = [[0] * COLUMNS for _ in range(ROWS)]  # Sets the board size

        self.game_over = False
        self.computer_wait = False

        self.canvas.bind("<Button-1>", self.player_click)
        self.build_board()

    def reset_game(self):  # For continuous playing
        self.board = [[0] * COLUMNS for _ in range(ROWS)]
        self.game_over = False
        self.build_board()

    def for_draw(self):
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.board[row][column] == 0:
                    return False
        return True

    def player_click(self, event):
        if self.game_over or self.computer_wait:
            return

        column = event.x // 100  # event for x axis divided by pixels (column width)
        if self.drop_piece(column, PLAYER):
            self.build_board()

            if self.check_winner(PLAYER):
                self.game_over = True
                self.player_score =+ 1
                messagebox.showinfo("Game Over", "You Win")
                self.window.after(1000, self.reset_game)
                return

            if self.for_draw():
                self.game_over = True
                messagebox.showinfo("Game Over", "Its a Draw")
                self.window.after(1000, self.reset_game)
                return
            if self.check_winner(COMPUTER):
                self.game_over = True
                self.computer_score =+ 1
                messagebox.showinfo("Game Over", "Computer Wins")
                self.window.after(1000, self.reset_game)
                return

        self.computer_wait = True
        self.window.after(600, self.computer_turn)

    def computer_turn(self):
        if self.game_over:
            self.computer_wait = False
            return

        valid_columns = []  # picks a random empty column
        for column in range(COLUMNS):
            if self.board[0][column] == 0:
                valid_columns.append(column)

        if valid_columns:  # Computer decisionmaking for each play (it random fr)
            column = random.choice(valid_columns)
            self.drop_piece(column, COMPUTER)
            self.build_board()

            if self.check_winner(COMPUTER):
                self.game_over = True
                messagebox.showinfo("Game Over", "Computer wins!")
            elif self.for_draw():
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")

        self.computer_wait = False

    def drop_piece(self, column, player):
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                return True
        return False

    def check_winner(self, player):
        for row in range(ROWS):  # checks horizontal, x-axis
            for column in range(COLUMNS - 3):
                if (
                    self.board[row][column] == player
                    and self.board[row][column + 1] == player
                    and self.board[row][column + 2] == player
                    and self.board[row][column + 3] == player
                ):
                    return True

        for row in range(ROWS - 3):  # checks vertical, y-axis
            for column in range(COLUMNS):
                if (
                    self.board[row][column] == player
                    and self.board[row + 1][column] == player
                    and self.board[row + 2][column] == player
                    and self.board[row + 3][column] == player
                ):
                    return True

        for row in range(ROWS - 3):  # diagonal check (top to bottom)
            for column in range(COLUMNS - 3):
                if (
                    self.board[row][column] == player
                    and self.board[row + 1][column + 1] == player
                    and self.board[row + 2][column + 2] == player
                    and self.board[row + 3][column + 3] == player
                ):
                    return True

        for row in range(3, ROWS):  # diagonal check (bottom to top)
            for column in range(COLUMNS - 3):
                if (
                    self.board[row][column] == player
                    and self.board[row - 1][column + 1] == player
                    and self.board[row - 2][column + 2] == player
                    and self.board[row - 3][column + 3] == player
                ):
                    return True

        return False


GameC4()  # To run the program by creating the object

print("Goodbye.")  # Farewell text to the valued user
