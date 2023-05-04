from playlist import MusicPlaylist

reggae = MusicPlaylist()

reggae.add_songs(("REMEMBER", 5.19))
reggae.add_songs(("comfy vibes", 3.12))
reggae.add_songs(("Into the blue's", 4.03))
reggae.add_songs(("E.M.A", 4.16))


reggae.all_songs()
print('-'*10)
reggae.play_all()