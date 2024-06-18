gridSize = 20
cols, rows = 0, 0
pacMan = None

def setup():
    global cols, rows, pacMan
    size(400, 400)
    cols, rows = width // gridSize, height // gridSize
    pacMan = PacMan(int(cols / 2), int(rows / 2))

def draw():
    background(0)
    stroke(100) 
    for i in range(cols):
        line(i * gridSize, 0, i * gridSize, height)
    for j in range(rows):
        line(0, j * gridSize, width, j * gridSize)
    
    pacMan.show()
    pacMan.move()

def keyPressed():
    if key == 'w' or key == 'W':
        pacMan.dir(0, -1)
    elif key == 's' or key == 'S':
        pacMan.dir(0, 1)
    elif key == 'a' or key == 'A':
        pacMan.dir(-1, 0)
    elif key == 'd' or key == 'D':
        pacMan.dir(1, 0)

class PacMan:
    def __init__(self, x, y):
        self.x = x * gridSize
        self.y = y * gridSize
        self.speed = 2 
        self.xdir = 0
        self.ydir = 0
        self.next_xdir = 0
        self.next_ydir = 0

    def show(self):
        fill(255, 255, 0)
        ellipse(self.x + gridSize / 2, self.y + gridSize / 2, gridSize, gridSize)

    def move(self):
        if self.x % gridSize == 0 and self.y % gridSize == 0:
            self.xdir = self.next_xdir
            self.ydir = self.next_ydir

        # Continuous movement
        self.x += self.xdir * self.speed
        self.y += self.ydir * self.speed

        if self.x < 0:
            self.x = width - gridSize
        elif self.x >= width:
            self.x = 0

        if self.y < 0:
            self.y = height - gridSize
        elif self.y >= height:
            self.y = 0

    def dir(self, xdir, ydir):
        self.next_xdir = xdir
        self.next_ydir = ydir
