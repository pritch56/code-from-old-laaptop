import pygame

ROWS = 6
COLS = 7
BOXSIZE = 100

WIDTH = BOXSIZE*COLS
HEIGHT = BOXSIZE*ROWS

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

moveNumber = 0 # when this reaches 42 the game is finshed and if odd it's red's move and if even it's blue's move
moveSuccessful = False

board = ([[[] for i in range(WIDTH//BOXSIZE)]for i in range(HEIGHT//BOXSIZE)])

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

def dropPiece(col, color): # takes a column number and "drops" a piece in that "slot", returns false if the move is invalid
    for i in range(5, -1, -1): #because the height of the board is 6 tiles
        if board[i][col] == []: 
            board[i][col] = color
            return True
    return False

def drawBoard():
    for col in range(HEIGHT//BOXSIZE):
        for row in range(WIDTH//BOXSIZE):
            currentSpace = board[col][row]
            rect = pygame.Rect(row*BOXSIZE, col*BOXSIZE, BOXSIZE, BOXSIZE) # left top width height

            if currentSpace == "B": 
                pygame.draw.rect(window, BLUE, rect)
            elif currentSpace == "R":
                pygame.draw.rect(window, RED, rect)
            else:
                pygame.draw.rect(window, BLACK, rect)

def gameWon(piece):
    # horizontals
    for col in range(COLS-3): #since a horisontal row cannot start in the last 3 boxes
        for row in range(ROWS):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True

    # Check vertical locations for win
        for col in range(COLS):
            for row in range(ROWS-3):
                if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                    return True

        # Check positively sloped diaganols
        for col in range(COLS-3):
            for row in range(ROWS-3):
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for col in range(COLS-3):
            for row in range(3, ROWS):
                if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                    return True

while True:
    if moveNumber == 42:
        pygame.quit()

    if gameWon("B"):
        print("Blue Has Won")
        pygame.quit()

    if gameWon("R"):
        print("Red Has Won")
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            row = mouseX//BOXSIZE

            if moveNumber % 2 == 0:   # if movenumber is even then it is red's turn else it is blue's 
                moveSuccessful = dropPiece(row, "R")
            else:
                moveSuccessful = dropPiece(row, "B")
            
            if moveSuccessful:      
                moveSuccessful = False
                moveNumber += 1

    drawBoard()
    pygame.display.update()