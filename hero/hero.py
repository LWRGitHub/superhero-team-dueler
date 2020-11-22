import random
from Armor import Armor
from Weapon import Weapon
from Ability import Ability

# class Ability:
#     def __init__(self, name, max_damage):
#         '''
#        Initialize the values passed into this
#        method as instance variables.
#         '''

#         # Assign the "name" and "max_damage"
#         # for a specific instance of the Ability class
#         self.name = name
#         self.max_damage = max_damage

#     def attack(self):
#         ''' Return a value between 0 and the value set by self.max_damage.'''

#         # Pick a random value between 0 and self.max_damage
#         random_value = random.randint(0,self.max_damage)
#         return random_value

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.armor_class = Armor(self.name, 100)

        self.deaths = 0
        self.kills = 0

    # def fight(self, opponent):
    #     ''' Current Hero will take turns fighting the opponent hero passed in.
    #     '''
    #     mylist = [self.name, opponent.name]

    #     return random.choice(mylist)  

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    

    def defend(self, damage_amt):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        # TODO: This method should run the block method on each armor in self.armors
        # armors = self.armors
        # if armors.count() != 0:
        # print(self.current_health)
        # for key in self.armors:
        #     print("--------------")
        #     print(self.armor_class.block())
        #     print("--------------")
        #     damage_amt -= self.armor_class.block()
        
        # print(self.current_health)
        # return self.current_health - damage_amt
        
        for key in self.armors:
            damage_amt -= self.armor_class.block()
        return damage_amt
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        
        self.current_health -= self.defend(damage)

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        #  Check the current_health of the hero.
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if len(opponent.abilities) == 0 or len(self.abilities) == 0:
            print("Draw")
        # 1) else, start the fighting loop until a hero has won
        else:
            while(self.current_health > 0 or opponent.current_health > 0):
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())  
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
            if len(self.abilities) > 0:
                print(f"{opponent.name} won!")
            else:
                print(f"{self.name} won!")

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # adds the number of deaths to self.deaths
        self.deaths += num_deaths
        

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())