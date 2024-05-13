from ITS.room import Room


class Building:

    def __init__(self, name: str, address: str, floors: int):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[Room] = []
    
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_floors(self):
        return self.floors
    def get_rooms(self):
        return self.rooms
    
    def add_room(self,room: Room):
        if room not in self.get_rooms() and room.floor <= self.get_floors():
            self.rooms.append(room)
            return True
        else:
            return False
        
    def __str__(self):
        s: str = f"Buildingname = {self.get_name()}, address = {self.get_address()}, floors = {self.get_floors()}, rooms = {self.get_rooms()}"
        