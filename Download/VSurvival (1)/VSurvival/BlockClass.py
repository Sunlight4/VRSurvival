import pygame

class Block:
    def __init__(self,name,texture,blockid,hardness):
        self.name = name
        self.texture = texture
        self.blockid = blockid
        self.hardness = hardness
    def render(self,surf,pos,transform=False):
        self.surf = surf
        self.pos = pos
        img = pygame.image.load(self.texture)
        if transform:img=pygame.transform.scale2x(img)
        surf.blit(img, self.pos)
    def info(self):
        return [self.name,self.texture,self.blockid,self.hardness]
    
        
