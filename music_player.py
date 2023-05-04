class Nodes():
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class PlayList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def add_song(self, data):
        new_song = Nodes(data)
        if self.count == 0:
            self.head = new_song
            self.tail = new_song
        else:
            new_song.previous = self.tail
            self.tail.next = new_song
            self.tail = new_song
        self.count += 1

    def play_song(self):
        if self.count == 0:
            print('No more songs able')

        elif self.count == 1:
            current = self.head.data
            print(f'Playing {current[0]} for {current[1]}')
            self.head = None
            self.tail = None
            self.count = 0

        elif self.count > 1:
            current = self.head.data
            print(f'Playing {current[0]} for {current[1]}')
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

    def play_all(self):
        while self.head:
            self.play_song()

    def all_songs(self):
        """
            Recorriendo todas las canciones
        """
        print('Recorriendo todas las canciones')
        item = self.head
        for i in range(self.count):
            print(f'Song: {item.data[0]}  -  Duration: {item.data[1]}')
            item = item.next