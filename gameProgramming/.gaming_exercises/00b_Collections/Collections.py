#Collections.py, casey Boyce v0.4
#add Items
#player_inventory = []
#while len(player_inventory) < 10:
#    item = input("What items do you want to add to your inventory")
#    player_inventory.append(item)

#while len(player_inventory) > 5:
#    item = input("Oh No, you have to many items you need to drop something")
#    player_inventory.remove(item)

#player_inventory.sort
#print(player_inventory)

#dor_kees = [
#    "green",
#    "purple",
#    "red",
#    "brown",
#    "gray",
#]

#kee = input("You can use a key on the door. But, whitch one.\n")

#if kee in dor_kees:
#    print("Ah cool you geussed the right key.")
#else:
#    print("Darn it, Nope geuss that was the wrong key.")

weapon_list = [
    True, #Sword
    False, # Pile o' Rocks
    True, # Bow
    False, # The launching Stick 
    False, # suicidal knife
]

weapon_numb = 0
while weapon_numb < len(weapon_list):
    if weapon_numb == 0 and weapon_numb[0] == True:
        print("You have a wonderful weapon with the name of A Sword. Its a sword. you swing it at people and they should die.\n")
    elif weapon_numb == 1 and weapon_numb[1] == True:
        print("You have a wonderful weapon with the name of A Pile o' Rocks. You have a special power of stoneing people to death.\n")
    elif weapon_numb == 2 and weapon_numb[2] == True:
        print("You have a wonderful weapon with the name of A Bow. This bow fires arrows. If you have any.\n")
    elif weapon_numb == 3 and weapon_numb[3] == True:
        print("You have a wonderful weapon with the name of The Launching Stick. A Stick That Launches.\n")
    elif weapon_numb == 4 and weapon_numb[4] == True:
        print("You have a wonderful weapon with the name of A Suicidal Knife. A talking knife that wants to break itself.\n")
    else:
        break