from lyricsgenius import Genius
import json

# cria acesso a API

token = 'SRY7bkiOpAIaIm6Uh_fz0xyv3cEpKzph9RTpe6bQ4xVRfnwPdEeoCZ1oTeesYR7a'

genius = Genius(token, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
genius.verbose = True
genius.remove_section_headers = True
genius.skip_non_songs = True

# busca artista 
artist = genius.search_artist("Gilberto Gil", sort="title") #, max_songs=50, sort="title")

artist.save_lyrics(overwrite=True, filename='lyrics.json')

with open('lyrics.json', 'r') as file:
    data = json.load(file)

# busca musicas do autor e salva em dicionario 
dict_songs_pos = {}
tam_songs = len(artist.songs)

for song in range(tam_songs):
    lyrics = data['songs'][song]['lyrics'] #.split("Lyrics")[song].split("You might also likeEmbed")[0]
    title = data['songs'][song]['title']
    print(type(title))
    dict_songs_pos[title] = lyrics

# salva em json
file = './data/data_music.json'

with open(file, "w") as json_file:
    json.dump(dict_songs_pos, json_file, indent=4)