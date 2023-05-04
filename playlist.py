
class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            current = self.items.pop()
            self.size -= 0
            return current

class MusicPlaylist(ListQueue):
    def __init__(self):
        super().__init__()

    def add_songs(self, song: tuple):
        self.enqueue(song)
    
    def play_song(self):
        current = self.dequeue()
        if current:
            print(f'playing {current[0]} for {current[1]}')
        else:
            print('There is not more songs')
    
    def play_all(self):
        while self.items:
            self.play_song()

    def all_songs(self):
        for item in self.items:
            print(item[0])
