import pygame
import random

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lazer Battle")

class Background:
    def __init__(self, color):
        """
        Initializes the background 
        """
        self.color = color
    
    def draw(self):
        """
        Adds more clouds to make it look like screen is moving 
        """
        screen.fill(self.color)
    
    def add_ground(self):
        """
        Adds more ground to make it look like screen is moving 
        """