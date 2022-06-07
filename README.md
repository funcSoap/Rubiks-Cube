# Rubiks-Cube
A Rubik's cube program.

The moveSet variable is where the moves to be done by the program are stored as a list of lists. The faces are numbered: 0 Front, 1 Left, 2 Back, 3 Right, 4 Top and 5 Down. The directions are 1 for clockwise and -1 for anti-clockwise. Each move is therefore a 2 element list with a Face number followed by a Direction number (eg [1, -1] for left anti-clockwise) held in chronological order in the moveSet list.

