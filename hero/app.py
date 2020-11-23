from Ability import Ability
from Weapon import Weapon
from Armor import Armor
from Team import Team
from hero import Hero
from Arena import Arena

if __name__ == "__main__":
    game_is_running = True

    team_one = Team("team_one")
    team_two = Team("team_two")

    # Instantiate Game Arena
    arena = Arena(team_one, team_two)

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()