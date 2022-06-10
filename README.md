# Rubiks-Cube
A Rubik's cube program.

The moveSet variable is where the moves to be done by the program are stored as a list of lists. Move options are therefore:

Front;  [faceF, clockwise] or [faceF, anticlockwise]
Left;   [faceL, clockwise] or [faceL, anticlockwise]
Back;   [faceB, clockwise] or [faceB, anticlockwise]
Right;  [faceR, clockwise] or [faceR, anticlockwise]
Top;    [faceT, clockwise] or [faceT, anticlockwise]
Down;   [faceD, clockwise] or [faceD, anticlockwise]

By changing from 'test = False' to 'test = True' and by copying the above moves into the blank 'moveSet[]' within the square brackets and separated by a comma, the program will allow for easy tracking of specific cells.

In total ~10 hrs work.

The colour characters can be changed in 'makeRubiks' to represent the different faces of the Rubik's Cube differently when using the non-test run, and specific cells can be changed in 'makeTestRubiks'. The spacing of the display is determined by the length of the top left cell of the front face however, so the display is designed around all cells being a uniform size.

Run in your choice of Python environment.
