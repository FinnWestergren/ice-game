class grid: #prototype grid class
    #for classes the word "self" is used a shitload
    def create(self, cellSize, rowCount, colCount,gridColor, pygame):
        self.pygame = pygame
        self.cellSize = cellSize
        self.rowCount = rowCount
        self.colCount = colCount
        self.gridColor = gridColor
        self.x0 = 10 # you can use "self." as variable declaration. you don't need to declare x0 elsewhere first, for instance'
        self.y0 = 10
    def display(self,window):
        for x in range (0, self.colCount):
            for y in range (0, self.rowCount):
                self.cellXPos = self.x0 + x * self.cellSize
                self.cellYPos = self.y0 + y * self.cellSize
                self.pygame.draw.rect(window, self.gridColor, 
                [self.cellXPos,self.cellYPos,self.cellSize,self.cellSize],1)
                #rectangle created in window, with color gridColor, a position cellXPos,cellYPos, has 2 sides of length cellSize, and has a strokewidth of 1.