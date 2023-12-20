import random

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_over = None


def game_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | "
          f"{board[8]}\n")


def player_one_input():
    try:
        player_one = int(input("Enter a number between 1-9: "))
        if player_one not in numbers:
            print("It should be a number between 1-9!\nTry again!")
            player_one_input()
        elif board[player_one - 1] != "-":
            print("Spot has already taken!")
            player_one_input()
        elif board[player_one - 1] == "-":
            board[player_one - 1] = "X"
    except ValueError:
        print("It should be a number between 1-9! _|_\nTry again!")
        player_one_input()


def player_two_input():
    try:
        player_two = int(input("Enter a number between 1-9: "))
        if player_two not in numbers:
            print("It should be a number between 1-9!\nTry Again!")
            player_two_input()
        elif board[player_two - 1] != "-":
            print("Spot has already taken!")
            player_two_input()
        elif board[player_two - 1] == "-":
            board[player_two - 1] = "O"
    except ValueError:
        print("It should be a number between 1-9!\nTry again!")
        player_two_input()


def computer_input():
    computer = random.randint(1, 9)
    if board[computer - 1] == "-":
        board[computer - 1] = "O"
        print(f"Computer Chose '{computer}':")
    elif board[computer - 1] != "-":
        computer_input()


def win():
    game_board()
    global game_over
    if board[0] == board[1] == board[2] == "X":
        print("X wins!")
        game_over = 1
    elif board[3] == board[4] == board[5] == "X":
        print("X wins!")
        game_over = 1
    elif board[6] == board[7] == board[8] == "X":
        print("X wins!")
        game_over = 1
    elif board[0] == board[3] == board[6] == "X":
        print("X wins!")
        game_over = 1
    elif board[1] == board[7] == board[4] == "X":
        print("X wins!")
        game_over = 1
    elif board[2] == board[5] == board[8] == "X":
        print("X wins!")
        game_over = 1
    elif board[6] == board[4] == board[2] == "X":
        print("X wins!")
        game_over = 1
    elif board[0] == board[4] == board[8] == "X":
        print("X wins!")
        game_over = 1
    elif board[0] == board[1] == board[2] == "O":
        print("O wins!")
        game_over = 1
    elif board[3] == board[4] == board[5] == "O":
        print("O wins!")
        game_over = 1
    elif board[6] == board[7] == board[8] == "O":
        print("O wins!")
        game_over = 1
    elif board[0] == board[3] == board[6] == "O":
        print("O wins!")
        game_over = 1
    elif board[1] == board[7] == board[4] == "O":
        print("O wins!")
        game_over = 1
    elif board[2] == board[5] == board[8] == "O":
        print("O wins!")
        game_over = 1
    elif board[6] == board[4] == board[2] == "O":
        print("O wins!")
        game_over = 1
    elif board[0] == board[4] == board[8] == "O":
        print("O wins!")
        game_over = 1
    elif "-" not in board:
        print("It's a Tie!")
        game_over = 1


def play_again():
    global game_over, board
    if game_over == 1:
        play_again_input = input("Do you want to play again? (y, n): ")
        if play_again_input.lower() == "y":
            board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
            game_over = 0
        else:
            pass


while True:
    try:
        print("\nMode'1' ( 1 Vs 1 )\nMode '2' ( Vs computer )\n\n")
        game_mode = int(input("Enter your mode (1, 2): "))
        if game_mode == 1:
            game_board()
            while True:
                player_one_input()
                win()
                if game_over == 1:
                    break
                player_two_input()
                win()
                if game_over == 1:
                    break
        elif game_mode == 2:
            game_board()
            while True:
                player_one_input()
                win()
                if game_over == 1:
                    break
                computer_input()
                win()
                if game_over == 1:
                    break
    except ValueError:
        print("Only Choose '1' or '2'!")
    play_again()
    if game_over == 1:
        print("\n-----------\nBye!")
        break
