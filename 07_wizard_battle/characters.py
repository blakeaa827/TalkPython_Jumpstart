import random


class Character:
    def __init__(self, name, level, die=16):
        self.die = die
        self.name = name
        self.level = level

    def __repr__(self):
        return f'Creature named {self.name} of level {self.level}.'

    def attack_roll(self):
        return random.randint(1, self.die) * self.level


class SmallAnimal(Character):
    def attack_roll(self):
        return super().attack_roll() // 2


class Predator(Character):
    pass


class Dragon(Character):
    def __init__(self, name, level, scale_thickness=1, fire_breath=False):
        super().__init__(name, level)
        self.fire_breath = fire_breath
        self.scale_thickness = scale_thickness

    def attack_roll(self):
        if self.fire_breath:
            print('This dragon breaths fire. Take cover!')
            if random.randint(0, 1):
                print('The dragon scorches you before you can move. You never stood a chance.')
                return 99999999
            else:
                print('You got lucky. The dragon appears to have choked on his spit.')
        else:
            pass

        return random.randint(1, self.die) * self.level * self.scale_thickness


class Wizard(Character):
    pass
