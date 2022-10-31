
class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet=wallet
        self.favourite_song=favourite_song
        self.tab = 0.0

    def song_in_playlist(self, room, song):
        for song_in_playlist in room.play_list:
            if song_in_playlist == song:
             return "Jippeee"

    def tab_increase(self, amount):
        self.tab+= amount

    def pay_tab(self, room):
        self.wallet -= self.tab
        room.till += self.tab
        self.tab = 0



    