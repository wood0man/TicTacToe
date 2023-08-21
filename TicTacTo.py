import random
def ticTacTo(board=[]):
    continueTheMatch=True;
    #1 for O and 2 for X
    turn= random.randint(1, 2);
    while continueTheMatch:
        printTheBoard(board)
        if turn ==1:
            userChoiceRows=input("Enter your index of choice for rows(Os) => ");
            userChoiceColumn=input("Enter your index of choice for columns(Os) => ");
        else:
            userChoiceRows=input("Enter your index of choice for rows(Xs) => ");
            userChoiceColumn=input("Enter your index of choice for columns(Xs) => ");
        choosenRow=int(userChoiceRows)
        choosenColumn=int(userChoiceColumn)
        index=(choosenRow,choosenColumn)
        if turn==1:
           board= Os(board,index);
           turn=2;
        else:
            board=Xs(board,index);
            turn = 1
        continueTheMatch=winner(board);
    print("We have a winner!!");
    printTheBoard(board);
        
        
        

def winner(board=[]):
    #checks wether there's a winner
    if board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O' or board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O'or board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O'or board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O' or board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O'   or board[0][0]=='O' and board[0][1] == 'O' and board[0][2]=='O' or board[1][0]=='O' and board[1][1] == 'O' and board[1][2]=='O' or board[2][0]=='O' and board[2][1] == 'O' and board[2][2]=='O' or board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X'  or board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X' or board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X' or board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X' or board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X' or board[0][0]=='X' and board[0][1] == 'X' and board[0][2]=='X' or board[1][0]=='X' and board[1][1] == 'X' and board[1][2]=='X' or board[2][0]=='X' and board[2][1] == 'X' and board[2][2]=='X' :
    #return  false to break the while loop
        return False;
    else:
        return True;
#makes the player O choose
def Os(board=[],index=0):
    
            
    board[index[0]][index[1]]='O'
    return board;    
#makes the player X choose
def Xs(board=[],index=0):
    
    board[index[0]][index[1]]='X'
    return board;
    
    
def printTheBoard(board=[]):
    for i in board:
        print(i);



board=[['','',''],['','',''],['','','']];

ticTacTo(board);