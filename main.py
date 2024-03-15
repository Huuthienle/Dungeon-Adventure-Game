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
        "description" : "A stone roon with a purple crystal flow in middle",
        "options" : ["(1) Escape a dungeon", 
                     "(2) Touch the crystal to teleport to the next rooms"]
    },
    "room1" : {
        "description" : "A room which is simulated to the forest with \
            a green crystal flow in front of you. There is a lake in the left\
            of a forest with a purple crystal flow in the middle",
        "options" : ["(1) Explore the forest",
                     "(2) Touch purple crystal to teleport to the next room",
                     "(3) Touch green crystal to teleport to unlocked rooms"]
    },
    "fight_room1" : {
        "description" : "You in a middle of the Greek Arena with \
             2 kind of crystal flow in front of you, \
             one is green and one is red",
        "options" : ["(1) Touch the red crystal to open the battle",
                     "(2) Touch green crystal to teleport to unlocked rooms"]
    },
    "gate1" : {
        "description" : "A room with a closed gate and a green crystal",
        "options" : ["(1) Enter gate to the second floor, need the first key",
                     "(2) Touch green crystal to teleport to unlocked rooms"]
    }
}


floor2 = {
    "start_floor2" : {
        "description" : "A room with 3 crystals flow in the air, \
            a purple crystal in the right side of the room, \
            another purple crystal in the left of the room, \
            and a green crystal in the middle of the room.",
        "options" : ["(1) Touch green crystal to teleport to unlocked rooms",
                     "(2) Touch left purple crystal", 
                     "(3) Touch right purple crystal"]
    },
    "gate2" : {
        "description" : "A room with closed gate and \
            green crystal in the middle, and grey crystal in the left",
        "options" : ["(1) Touch green crystal to teleport to unlocked rooms", 
                     "(2) Fix the grey crystal and enter the room", 
                     "(3) Enter gate to the third floor, need the second key"]
    },
    "secret_room" : {
        "description" : "A room with a treasure chest in end of the room \
            and green crystal in front of you.",
        "options" : ["(1) Touch green crystal to teleport to unlocked rooms", 
                     "(2) Open the treasure chest"]
    },
    "subboss_room" : {
        "description" : "You in the main room of the Britain castle \
            which have a throne in front of. There is a knight in a red armor\
            with a long greatsword beside it. There are some sentences appear \
            in front of you: ''"
        
    }
}
#----Main---------------------------------------------------------------------
Dungeon_map = [
    ["start_floor1", "room1", "fight_room1", "gate1"],
    ["secret_room", "gate2", "start_floor2", "subboss_room"],
    ["room2", "elite_room", "start_floor3", "boss_room"]
]