from pirates import *
from ranges import *

def try_push(pirate, game):
    """
    Makes the pirate try to push an enemy pirate. Returns True if it did.

    :param pirate: The pushing pirate.
    :type pirate: Pirate
    :param game: The current game state.
    :type game: PirateGame
    :return: True if the pirate pushed.
    :rtype: bool
    """
    # Go over all enemies.
    holder1 = PirateGame.get_enemy_capsule(game).holder
    for enemy in game.get_enemy_living_pirates():
        # Check if the pirate can push the enemy.
        if holder1 != None and pirate.can_push(holder1):
                # Push enemy!
                push_location = Location(60000,60000)
                pirate.push(holder1, push_location)
                # Print a message.
                print 'pirate', pirate, 'pushes', holder1, 'towards', holder1.initial_location
                # Did push.
                return True

        elif pirate.can_push(enemy):
            # Push enemy!
            push_location = Location(60000,60000)
            pirate.push(enemy, push_location)
            # Print a message.
            print 'pirate', pirate, 'pushes', enemy, 'towards', enemy.initial_location
            # Did push.
            return True
        elif holder1 != None and pirate.in_range(holder1, 600):
            pirate.sail(holder1)
            return True
            
    # Didn't push.
    return False

def try_push_campers(pirate, game):
    """
    Makes the pirate try to push an enemy pirate. Returns True if it did.

    :param pirate: The pushing pirate.
    :type pirate: Pirate
    :param game: The current game state.
    :type game: PirateGame
    :return: True if the pirate pushed.
    :rtype: bool
    """
    # Go over all enemies.
    holder1 = PirateGame.get_enemy_capsule(game).holder
    for enemy in game.get_enemy_living_pirates():
        # Check if the pirate can push the enemy.
        if holder1 != None and pirate.can_push(holder1):
            # Push enemy!
            push_location = Location(257,553)
            pirate.push(holder1, push_location)
            # Print a message.
            print 'pirate', pirate, 'pushes', holder1, 'towards', holder1.initial_location
            # Did push.
            return True
            
        elif holder1 != None and pirate.in_range(holder1, 600):
            pirate.sail(holder1)
            return True

    # Didn't push.
    return False
	
def try_friendly_push(pirate, game):
    for friend in game.get_my_living_pirates():
        # Check if the pirate can push the enemy.
        if pirate.can_push(friend):
                # Push enemy!
                if friend.has_capsule():
                    pirate.push(friend, game.get_my_mothership())
                else:
                    pirate.push(friend, game.get_my_capsule().initial_location)
                # Print a message.                # Did push.
                return True
    # Didn't push.
    return False

# def camper_cleaner(game):
#     cleaner1 = game.get_all_my_pirates()[4]
#     cleaner2 = game.get_all_my_pirates()[5]
#     default_location = game.get_my_mothership().get_location()
#     if check_my_capsule(game) and check_my_mothership(game):
#         cleaner1_location = Location(game.get_my_mothership().get_location().row - 50, game.get_my_mothership().get_location().col)
#         cleaner2_location = Location(game.get_my_capsule().initial_location.row + 50, game.get_my_capsule().initial_location.col)
#     elif check_my_capsule(game) and not check_my_mothership(game):
#         cleaner1_location = Location(game.get_my_capsule().initial_location.row - 50, game.get_my_capsule().initial_location.col)
#         cleaner2_location = Location(game.get_my_capsule().initial_location.row + 50, game.get_my_capsule().initial_location.col)
#     elif check_my_mothership(game) and not check_my_capsule(game):
#         cleaner1_location = Location(game.get_my_mothership().get_location().row - 50, game.get_my_mothership().get_location().col)
#         cleaner2_location = Location(game.get_my_mothership().get_location().row + 50, game.get_my_mothership().get_location().col)
#     else:
#         cleaner1_location = default_location
#         cleaner2_location = default_location
#     if not try_push(cleaner1, game):
#         if cleaner1.capsule is None:
#             cleaner1.sail(cleaner1_location)
#         else:
#             cleaner1.sail(game.get_my_mothership())
#     if not try_push(cleaner2, game):
#         if cleaner2.capsule is None:
#             cleaner2.sail(cleaner2_location)
#         else:
#             cleaner2.sail(game.get_my_mothership())
#     if game.get_myself().bot_name != "11572":
#         raise

def capsule_collector(game):
    collector1 = game.get_all_my_pirates()[6]
    collector2 = game.get_all_my_pirates()[7]
    collector3 = game.get_all_my_pirates()[4]
    collector4 = game.get_all_my_pirates()[5]
    wait_for_capsule = Location(game.get_my_capsule().initial_location.row, game.get_my_capsule().initial_location.col - 50)
    start_capsule = game.get_my_capsule().initial_location
    capsule = game.get_my_capsule()
    if not try_push(collector1, game):
        if not try_friendly_push(collector1, game):
            if capsule.is_alive:
                if collector1.capsule is None:
                    collector1.sail(capsule)
                elif game.turn > 200 and game.get_myself().score <= 3:
                    manhatten(game, collector1)
                else:
                    collector1.sail(game.get_my_mothership())
            else:
                collector1.sail(wait_for_capsule)
    if not try_push(collector2, game):
        if not try_friendly_push(collector2, game):
            if capsule.is_alive:
                if collector2.capsule is None:
                    capsule = game.get_my_capsule()
                    collector2.sail(capsule)
                elif game.turn > 200 and game.get_myself().score <= 3:
                    manhatten(game, collector2)
                else:
                    collector2.sail(game.get_my_mothership())
            else:
                collector2.sail(wait_for_capsule)
    if not try_push(collector3, game):
        if not try_friendly_push(collector3, game):
            if capsule.is_alive:
                if collector3.capsule is None:
                    collector3.sail(capsule)
                elif game.turn > 200 and game.get_myself().score <= 3:
                    manhatten(game, collector3)
                else:
                    collector3.sail(game.get_my_mothership())
            else:
                collector3.sail(wait_for_capsule)
    if not try_push(collector4, game):
        if not try_friendly_push(collector4, game):
            if capsule.is_alive:
                if collector4.capsule is None:
                    collector4.sail(capsule)
                elif game.turn > 200 and game.get_myself().score <= 3:
                    manhatten(game, collector4)
                else:
                    collector4.sail(game.get_my_mothership())
            else:
                collector4.sail(wait_for_capsule)

def manhatten(game, pirate):
    x = game.get_my_mothership().get_location().row
    y = game.get_my_mothership().get_location().col
    if (pirate.get_location().row != x):
        pirate.sail(Location(x, pirate.get_location().col))
    elif (pirate.get_location().col != y):
        pirate.sail(Location(x, y))