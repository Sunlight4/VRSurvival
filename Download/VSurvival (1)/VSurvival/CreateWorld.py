import Biome, Biomes, random

def create():
    world = []
    
    for i in range(1,65):
        biome = random.choice([Biomes.forest(),Biomes.plains(),Biomes.mountains()])
        for block in biome:
            world.append(block)
    return world
