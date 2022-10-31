import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.till import Till

class TestRoom (unittest.TestCase):
    def setUp(self):
        self.room1= Room("Silver", 5, 2.50)
        self.room2=Room("Gold", 10, 3.00)
        self.room3= Room("Diamond", 20, 4.50)
        self.guest1 = Guest("Harris", 50, "Over and Over")
        self.guest2= Guest("Ines", 60, "Sugar Man")
        self.guest3 =Guest ("Aurelia", 20, "99 Luftballons")
        self.guest4= Guest("Ljuba", 500, "MFG")
        self.guest5= Guest("Samuel", 5, "MFG")
        self.guest6= Guest("Winni", 1000, "MFG")
        self.song1= Song("Rodriguez","Sugar Man")
        self.song2= Song("Nena", "99 Luftballons")
        self.song3= Song("Fantastischen 4", "MFG")
        # self.tab1= Tab(self.guest1)

    def test_room_has_name(self):
        self.assertEqual("Diamond", self.room3.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)

    def test_room_can_have_guests(self):
        self.assertEqual(0, len(self.room1.guests_checked_in))
    
    def test_room_has_entry_fee(self):
        self.assertEqual(2.50, self.room1.entry_fee)
    
    # def test_room_has_earnings(self):
    #     self.assertEqual(0,self.room3.earnings)

    def test_room_has_playlist(self):
        self.assertEqual(0, len(self.room1.play_list))

    def test_room_can_add_guests(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guests_checked_in))
        
    def test_room_can_remove_guest(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        self.room1.remove_guest(self.guest1)
        self.assertEqual(2, len(self.room1.guests_checked_in))

    def test_room_can_add_to_Playlist(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.play_list))


    #What happens if there are more guests 
    # # # trying to be checked in than there is free space in the room?
    
    def test_room_not_admits_if_no_space_availabe(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        self.room1.add_guest(self.guest4)
        self.room1.add_guest(self.guest5)
        self.assertEqual("The Silver room is sadly full!", self.room1.check_if_room_is_full(self.guest6))

    def test_room_does_admit_if_space_availabe(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        self.room1.add_guest(self.guest4)
        self.assertEqual("There is 1 space available, please enter the Silver room!", self.room1.check_if_room_is_full(self.guest6))
        self.assertEqual(5, len(self.room1.guests_checked_in))

    def test_room_does_admit_if_space_availabe_morethan_one_space_left(self):
        self.room2.add_guest(self.guest1)
        self.room2.add_guest(self.guest2)
        self.room2.add_guest(self.guest3)
        self.room2.add_guest(self.guest4)
        self.assertEqual("There are 6 spaces available, please enter the Gold room!", self.room2.check_if_room_is_full(self.guest6))
        self.assertEqual(5, len(self.room2.guests_checked_in))

    def test_tab_increaes_when_guest_checks_into_room(self):
        self.room2.tab_increases_as_guest_checks_in(self.guest1)
        self.assertEqual(3.00, self.guest1.tab)

    



        #def test_room_not_admits_if_space_not_availabe(self):

    

    
