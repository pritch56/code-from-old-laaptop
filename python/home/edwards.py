import math
import sys

import pygame
from pygame.locals import *

##### Color Data #####
GREY = (100,100,100)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (255, 0, 255)
CYAN = (52, 113, 235)
RED = (200,0,0)
GREEN = (0,200,0)

##### GAME OPTIONS #####
FPS = 15
fontSize = 10
lineColor = GREY
WIDTH = 500
boxWidth = 20
gapWidth = 1
NumberOfBoxesInRow = WIDTH//boxWidth

##### Node Data #####
openList = [] # stores all the open Nodes
closedList = [] # stores all the closed Nodes

startHasBeenSet = False # Whether or not the start has been placed (prevents being placed many times)
endHasBeenSet = False # Whether or not the end has been placed (prevents being placed many times)

startNode = '' # the class of the start node will be stored here
endNode = '' # the class of the end node will be stored here

##### Initialising Libraries ######
pygame.font.init()
font = pygame.font.SysFont('arial', fontSize)
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Algorithm")

#### main class structure #### 
class Node(object):
    def __init__(self, rowNumber, columnNumber): #gridTuple is in (row, collum) form
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        self.gridPosition = (self.rowNumber, self.columnNumber)

        self.parent = None
        self.isBarrier = False
        self.isStart = False
        self.isEnd = False
        self.isPath = False
        self.isClosed = False
        self.isOpen = False
        self.isEmpty= True
 
        self.left = self.rowNumber * boxWidth
        self.right = self.left+boxWidth
        self.top = self.columnNumber * boxWidth
        self.bottom = self.top+boxWidth

        self.centrePixel = ((self.left+self.right)/2),((self.top+self.bottom)/2) # pixel at the centre of the node
        self.color = BLACK # default color (will be changed)

        self.gCost = None # distance from starting node
        self.hCost = None # distance from end node
        self.fCost = None # GCost + HCost

    def setStatesFalse(self): ## shouldnt effect start and end
        self.isBarrier = False
        #self.isStart = False
        #self.isEnd = False
        self.isPath = False
        self.isClosed = False
        self.isOpen = False
        self.isEmpty = False

    def updateColor(self):
        if self.isBarrier:
            self.color = BLACK
        if self.isEmpty:
            self.color = WHITE
        if self.isClosed:
            self.color = RED
        if self.isOpen:
            self.color = GREEN
        if self.isPath:# must be near end
            self.color = CYAN
        if self.isEnd: # must be near end
            self.color = PURPLE
        if self.isStart:# must be near end
            self.color = PURPLE

    def draw_square(self):
        self.updateColor()
        rect = pygame.Rect(self.left, self.top, boxWidth, boxWidth) #Rect(left, top, width, height)
        pygame.draw.rect(WIN, self.color,rect) # surface, color, rectangle, width
	
    def getGCost(self): # distance from start # could have made this recursive
        totalDistance=0
        horisontalDistance = abs(startNode.rowNumber - self.rowNumber)
        verticalDistance = abs(startNode.columnNumber - self.columnNumber)
        totalDistance += math.sqrt((horisontalDistance**2)+(verticalDistance**2))
        return totalDistance

    def getHCost(self): # distance from end
        horisontalDistance = abs((endNode.rowNumber) - int(self.rowNumber))
        verticalDistance = abs((endNode.columnNumber) - int(self.columnNumber))
        ## pythagoras theorem
        return math.sqrt((horisontalDistance**2)+(verticalDistance**2))

    def getFCost(self):
        return float(self.getHCost() + self.getGCost())

def showTextInNode(text, centrePixel):
    #if not(self.isBarrier or self.isStart or self.isEnd):
    text = str(text)
    textsurface = font.render(text, False, (0, 0, 0))
    WIN.blit(textsurface,(centrePixel[0]-3, centrePixel[1]-10)) # -3 and -10 makes the text more centred

def make_grid():
	grid = []
	for rowNum in range(NumberOfBoxesInRow):
		grid.append([])
		for colNum in range(NumberOfBoxesInRow):
			node = Node(rowNum, colNum)
			grid[rowNum].append(node)
	return grid
grid = make_grid()

for row in grid:
    row[0].isBarrier = True
    row[NumberOfBoxesInRow-1].isBarrier = True

def drawLines():
    for x in grid:
        for column in x:
            verticalStart = 0, column.left
            verticalEnd = WIDTH, column.left
            pygame.draw.line(WIN, lineColor, verticalStart, verticalEnd, gapWidth) #surface, color, start, end, width

    for x in grid:
        for row in x:
            horizontalStart = row.left, 0
            horizontalEnd = row.left, WIDTH
            pygame.draw.line(WIN, lineColor, horizontalStart, horizontalEnd, gapWidth) #surface, color, start, end, width

