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
        self.grid = [[value for i in range(self.y)] for j in range(self.x)]

    def swapTwo(self, x1, y1, x2, y2):
        temp = self.getCellValue(x1,y1)
        
        self.setCellValue(x1, y1, self.getCellValue(x2,y2))
        self.setCellValue(x2, y2, temp)
