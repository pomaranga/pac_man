GRID_SIZE = 30
cols, rows = 28, 31
#poprawki by Gabrysia
class PacMan:
    def __init__(self, x, y):
        self.x = x * GRID_SIZE
        self.y = y * GRID_SIZE
        self.speed = 3 
        self.xdirection = 0
        self.ydirection = 0
        self.next_xdirection = 0
        self.next_ydirection = 0
        self.score = 0

    def show(self):
        fill(255, 255, 0)
        ellipse(self.x + GRID_SIZE, self.y + GRID_SIZE, GRID_SIZE, GRID_SIZE)

    def move(self):
        if self.x % GRID_SIZE == 0 and self.y % GRID_SIZE == 0:
            self.xdirection = self.next_xdirection
            self.ydirection = self.next_ydirection

        self.x += self.xdirection * self.speed
        self.y += self.ydirection * self.speed

        if self.x < 0:
            self.x = width - GRID_SIZE
        elif self.x >= width:
            self.x = 0

        if self.y < 0:
            self.y = height - GRID_SIZE
        elif self.y >= height:
            self.y = 0

    def dir(self, xdirection, ydirection):
        self.next_xdirection = xdirection
        self.next_ydirection = ydirection
        
        
class Coin:
    def __init__(self, x, y):
        self.x = x * GRID_SIZE
        self.y = y * GRID_SIZE
        self.collected = False

    def show(self):
        if not self.collected:
            fill(255, 255, 255)
            ellipse(self.x, self.y, GRID_SIZE/3, GRID_SIZE/3)

    def collect(self, pacman):
        if dist(self.x, self.y, pacman.x+GRID_SIZE, pacman.y+GRID_SIZE) < GRID_SIZE:
            if not self.collected:
                self.collected = True
                pacman.score += 1        
    

#poprawki by oliwia
def setup():
    global cols, rows, pacMan, coins, score
    size(840, 930)
    coins=[]
    cols, rows = width // GRID_SIZE, height // GRID_SIZE
    pacMan = PacMan(int(cols / 2-1), int(rows -9))
    
    
    for i in range(1,cols):
        for j in range(1,rows):
            #if i%2==0 and j%2!=0:
                coins.append(Coin(i, j))

def draw():
    global score
    background(0)
    stroke(100) 
    for i in range(cols):
        line(i * GRID_SIZE, 0, i * GRID_SIZE, height)
    for j in range(rows):
        line(0, j * GRID_SIZE, width, j * GRID_SIZE)
    
    pacMan.show()
    pacMan.move()
    
    coins_collected = 0
    for coin in coins:
        coin.show()
        coin.collect(pacMan)
        if coin.collected:
            coins_collected += 1
    
    img=loadImage("maze01.png")       
    image(img,0,0)
    
    fill(255)
    textSize(20)
    text("Score: " + str(pacMan.score), 10, height - 10)

def keyPressed():
    if key == 'w' or key == 'W':
        pacMan.dir(0, -1)
    elif key == 's' or key == 'S':
        pacMan.dir(0, 1)
    elif key == 'a' or key == 'A':
        pacMan.dir(-1, 0)
    elif key == 'd' or key == 'D':
        pacMan.dir(1, 0)
