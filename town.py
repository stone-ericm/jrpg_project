# class Region:
#     #enemy level range
#     #climate
#     #topography
#     #enterence, exit - multi-directional linked list?
#     pass
# class Town:
#     #region (towns have a region)
#     #buildings
#         #shop
#         #inn
#         #story-relevent locations
#     #npcs
#     pass
# class Building:
#     #npcs
#     #description
#     #things to interact with
#     #items?
#     pass

import views

def town(player):
    while True:
        choice = input("You arrive in a small down. To your left you see a [T]abernacle where you can rest and heal your wounds. In front of you is Town [H]all. To your right you notice a distressed looking [o]ld man.")
        if choice.lower() == 't':
            print("You enter the local tabernacle. Along the sides you notice shrines devoted to various gods, many you don't recognize. You kneel by a statue of a women and suddely feel yourself filled with vitality! Your wounds have been healed!")
            player.hp = player.max_hp
            player.mp = player.max_mp
            pass
        elif choice.lower() == 'h':
            
            pass
        elif choice.lower() == 'o':
            pass
        else:
            print(views.try_again)
            pass