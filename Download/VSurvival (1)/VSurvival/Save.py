import pygame, getpass

username = getpass.getuser()

def writetofile(code):
    fl = open("/Users/" + username + "/Desktop/VSurvival/world/world1.txt","w+")
    fl.write(code)
    fl.close()
