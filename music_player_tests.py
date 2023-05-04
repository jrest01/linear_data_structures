from music_player import PlayList

salsa = PlayList()

salsa.add_song(('Cancion 1',1))
salsa.add_song(('Cancion 2',2))
salsa.add_song(('Cancion 3',3))
salsa.add_song(('Cancion 4',4))

# salsa.play_all()
print('-'*10)

salsa.all_songs()