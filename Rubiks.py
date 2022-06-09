import numpy as np

#makeRubiks returns a 6 element array with each element a 3 element array of 3 elements of strings of the face colour.
def makeRubiks():
    frontFace   = np.full((3, 3), "G")
    leftFace    = np.full((3, 3), "O")
    backFace    = np.full((3, 3), "B")
    rightFace   = np.full((3, 3), "R")
    topFace     = np.full((3, 3), "W")
    downFace    = np.full((3, 3), "Y")
    return(np.array([frontFace, leftFace, backFace, rightFace, topFace, downFace]))
#

#makeTestRubiks returns a 6 element array with each element a 3 element array of 3 elements of strings individually customiseable.
def makeTestRubiks():
    frontFace   = np.array([["F00", "F01", "F02"],["F10", "F11", "F12"],["F20", "F21", "F22"]])
    leftFace    = np.array([["L00", "L01", "L02"],["L10", "L11", "L12"],["L20", "L21", "L22"]])
    backFace    = np.array([["B00", "B01", "B02"],["B10", "B11", "B12"],["B20", "B21", "B22"]])
    rightFace   = np.array([["R00", "R01", "R02"],["R10", "R11", "R12"],["R20", "R21", "R22"]])
    topFace     = np.array([["T00", "T01", "T02"],["T10", "T11", "T12"],["T20", "T21", "T22"]])
    downFace    = np.array([["D00", "D01", "D02"],["D10", "D11", "D12"],["D20", "D21", "D22"]])
    return(np.array([frontFace, leftFace, backFace, rightFace, topFace, downFace]))
#

#explodeView provides an exploded view in console of the current rubiks cube state. Designed for cell markers of uniform size.
def explodeView(rubiks, cellMarkerLength): #Is it better to pass a global variable into a function or to just leave it global?
    for row in range(3):
        print("{}{}|{}|{}".format(3*" "*cellMarkerLength+4*" ", rubiks[faceT][row][0], rubiks[faceT][row][1], rubiks[faceT][row][2]))
    print()
    for row in range(3):
        print("{}|{}|{}  {}|{}|{}  {}|{}|{}  {}|{}|{}".format(
            rubiks[faceL][row][0], rubiks[faceL][row][1], rubiks[faceL][row][2],
            rubiks[faceF][row][0], rubiks[faceF][row][1], rubiks[faceF][row][2],
            rubiks[faceR][row][0], rubiks[faceR][row][1], rubiks[faceR][row][2],
            rubiks[faceB][row][0], rubiks[faceB][row][1], rubiks[faceB][row][2]))
    print()
    for row in range(3):
        print("{}{}|{}|{}".format(3*" "*cellMarkerLength+4*" ", rubiks[faceD][row][0], rubiks[faceD][row][1], rubiks[faceD][row][2]))
#

#rotateSelection takes the face being rotated, the direction, and the rubiks matrix array to return the transformed matrix array.
def rotateSelection(faceNumber, direction, rubiks):

    rubiks[faceNumber] = rotateFace(direction, rubiks[faceNumber])

    if faceNumber == faceT or faceNumber == faceD:              #If clause handles top and down faces.
        rubiks = rotateTopBottomEdges(faceNumber, direction, rubiks)
    elif faceNumber == faceL or faceNumber == faceR:            #Elif clause handles left and right faces.
        rubiks = rotateLeftRightEdges(faceNumber, direction, rubiks)
    else:                                                       #Remainder of faces must be front and back, handled here.
        rubiks = rotateFrontBackEdges(faceNumber, direction, rubiks)

    return(rubiks)
#

#rotateFace takes direction and the 3x3 face array and returns the face after rotating the elements around the centre in direction.
def rotateFace(direction, face):
    #Unwrap face of cube into a list by taking the perimeter 8 elements from specified face of the cube in specific order:
    faceList = [face[0][0], face[0][1], face[0][2], face[1][2],
                face[2][2], face[2][1], face[2][0], face[1][0]]

    #Move 2 end of list to start if clockwise, start of list to end if counterclockwise:
    temp = faceList[-2*direction:]
    faceList = temp + faceList[:-2*direction]

    #Overwrite the old face with the rotated face:
    face[0][0] = faceList[0]; face[0][1] = faceList[1]
    face[0][2] = faceList[2]; face[1][2] = faceList[3]
    face[2][2] = faceList[4]; face[2][1] = faceList[5]
    face[2][0] = faceList[6]; face[1][0] = faceList[7]

    return(face)
#

#rotateTopBottom takes the number associated with the face, the direction to rotate in, and the rubiks matrix, and returns the rubiks matrix after applying the rotation.
def rotateTopBottomEdges(faceNumber, direction, rubiks):
    heightModifier = (faceNumber - 4) * 2 #heightModifier = 0 for top, 2 for bottom, allows for finding correct sub-array.
    edgeList = []
    row = heightModifier
    for face in range(4):
        edgeList.append(list(rubiks[face][row])) #Appends edgeList with each 3-element list at the top / bottom of each face edge to rotating one.

    #Move 3 end of list to start if clockwise, start of list to end if counterclockwise:
    directionModifier = (heightModifier - 1) * (-1) #directionModifier = 1 for top, -1 for bottom as edgeList is inverse order for bottom.
    temp = edgeList[-1*direction*directionModifier:]
    edgeList = temp + edgeList[:-1*direction*directionModifier]
        
    #Overwrite the old edges with the rotated edges:
    for face in range(4):
        rubiks[face][row] = edgeList[face]

    return(rubiks)
