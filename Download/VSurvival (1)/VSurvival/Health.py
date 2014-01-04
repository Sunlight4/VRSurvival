import pygame

class Health:
    def __init__(self,hearts,texture):
        self.hearts = hearts
        self.texture = texture
        self.img = pygame.image.load(self.texture)
    def hurt(self):
        self.hearts -= 1
    def heal(self):
        self.hearts += 1
        
        
