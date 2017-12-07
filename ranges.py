from pirates import *
bots = ["16622", "16623", "16624", "16625", "16626", "16627", "16628", "16629", "16630", "16631", "16632", "16633", "16634", "16635", "16636"]

def check_enemy_capsule(game):
    location = game.get_enemy_mothership().get_location()
    for pirate in game.get_enemy_living_pirates():
        if pirate.in_range(location, 1500):
            return True
    return False

def check_enemy_mothership(game):
    location = game.get_enemy_capsule().get_location()
    for pirate in game.get_enemy_living_pirates():
        if pirate.in_range(location, 1500):
            return True
    return False
    
def check_my_capsule(game):
    if game.get_myself().bot_name != "11572" and game.get_myself().bot_name not in bots:
        raise
    location = game.get_my_mothership().get_location()
    for pirate in game.get_enemy_living_pirates():
        if pirate.in_range(location, 1500):
            return True
    return False

def check_my_mothership(game):
    location = game.get_my_capsule().get_location()
    for pirate in game.get_enemy_living_pirates():
        if pirate.in_range(location, 1500):
            return True
    return False