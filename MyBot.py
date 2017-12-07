"""
This is an example for a bot.
"""
from pirates import *
from defense import *
from attack import *
from assasians import *

def do_turn(game):
    if game.get_myself().bot_name != "11572":
        raise
    """
    Makes the bot run a single turn.

    :param game: The current game state.
    :type game: PirateGame
    """
    # Get one of my pirates.
    
    # Try to push, if you didn't - take the capsule and go to the mothership.
    # for pirate in game.get_my_living_pirates()[4:]:
    #     if not pirate.has_capsule():
    #         if not try_push(pirate, game):
    #             # If the pirate doesn't have a capsule, go and get it!
    #             if pirate.capsule is None:
    #                 if game.get_my_capsule().turns_to_revive <= 3:
    #                     capsule = game.get_my_capsule()
    #                     pirate.sail(capsule)
    #                 else:
    #                     pirate.sail(game.get_my_mothership())
    #             # Else, go to my mothership.
    #             else:
    #                 mothership = game.get_my_mothership()
    #                 # Go towards the mothership.
    #                 pirate.sail(mothership)
    #     else:
    #         pirate.sail(game.get_my_mothership())
    #assassins(game)
    capsule_collector(game)
    #camper_cleaner(game)
    create_campers1(game)     
    create_campers2(game)        
    game.debug(PirateGame.get_enemy(game).bot_name)
    game.debug(PirateGame.get_myself(game).bot_name)



