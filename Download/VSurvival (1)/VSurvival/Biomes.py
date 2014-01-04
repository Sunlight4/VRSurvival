from Generator import *
from Biome import *
import Structures as s


def forest():
    forest = Biome([s.tree])
    return forest.create()

def plains():
    plains = Biome([None,None,None,None,s.tree])
    return plains.create()

def mountains():
    mt = Biome([None,None,s.mountain])
    return mt.create()

def devworld():
    w = Biome([None,None,s.tree,None,s.mountain])
    return w.create()
