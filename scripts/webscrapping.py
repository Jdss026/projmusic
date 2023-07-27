from lyricsgenius import Genius
import json
import codecs

# cria acesso a API

token = 'SRY7bkiOpAIaIm6Uh_fz0xyv3cEpKzph9RTpe6bQ4xVRfnwPdEeoCZ1oTeesYR7a'

genius = Genius(token, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

# busca artista 
artist = genius.search_artist("Gilberto Gil", max_songs=10,sort="title")

# busca musicas do autor e salva em dicionario 
dict_songs_pos = dict()
for song in artist.songs:
    title = song.title.encode('utf-8')
    title = codecs.decode(title, "UTF-8")
    lyrics = song.lyrics.encode('utf-8')
    lyrics = codecs.decode(lyrics, "UTF-8")
    dict_songs_pos[str(title)] = str(lyrics)


# salva musicas em json no schema:{"song": "lyrics", ... }
file = './data/data_music.json'
json_data = json.dumps(dict_songs_pos)

with open(file, "w") as json_file:
    json.dump(json_data, json_file, indent=4)