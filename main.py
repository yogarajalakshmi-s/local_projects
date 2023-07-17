print("Tic-Tac-Toe game\n")
arr = ["", "", "", "", "", "", "", "", ""]


def print_board():
    board = f"  {arr[0]}  | {arr[1]} |  {arr[2]} \n\
-------------\n\
  {arr[3]}  | {arr[4]} |  {arr[5]}  \n\
-------------\n\
  {arr[6]}  | {arr[7]} |  {arr[8]}  "

    print(board+"\n")


def check_player_position(current_player, move_num):
    if diagonal(current_player) or vertical(current_player) or horizontal(current_player):
        print(f"Player {current_player} won!")
        return True

    if move_num == 8:
        print(f"Draw!")
    return False


def diagonal(current_player):
    if arr[0] == current_player and arr[4] == current_player and arr[8] == current_player:
        return True
    elif arr[2] == current_player and arr[4] == current_player and arr[6] == current_player:
        return True
    return False


def vertical(current_player):
    if arr[0] == current_player and arr[3] == current_player and arr[6] == current_player or\
       arr[1] == current_player and arr[4] == current_player and arr[7] == current_player or\
       arr[2] == current_player and arr[5] == current_player and arr[8] == current_player:
        return True

    return False


def horizontal(current_player):
    if arr[0] == current_player and arr[1] == current_player and arr[2] == current_player or\
       arr[3] == current_player and arr[4] == current_player and arr[5] == current_player or\
       arr[6] == current_player and arr[7] == current_player and arr[8] == current_player:
        return True

    return False


for i in range(0, 9):
    player = "X" if i % 2 == 0 else "O"
    player_num = "1" if i % 2 == 0 else "2"
    position = int(input(f"Player {player_num}: Enter the position where you wish to place {player} (1 - 9) - "))
    arr[position - 1] = player
    won = check_player_position(player, i)
    print(print_board())
    if won:
        break
