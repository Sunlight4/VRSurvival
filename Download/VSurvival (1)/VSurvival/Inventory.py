import ItemClass, getpass,pygame

user = getpass.getuser()

class Inventory:
    def __init__(self,surf,rhand,lhand,rpocket,lpocket,using):
        self.rhand = rhand
        self.lhand = lhand
        self.rpocket = rpocket
        self.lpocket = lpocket
        self.surf = surf
        self.using = using
    def update(self, nrh, nlh):
        self.nrh = nrh
        self.nlh = nlh

        if not self.rhand or not self.lhand or not self.rpocket or not self.lpocket:
            if self.nrh.fitsinpockets:
                self.rhand = nrh
                return True
            else:
                return False
            
            if self.nlh.fitsinpockets:
                self.nlh = nlh
                return True
            else:
                return False
    def render(self):
        pygame.draw.rect(self.surf,[255,255,255],[100,462,218,18])
        space1 = pygame.image.load(
            "/Users/" + user + "/Desktop/VSurvival/images/invspace.png")
        
        space2 = pygame.image.load(
            "/Users/" + user + "/Desktop/VSurvival/images/invspace2.png")
        
        self.surf.blit(space1,[100,462])
        self.surf.blit(space1,[118,462])
        self.surf.blit(space1,[200,462])
        self.surf.blit(space1,[218,462])
        
        pos = [100,462]
        if self.using == "rhand":
            pos = pos
        elif self.using == "lhand":
            pos [0] += 18
        elif self.using == "rpocket":
            pos [0] += 100
        elif self.using == "lpocket":
            pos [0] += 118
            
        self.surf.blit(space2, pos)

        self.surf.blit(self.rhand().img(),[101,463])
        self.surf.blit(self.lhand().img(),[119,463])
        self.surf.blit(self.rpocket().img(),[201,463])
        self.surf.blit(self.lpocket().img(),[219,463])

    def iteminhand(self):
        return self.using


