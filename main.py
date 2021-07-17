# I found a bug at least. When playing for a draw, not only the last move never gets filled in but it also prints the text "what is your next move"
# with the coursor haging on the user input number. 

# Another thing is, you win pretty easily and the message is "Player won". Wouldn't be cool to get the user's name?

# Welcome to my Tic Tac Toe python game
import random as random
import sys

theBoard = {}
i = 1
while i < 10:
    theBoard[str(i)] = " "
    i += 1


def board_print(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


player_ID = input("\nWelcome, what's your name?\n")


def game():  # This is the main part of the code
    board_print(theBoard)
    turn = "player"
    count = 0
    while turn == "player":
        checkpoint = input("\nSo, "+player_ID+", what's your next move?\nInput a number from 1-9, counting from the bottom left ")
        if "1" <= checkpoint <= "9":
            if theBoard[checkpoint] != " ":
                print("That space is already taken, try again.")
            else:
                theBoard[checkpoint] = "X"
                count += 1
                win_check(turn, count)
                turn = "CPU"

        else:
            print("Invalid input, try again.")
    while turn == "CPU":
        cpu_play = str(random.randrange(1, 10))
        if theBoard[cpu_play] == " ":
            theBoard[cpu_play] = "O"
            count += 1
            game()


def win_check(turn, count):
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)

    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)

    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)

    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)

    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)

    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)

    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
        board_print(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn.capitalize() + " won. ****")
        play_again(theBoard)
    elif count == 9:
        board_print(theBoard)
        print("\nGame Over.\n")
        print("**** It's a tie ****")
        play_again(theBoard)


def play_again(board):
    try_again = input("\n\nDo you wish to play again?(Y/N) ")
    if try_again.capitalize() == "Y":
        for value in board:
            theBoard[value] = " "
        game()
    elif try_again.capitalize() == "N":
        print("Thank you for playing with us!\n")
        sys.exit()
    else:
        print("Invalid input. Try again.\n")
        play_again(theBoard)


game()
