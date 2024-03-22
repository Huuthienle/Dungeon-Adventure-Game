##############################################################################
#Title: Dungeon Adventure Map
#Class: CS 30        
#Date: March 12, 2024            
#Coders Name: HuuThienLe               
#Version: 001                                      
##############################################################################
'''
 The programme creates a map for a simple game. 
 Use a Multiple Dimensional Lists (list of lists).
'''
#-----------------------------------------------------------------------------
#-----Functions---------------------------------------------------------------
floor1 = {
    "start_floor1" : {
        "description" : "Floor 1-1:\
     A stone roon with a purple crystal flow in middle",
        "options" : ["(3) Escape a dungeon", 
                     "(2) Touch the crystal to teleport to the next rooms"]
    },
    "room1" : {
        "description" : "Floor 1-2:\
    A room which is simulated to the forest with \
a green crystal flow in front of you. There is a lake in the left\
of a forest with a purple crystal flow in the middle",
        "options" : ["(3) Explore the forest",
                     "(2) Touch purple crystal to teleport to the next room",
                     "(1) Touch green crystal to teleport to unlocked rooms"]
    },
    "fight_room1" : {
        "description" : "Floor 1-3\
    You in a middle of the Greek Arena with\
2 kind of crystal flow in front of you,\
one is green and one is red",
        "options" : ["(3) Touch the red crystal to open the battle",
                     "(1) Touch green crystal to teleport to unlocked rooms"]
    },
    "gate1" : {
        "description" : "Floor 1-4\
    A room with a closed gate and a green crystal",
        "options" : ["(4) Enter gate to the second floor, need the first key",
                     "(1) Touch green crystal to teleport to unlocked rooms"]
    }
}


floor2 = {
    "start_floor2" : {
        "description" : "Floor 2-3:   A room with 3 crystals flow in the air,\
a purple crystal in the right side of the room, \
another purple crystal in the left of the room, \
and a green crystal in the middle of the room.",
        "options" : ["(1) Touch green crystal to teleport to unlocked rooms",
                     "(3) Need to kill a subboss \
                            to active left purple crystal", 
                     "(2) Touch right purple crystal"]
    },
    "gate2" : {
        "description" : "Floor 2-2: A room with closed gate and \
green crystal in the middle, and grey crystal in the left",
        "options" : ["(1) Touch green crystal to teleport to unlocked rooms", 
                     "(3) Fix the grey crystal and enter the room", 
                     "(4) Enter gate to the third floor, need the second key"]
    },
    "secret_room" : {
        "description" : "Floor 2-1: \
A room with a treasure chest in end of the room \
and green crystal in front of you.",
        "options" : ["(1) Touch green crystal to teleport to unlocked rooms", 
                     "(3) Open the treasure chest"]
    },
    "subboss_room" : {
        "description" : "Floor 2-4: \
You in the main room of the Britain castle \
which have a throne in front of. There is a knight in a red armor\
with a long greatsword beside it. There are some sentences appear\
in front of you: 'You can choose to surrender or resist.'",
        "options" : ["(4) Surrender and pass the room.", 
                     "(3) Fight the knight to get it respect."]
    }
}


floor3 = {
    "start_floor3" : {
        "description" : "Floor 3-3: A room with 3 crystals flow in the air,\
a purple crystal in the right side of the room, \
another purple crystal in the left of the room, \
and a green crystal in the middle of the room.",
        "options" : ["(1) Touch green crystal to teleport to unlocked rooms",
                     "(2) Touch left purple crystal", 
                     "(3) Required 3 keys to active right purple crystal"]
    },
    "elite_room" : {
        "description" : "Floor 3-2: You in a middle of the Greek Arena with\
2 kind of crystal flow in front of you, \
one is green and one is red",
        "options" : ["(3) Touch the red crystal to open the battle",
                     "(1) Touch green crystal to teleport to unlocked rooms"]
    },
    "room2" : {
        "description" : "Floor 3-1:\
A room which is simulated to the desert with \
a green crystal flow in front of you.",
        "options" : ["(3) Explore the desert",
                     "(1) Touch green crystal to teleport to unlocked rooms"]
    },
    "boss_room" : {
        "description" : "Floor 3-4: \
A destroyed castle with surrounded by fires.\
You see red eyes warrior gets out from the fire while \
riding a horse with a spear on the left hand.",
        "options" : ["(3) FIGHT THE BOSS TO SURVIVE"]
    }
}


Dungeon_map = [
    ["start_floor1", "room1", "fight_room1", "gate1"],
    ["secret_room", "gate2", "start_floor2", "subboss_room"],
    ["room2", "elite_room", "start_floor3", "boss_room"]
]


player = {"row" : 0, "col" : 0}


def setup():
    global floor, playerloc
    if player["row"] == 0:
        floor = floor1
    if player["row"] == 1:
        floor = floor2
    if player["row"] == 2:
        floor = floor3
    playerloc = (Dungeon_map[player["row"]][player["col"]])


def information():
    global decision, playerloc
    setup()
    print(floor[playerloc]["description"])
    print(floor[playerloc]["options"])
    decision = int(input("Your choice is "))


def room_choose():
    global room_choice
    room_choice = int(input("You want to room: "))
    if room_choice == 1:
        player["col"] = 0
    if room_choice == 2: 
        player["col"] = 1
    if room_choice == 3:
        player["col"] = 2
    if room_choice == 4: 
        player["col"] = 3


def choice():
    global col, row, floor_choice
    if decision == 1:
        floor_choice = int(input("Your floor you want to go to is "))
        if floor_choice == 1:
            row = 0
            room_choose()
        if floor_choice == 2:
            row = 1
            room_choose()
        if floor_choice == 3:
            row = 2
            room_choose()
    if decision == 2:
        player["col"] = player["col"] + 1
        if player["row"] == 2:
            player["col"] = player["col"] - 1
        information()
    if decision == 4:
        player["row"] = player["row"] + 1
        if player["row"] == 1:
            player["col"] = 2
        if player["row"] == 2:
            player["col"] = 2
        information()
    else:
        return("Your choice is invalid")


def start():
    information()
    while True:
        choice()
#----Main---------------------------------------------------------------------
start()