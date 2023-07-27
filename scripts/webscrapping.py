from lyricsgenius import Genius
import json

# cria acesso a API

token = 'SRY7bkiOpAIaIm6Uh_fz0xyv3cEpKzph9RTpe6bQ4xVRfnwPdEeoCZ1oTeesYR7a'

genius = Genius(token, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

# busca artista 
artist = genius.search_artist("Gilberto Gil"
                              , max_songs=3,
                              sort="title")

# busca musicas do autor e salva em dicionario 
num_songs = len(artist.songs)
list_songs_pos = list()

for song in artist.songs:
    temp = {}
    temp['artist'] = artist.name
    temp['song'] = song.title
    temp['lyrics'] = song.lyrics
    list_songs_pos.append(temp)

print(list_songs_pos)

# salva musicas em json ex:{"artist":"", "song":"", lyrics:["""] }

# for i in artist.songs:
#     print(i.lyrics, "\n")

# artist.save_lyrics()
# song = genius.search_song("2001", artist.name)
# print(song.lyrics)

# https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29