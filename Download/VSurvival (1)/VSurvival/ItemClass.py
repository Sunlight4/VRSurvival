import pygame

class Item:
    def __init__(self,name,texture,itemid,size=1):
        self.name = name
        self.texture = texture
        self.size = size
        self.itemid = itemid
        
    def fitspocket(self):
        if self.size > 1:
            return 0
        else:
            return 1
    def img(self):
        img = pygame.image.load(self.texture)
        return img
