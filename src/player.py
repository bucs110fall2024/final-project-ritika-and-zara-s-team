import pygame

class Player:
  def __init__(self, pnum=1):
    """
    Initialize the player object
    args: pnum [int] the player's id number
    """
    self.player_num = pnum
    self.lives = 3 # players always start with 3 lives
    self.is_large = False # player always starts small
    self.width = 50
    self.height = 60
    self.x = 100
    self.y = SCREEN_HEIGHT - self.height - 100
    self.vel_x = 0
    self.vel_y = 0
    self.speed = 5
    self.jump = False
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    self.image = pygame.Surface((self.width, self.height))
    self.image.fill(RED)



class Player:
    def __init__(self):
        self.width = 50
        self.height = 60
        self.x = 100
        self.y = SCREEN_HEIGHT - self.height - 100
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)

def move(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        self.vel_x = -self.speed
    elif keys[pygame.K_RIGHT]:
        self.vel_x = self.speed
    else:
        self.vel_x = 0

    if self.jump:
        self.vel_y = -JUMP_STRENGTH
        self.jump = False

    self.vel_y += GRAVITY

    # Move the player
    self.rect.x += self.vel_x
    self.rect.y += self.vel_y

    # Keep player inside the screen boundaries
    if self.rect.x < 0:
        self.rect.x = 0
    if self.rect.x + self.width > SCREEN_WIDTH:
        self.rect.x = SCREEN_WIDTH - self.width
    if self.rect.y + self.height > SCREEN_HEIGHT:
        self.rect.y = SCREEN_HEIGHT - self.height
        self.vel_y = 0

