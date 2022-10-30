import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1= Song("Rodriguez","Sugar Man")
        self.song2= Song("Nena", "99 Luftballons")
        self.song3= Song("Fantastischen 4", "MFG")

    def test_song_has_artist(self):
        self.assertEqual("Rodriguez", self.song1.artist)

    def test_song_has_title(self):
        self.assertEqual("MFG", self.song3.song_title)

    


   