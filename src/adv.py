from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items = ['bone', 'torch']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
run = True
player_1 = Player('outside')
player_room = room[player_1.room]

while run == True:

    try:
        room_name = player_room.name
        room_desc = player_room.description
        items = player_room.items
    except AttributeError:
        print('Woah there cowboy, try again')
        player_room = room[player_1.room]

    print(room_name, room_desc, items)
    cmd = input()

    if len(cmd.split( )) > 1:
        action = cmd.split( )[0]
        item = cmd.split( )[1]
    else:
        action = cmd

    if action == 'n':
        player_room = player_room.n_to
    elif action == 's':
        player_room = player_room.s_to
    elif action == 'e':
        player_room = player_room.e_to
    elif action == 'w':
        player_room = player_room.w_to
    elif action == 'q':
        run = False
        print("Bye")
    elif action == 'i':
        print(player_1.items)

    if action == 'get':
        items = player_1.get_item(item, items)
        print("Picked up", player_1.items[-1])
    elif action == 'drop':
        items = player_1.drop_item(item, items)
        print("Dropped", items[-1])

    else:
        print("Not a valid choice")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
