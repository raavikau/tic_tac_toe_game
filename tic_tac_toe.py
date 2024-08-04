# Build a two-player Tic-Tac-Toe game
import os
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

def draw_board(spot):
    board = f"|{spot[1]}|{spot[2]}|{spot[3]}|\n|{spot[4]}|{spot[5]}|{spot[6]}|\n|{spot[7]}|{spot[8]}|{spot[9]}|"
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'

playing = True
turn = 0
prev_turn = -1
while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn:
        print("Spot already fill, please pick other")
    prev_turn = turn
    print("Player ", str((turn % 2)+1), "'s turn: pick your spot")
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {'X', 'O'}:
            turn += 1
            spots[int(choice)] = check_turn(turn)
