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

class Ghost:
    def __init__(self, x, y, color, behavior, start_delay):
        self.x = x * GRID_SIZE
        self.y = y * GRID_SIZE
        self.start_x = self.x
        self.start_y = self.y
        self.speed = 3
        self.color = color
        self.behavior = behavior
        self.start_delay = start_delay  # Opóźnienie startu w klatkach
        self.active = False
        self.xdirection = 0
        self.ydirection = 0

    def show(self):
        fill(self.color)
        ellipse(self.x + GRID_SIZE / 2, self.y + GRID_SIZE / 2, GRID_SIZE, GRID_SIZE)

    def move(self, pacman, blinky=None):
        if frameCount > self.start_delay:
            self.active = True  # Duch staje się aktywny po upływie start_delay
        if not self.active:
            return

        # Wybieranie nowego kierunku na skrzyżowaniach
        if self.x % GRID_SIZE == 0 and self.y % GRID_SIZE == 0:
            self.choose_direction(pacman, blinky)
        self.x += self.xdirection * self.speed
        self.y += self.ydirection * self.speed
        self.wrap_around()
        
        # Sprawdzenie kolizji i zmiana kierunku jeśli jest kolizja
        if self.collision():
            self.choose_direction(pacman, blinky)

    def choose_direction(self, pacman, blinky):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        target_x, target_y = self.get_target(pacman, blinky)
        best_direction = None
        min_distance = float('inf')


        for d in directions:
            next_x = self.x + d[0] * GRID_SIZE
            next_y = self.y + d[1] * GRID_SIZE
            if not self.collision(next_x, next_y):
                distance = dist(next_x, next_y, target_x, target_y)
                if distance < min_distance:
                    min_distance = distance
                    best_direction = d

        if best_direction:
            self.xdirection, self.ydirection = best_direction

    def get_target(self, pacman, blinky):
        if self.behavior == "blinky":
            return pacman.x, pacman.y  # Blinky ściga bezpośrednio Pac-Mana
        elif self.behavior == "pinky":
            # Pinky celuje 4 kratki przed Pac-Manem
            return pacman.x + pacman.xdirection * GRID_SIZE * 4, pacman.y + pacman.ydirection * GRID_SIZE * 4
        elif self.behavior == "inky" and blinky:
            # Inky celuje w pozycję względem Blinky'ego
            target_x = pacman.x + pacman.xdirection * GRID_SIZE * 2
            target_y = pacman.y + pacman.ydirection * GRID_SIZE * 2
            return 2 * target_x - blinky.x, 2 * target_y - blinky.y
        elif self.behavior == "clyde":
            # Clyde ściga Pac-Mana, ale jeśli jest blisko, wraca do pozycji startowej
            if dist(self.x, self.y, pacman.x, pacman.y) > GRID_SIZE * 8:
                return pacman.x, pacman.y
            return self.start_x, self.start_y
        return self.x, self.y

    def collision(self, x=None, y=None):
        next_x = x if x is not None else self.x + self.xdirection * GRID_SIZE
        next_y = y if y is not None else self.y + self.ydirection * GRID_SIZE
        col = next_x // GRID_SIZE
        row = next_y // GRID_SIZE
        # Sprawdzenie kolizji z murem
        if col < 0 or col >= cols or row < 0 or row >= rows or map_data[row][col] == 1:
            return True
        return False

    def wrap_around(self):
        self.x = (self.x + width) % width
        self.y = (self.y + height) % height

def initialize_game():
    global cols, rows, pacMan, coins, ghosts, game_over, game_over_time
    pacMan = PacMan(int(cols / 2 - 1), int(rows - 9))
    coins = [Coin(i, j) for i in range(cols) for j in range(rows) if map_data[j][i] == 0]
    ghost_start_x = int(cols / 2)
    ghost_start_y = int(rows / 2-10) #Wiem że nie zaczynają tak jak w grze ale blokują się na spawnie :/
    ghosts = [
        Ghost(ghost_start_x, ghost_start_y, color(255, 0, 0), "blinky", 0),  # Blinky startuje od razu
        Ghost(ghost_start_x, ghost_start_y, color(255, 184, 255), "pinky", 60),  # Pinky startuje po 1 sekundzie
        Ghost(ghost_start_x, ghost_start_y, color(0, 255, 255), "inky", 120),  # Inky startuje po 2 sekundach
        Ghost(ghost_start_x, ghost_start_y, color(255, 184, 82), "clyde", 180)  # Clyde startuje po 3 sekundach
    ]
    game_over = False
    game_over_time = 0

def draw():
    global game_over, game_over_time
    if game_over:
        if frameCount - game_over_time > 180:
            initialize_game()
        else:
            background(0)
            fill(255)
            textSize(64)
            textAlign(CENTER, CENTER)
            text("Game Over", width / 2, height / 2)
        return

    background(0)
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

    blinky = next((ghost for ghost in ghosts if ghost.behavior == "blinky"), None)
    for ghost in ghosts:
        ghost.show()
        ghost.move(pacMan, blinky)
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
