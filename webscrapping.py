from lyricsgenius import Genius

# cria acesso a API

token = 'SRY7bkiOpAIaIm6Uh_fz0xyv3cEpKzph9RTpe6bQ4xVRfnwPdEeoCZ1oTeesYR7a'

genius = Genius(token)

# busca artista 
artist = genius.search_artist("Gilberto Gil"
                              , max_songs=3,
                              sort="title")

# busca musicas do autor
#print(artist.songs[0].title)
#print(artist.songs[0].lyrics)
num_songs = len(artist.songs)
print(num_songs)

# salva musicas em json ex:{"autor":"", "musicas":[]}

# for i in artist.songs:
#     print(i.lyrics, "\n")

# artist.save_lyrics()
# song = genius.search_song("2001", artist.name)
# print(song.lyrics)

# https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29