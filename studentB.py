import random

def is_player_starting():
    choice = input("Czy chcesz zaczac gre? y/n:")
    if choice == 'y' or choice == 'Y':
        return 1
    if choice =='n' or choice == 'N':
        return 0
    else:
        print("Nieprawidlowy wybor!")


def ai_move(board):
    empty_positions = [(i, j) for i in range(5) for j in range(5) if board[i][j] == ' ']
    if not empty_positions:
        return board
    move = random.choice(empty_positions)
    board[move[0]][move[1]] = 'O'  # AI - O, player - X
    return board

def get_user_move(board):
    valid_move = False
    while not valid_move:
        user_input = input("Enter your move (x,y): ")
        x, y = map(int, user_input.split(","))
        if 0 <= x < 5 and 0 <= y < 5 and board[x][y] == ' ':
            board[x][y] = X
            valid_move = True
        else:
            print("Nieprawidlowy ruch!")
    return board
