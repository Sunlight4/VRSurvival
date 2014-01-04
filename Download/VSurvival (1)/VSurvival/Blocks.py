from BlockClass import Block
import getpass, getfile


user= getpass.getuser()

folder = getfile.getfile("images/")

def grass():
    grass = Block("Grass",folder+"grass.png",3,2)
    return grass

def stone():
    stone = Block("Stone",folder+"stone.png",1,5)
    return stone

def log():
    log = Block("Log",folder+"log.png",4,4)
    return log

def dirt():
    dirt=Block("Dirt",folder+"dirt.png",2,2)
    return dirt

def leaves():
    leaves=Block("Leaves", folder+"leaves.png",5,1)
    return leaves

def ironore():
    ironore=Block("Iron Ore", folder+"ironore.png",8,5)
    return ironore

def bedrock():
    bedrock=Block("Bedrock", folder+"bedrock.png",16,5)
    return bedrock

def goldore():
    goldore=Block("Gold Ore", folder+"goldore.png",13,5)
    return goldore
def diamondore():
    diamondore=Block("Diamond Ore", folder+"diamondore.png",9,5)
    return diamondore
def emeraldore():
    emeraldore=Block("Emerald Ore", folder+"emeraldore.png",10,5)
    return emeraldore
def coalore():
    coalore=Block("Coal Ore", folder+"coalore.png",7,4)
    return coalore
def chest():
    chest=Block("Chest",folder+"chest.png",7,4)
    return chest

def rubyore():
    rubyore = Block("Ruby",folder+"rubyore.png",11,5)
    return rubyore
