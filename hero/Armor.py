import random

class Armor:
    def __init__(self, name, max_block):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        # Pick a random value between 0 and self.max_damage
        random_value = random.randint(0,self.max_block)
        return random_value