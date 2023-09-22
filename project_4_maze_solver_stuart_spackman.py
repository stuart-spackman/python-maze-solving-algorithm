from classes import Stack, Queue, Maze


def depthFirst(maze):
    """Takes in a maze from the Maze class and then solves it."""
    """Using a stack for this happens in linear time ciomplexity due to tracking one path at a time."""
    startRow = maze.start[0]
    startCol = maze.start[1]
    currCell = maze.grid[startRow][
        startCol
    ]  # make the current cell equal to the starting cell and push it to the stack
    s = Stack()  # stack will track visited spots
    q = (
        Queue()
    )  # queuing will be used to track path forward or dequeuing will be used to print the path
    s.push(maze.grid[startRow][startCol])
    q.enqueue(maze.grid[startRow][startCol])
    print(
        f"Starting point with coordinates of ({startRow}, {startCol}) has been added to the stack."
    )
    iteration = 0
    while not s.isEmpty():
        """Time complexity for this algorithm is O(N)"""
        currCell = s.pop()  # current cell being examined
        currCell.visited = True
        print("------------")
        print(f"Iteration: {iteration}")
        print("------------")
        maze.print_accounting_for_visits()
        # print(f"The cell we just popped off the stack has coordiantes of: ({currCell.row}, {currCell.col})")
        if (currCell.row, currCell.col) == maze.end:
            print("\nWe have now reached the end!")
            print(f"The coordinates are: ({currCell.row}, {currCell.col})")
            print("The path we took after the start was: ")
            while not q.isEmpty():
                currCell = q.deuqeue()
                print(f"({currCell.row}, {currCell.col})")
            break
        else:
            deadEnd = True  # this variable remains true neighbors DON'T get added
            i, j = (
                currCell.row,
                currCell.col,
            )  # simplify our coordinates for the current cell
            # west neighbor: [i][j-1]
            if j - 1 >= 0:  # check if out of bounds
                if maze.grid[i][j - 1] != 0:  # check if we hit a wall
                    if maze.grid[i][j - 1].visited == False:
                        s.push(maze.grid[i][j - 1])
                        q.enqueue(maze.grid[i][j - 1])
                        deadEnd = False
            # east neighbor: [i][j+1]
            if j + 1 <= maze.numOfCols - 1:  # check if out of bounds
                if maze.grid[i][j + 1] != 0:  # check if we hit a wall
                    if maze.grid[i][j + 1].visited == False:
                        s.push(maze.grid[i][j + 1])
                        q.enqueue(maze.grid[i][j + 1])
                        deadEnd = False
            # north neighbor: [i-1][j]
            if i - 1 >= 0:  # check if out of bounds
                if maze.grid[i - 1][j] != 0:  # check if we hit a wall
                    if maze.grid[i - 1][j].visited == False:
                        s.push(maze.grid[i - 1][j])
                        s.enqueue(maze.grid[i - 1][j])
                        deadEnd = False
            # south neighbor: [i+1][j]
            if i + 1 <= maze.numOfRows - 1:  # check if out of bounds
                if maze.grid[i + 1][j] != 0:  # check if we hit a wall
                    if maze.grid[i + 1][j].visited == False:
                        s.push(maze.grid[i + 1][j])
                        q.enqueue(maze.grid[i + 1][j])
                        deadEnd = False
            if deadEnd:
                """if we reach a dead end we took the wrong path and we can empty the queue"""
                """This appends the algorithm with a O(N) process so we're still linear."""
                while not q.isEmpty():
                    q.deuqeue()
        iteration += 1
        print("")


if __name__ == "__main__":
    print("Testing stack class".upper())
    MyStack = Stack()
    for i in range(1, 7):
        MyStack.push(i)
    print(f"If we push 1, 2, 3, 4, 5, 6, we get: {MyStack.items}")
    print(f"If we peek at the top item, we get: {MyStack.peek()}")
    print(f"If we pop the top item, we get: {MyStack.pop()}")
    print(f"If we check for empty, we get: {MyStack.isEmpty()}")
    print(f"If we check the size, we get: {MyStack.size()}\n")

    print("testing queue class".upper())
    MyQueue = Queue()
    for i in range(1, 7):
        MyQueue.enqueue(i)
    print(f"If we enqueue 1, 2, 3, 4, 5, 6, we get: {MyQueue.items}")
    print(f"If we dequeue the first item, we get, we get: {MyQueue.deuqeue()}")
    print(f"If we check the size, we get: {MyQueue.size()}")
    print(f"If we check for empty, we get: {MyQueue.isEmpty()}\n")

    print("Testing maze class".upper())
    print("When we create our maze and try printing it, we get...")
    maze = Maze("CST-201-Project4-maze.in.txt")
    maze.print()

    print("\nTesting the depth first algorithm".upper())
    print("Visited cells are accounted for by X's.")
    depthFirst(maze)
