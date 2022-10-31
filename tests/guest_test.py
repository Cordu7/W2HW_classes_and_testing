import unittest

from src.guest import Guest
from src.room import   Room
from src.song import Song
from src.till import Till


class TestGuest(unittest.TestCase):
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
        self.song4= Song("Hot Chip", "Over and Over")
        self.till=Till()

    def test_guest_has_name(self):
        self.assertEqual("Harris", self.guest1.name)
    

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Over and Over", self.guest1.favourite_song)

    def test_has_tab(self):
        self.assertEqual(0, self.guest2.tab)

    def test_guest_has_favourite_song_in_playlist(self):
        self.room1.add_guest(self.song1)
        self.room1.add_song(self.song2)
        self.room1.add_song(self.song3)
        self.room1.add_song(self.song4)
        self.assertEqual("Jippeee", self.guest1.song_in_playlist(self.room1, self.song4))

    def test_tab_can_increase(self):
        self.guest6.tab_increase(2.50)
        self.assertEqual(2.50, self.guest6.tab)

    def test_guest_can_pay_tab(self):
        self.room2.tab_increases_as_guest_checks_in(self.guest4)
        print(self.guest4)
        self.guest4.pay_tab(self.room2)
        self.assertEqual(0, self.guest4.tab)
        self.assertEqual(597, self.guest4.wallet)
        self.assertEqual(3, self.till.amount)