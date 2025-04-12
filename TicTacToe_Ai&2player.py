import random


def print_matrix(initial_matrix):
    print(
        f"\n     |     |     \n  {initial_matrix[0]}  |  {initial_matrix[1]}  |  {initial_matrix[2]}\n"
        f"_____|_____|_____\n     |     |     \n  {initial_matrix[3]}  |  {initial_matrix[4]}  |  {initial_matrix[5]}\n"
        f"_____|_____|_____\n     |     |     \n  {initial_matrix[6]}  |  {initial_matrix[7]}  |  {initial_matrix[8]}\n"
        "     |     |     \n"
    )


def check_winner(initial_matrix, player_symbol):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Horizontal
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Vertical
        [0, 4, 8],
        [2, 4, 6],  # Diagonal
    ]
    return any(
        all(initial_matrix[i] == player_symbol for i in condition)
        for condition in win_conditions
    )


def valid_input(player_input, initial_matrix):
    return (
        player_input.isdigit()
        and 1 <= int(player_input) <= 9
        and initial_matrix[int(player_input) - 1] not in ["X", "O"]
    )


def computer_move(initial_matrix):
    available_moves = [
        i for i, spot in enumerate(initial_matrix) if spot not in ["X", "O"]
    ]
    return random.choice(available_moves)


def tic_tac_toe():
    initial_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nWelcome to Naman's TIC TAC TOE!\n")
    game_over = False
    print("Here is the Board:")
    print_matrix(initial_matrix)

    mode = input("Choose mode: 1 for Two Players, 2 for Single Player: ")
    while mode not in ["1", "2"]:
        mode = input(
            "Invalid input. Choose mode: 1 for Two Players, 2 for Single Player: "
        )

    if mode == "1":
        # Two-player mode
        name_player1 = input("Enter the name of player 1: ").capitalize()
        name_player2 = input("Enter the name of player 2: ").capitalize()
        print(f"\n{name_player1} (O) vs {name_player2} (X)\n")
        i = 0
        while i < 9 and not game_over:
            current_player = name_player1 if i % 2 == 0 else name_player2
            symbol = "O" if i % 2 == 0 else "X"
            print(f"{current_player}'s Turn! ({symbol})")
            player_input = input(
                "Enter the number at which you want to place your marker: "
            )
            while not valid_input(player_input, initial_matrix):
                print("Invalid input. Please enter a valid position.")
                player_input = input(
                    "Enter the number at which you want to place your marker: "
                )
            player_input = int(player_input)
            initial_matrix[player_input - 1] = symbol
            print_matrix(initial_matrix)
            if check_winner(initial_matrix, symbol):
                print(f"{current_player} is the winner!")
                game_over = True
            elif i == 8:
                print("It's a tie!")
            i += 1
    else:
        # Single-player mode
        name_player = input("Enter your name: ").capitalize()
        print(f"\n{name_player} (O) vs Computer (X)\n")
        i = 0
        while i < 9 and not game_over:
            if i % 2 == 0:
                current_player = name_player
                symbol = "O"
                print(f"{current_player}'s Turn! ({symbol})")
                player_input = input(
                    "Enter the number at which you want to place your marker: "
                )
                while not valid_input(player_input, initial_matrix):
                    print("Invalid input. Please enter a valid position.")
                    player_input = input(
                        "Enter the number at which you want to place your marker: "
                    )

                player_input = int(player_input)
                initial_matrix[player_input - 1] = symbol
                print_matrix(initial_matrix)

                if check_winner(initial_matrix, symbol):
                    print(f"{current_player} is the winner!")
                    game_over = True
                elif i == 8:
                    print("It's a tie!")

                i += 1

            print("\nGame Over")
            print_matrix(initial_matrix)
