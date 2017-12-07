from pirates import *
from attack import *

def create_campers1(game):
    mx = game.get_enemy_mothership().get_location().row
    my = game.get_enemy_mothership().get_location().col
    cx = game.get_enemy_capsule().initial_location.row
    cy = game.get_enemy_capsule().initial_location.col
    location = Location(mx + int((cx-mx)/3), my + int((cy-my)/3))
    camper1 = game.get_all_my_pirates()[0]
    camper2 = game.get_all_my_pirates()[1]
    if not camper1.has_capsule():
        if not try_push(camper1, game):
            camper1.sail(location)
    if not camper2.has_capsule():
        if not try_push(camper2, game):
            camper2.sail(location)
            
def create_campers2(game):
    mx = game.get_enemy_mothership().get_location().row
    my = game.get_enemy_mothership().get_location().col
    cx = game.get_enemy_capsule().initial_location.row
    cy = game.get_enemy_capsule().initial_location.col
    location = Location(mx + int((cx-mx)/4), my + int((cy-my)/4))
    camper3 = game.get_all_my_pirates()[2]
    camper4 = game.get_all_my_pirates()[3]
    if not camper3.has_capsule():
        if not try_push_campers(camper3, game):
            camper3.sail(location)
    if not camper4.has_capsule():
        if not try_push_campers(camper4, game):
            camper4.sail(location)