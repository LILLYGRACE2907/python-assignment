# Question 13
# Create a House class that HAS-A Room objects.

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, obj):
        self.rooms.append(obj)

    def show_rooms(self):
        print("House contains:", [x.name for x in self.rooms])

obj = House()
obj.add_room(Room("Example 1"))
obj.add_room(Room("Example 2"))
obj.show_rooms()
