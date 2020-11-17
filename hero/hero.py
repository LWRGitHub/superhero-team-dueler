import random
from Armor import Armor

class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        # Pick a random value between 0 and self.max_damage
        random_value = random.randint(0,self.max_damage)
        return random_value

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        mylist = [self.name, opponent.name]

        return random.choice(mylist)  

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())