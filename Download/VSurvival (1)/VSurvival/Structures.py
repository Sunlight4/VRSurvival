from Generator import Generator


def tree3d(pos):
    tree = Generator([[4,[0,0,0]],[4,[0,1,0]],[4,[0,2,0]],
                      [4,[0,3,0]],[4,[0,4,0]],[4,[0,5,0]],
                      [5,[1,4,0]],[5,[0,4,1]],[5,[-1,4,0]],
                      [5,[0,4,-1]],[5,[1,4,1]],[5,[1,4,-1]],
                      [5,[-1,4,-1]],[5,[-1,4,1]],[5,[0,6,0]]])
    code = tree.generate(pos)

    return code

def mountain(pos):
    blocks = []

    for x in range(1,50):    
        for y in range(-x,x+1):
                blocks.append([1,[x*16,y*16]])
            
    m = Generator(blocks,pos)
    return m.generate()

def tree(pos):
    tree = Generator([[4,[0,0]],[4,[0,1*16]],[4,[0,2*16]],
                      [4,[0,3*16]],[4,[0,4*16]],[5,[0,5*16]],
                      [5,[-16,5*16]],[5,[0,6*16]],[5,[16,5*16]]])
    code = tree.generate(pos)

    return code
