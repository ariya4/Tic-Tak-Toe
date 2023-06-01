import random

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_over = None


def game_board():
    print(f"{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | "
          f"{board[8]}")


def player_one_input():
    try:
        player_one = int(input("Enter a number between 1-9: "))
        if player_one not in numbers:
            print("Number should be between 1 - 9!")
            player_one_input()
        elif board[player_one - 1] == "-":
            board[player_one - 1] = "X"
        elif board[player_one - 1] != "-":
            print("Spot has already taken!")
            player_one_input()
    except ValueError:
        print("Number should be between 1 - 9: ")
        player_one_input()


def computer_input():
    computer = random.randint(1, 9)
    if board[computer - 1] == "-":
        board[computer - 1] = "O"
        print(f"Computer Chose '{computer}':")
    elif board[computer - 1] != "-":
        computer_input()


def win():
    global game_over
    game_board()
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
