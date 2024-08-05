## Two player Tic Tac Toe Game implement in python
### Initial State
* Make a Game board that initially filled with numbers 1 through 9, with help of dictionary.
* In dictionary, key represent a block in the board and value represent move made by player.
* Check the turn of the player and take input from player to take the spot.
### Running State
* If player choose valid spot, clear the console and updates the spot with 'X' or 'O' and increment the turn.
* Keep track of the turn and previous turn that detects invalid turns.
### Terminal State
* Player choose to quit by pressing 'q'.
* If turns exceed than 8 that means the game is tie.
* Check for winning combination on the board if its true declare the winner and game is finished.
