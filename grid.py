class Grid:
    def __init__(self, x, y, fill=None):
        if isinstance(x, int) is not True or isinstance(y, int) is not True:
            raise TypeError("Grid x and y values must be integers")
        if x <= 0 or y <= 0:
            raise TypeError("Grid x and y values must be greater than zero")

        self.x = x
        self.y = y
        self.grid = []
        self.setGridValues(fill)

    def setCellValue(self, x, y, value):
        if isinstance(x, int) is not True or isinstance(y, int) is not True:
            raise TypeError("Grid x and y values must be integers")
        if x < 0 or x > (self.x - 1) or y < 0 or y > (self.y - 1):
            raise TypeError("Grid x and y values must be within range of grid")
        
        self.grid[x][y] = value

    def getCellValue(self, x, y):
        if isinstance(x, int) is not True or isinstance(y, int) is not True:
            raise TypeError("Grid x and y values must be integers")
        if x < 0 or x > (self.x - 1) or y < 0 or y > (self.y - 1):
            raise TypeError("Grid x and y values must be within range of grid")
        
        return self.grid[x][y]

    def setXStripValues(self, x, value, set_independent=0):
        if isinstance(x, int) is not True:
            raise TypeError("Grid x value must be integers")
        if x < 0 or x > (self.x - 1):
            raise TypeError("Grid x value must be within range of grid")
        
        if set_independent == 1:
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
        if isinstance(y, int) is not True:
            raise TypeError("Grid y value must be integers")
        if y < 0 or y > (self.y - 1):
            raise TypeError("Grid y value must be within range of grid")
        
        if set_independent == 1:
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
        for i in range(self.x):
            for j in range(self.y):
                if self.grid[i][j] == value:
                    return [i, j]
        return None

    def setGridValues(self, value):
        self.grid = [[value for _ in range(self.y)] for __ in range(self.x)]

    def swapTwo(self, x1, y1, x2, y2):
        if (isinstance(x1, int) is not True or isinstance(y1, int) is not True or 
                isinstance(x2, int) is not True or isinstance(y2, int) is not True):
            raise TypeError("Grid x and y values must be integers")
        if (x1 < 0 or x1 > (self.x - 1) or y1 < 0 or y1 > (self.y - 1) or
                x2 < 0 or x2 > (self.x - 1) or y2 < 0 or y2 > (self.y - 1)):
            raise TypeError("Grid x and y values must be within range of grid")
        
        temp = self.grid[x1][y1]

        self.setCellValue(x1, y1, self.grid[x2][y2])
        self.setCellValue(x2, y2, temp)
