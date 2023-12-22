import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]      # Initializing the Board.
player = "x"
comp = "o"                 # Assigning variables to player and Computer
winner = None
gameRunning = True
playAgain = True

# Function for printing the Board of Tic Tac Toe game

def printBoard(board):
    print(board[0]," | ",board[1]," | ",board[2])
    print("--------------")
    print(board[3]," | ",board[4]," | ",board[5])
    print("--------------")
    print(board[6]," | ",board[7]," | ",board[8])
    
# Taking input from Player

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp<= 9 and board[inp-1] == "-":
        board[inp-1] = player
    else:
        print("This place is fill enter again: ")
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp<= 9 and board[inp-1] == "-":
            board[inp-1] = player
        
# Checking Winning conditions in Rows        

def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[6]
        return True

# Checking Winning conditions in Coloumns

def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[6]
        return True

# checking Winning conditions in Diagnals

def checkDiagnal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
# A Master function for checking winning.

def checkWin(name):
    global gameRunning
    if checkRow(board) or checkColumn(board) or checkDiagnal(board):
        if name == "Computer":
            print("\t-----------------------------")
            print("\tOops you lose,",name,"Wins")
            print("\t-----------------------------")
            printBoard(board)
            gameRunning = False
        else:
            print("\t-------------------------------------")
            print("\tCongratulation, The Winner is",name)
            print("\t-------------------------------------")
            printBoard(board)
            gameRunning = False
        
# A function which Returns True if anyone is winning. it is used in coputer input.

def isWinner(bo, le):
    if ((bo[0] == le and bo[1] == le and bo[2] == le) or
        (bo[3] == le and bo[4] == le and bo[5] == le) or
        (bo[6] == le and bo[7] == le and bo[8] == le) or
        (bo[0] == le and bo[3] == le and bo[6] == le) or
        (bo[1] == le and bo[4] == le and bo[7] == le) or
        (bo[2] == le and bo[5] == le and bo[8] == le) or
        (bo[0] == le and bo[4] == le and bo[8] == le) or
        (bo[2] == le and bo[4] == le and bo[6] == le)):
        return True

# Checking if the Game is a Draw. 

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("itz a draw")
        gameRunning = False

# Function which tells computer that player is winning and compter takes action in Responce. 

def isWinning(i,board,mark):
    boardCopy = board[:]
    boardCopy[i] = mark
    if isWinner(boardCopy,mark):
        return True
    else:
        return False
    
  # Taking input from the Computer.      

def computerInput(board):
    if board[4] == "-":
        move = 4
        return move
    else:
        for i in range(0,9):
            if isWinning(i,board,player) and board[i] == "-":
                return i
            elif isWinning(i,board,comp) and board[i] == "-":
                return i
        for i in [0,2,6,8]:
            if board[i] == "-":
                return i
        for i in [7,5,1,3]:
            if board[i] == "-":
                return i

# Asking if Player want to play again or not.

def secondGame():
    global playAgain
    global board
    global gameRunning
    print()
    print("\t---------------------------------------------")
    inp = str(input("\tEnter \'y\' for second game and \'n\' to quit: ")).lower()
    print("\t---------------------------------------------")
    if inp == 'y':
        board = ["-","-","-",
                "-","-","-",
                "-","-","-"]
        playAgain = True
        gameRunning = True
    else:
        playAgain = False

# Function for toss between player and computer. it will decide who will play first.

def toss():
    coin = random.randint(0,1)
    playerSelection = int(input("Enter 0 or 1 for toss: "))
    if coin == playerSelection:
        print("You won the toss. its your turn.")
        tosser = 'user'
        return tosser
    else:
        print("You lose the toss. its computer turn")
        tosser = 'comp'
        return tosser

# Asking from player that with which symbol he/she want to play

def symbol():
    inp = str(input("Enter your symbol ie \'x\' or \'o\': ")).upper()
    if inp == "X":
        mark  = "X"
        return mark
    else:
        mark = "O"
        return mark

# main function for running the game

def main():
    while playAgain:
        global player
        global comp
        print("\t=============================")
        print("\tWelcome to TIC TAC TOE game")
        print("\t Version: 10.1.01")
        print("\t Level : Impossible")
        print("\t=============================")
        print()
        nam = str(input("Enter your name here: ")).upper()
        print("Hi",nam,"! Lets, ready for the game.")
        print()
        printBoard(board)
        sym = symbol()
        if sym == "X":
            player = "X"
            comp = "O"
        elif sym == "O":
            player = "O"
            comp = "X"
        tosser = toss()
        while gameRunning:
            if tosser == 'user':
                printBoard(board)
                playerInput(board)
                checkWin("nam")
                checkTie(board)
                if gameRunning:
                    move = computerInput(board)
                    board[move] = comp
                    checkWin("Computer")
                    checkTie(board)
            else:
                move = computerInput(board)
                board[move] = comp
                printBoard(board)
                checkWin("Computer")
                checkTie(board)
                if gameRunning:
                    playerInput(board)
                    checkWin("nam")
                    checkTie(board)

        secondGame()

    print("\t-----------------------")
    print("\tThanks for Playing game")
    print("\t-----------------------")

main()