#

#rotateLeftRight takes the number associated with the face, the direction to rotate in, and the rubiks matrix, and returns the rubiks matrix after applying the rotation.
def rotateLeftRightEdges(faceNumber, direction, rubiks):
    depthModifier = faceNumber - 1 #depthModifier = 0 for left, 2 for right
    edgeList = []

    for row in range(3):
        column = depthModifier
        edgeList.append(rubiks[faceF][row][column])
        
    for row in range(3):
        column = depthModifier
        edgeList.append(rubiks[faceD][row][column])
        
    for row in range(2, -1, -1):
        column = 2 - depthModifier
        edgeList.append(rubiks[faceB][row][column])
        
    for row in range(3):
        column = depthModifier
        edgeList.append(rubiks[faceT][row][column])
            
    #Move 3 end of list to start if clockwise, start of list to end if counterclockwise:
    directionModifier = (depthModifier - 1) * (-1) #directionModifier = 1 for left, -1 for right, as edgeList is inverse order for right.
    temp = edgeList[-3*direction*directionModifier:]
    edgeList = temp + edgeList[:-3*direction*directionModifier]

    #Overwrite the old edges with the rotated edges:
    Counter = 0
    for row in range(3):
        column = depthModifier
        rubiks[faceF][row][column] = edgeList[Counter]
        Counter += 1
        
    for row in range(3):
        column = depthModifier
        rubiks[faceD][row][column] = edgeList[Counter]
        Counter += 1
        
    for row in range(2, -1, -1):
        column = 2 - depthModifier
        rubiks[faceB][row][column] = edgeList[Counter]
        Counter += 1
        
    for row in range(3):
        column = depthModifier
        rubiks[faceT][row][column] = edgeList[Counter]
        Counter += 1
        
    return(rubiks)
#

#rotateFrontBack takes the number associated with the face, the direction to rotate in, and the rubiks matrix, and returns the rubiks matrix after applying the rotation.
def rotateFrontBackEdges(faceNumber, direction, rubiks):
    depthModifier = faceNumber
    edgeList = []

    for column in range(3):
        row = 2 - depthModifier
        edgeList.append(rubiks[faceT][row][column])
        
    for row in range(3):
        column = depthModifier
        edgeList.append(rubiks[faceR][row][column])
        
    for column in range(2, -1, -1):
        row = depthModifier
        edgeList.append(rubiks[faceD][row][column])
        
    for row in range(2, -1, -1):
        column = 2 - depthModifier
        edgeList.append(rubiks[faceL][row][column])

    directionModifier = (depthModifier - 1) * (-1) #directionModifier = 1 for front, -1 for back, as edgeList is inverse order for back.
    temp = edgeList[-3*direction*directionModifier:]
    edgeList = temp + edgeList[:-3*direction*directionModifier]

    #Overwrite the old edges with the rotated edges:
    counter = 0
    
    for column in range(3):
        row = 2 - depthModifier
        rubiks[faceT][row][column] = edgeList[counter]
        counter += 1
        
    for row in range(3):
        column = depthModifier
        rubiks[faceR][row][column] = edgeList[counter]
        counter += 1
        
    for column in range(2, -1, -1):
        row = depthModifier
        rubiks[faceD][row][column] = edgeList[counter]
        counter += 1
        
    for row in range(2, -1, -1):
        column = 2-depthModifier
        rubiks[faceL][row][column] = edgeList[counter]
        counter += 1

    return(rubiks)
#

#####
faceF, faceL, faceB, faceR, faceT, faceD = 0, 1, 2, 3, 4, 5 #Global variable associating given faces of cube with a number.
clockwise, anticlockwise = 1, -1 #Global variable associating direction of rotation with a number.
test = False         #Set to false to run the routine with the colour characters, set to true to track movement of specific cells.

if test == True:
    moveSet = []    #Add moves to test in format '[[First-Face, First-Direction], [Second-Face, Second-Direction]]' etc, with example below.
    rubiksCube = makeTestRubiks()
    print("Test Cube Initialised:")
    print()
    
else:
    moveSet = [[faceF, clockwise], [faceR, anticlockwise], [faceT, clockwise], [faceB, anticlockwise], [faceL, clockwise], [faceD, anticlockwise]]
    rubiksCube = makeRubiks()
    print("Standard Cube Initialised:")
    print()

cellMarkerLength = len(rubiksCube[0][0][0])
explodeView(rubiksCube, cellMarkerLength)
for move in moveSet:
    print()
    print("-"*27)
    print()
    print("Next Move")
    print("Face:{} | Direction: {}".format(move[0], move[1]))
    print()
    rotateSelection(move[0], move[1], rubiksCube)
    explodeView(rubiksCube, cellMarkerLength)
    
        
