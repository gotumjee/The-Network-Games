class Grid:
    """ A general container for game boards. """

    def __init__(self, x, y, fill=None):
        """ Initialises grid object.

        x and y denote the size of the board, and fill denotes
        what value should be placed in every space in the board. fill is None by default.
        """
        # Input Sanitation
        if isinstance(x, int) is not True or isinstance(y, int) is not True:
            raise TypeError("Grid x and y values must be integers")
        if x <= 0 or y <= 0:
            raise TypeError("Grid x and y values must be greater than zero")

        # Initialising Variables
        self.x = x
        self.y = y
        self.grid = []

        # Fill board with default value
        self.setGridValues(fill)

    def setCellValue(self, x, y, value):
        """ Set the space at (x, y) to the value in the variable value """
        # Input Sanitation
        if isinstance(x, int) is not True or isinstance(y, int) is not True:
            raise TypeError("Grid x and y values must be integers")
        if x < 0 or x > (self.x - 1) or y < 0 or y > (self.y - 1):
            raise TypeError("Grid x and y values must be within range of grid")

        self.grid[x][y] = value

    def getCellValue(self, x, y):
        """ Get value at space (x, y)"""
        # Input Sanitation
        if isinstance(x, int) is not True or isinstance(y, int) is not True:
            raise TypeError("Grid x and y values must be integers")
        if x < 0 or x > (self.x - 1) or y < 0 or y > (self.y - 1):
            raise TypeError("Grid x and y values must be within range of grid")
        
        return self.grid[x][y]

    def setXStripValues(self, x, value, set_independent=0):
        """ Set all spaces with the same x value

        When set_independent = 0, all spaces are set to the same value - the variable value. When set_independent = 1,
        however, each space can be set a different value. This is achieved by providing a list or tuple with the same
        length as the size of the board in the y direction.
        """
        # Input Sanitation
        if isinstance(x, int) is not True:
            raise TypeError("Grid x value must be integers")
        if x < 0 or x > (self.x - 1):
            raise TypeError("Grid x value must be within range of grid")

        if set_independent == 1:
            # Input Sanitation
            if isinstance(value, tuple) is not True and isinstance(value, list) is not True:
                raise TypeError("Grid X value set as independent, but not provided a list")
            elif len(value) != self.y:
                raise TypeError("Grid X value set as independent, but not provided a list of the correct length")
            
            for n in range(self.y):
                self.grid[x][n] = value[n]

        else:
            for n in range(self.y):
                self.grid[x][n] = value

    def setYStripValues(self, y, value, set_independent=0):
        """ Set all spaces with the same y value

        When set_independent = 0, all spaces are set to the same value - the variable value. When set_independent = 1,
        however, each space can be set a different value. This is achieved by providing a list or tuple with the same
        length as the size of the board in the x direction.
        """
        # Input Sanitation
        if isinstance(y, int) is not True:
            raise TypeError("Grid y value must be integers")
        if y < 0 or y > (self.y - 1):
            raise TypeError("Grid y value must be within range of grid")

        if set_independent == 1:
            # Input Sanitation
            if isinstance(value, tuple) is not True and isinstance(value, list) is not True:
                raise TypeError("Grid Y value set as independent, but not provided a list")
            elif len(value) != self.x:
                raise TypeError("Grid Y value set as independent, but not provided a list of the correct length")

            for n in range(self.x):
                self.grid[n][y] = value[n]

        else:
            for n in range(self.x):
                self.grid[n][y] = value

    def findPiece(self, value):
        """ Find the first occurrence of value in the board """
        for i in range(self.x):
            for j in range(self.y):
                if self.grid[i][j] == value:
                    return [i, j]
        return None

    def setGridValues(self, value):
        """ Create board filled with value of variable value """
        self.grid = [[value for _ in range(self.y)] for __ in range(self.x)]

    def swapTwo(self, x1, y1, x2, y2):
        """ Swap the values of (x1, y1) and (x2, y2) """
        # Input Sanitation
        if (isinstance(x1, int) is not True or isinstance(y1, int) is not True or
                isinstance(x2, int) is not True or isinstance(y2, int) is not True):
            raise TypeError("Grid x and y values must be integers")
        if (x1 < 0 or x1 > (self.x - 1) or y1 < 0 or y1 > (self.y - 1) or
                x2 < 0 or x2 > (self.x - 1) or y2 < 0 or y2 > (self.y - 1)):
            raise TypeError("Grid x and y values must be within range of grid")
        
        temp = self.grid[x1][y1]
        self.setCellValue(x1, y1, self.grid[x2][y2])
        self.setCellValue(x2, y2, temp)
