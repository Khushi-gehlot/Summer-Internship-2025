print("Welcome to Tic Tac Toe")

def displayboard(board):
    n = 0
    for i in range(3):
        for j in range(i,i+3):
            print(board[n], "| ", end="")
            n = n + 1
        print("\n-----------")

def setboard(choice, player,board):
    if board[choice-1] == choice:
        board[choice-1] = player
    else :
        print("That is not a valid choice")




def selectplayer(cplayer):
    if cplayer == "X":
        cplayer = "O"
        print("Player O: ", end="")
    else:
        cplayer = "X"
        print("Player X: ", end="")
    return cplayer

def isover(boards):
    win_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i, j, k in win_combos:
        if boards[i] == boards[j] == boards[k]:
            return True
    return False

def newgame():
    currplayer = "O"
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chances = 9
    over = False
    displayboard(board)
    while chances and over == False:

        currplayer = selectplayer(currplayer)
        chances -= 1
        choice = int(input())
        setboard(choice, currplayer, board)
        displayboard(board)
        over = isover(board)
        if over:
            print("Game Over! Player", currplayer, "Wins")
            break

    if over != True:
        print("Game Draw")

newgame()
while True:
    res = input("Do you want to play again? (y/n) ")
    if res.lower() == "y":
        newgame()
    elif res.lower() == "n":
        break
    else:
        print("Please enter y or n")















