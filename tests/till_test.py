import unittest

from src.till import Till
from src.room import Room
from src.guest import Guest

class TestTill (unittest.TestCase):
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
        self.till=Till()
        
        


        
    def test_till_starts_with_(self):
        self.assertEqual(0, self.till.amount)

    def test_till_can_increase(self):
        self.till.till_increase(self.room1.entry_fee)
        self.assertEqual(2.50, self.till.amount)