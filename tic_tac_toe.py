# Build a two-player Tic-Tac-Toe game
import os
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

def draw_board(spot):
    board = f"|{spot[1]}|{spot[2]}|{spot[3]}|\n|{spot[4]}|{spot[5]}|{spot[6]}|\n|{spot[7]}|{spot[8]}|{spot[9]}|"
    print(board)
draw_board(spots)