def drawNodeSquares():
    WIN.fill(BLACK)
    for row in grid:
        for node in row:
            node.draw_square()
            if endNode != '' and startNode != '':
                if node.isOpen == True:
                    showTextInNode(node.getFCost(), node.centrePixel)
    drawLines()
    
def getRowAndColNumber(xy): ## takes x and y coordinates and returns the grid square values
    if xy == None:
        return None
    x, y = xy
    for row in range(len(grid)):
        for col in range(len(grid)):
            bottomXLimit = grid[row][col].left
            topXLimit = grid[row][col].right

            if x > bottomXLimit and x < topXLimit:
                bottomYLimit = grid[row][col].top
                topYLimit = grid[row][col].bottom

                if y > bottomYLimit and y < topYLimit:
                    return (row, col)

def getLowestOpenFCost():
    lowestFCost = float('inf') ## posative infinity
    lowestNode = ''
    openList = getOpenList()
    if openList != None:
        for node in openList: 
            if node.getFCost () < lowestFCost:
                lowestFCost = node.getFCost()
                lowestNode = node
    return lowestNode

def getNeighbours(node):
    row = node.rowNumber
    col = node.columnNumber

    neighbours = [
        grid[row-1][col-1], # top left neighbour
        grid[row-1][col], # left of neighbour
        grid[row-1][col+1], # bottom left neighbour

        grid[row][col-1], # top middle neighbour
        grid[row][col+1], # bottom neighbour

        grid[row+1][col-1], # top right neighbour
        grid[row+1][col], # right of neighbour
        grid[row+1][col+1] # bottom right neighbour
    ]
    return neighbours

def getOpenList():
    openList = []
    for row in grid:
        for node in row:
            if node.isOpen:
                openList.append(node)

    return openList

def UpdateAllColors():
    for row in grid:
        for node in row:
            node.updateColor()

nextparent = ''
def drawPath():
    parent = endNode.parent
    while True:
        if parent.parent == None:
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()
            
        parent.setStatesFalse()
        parent.isPath = True
        pygame.time.wait(100)
        UpdateAllColors()
        drawNodeSquares()
        pygame.display.update()
        clock.tick(FPS)
        parent = parent.parent

def main():
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    startNode.setStatesFalse()
    startNode.isOpen = True
    pathFound = False
    while not pathFound:
        currentNode = getLowestOpenFCost() ## this will return a class object
        currentNode.isOpen = False # remove node from open
        currentNode.isClosed = True

        if currentNode == endNode:
            drawPath()
            pathFound = True

        for neighbour in getNeighbours(currentNode):
            if neighbour.isBarrier or neighbour.isClosed:
                pass
            else:
                if not(neighbour.isOpen): #or neighbour.getFCost() > currentNode.getFCost(): ## or path to the neighbour is shorter
                    neighbour.getFCost()
                    neighbour.parent = currentNode
                    if not(neighbour.isOpen):
                        neighbour.setStatesFalse()
                        neighbour.isOpen = True
        for rows in grid:
            for node in rows:
                node.updateColor()
        drawNodeSquares()
        clock.tick(FPS)
        pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
  
        if pygame.key.get_pressed():
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if startHasBeenSet and endHasBeenSet:
                    run = False
                    main()

        if pygame.mouse.get_pressed():
            pos = pygame.mouse.get_pos()
            try: ## sometimes returns none if you click on a line and not a square, this prevents the program from crashing
                clickedRow, clickedCol = getRowAndColNumber(pos) ##returns (row, col)
                clickedNode = grid[clickedRow][clickedCol]
            except:
                clickedNode = None ## this stays as None if the "getRowAndColNumber(pos)" fails, else it is redefined to the class
                
        if clickedNode != None: ## if the program has not thrown an error
            if pygame.mouse.get_pressed()[0]: # LEFT
                clickedNode.setStatesFalse()

                if startHasBeenSet and not endHasBeenSet: ## if the end has not been set but the start HAS been set
                    clickedNode.isEnd = True
                    endHasBeenSet = True
                    endNode = clickedNode

                if not startHasBeenSet:
                    clickedNode.isStart = True
                    startHasBeenSet = True
                    startNode = clickedNode

                else: ## if the start and the end have been set
                    if not(clickedNode.isEnd or clickedNode.isStart): ## if the square is not the start node or the end node
                        clickedNode.setStatesFalse
                        clickedNode.isBarrier = True

            if pygame.mouse.get_pressed()[2]: # RIGHT
                if not(clickedNode.isEnd or clickedNode.isStart): ## if the square is not the start node or the end node
                    clickedNode.setStatesFalse 
                    clickedNode.isBarrier = False
                    clickedNode.isEmpty = True

    drawNodeSquares()
    clock.tick(FPS)
    pygame.display.update()