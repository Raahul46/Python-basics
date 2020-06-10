oard=[]
def disp_board(board):

    print("|\t", board[0], "\t|\t", board[1], "\t|\t", board[2], "\t|")
    print("-----------------------")
    print("|\t", board[3], "\t|\t", board[4], "\t|\t", board[5], "\t|")
    print("-----------------------")
    print("|\t", board[6], "\t|\t", board[7], "\t|\t", board[8], "\t|")


def player_input():

    marker = input("Player 1:Choose X or O:").upper()

    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"

def win_check(board, mark):
        return ((board[0] == mark and board[1] == mark and board[2] == mark) or
                (board[3] == mark and board[4] == mark and board[5] == mark) or
                (board[6] == mark and board[7] == mark and board[8] == mark) or
                (board[0] == mark and board[3] == mark and board[6] == mark) or
                (board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[0] == mark and board[4] == mark and board[8] == mark) or
                (board[2] == mark and board[4] == mark and board[6] == mark))


import random


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "player 1"
    else:
        return "player 2"

def space_check(board,position):
        return board[position] == " "

def full_board_check(board):

        for i in range(1, 10):
            if space_check(board, i):
                return False

        return True


def player_choice():

    position = int(input("enter position (0-8)"))

    return position

def main():
 testt=[]
 print("WELCOME TO TIC-TAC-TOE")
 while True:
    for x in range(0, 10):
        board.append(" ")
        testt.append(x)
    print("Enter values like")
    disp_board(testt)
    play1, play2 = player_input()
    gameon = True

    turn = choose_first()

    print(turn, " will play first")

    while gameon:

        if turn == "player 1":
            disp_board(board)
            print("\n"*2)
            player1 = player_choice()
            board[player1] = play1

            if win_check(board,play1):
                disp_board(board)
                print("\n" * 2)
                print("player1 wins ")
                gameon = False
            else:
                if full_board_check(board):
                    disp_board(board)
                    print("\n" * 2)
                    print("TIE")
                    gameon = False
                else:
                    turn = "player 2"
        else:
            if turn == "player 2":
                disp_board(board)
                player2 = player_choice()
                board[player2] = play2

                print("\n" * 2)
                if win_check(board, play2):
                    disp_board(board)
                    print("player2 wins ")
                    gameon = False
                    print("\n" * 2)
                else:
                    if full_board_check(board):
                        disp_board(board)
                        print("TIE")
                        gameon = False
                        continue
                    else:
                        turn = "player 1"
                        continue
if __name__ == '__main__':
      main()
