#josue gallardo 12/17/2021


sudokuExample=[
    [0,0,0,0,0,0,0,0,8],
    [1,8,0,0,0,2,3,0,0],
    [0,6,0,0,5,7,0,0,1],
    [0,7,0,9,6,0,0,0,0],
    [0,9,0,7,0,4,0,1,0],
    [0,0,0,0,8,1,0,4,0],
    [6,0,0,2,4,0,0,8,0],
    [0,0,4,5,0,0,0,9,3],
    [5,0,0,0,0,0,0,0,0]
]

#print the sudo board
def printSudoku(example):
    for i in range(len(example)):
        #creating horizonal lines
        if i % 3 ==0 and i !=0:
            print("------------------------")
        #creating vertical lines
        for j in range(len(example[0])):
            if j % 3 ==0 and j !=0:
                print(" | ", end="")
            #max
            if j==8:
                print(example[i][j])
            #every value
            else:
                print(str(example[i][j]) + " ", end="")

#check each possible solution using recursion and backtracking
def backTrackRec(example):

    #check if we finished
    validSpace = findEmptySpace(example)
    if not validSpace:
        print("Result:")
        return True
    else:
        #test current spot
        row, col = validSpace

    #check input value from 1-9
    for i in range(1,10):
        #check if its valid by checking its postion,rep, etc...
        if checkValid(example, (row, col), i):
            example[row][col] = i

            if backTrackRec(example):
                return True

            #reset if its wrong
            example[row][col]=0

    #incorrect, try again
    return False

#rules of sudoku
def checkValid(example, emptyPostion, inputValue):

    #check rows for rep
    for x in range(len(example[0])):
        if example[emptyPostion[0]][x] == inputValue and emptyPostion[1] !=x:
            return False

    #check cols for rep
    for y in range(len(example)):
        if example[y][emptyPostion[1]] == inputValue and emptyPostion[0] !=y:
            return False

    #determine current box (4,4)
    boxX = emptyPostion[1] // 3
    boxY = emptyPostion[0] // 3

    # checking box of 3x3
    for i in range(boxY * 3, boxY*3 + 3):
        for j in range(boxX * 3, boxX*3 + 3):
            if example[i][j] == inputValue and (i,j)!=emptyPostion:
                return False

    #if passes all test= valid
    return True


#go through evey row and col to check for empty available spaces
def findEmptySpace(exaple):
    for i in range(len(exaple)):
        for j in range(len(exaple[0])):
            #0 represent empty spaces, return tuple with (row,col)
            if exaple[i][j]==0:
                return (i,j)

    #no more empty spaces
    return None

print("Sudoku Problem\n")
printSudoku(sudokuExample)
print("After BackTracking \n")
backTrackRec(sudokuExample)
printSudoku(sudokuExample)

