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

        self.grid[x][y] = value

    def getCellValue(self, x, y):
        return self.grid[x][y]

    def setXStripValues(self, x, value, set_independent=0):
        if set_independent:
            for n in range(self.y):
                self.grid[x][n] = value[n]
        else:
            for n in range(self.y):
                self.grid[x][n] = value

    def setYStripValues(self, y, value, set_independent=0):
        if set_independent:
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
        temp = self.grid[x1][y1]

        self.setCellValue(x1, y1, self.grid[x2][y2])
        self.setCellValue(x2, y2, temp)
