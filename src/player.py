# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, room):
        self.room = room
        self.items = []

    def get_item(self, item, list_of_items):
        if item in list_of_items:
            self.items.append(item)
            list_of_items.remove(item)
            return list_of_items
        else:
            print("Can't get that")

    def drop_item(self, item, list_of_items):
        if item in self.items:
            self.items.remove(item)
            list_of_items.append(item)
            print("Dropped", item)
            return list_of_items
        else:
            print("Can't drop")
