GRID_SIZE = 30
cols, rows = 28, 31
change_interval = 180
game_over_duration = 180
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Definicja: 0 = nic, 1 = ściana
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


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
        ellipse(self.x + GRID_SIZE / 2, self.y + GRID_SIZE / 2, GRID_SIZE, GRID_SIZE)

    def move(self):
        prev_x = self.x
        prev_y = self.y

        if self.x % GRID_SIZE == 0 and self.y % GRID_SIZE == 0:
            self.xdirection = self.next_xdirection
            self.ydirection = self.next_ydirection

        self.x += self.xdirection * self.speed
        self.y += self.ydirection * self.speed

        self.kolizje(prev_x, prev_y)

        self.krawedzie()

    def kolizje(self, prev_x, prev_y):
        for row in range(rows):
            for col in range(cols):
                if map_data[row][col] == 1:
                    block_x = col * GRID_SIZE
                    block_y = row * GRID_SIZE
                    if self.x + GRID_SIZE > block_x and self.x < block_x + GRID_SIZE and self.y + GRID_SIZE > block_y and self.y < block_y + GRID_SIZE:
                        self.x = prev_x
                        self.y = prev_y
                        self.wybor_kierunku()

    def wybor_kierunku(self):
        if self.next_xdirection != 0 and not self.kolizja(self.next_xdirection, 0):
            self.xdirection = self.next_xdirection
            self.ydirection = 0
        elif self.next_ydirection != 0 and not self.kolizja(0, self.next_ydirection):
            self.xdirection = 0
            self.ydirection = self.next_ydirection
        else:
            self.xdirection = 0
            self.ydirection = 0

    def krawedzie(self):
        if self.x < 0:
            self.x = width - GRID_SIZE
        elif self.x >= width:
            self.x = 0

        if self.y < 0:
            self.y = height - GRID_SIZE
        elif self.y >= height:
            self.y = 0

    def kolizja(self, xdirection, ydirection):
        next_x = self.x + xdirection * GRID_SIZE
        next_y = self.y + ydirection * GRID_SIZE
        col = next_x // GRID_SIZE
        row = next_y // GRID_SIZE
        if col < 0 or col >= cols or row < 0 or row >= rows:
            return True
        return map_data[row][col] == 1

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
                
class Ghost:
    def __init__(self, x, y):
        self.x = x * GRID_SIZE
        self.y = y * GRID_SIZE
        self.speed = 3
        self.xdirection = 1
        self.ydirection = 0
        self.next_xdirection = 1
        self.next_ydirection = 0

    def show(self):
        fill(255, 0, 0)
        ellipse(self.x + GRID_SIZE / 2, self.y + GRID_SIZE / 2, GRID_SIZE, GRID_SIZE)

    def move(self):
        prev_x = self.x
        prev_y = self.y

        if self.x % GRID_SIZE == 0 and self.y % GRID_SIZE == 0:
            if not self.kolizja(self.next_xdirection, self.next_ydirection):
                self.xdirection = self.next_xdirection
                self.ydirection = self.next_ydirection

       if not self.kolizja(self.xdirection, self.ydirection):
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

    def kolizja(self, xdirection, ydirection):
        next_x = self.x + xdirection * GRID_SIZE
        next_y = self.y + ydirection * GRID_SIZE
        col = next_x // GRID_SIZE
        row = next_y // GRID_SIZE
        if col < 0 or col >= cols or row < 0 or row >= rows:
            return True
        return map_data[row][col] == 1

    def dir(self, xdirection, ydirection):
        self.next_xdirection = xdirection
        self.next_ydirection = ydirection
        
def pseudo_random_choice(index):
    """Pseudo-random choice based on index and frameCount."""
    return directions[(frameCount // change_interval + index) % len(directions)]

def setup():
    global cols, rows, pacMan, coins, score, ghosts, img, game_over, game_over_time
    size(840, 930)
    initialize_game()
    
def initialize_game():
    global cols, rows, pacMan, coins, ghosts, img, game_over, game_over_time
    coins = []
    cols, rows = len(map_data[0]), len(map_data)
    pacMan = PacMan(int(cols / 2 - 1), int(rows - 9))

    for i in range(cols):
        for j in range(rows):
            if map_data[j][i] == 0:  # place coins only in empty spaces
                coins.append(Coin(i, j))

    ghosts = []
    for i in range(4):
        x = (frameCount + i) % cols
        y = (frameCount + i * 2) % rows
        ghosts.append(Ghost(x, y))

    game_over = False
    game_over_time = 0


def draw():
    global score, game_over, game_over_time
    if game_over:
        if frameCount - game_over_time > game_over_duration:
            initialize_game()
        else:
            background(0)
            fill(255)
            textSize(64)
            textAlign(CENTER, CENTER)
            text("Game Over", width / 2, height / 2)
        return
  
    background(0)
    # Draw walls
    for row in range(rows):
        for col in range(cols):
            if map_data[row][col] == 1:
                fill(0, 0, 255)
                rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    
    pacMan.show() 
    pacMan.move()

    for coin in coins:
        coin.show()
        coin.collect(pacMan)

    if frameCount % change_interval == 0:
        for i, ghost in enumerate(ghosts):
            xdirection, ydirection = pseudo_random_choice(i)
            ghost.dir(xdirection, ydirection)

    for ghost in ghosts:
        ghost.show()
        ghost.move()

        if dist(ghost.x + GRID_SIZE / 2, ghost.y + GRID_SIZE / 2, pacMan.x + GRID_SIZE / 2, pacMan.y + GRID_SIZE / 2) < GRID_SIZE:
            game_over = True
            game_over_time = frameCount

    fill(50)
    rect(50, height - 30, 120, 30)

    fill(255)
    textSize(20)
    text("Score: " + str(pacMan.score), 60, height - 10)

def keyPressed():
    global pacMan
    
    if key == 'w' or key == 'W':
        pacMan.dir(0, -1)
        return
    elif key == 's' or key == 'S':
        pacMan.dir(0, 1)
        return
    elif key == 'a' or key == 'A':
        pacMan.dir(-1, 0)
        return
    elif key == 'd' or key == 'D':
        pacMan.dir(1, 0)
