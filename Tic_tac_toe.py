"""Program: Tic tac toe game with numbers, we will display a board 3x3,
player1 will take odd numbers and player2 will take even numbers The first player to complete a line
that adds up to 15 is the winner."""
# Author: Malak mansour ibrahim ahmed
# Version: 1.3
# Date: 29/2/2024

# Display welcome message
print("\n*********** WELCOME TO TIC TAC TOE GAME WITH NUMBERS ***********")
# Display instructions
print("""
================================================================================
Instructions: player 1 takes odd numbers (1, 3, 5, 7, 9) and player 2 takes
even numbers (0, 2, 4, 6, 8). Players take turns to write their numbers. 
Odd numbers start. Use each number only once. The first person to complete a line 
that adds up to 15 is the winner.The line can have both odd and even numbers.
================================================================================
""")
# Game board
board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']


# Define a function to display game board
def display_board(board):
    print("_____________")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("_____________")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("_____________")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("_____________\n")


# Define a function to check the winner
def check_winner(board):
    # check horizontal line
    if int(board[0]) + int(board[1]) + int(board[2]) == 15:
        return True
    if int(board[3]) + int(board[4]) + int(board[5]) == 15:
        return True
    if int(board[6]) + int(board[7]) + int(board[8]) == 15:
        return True
    # check vertical line
    if int(board[0]) + int(board[3]) + int(board[6]) == 15:
        return True
    if int(board[1]) + int(board[4]) + int(board[7]) == 15:
        return True
    if int(board[2]) + int(board[5]) + int(board[8]) == 15:
        return True
    # check diagonal line
    if int(board[0]) + int(board[4]) + int(board[8]) == 15:
        return True
    if int(board[2]) + int(board[4]) + int(board[6]) == 15:
        return True
    return False


# Define a function to check if the game is a draw
def check_tie(board):
    for row in board:
        if row == '0':
            return False  # Game can continue, there is still '0' in the board
    return True  # All cells are filled it's a tie


player1_nums = [1, 3, 5, 7, 9]
player2_nums = [0, 2, 4, 6, 8]

display_board(board)
while True:
    # player 1
    player = 1
    print("Player1 turn")
    try:
        position = int(input("Enter a position (from 1 to 9): "))
    except ValueError:
        print("Error: Please enter a valid number!")
        continue
    # check if position is not between 1 and 9
    while position < 1 or position > 9:
        position = int(input("Error: Please enter a position (from 1 to 9): "))
        continue

    print(f"The numbers you have: {player1_nums}")
    num = int(input(f"Choose a number to add in position {position}: "))

    while num not in player1_nums:
        num = int(input(f"The numbers you have: {player1_nums} please choose one of them: "))

    position -= 1
    while board[position] != '0':
        position = int(input("This position is taken please choose another position: "))
        position -= 1
        continue
    # Replace "0" in the board with the number
    board[position] = num
    # Remove the number from the list
    player1_nums.remove(num)
    display_board(board)
    if check_winner(board):
        print(f"Player {player} is the winner!")
        break
    # check if the game is a draw
    if check_tie(board):
        print("It's a tie!")
        user_choice = input("Do you want to restart the game or to exit? (restart/exit): ").lower()
        if user_choice == 'restart':
            continue
        elif user_choice == 'exit':
            break
        else:
            print("Invalid choice! Exiting the game")
            break

    # player 2
    player = 2
    print("Player2 turn")
    try:
        position = int(input("Enter a position (from 1 to 9): "))
    except ValueError:
        print("Error: Please enter a valid number!")
        continue
    # check if position is not between 1 and 9
    while position < 1 or position > 9:
        position = int(input("Error: Please enter a position (from 1 to 9): "))
        continue

    print(f"The numbers you have: {player2_nums}")
    num = int(input(f"Choose a number to add in position {position}: "))

    while num not in player2_nums:
        num = int(input(f"The numbers you have: {player2_nums} please choose one of them: "))

    position -= 1
    while board[position] != '0':
        position = int(input("This position is taken please choose another position: "))
        position -= 1
        continue
    # Replace "0" in the board with the number
    board[position] = num
    # Remove the number from the list
    player2_nums.remove(num)
    display_board(board)
    if check_winner(board):
        print(f"Player {player} is the winner!")
        break
    # check if the game is a draw
    if check_tie(board):
        print("It's a tie!")
        user_choice = input("Do you want to restart the game or to exit? (restart/exit): ").lower()
        if user_choice == 'restart':
            continue
        elif user_choice == 'exit':
            break
        else:
            print("Invalid choice! Exiting the game.")
            break
