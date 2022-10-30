
from src.till import Till
class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name=name
        self.capacity= capacity
        self.entry_fee= entry_fee
        self.guests_checked_in =[]
        self.play_list=[]
        self.earnings= 0
        
        


    def add_guest(self, guest):
        self.guests_checked_in.append(guest)

    def add_song (self, song):
        self.play_list.append(song)

    def remove_guest(self, guest):
        for guest_checked_in in self.guests_checked_in:
            if guest ==guest_checked_in:
                self.guests_checked_in.remove(guest_checked_in)

    def check_if_room_is_full(self, guest):
        amount_people_in_room= len(self.guests_checked_in)
        spaces_available= self.capacity - amount_people_in_room
        if spaces_available == 1:
            self.add_guest(guest)
            return f"There is {spaces_available} space available, please enter the {self.name} room!"
        elif spaces_available>1:
            self.add_guest(guest)
            return f"There are {spaces_available} spaces available, please enter the {self.name} room!"
        else:
            return f"The {self.name} room is sadly full!"


    def tab_increases_as_guest_checks_in(self, guest):
        self.add_guest(guest)
        guest.tab_increase(self.entry_fee)



    