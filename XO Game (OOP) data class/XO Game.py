from dataclasses import dataclass, field
from sys import exit
import os

# Clear the terminal screen depending on the operating system
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Player:
    name: str = ""    # Player's name
    symbol: str = ""  # Player's symbol (X or O)

    # Ask the player to choose their name (letters only)
    def Choose_name(self):
        while True:
            name = input("Enter Your Name (Letters Only!): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    # Ask the player to choose their symbol (a single letter)
    def Choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (a single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid input. Please choose a single letter.")


class Menu:
    # Show the main menu at the start of the game
    def display_main_menu(self):
        print("""Welcome to my X-O Game! 
              Enter 1 to Start Game 
              Enter 2 to Quit""")
        while True:
            try:
                choice = int(input("Enter Number: "))
                if choice not in [1, 2]:
                    print("Invalid Number. Please enter 1 or 2.")
                else:
                    return choice
            except ValueError:
                print("Please enter a valid number.")

    # Show the menu after a game ends
    def display_endgame_menu(self):
        print("""End of the X-O Game!
              Enter 1 to Play Again
              Enter 2 to Quit""")
        while True:
            try:
                choice = int(input("Enter Number: "))
                if choice not in [1, 2]:
                    print("Invalid Number. Please enter 1 or 2.")
                else:
                    return choice
            except ValueError:
                print("Please enter a valid number.")


@dataclass
class Board:
    board: list = field(default_factory=lambda: [str(i) for i in range(1, 10)])

    # Print the current state of the board
    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)

    # Update the board with the player's symbol
    def update_borad(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    # Check if the move is valid (cell not already taken)
    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    # Reset the board for a new game
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


@dataclass
class Game:
    players: list = field(default_factory=lambda: [Player(), Player()])
    board: Board = field(default_factory=Board)
    menu: Menu = field(default_factory=Menu)
    current_player_index: int = 0

    # Start the game
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            clear_screen()
            self.play_game()
        else:
            self.quit_game()

    # Collect player details (name and symbol)
    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details:")
            player.Choose_name()
            player.Choose_symbol()

    # Main game loop
    def play_game(self):
        while True:
            self.play_turn()
            clear_screen()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    # Restart the game with a fresh board
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    # Check if the current board has a winning combination
    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combinations:
            if (self.board.board[combo[0]] ==
                self.board.board[combo[1]] ==
                self.board.board[combo[2]]):
                return True
        return False

    # Check if all cells are filled without a winner
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    # Handle a single player's turn
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"\n{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_borad(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        self.switch_player()

    # Switch to the other player
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    # Quit the game gracefully
    def quit_game(self):
        print("Thank you for playing!")
        return exit(0)

# Create a Game instance and start it
if __name__ == "__main__":
    game = Game()
    game.start_game()
