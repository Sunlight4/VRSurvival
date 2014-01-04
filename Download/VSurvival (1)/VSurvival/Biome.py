import random, Generator
  
class Biome:
    def __init__(self,structures):
        self.structures = structures
    def create(self):

            
        biome = []
        xsize = 150 * 16
        ysize = 304
        
        
        for x in range(0,xsize,16):
            biome.append([3,[x,304]])

            for y in range(320,800,16):
                biome.append([2,[x,y]])
                
            for y in range(480,1600,16):
                if random.choice([1,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,0,0]):
                    ore = random.choice([7,7,7,8,8,9,10,11,
                                         13])
                    biome.append([ore,[x,y]])
                else:
                    biome.append([1,[x,y]])


                if random.choice([1,0,0,0,0,0,0,0]):
                    try:
                        structure = random.choice(self.structures)
                        biome.append(structure.generate([x,151]))
                    except:
                        pass
            y = 1920

            biome.append([16,[x,y]])
            #biome.append([-2,[x,y+16]])
            
            
        return biome
                            
        
