import pygame, Blocks, getpass

user = getpass.getuser()

def texturedpolygon(surf,poslist,img,imgpos):
    surf.blit(img,imgpos)
    ply = pygame.draw.polygon(surf, [255,255,255,255], poslist)
