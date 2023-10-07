import random

random.seed()

def draw_board(board):
    '''drawing board for noughts and crosses'''
    
    print(' ----------')
    print('|',board[0][0],'|',board[0][1],'|',board[0][2],'|')
    print(' ----------')
    print('|',board[1][0],'|',board[1][1],'|',board[1][2],'|')
    print(' ----------')
    print('|',board[2][0],'|',board[2][1],'|',board[2][2],'|')
    print(' -----------')
    

def welcome(board):
    '''to print welcome message for user'''
    print("Welcome to the 'Unbeatable Noughts and Crosses' game.")
    draw_board(board)
    

def initialise_board(board):
    '''to set all elements of the board to one space'''
    for i in range(3):
        for x in range(3):
           board[i][x]=' '
    return board

def get_player_move(board):
    '''to ask user for the move'''
    
    print("Your Options: ")
    print('1 2 3 \n4 5 6 \n7 8 9')
    try:
        choice=int(input("What's your move: "))
        if choice==1:
            row=0
            col=0
        elif choice==2:
            row=0
            col=1
        elif choice==3:
            row=0
            col=2
        elif choice==4:
            row=1
            col=0
        elif choice==5:
            row=1
            col=1
        elif choice==6:
            row=1
            col=2
        elif choice==7:
            row=2
            col=0
        elif choice==8:
            row=2
            col=1
        elif choice==9:
            row=2
            col=2
        while board[row][col]!=' ':
            print("Position Taken.")
            choice=int(input("What's your move: "))
            if choice==1:
                row=0
                col=0
            elif choice==2:
                row=0
                col=1
            elif choice==3:
                row=0
                col=2
            elif choice==4:
                row=1
                col=0
            elif choice==5:
                row=1
                col=1
            elif choice==6:
                row=1
                col=2
            elif choice==7:
                row=2
                col=0
            elif choice==8:
                row=2
                col=1
            elif choice==9:
                row=2
                col=2
    except ValueError:
        print("valid move!!\n")
    return row, col

def choose_computer_move(board):
    '''to let the computer choose a cell to put a nought in'''

    choice=random.randint(1,9)

    if choice==1:
        row=0
        col=0
    elif choice==2:
        row=0
        col=1
    elif choice==3:
        row=0
        col=2
    elif choice==4:
        row=1
        col=0
    elif choice==5:
        row=1
        col=1
    elif choice==6:
        row=1
        col=2
    elif choice==7:
        row=2
        col=0
    elif choice==8:
        row=2
        col=1
    elif choice==9:
        row=2
        col=2
    while board[row][col]!=' ':
        choice=random.randint(1,9)

        if choice==1:
            row=0
            col=0
        elif choice==2:
            row=0
            col=1
        elif choice==3:
            row=0
            col=2
        elif choice==4:
            row=1
            col=0
        elif choice==5:
            row=1
            col=1
        elif choice==6:
            row=1
            col=2
        elif choice==7:
            row=2
            col=0
        elif choice==8:
            row=2
            col=1
        elif choice==9:
            row=2
            col=2
    return row, col


def check_for_win(board, mark):
    '''to check if user won or computer won'''

    if board[0][0]==mark and board[0][1]==mark and board[0][2]==mark:
        return True
    elif  board[1][0]==mark and board[1][1]==mark and board[1][2]==mark:
        return True
    elif  board[2][0]==mark and board[2][1]==mark and board[2][2]==mark:
        return True
    elif  board[0][0]==mark and board[1][0]==mark and board[2][0]==mark:
        return True
    elif  board[0][1]==mark and board[1][1]==mark and board[2][1]==mark:
        return True
    elif  board[0][2]==mark and board[1][2]==mark and board[2][2]==mark:
        return True
    elif  board[0][0]==mark and board[1][1]==mark and board[2][2]==mark:
        return True
    elif  board[0][2]==mark and board[1][1]==mark and board[2][0]==mark:
        return True
    return False

def check_for_draw(board):
    '''to check if all cells are occupied'''

    for x in range(3):
        for i in range(3):
            if board[x][i]==' ':
                return False
    return True

def play_game(board):
    '''working mechanism of game'''

    board = initialise_board(board)
    draw_board(board)
    
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0
    

def menu():
    '''Main menu of to display the game with diffrent choices to do'''

    print ("Your choices are as follows")
    print (" 1 - Play the game \n 2 - Save Score \n 3 - Display Scores \n q - Quit Game")
    choice=input("Enter your choice: ")
    return choice 

def load_scores():
    '''to read the status of the learderboard file'''

    leaders={}
    with open("leaderboard.txt",'r') as f:
        for line in f:
           (key, val) = line.split()
           leaders[key] = val
    return leaders


def save_score(score):
    '''To save score of the user stats by asking their name'''

    player_name=input("Enter your name: ")
    with open("leaderboard.txt",'a') as f:
        f.write(player_name+" "+str(score)+"\n")
    return


def display_leaderboard(leaders):
    '''To display the score of game'''

    print("\n\n\t\tLEADERBOARD\n")
    print("\tName\t\tScore")
    print("\t----\t\t-----")
    for name, score in leaders.items():
        print("\t{}\t\t{}".format(name, score))