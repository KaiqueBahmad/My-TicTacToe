#match_sample = [['X','O','X'],['O','X','O'],['X','O','']]



#Error Will raise if move is invalid
class InvalidMoveError(Exception):
    pass

#Tutorial about how to play
def tutorial():
    pass

#Runs a full match of the game
def play():
    X, O = 'X','O'
    match = createBlankGame()     #this is the place where the game will happen (the game is stored in a list, 1° line shows a sample)
    won = False
    while True:         #Loop where the rounds happen
        printGame(match) 

        #Get the move of X and see if it won, if Won, then congrats will appear and matchs end
        x_play = 'X' + input('X, your turn: ')     
        match = makeaMove(match, x_play)
        won, winner = checkWin(match)
        if won == True:
            break
        printGame(match)
        o_play = 'O' + input('O, your turn: ')
        match = makeaMove(match, o_play)
        won, winner = checkWin(match)
        if won == True:
            break

    printGame(match)
    print(f'{winner} won.')
    
def createBlankGame(): #blank game, with none move stored on it
    return [['','',''] for x in range(3)]

def printGame(game): #format the match display
    game = game.copy()
    for index_i, i in enumerate(game):
        for index_j, j in enumerate(i):
            if j == '':
                game[index_i][index_j] = 'TRIGGER'
    l1, l2, l3 = game[0], game[1], game[2]
    print(' '*5, f'{l1[0]} || {l1[1]} || {l1[2]}'.replace('TRIGGER','❒'),sep = '')
    print(' '*3, '========')
    print(' '*5, f'{l2[0]} || {l2[1]} || {l2[2]}'.replace('TRIGGER','❒'),sep = '')
    #print('|', f'{l2[1]}','|', sep = '')
    print(' '*3, '========')
    print(' '*5, f'{l3[0]} || {l3[1]} || {l3[2]}'.replace('TRIGGER','❒'),sep = '')

    
#This func was just to clean a little some parts of the code, Input is a list of string (like -> ['A', 'B', 'c']) and returns the sum of all the index (would be 'ABc')
def sumString(string): 
    new_string = ''
    for i in string:
        new_string += i
    return new_string

#Check every condition for if the game was won 
def checkWin(game):
    won = False
    winner = None
    for line in game:
        if sumString(line) == 'XXX':
            won, winner = True, 'X'
        elif sumString(line) == 'OOO':
            won, winner = True, 'O'
    stringed = ''
    for i in range(3):
        stringed += game[i][i]
    if stringed == 'XXX':
        won, winner =True, 'X'
    if stringed == 'OOO':
        won, winner = True, 'O'
    stringed = ''
    for i in range(3):
        stringed += game[i][2-i]
    if stringed == 'XXX':
        won, winner =True, 'X'
    if stringed == 'OOO':
        won, winner = True, 'O'

    vertical = [[game[j][i] for j in range(3)] for i in range(3)]
    for line in vertical:
        if sumString(line) == 'XXX':
            won, winner = True, 'X'
        elif sumString(line) == 'OOO':
            won, winner = True, 'O'
    
    set_content = set()
    for line in game:
        for square in line:
            set_content.add(square)
    if 'TRIGGER' not in set_content:
        won, winner = True, 'no ones'
        print('DRAW')
            
    return won, winner


#play should be a string with 2 numbers for index like, 'X11' for the first square and  'X21' for the square bellow it (allways describe if X or O before the play)
def makeaMove(game, move):
    x, y = int(move[1]) - 1, int(move[2]) - 1
    if game[x][y] == 'TRIGGER':
        game[x][y] = move[0]
        return game
    else:
        raise InvalidMoveError('Invalid Move')

play()
