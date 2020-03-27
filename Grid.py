### TODO Error Checking

class Grid():
    def __init__(self, x, y, fill = None):
        self.x = x
        self.y = y
        self.setGridValues(fill)
        
    def setCellValue(self, x, y, value):
        self.grid[x][y] = value

    def getCellValue(self, x, y):
        return self.grid[x][y]

    def setXStripValues(self, x, value):
        for n in range(self.y):
                self.grid[x][n] = value

    def setYStripValues(self, y, value):
        for n in range(self.x):
                self.grid[n][y] = value

    def setGridValues(self, value):
        row = []
        self.grid = []
        
        for n in range(y):
            row.append(fill)    

        for n in range(x):
            self.grid.append(row)
