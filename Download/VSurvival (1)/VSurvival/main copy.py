import pygame,Tkinter,random,time,socket,urllib2,os,getpass
import Generator, Save, Structures,ItemClass,CreatureClass
import Biome, Biomes, BlockClass, Blocks, Inventory, Items,CreateWorld
import mod,mods

pygame.init()

mod.search_and_run() # Run the extra Python files
user = getpass.getuser()

screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("VSurvival","VSurvival")
itempairs = []

draw = screen.blit
update = pygame.display.flip
load = pygame.image.load
fill = screen.fill
convert_list=[None, Blocks.stone, Blocks.dirt, Blocks.grass, Blocks.log,
              Blocks.leaves, None, Blocks.coalore, Blocks.ironore, Blocks.diamondore,
              Blocks.emeraldore,Blocks.rubyore,None, Blocks.goldore, None,
              None,Blocks.bedrock]
def text(text,pos,color,size):
    font = pygame.font.Font(None,size)
    txt = font.render(text,0,color)
    screen.blit(txt,pos)
    update()
def convert(blockid):
    block = convert_list[blockid]

    return block()

credit = ["VSurvival",  # Credits
          "Programmed by: Ian Huang and Ethan Saff",
          "Textures: Ian Huang",
          "Extra ideas: Ian Luchars",
          "Also for friends who wanted to make their own Minecraft :)",
          "And for friends who have trouble with modding :)"
          ]
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]   # Colors
green = [0,255,0]
blue = [0,0,255]
player = pygame.image.load("/Users/" + user + "/Desktop/VSurvival/images/player.png")
damage = 0
c = False
breaking = False
nm = True

def start():
    fill(red)
    text("VSurvival",[50,50],blue,60)
    text("Start",[50,200],green,40)    # Title screen text
    text("Credits",[50,250],white,40)
start()
update()
world = []
run = True
quitgame = False

while run:
    mpos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame = True
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mpos[0] > 44:
                if mpos[1] > 194:
                    if mpos[0] < 125:
                        if mpos[1] < 224:
                            quitgame = False
                            run = False

            if mpos[0] > 50:
                if mpos[1] > 250:
                    if mpos[0] < 153:
                        if mpos[1] < 275:
                            fill(red)
                            for line in credit:
                                text(line,[50,50],blue,30)
                                update()
                                time.sleep(1)
                                fill(green)
                                update()
                            fill(white)
                            update()

                            start()

                            update()

                            
update()

if quitgame:
    pygame.quit()
else:
    world = []
    world2 = CreateWorld.create()
    fill(white)
    update()
    run = True
    if os.path.exists("/Users/" + user + "/Desktop/VSurvival/world/world1.txt"):
        fill(red)
        text("Loading world...",[50,50],blue,50)
        for i in os.listdir("/Users/" + user + "/Desktop/VSurvival/world"):
            wf = open("/Users/" + user + "/Desktop/VSurvival/world/" + i,"r")
            lines = wf.readlines()
            for line in lines:
                line = line.replace("\n","")
                info = line.split(",")
                if len(info):
                    try:
                        block = [int(info[0]),[info[1],info[2]]]
                        world.append(block)
                    except:
                        pass
            wf.close()
    else:
        text("Creating world...",[50,50],black,50)
        for i in range(1,65):
            fl = open(
                "/Users/" + user +"/Desktop/VSurvival/world/world" + str(i) + ".txt","w+")
            fl.write(str(world2[i]))
            fl.close()
            world = world2
    
    
    
    fill(white)
    for block in world:
        blockclass = convert(block[0])
        j=[int(x) for x in block[1]]
        blockclass.render(screen, j)
    update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        inv = Inventory.Inventory(screen,Items.air,Items.air,Items.air,Items.air,Items.air)
        inv.render()
        update()
        
        
##        for block in world:
##            blockclass = convert(block[0])
##            j=[int(x) for x in block[1]]
##            blockclass.render(screen, j)
        if pygame.mouse.get_pressed() == (1,0,0):
            try:
                oldsecs = 0
                x = pygame.mouse.get_pos()[0]


                diff = x % 16
                x -= diff 


                
                y = pygame.mouse.get_pos()[1]

                diff = y % 16
                y -= diff

                hardness=0
                blid = 0

                
                for bl in world:
                    if bl[1] == [str(x),str(y)]:
                        blid=bl[0]
                        blclass = convert(int(blid))
                        hardness = blclass.info()[3]
                        
                        
                secs = time.localtime(time.time())[5]
                if not breaking:
                    oldsecs = secs

                if secs == 0 and oldsecs == 59:
                    nm = 59
                
                if secs != oldsecs:
                    secs += nm + 1

                

                oldsecs = secs

                print "secs = " + secs
                print "oldsecs = " + oldsecs
                print "nm = " + nm
                    
                
                if not breaking:
                    breaktime = secs + hardness*5
                
                
                
 
          

                if secs == breaktime:
                    air = pygame.image.load("/Users/" + user + "/Desktop/VSurvival/images/air.png")
                    screen.blit(air,[x,y])
                    update()
                    world.remove([blid,[x,y]])
                breaking = True
            except:
                pass
        
        

                    

        if pygame.mouse.get_pressed()[0] == 0:
            secs = 0
            breaking = False
            nm = False
        
                
                                
               
        
        update()

    

        

    pygame.quit()
