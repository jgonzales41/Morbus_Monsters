from random import choice
from random import randrange

#Initializes the standard stats for all monsters
class Monsters(object):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.level = 1
        self.exp = 0
        self.power = 1
        self.acc = 80
        self.defense = .1

class Fire_Type(object):
    def __init__(self):
        super().__init__()
        self.p_type = 'Fire'
        self.weak = 'Water'

class Water_Type(object):
    def __init__(self):
        super().__init__()
        self.p_type = 'Water'
        self.weak = 'Electric'

class Ground_Type(object):
    def __init__(self):
        super().__init__()
        self.p_type = 'Ground'
        self.weak = 'Water'

class Electric_Type(object):
    def __init__(self):
        super().__init__()
        self.p_type = 'Electric'
        self.weak = 'Ground'
        
class Ignis(Monsters,Fire_Type):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.defense = .2
        self.name = 'Ignis-morbus'
        self.move1 = ('Harpoon','Normal')
        self.move2 = ('Fever','Fire')
        self.move3 = ('Self-Repair','Heal')

class Aqua(Monsters, Water_Type):
    def __init__(self):
        super().__init__()
        self.power = 1.3
        self.name = 'Aqua-morbus'
        self.move1 = ('Collide','Normal')
        self.move2 = ('Ooze','Water')
        self.move3 = ('Self-Repair','Heal')

class Fulgur(Monsters, Electric_Type):
    def __init__(self):
        super().__init__()
        self.power = 1.2
        self.name = 'Fulgur-morbus'
        self.move1 = ('Slash','Normal')
        self.move2 = ('Shock','Electric')
        self.move3 = ('Self-Repair','Heal')

class Terra(Monsters,Ground_Type):
    def __init__(self):
        super().__init__()
        self.health = 150
        self.power = 1.2
        self.name = 'Terra-morbus'
        self.move1 = ('Smash','Normal')
        self.move2 = ('Particle Throw','Ground')
        self.move3 = ('Self-Repair','Heal')
        
'''
This is the attack power function that checks whether or not
the character's health is below 35. If it is then it increases
the probability that the character will be healed instead of
casting an attack.
'''
def Attack(option,effect,power,defense):
    if option == 1:
        attack_power = randrange(15,22)
        return int((attack_power * effect * power) / (1 - defense))
    elif option == 2:
        attack_power = randrange(10,35)
        return int((attack_power * effect * power) / (1 - defense))
    else:
        attack_power = randrange(-20,-10)
        return attack_power

def CPU_Attack(option,effect,power,defense):
    if option == 1:
        attack_power = randrange(15,22)
        return int((attack_power * effect * power) / (1 - defense))
    elif option == 2:
        attack_power = randrange(10,35)
        return int((attack_power * effect * power) / (1 - defense))
    else:
        attack_power = randrange(-20,-10)
        return attack_power
   
        
available_monsters = {'Ignis': Ignis(),
                      'Terra': Terra(),
                      'Fulgur': Fulgur(),
                      'Aqua': Aqua()}
