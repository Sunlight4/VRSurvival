import pygame 

class Generator:
    def __init__(self,blocks):
        self.blocks = blocks
    def generate(self, pos):
        self.pos = pos
        for block in self.blocks:
           
            block[1][0] += self.pos[0]
            
            block[1][1] += self.pos[1]
               
              
        return self.blocks


