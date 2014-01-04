import creature, block
class TileEntity(creature.Creature, block.Block):
    pass
class Liquid(TileEntity):
    def update(self, world):
        super(Liquid, self).update(world)

