import numpy as np

#makeRubiks returns a 6 element array with each element a 3 element array of 3 elements of strings of the face colour.
def makeRubiks():
    frontFace = np.full((3, 3), "G")
    leftFace = np.full((3, 3), "O")
    backFace = np.full((3, 3), "B")
    rightFace = np.full((3, 3), "R")
    topFace = np.full((3, 3), "W")
    downFace = np.full((3, 3), "Y")
    return(np.array([frontFace, leftFace, backFace, rightFace, topFace, downFace]))
#

#explodeView provides an exploded view in console of the current rubiks cube state. Designed for single-character colours.
def explodeView(rubiks): #Is it better to pass a global variable into a function or to just leave it global?
    for i in range(3):
        print("       {}|{}|{}".format(rubiks[4][i][0], rubiks[4][i][1], rubiks[4][i][2]))
    print()
    for i in range(3):
        print("{}|{}|{}  {}|{}|{}  {}|{}|{}  {}|{}|{}".format(
            rubiks[1][i][0], rubiks[1][i][1], rubiks[1][i][2],
            rubiks[0][i][0], rubiks[0][i][1], rubiks[0][i][2],
            rubiks[3][i][0], rubiks[3][i][1], rubiks[3][i][2],
            rubiks[2][i][0], rubiks[2][i][1], rubiks[2][i][2]))
    print()
    for i in range(3):
        print("       {}|{}|{}".format(rubiks[5][i][0], rubiks[5][i][1], rubiks[5][i][2]))
#

#rotateSelection takes the face being rotated, the direction (1 for clockwise, -1 for counterclockwise) and the rubiks matrix array to return the transformed matrix array.
def rotateSelection(faceNumber, direction, rubiks):
    
    #Unwrap face of cube into a list:
    faceList = [rubiks[faceNumber][0][0], rubiks[faceNumber][0][1], rubiks[faceNumber][0][2], rubiks[faceNumber][1][2],
                rubiks[faceNumber][2][2], rubiks[faceNumber][2][1], rubiks[faceNumber][2][0], rubiks[faceNumber][1][0]]
    
    #Move 2 end of list to start if clockwise, start of list to end if counterclockwise:
    temp = faceList[-2*direction:]
    faceList = temp + faceList[:-2*direction]
    
    #Overwrite the old face with the rotated face:
    rubiks[faceNumber][0][0] = faceList[0]; rubiks[faceNumber][0][1] = faceList[1]
    rubiks[faceNumber][0][2] = faceList[2]; rubiks[faceNumber][1][2] = faceList[3]
    rubiks[faceNumber][2][2] = faceList[4]; rubiks[faceNumber][2][1] = faceList[5]
    rubiks[faceNumber][2][0] = faceList[6]; rubiks[faceNumber][1][0] = faceList[7]
    
    if faceNumber == 4 or faceNumber == 5: #If clause handles top and bottom faces.
        heightModifier = (faceNumber - 4) * 2 #heightModifier = 0 for top, 2 for bottom, allows for finding correct sub-array.
        adjacentList = []
        for i in range(4):
            adjacentList.append(list(rubiks[i][heightModifier]))
        
        #Move 3 end of list to start if clockwise, start of list to end if counterclockwise:
        directionModifier = (heightModifier - 1) * (-1) #directionModifier = 1 for top, -1 for bottom as adjacentList is inverse order for bottom.
        temp = [adjacentList[-1*direction*directionModifier]]
        adjacentList = temp + adjacentList[:-1*direction*directionModifier]
        
        #Overwrite the old adjacents with the rotated adjacents:
        for i in range(4):
            rubiks[i][heightModifier] = adjacentList[i]
        
    elif faceNumber == 1 or faceNumber == 3: #Elif clause handles left and right faces.
        depthModifier = faceNumber - 1 #depthModifier = 0 for left, 2 for right
        adjacentList = []
        sidesToEdit = [0, 5, 2, 4]
        for i in range(3):
            adjacentList.append(rubiks[sidesToEdit[0]][i][0+depthModifier])
        for i in range(3):
            adjacentList.append(rubiks[sidesToEdit[1]][i][0+depthModifier])
        for i in range(2, -1, -1):
            adjacentList.append(rubiks[sidesToEdit[2]][i][2-depthModifier])
        for i in range(3):
            adjacentList.append(rubiks[sidesToEdit[3]][i][0+depthModifier])
            
        #Move 3 end of list to start if clockwise, start of list to end if counterclockwise:
        directionModifier = (depthModifier - 1) * (-1) #directionModifier = 1 for left, -1 for right, as adjacentList is inverse order for right.
        temp = adjacentList[-3*direction*directionModifier:]
        adjacentList = temp + adjacentList[:-3*direction*directionModifier]
        
        #Overwrite the old adjacents with the rotated adjacents:
        Counter = 0
        for i in range(3):
            rubiks[sidesToEdit[0]][i][0+depthModifier] = adjacentList[Counter]
            Counter += 1
        for i in range(3):
            rubiks[sidesToEdit[1]][i][0+depthModifier] = adjacentList[Counter]
            Counter += 1
        for i in range(2, -1, -1):
            rubiks[sidesToEdit[2]][i][2-depthModifier] = adjacentList[Counter]
            Counter += 1
        for i in range(3):
            rubiks[sidesToEdit[3]][i][0+depthModifier] = adjacentList[Counter]
            Counter += 1

    else: #Remainder of faces must be front and back, handled here.
        depthModifier = faceNumber
        adjacentList = []
        sidesToEdit = [4, 3, 5, 1]
        for i in range(3):
            adjacentList.append(rubiks[sidesToEdit[0]][2-depthModifier][i])
        for i in range(3):
            adjacentList.append(rubiks[sidesToEdit[1]][i][0+depthModifier])
        for i in range(2, -1, -1):
            adjacentList.append(rubiks[sidesToEdit[2]][0+depthModifier][i])
        for i in range(2, -1, -1):
            adjacentList.append(rubiks[sidesToEdit[3]][i][2-depthModifier])
        print("Al:", adjacentList)
        
        directionModifier = (depthModifier - 1) * (-1) #directionModifier = 1 for front, -1 for back, as adjacentList is inverse order for back.
        temp = adjacentList[-3*direction*directionModifier:]
        adjacentList = temp + adjacentList[:-3*direction*directionModifier]
        
        #Overwrite the old adjacents with the rotated adjacents:
        Counter = 0
        for i in range(3):
            rubiks[sidesToEdit[0]][2-depthModifier][i] = adjacentList[Counter]
            Counter += 1
        for i in range(3):
            rubiks[sidesToEdit[1]][i][0+depthModifier] = adjacentList[Counter]
            Counter += 1
        for i in range(2, -1, -1):
            rubiks[sidesToEdit[2]][0+depthModifier][i] = adjacentList[Counter]
            Counter += 1
        for i in range(2, -1, -1):
            rubiks[sidesToEdit[3]][i][2-depthModifier] = adjacentList[Counter]
            Counter += 1
            
    return(rubiks)
#

#
moveSet = [[0, 1], [3, -1], [4, 1], [2, -1], [1, 1], [5, -1]]
rubiksCube = makeRubiks() ##If I decide to make rubiks global and not pass it into functions, replace rubiksCube with rubiks
print("Cube Initialised:")
explodeView(rubiksCube)
for move in moveSet:
    print("Next Move")
    print("Face:{} | Direction: {}".format(move[0], move[1]))
    rotateSelection(move[0], move[1], rubiksCube)
    explodeView(rubiksCube)
    print("-"*27)
    print()
    
        