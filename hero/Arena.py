from Ability import Ability
from Weapon import Weapon
from Armor import Armor
from hero import Hero

class Arena:
    def __init__(self, team_one, team_two):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = team_one
        self.team_two = team_two

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        name = input("What is the wepon name?  ")
        max_damage = input(
            "What is the max damage of the wepon?  ")

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        name = input("What is the armor name?  ")
        max_damage = input(
            "What is the max protection of the armor?  ")

        return Weapon(name, max_damage)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               #add an ability to the hero
               #creates the ability, then add it to the hero
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               # add a weapon to the hero
               #creates the weapon, then add it to the hero
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               #add an armor to the hero
               #creates the armor, then add it to the hero
               armor = self.create_armor()
               hero.add_armor(armor)
        return hero

   
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # This method should allow a user to create team two.
        # This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        # Add th
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # battle the teams together.
        # Calls the attack method that exists in team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills1 = 0
        team_deaths1 = 0
        for hero in self.team_one.heroes:
            team_kills1 += hero.kills
            team_deaths1 += hero.deaths
        if team_deaths1 == 0:
            team_deaths1 = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills1/team_deaths1))

        # TODO: Now display the average K/D for Team Two
        team_kills2 = 0
        team_deaths2 = 0
        for hero in self.team_two.heroes:
            team_kills2 += hero.kills
            team_deaths2 += hero.deaths
        if team_deaths2 == 0:
            team_deaths2 = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills2/team_deaths2))

        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        #TODO: Now list the heroes from Team Two that survived
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)