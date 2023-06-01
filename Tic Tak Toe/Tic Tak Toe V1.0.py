board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def game_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | "
          f"{board[8]}\n")


def player_one_input():
    player_one = int(input("Enter a number between 1-9: "))
    if board[player_one - 1] == "-":
        board[player_one - 1] = "X"
    elif board[player_one - 1] != "-":
        print("Spot has already taken!")
        player_one_input()


def player_two_input():
    player_two = int(input("Enter a number between 1-9: "))
    if board[player_two - 1] == "-":
        board[player_two - 1] = "O"
    elif board[player_two - 1] != "-":
        print("Spot has already taken!")
        player_two_input()


game_board()
while True:
    player_one_input()
    game_board()
    if board[0] == board[1] == board[2] == "X":
        print("X wins!")
        break
    elif board[3] == board[4] == board[5] == "X":
        print("X wins!")
        break
    elif board[6] == board[7] == board[8] == "X":
        print("X wins!")
        break
    elif board[0] == board[3] == board[6] == "X":
        print("X wins!")
        break
    elif board[1] == board[7] == board[4] == "X":
        print("X wins!")
        break
    elif board[2] == board[5] == board[8] == "X":
        print("X wins!")
        break
    elif board[6] == board[4] == board[2] == "X":
        print("X wins!")
        break
    elif board[0] == board[4] == board[8] == "X":
        print("X wins!")
        break
    elif board[0] == board[1] == board[2] == "O":
        print("O wins!")
        break
    elif board[3] == board[4] == board[5] == "O":
        print("O wins!")
        break
    elif board[6] == board[7] == board[8] == "O":
        print("O wins!")
        break
    elif board[0] == board[3] == board[6] == "O":
        print("O wins!")
        break
    elif board[1] == board[7] == board[4] == "O":
        print("O wins!")
        break
    elif board[2] == board[5] == board[8] == "O":
        print("O wins!")
        break
    elif board[6] == board[4] == board[2] == "O":
        print("O wins!")
        break
    elif board[0] == board[4] == board[8] == "O":
        print("O wins!")
        break
    elif "-" not in board:
        print("It's a Tie!")
        break
    player_two_input()
    game_board()
    if board[0] == board[1] == board[2] == "X":
        print("X wins!")
        break
    elif board[3] == board[4] == board[5] == "X":
        print("X wins!")
        break
    elif board[6] == board[7] == board[8] == "X":
        print("X wins!")
        break
    elif board[0] == board[3] == board[6] == "X":
        print("X wins!")
        break
    elif board[1] == board[7] == board[4] == "X":
        print("X wins!")
        break
    elif board[2] == board[5] == board[8] == "X":
        print("X wins!")
        break
    elif board[6] == board[4] == board[2] == "X":
        print("X wins!")
        break
    elif board[0] == board[4] == board[8] == "X":
        print("X wins!")
        break
    elif board[0] == board[1] == board[2] == "O":
        print("O wins!")
        break
    elif board[3] == board[4] == board[5] == "O":
        print("O wins!")
        break
    elif board[6] == board[7] == board[8] == "O":
        print("O wins!")
        break
    elif board[0] == board[3] == board[6] == "O":
        print("O wins!")
        break
    elif board[1] == board[7] == board[4] == "O":
        print("O wins!")
        break
    elif board[2] == board[5] == board[8] == "O":
        print("O wins!")
        break
    elif board[6] == board[4] == board[2] == "O":
        print("O wins!")
        break
    elif board[0] == board[4] == board[8] == "O":
        print("O wins!")
        break
    elif "-" not in board:
        print("It's a Tie!")
        break
