from pathlib import Path


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def deuqeue(self):
        return self.items.pop(0)


class MazeCell:
    def __init__(self, row=-1, col=-1, start=False, end=False):
        self.row = row
        self.col = col
        self.visited = False
        self.twiceVisited = False
        self.direction = 0
        self.start = start
        self.end = end
        # 0: north, 1: east, 2: south, 3: west, 4: complete

    def copy(self):
        CopyCell = MazeCell(self.row, self.col)
        CopyCell.visited = self.visited
        CopyCell.direction = self.direction
        return CopyCell

    def getDirection(self):
        return self.direction

    def advanceDirection(self):
        self.direction += 1
        if self.direction == 4:
            self.visited == True

    def setCoordinates(self, newRow, newCol):
        self.row = newRow
        self.col = newCol

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    """
    And here is where the @Override appears. 
    Is that necessary in Python?
    """

    def visit(self):
        self.visited = True

    def reset(self):
        self.visited = False

    def unvisited(self):
        return not self.visited

    def toString(self):
        string = f"(coordinates = {self.row}, {self.col})\nvisited = {self.visited}\ndirection = {self.direction}"


class Maze:
    """Takes in a text file and creates a maze out of it."""

    def __init__(self, textFile):
        path = Path(textFile)  # first read in text file
        contents = path.read_text()
        inputCells = contents.split()
        self.numOfRows = int(
            inputCells.pop(0)
        )  # then extract number of rows and columns
        self.numOfCols = int(inputCells.pop(0))

        inputGrid = self._create_input_grid(
            inputCells
        )  # then turn the text file into a list of lists
        self.start = Maze._get_start(
            self, inputGrid
        )  # get start and end coordinates as a tuple
        self.end = Maze._get_end(self, inputGrid)
        mazeGrid = self._convert_input_grid(inputGrid)  # create a MazeCell class

        self.grid = mazeGrid

    def _create_input_grid(self, inputCells):
        """Converts the input array to a grid with coordinates."""
        inputGrid = []
        for i in range(self.numOfRows):
            inputGrid.append([])
            for j in range(self.numOfCols):
                inputGrid[i].append(int(inputCells.pop(0)))
        return inputGrid

    def _convert_input_grid(self, inputGrid):
        """Converts the input grid to a grid of maze cells."""
        newGrid = []
        for i in range(self.numOfRows):
            newGrid.append([])
            for j in range(self.numOfCols):
                if inputGrid[i][j] == 0:
                    newGrid[i].append(0)
                elif inputGrid[i][j] == 1:
                    newGrid[i].append(MazeCell(i, j))
                elif inputGrid[i][j] == 3:
                    newGrid[i].append(MazeCell(i, j, start=True))
                elif inputGrid[i][j] == 4:
                    newGrid[i].append(MazeCell(i, j, end=True))
        return newGrid

    def _get_start(self, inputGrid):
        """Extracts starting coordinates as a tuple."""
        for i in range(self.numOfRows):
            for j in range(self.numOfCols):
                if inputGrid[i][j] == 3:
                    return (i, j)

    def _get_end(self, inputGrid):
        """Extracts ending coordinates as a tuple."""
        for i in range(self.numOfRows):
            for j in range(self.numOfCols):
                if inputGrid[i][j] == 4:
                    return (i, j)

    def print(self):
        """Prints the maze grid."""
        charArray = []
        for i in range(self.numOfRows):
            for j in range(self.numOfCols):
                if self.grid[i][j] == 0:
                    charArray.append(0)
                else:
                    if self.grid[i][j].start == True:
                        charArray.append("S")
                    elif self.grid[i][j].end == True:
                        charArray.append("E")
                    else:
                        charArray.append("1")
        Maze._print_array(charArray, self.numOfCols)

    def print_accounting_for_visits(self):
        """Prints the maze grid with visited spots accouted for."""
        charArray = []
        for i in range(self.numOfRows):
            for j in range(self.numOfCols):
                if self.grid[i][j] == 0:
                    charArray.append(0)
                else:
                    if self.grid[i][j].start == True:
                        charArray.append("X")
                    elif self.grid[i][j].end == True:
                        if self.grid[i][j].visited == True:
                            charArray.append("X")
                        else:
                            charArray.append("E")
                    elif self.grid[i][j].visited == True:
                        if self.grid[i][j].twiceVisited == True:
                            charArray.append("@")
                        else:
                            charArray.append("X")
                    else:
                        charArray.append("1")
        Maze._print_array(charArray, self.numOfCols)

    def _print_array(arr, num):
        """Prints a one dimensional array 'num' elements at a time."""
        for i in range(0, len(arr), num):
            print(*arr[i : i + num])
