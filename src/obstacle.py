import pygame

class Obstacle:
    def __init__(self, __):
        """
        Initializes the obstacle object
        args:
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)

    
    def draw(self):
        """
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def change_color(self):
        """
        Changes colors when you get hurt
        """
    
