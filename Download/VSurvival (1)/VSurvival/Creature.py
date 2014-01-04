class Creature(object): #Child of Block?
    clock = 0
    health = 8
    def __init__(self, pos):
        self.pos = pos
    def update(self, world):
        self.clock += 1
        if self.health <= 0:
            pass
            #creature dies
class Animal(Creature):
    activity = 'awake'
    happiness = 8
    hunger = 8
    food = 0
    def update(self, world):
        super(Creature, self).update(world)
        day_clock = self.clock % 60
        if self.activity == 'awake':
            hunger -= 1
            if day_clock % 2:
                happiness -= 1
        elif self.activity == 'sleeping' and (day_clock % 3):hunger -= 1
        elif self.activity == 'eating' and hunger < 8 and food > 1:
            hunger += 1
            food -= 1
            if day_clock % 3 and happiness < 8:happiness += 1
        if day_clock > 48:
            self.activity='sleeping'
        elif self.activity == 'sleeping':
            self.activity = 'awake'
