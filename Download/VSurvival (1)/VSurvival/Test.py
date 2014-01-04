import CreateWorld,Biome

world = CreateWorld.create()

for i in range(1,65):
    fl = open(
        "/Users/ianhuang/Desktop/VSurvival/world/world" + str(i) + ".txt","w+")
    fl.write(str(world[i]))
    fl.close()


##b = Biome.Biome([None])
##print b.create()
##fl = open("/Users/ianhuang/Desktop/VSurvival/world/world.txt","w+")
##fl.write(str(b.create()))
##fl.close()
