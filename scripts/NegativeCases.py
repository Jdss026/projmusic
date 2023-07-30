from lyricsgenius import Genius
import json
import csv

# cria acesso a API

token = 'SRY7bkiOpAIaIm6Uh_fz0xyv3cEpKzph9RTpe6bQ4xVRfnwPdEeoCZ1oTeesYR7a'

genius = Genius(token, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
genius.verbose = True
genius.remove_section_headers = True
genius.skip_non_songs = True

# lista alguns artistas de mpb
data = []
with open('./data/artistas.csv','r', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        data.append(row)

data = data[1:]
#print(data[2][0])
num_artistas = len(data)
# print(num_artistas)

master_list = []
for i in range(0,num_artistas):
    master_list.append(data[i][0])

len_master = len(master_list)
dict_songs_neg = {}
# busca letras de artistas e salva em dicionario
for i in range(len_master):
    artist = genius.search_artist(master_list[i], sort="popularity", max_songs=50)
    if artist:
        artist.save_lyrics(overwrite=True, filename='lyrics_neg.json')

        with open('lyrics_neg.json', 'r') as file:
            data = json.load(file)

        # busca musicas do autor e salva em dicionario 
        
        tam_songs = len(artist.songs)
    
        for song in range(tam_songs):
            lyrics = data['songs'][song]['lyrics'] #.split("Lyrics")[song].split("You might also likeEmbed")[0]
            title = data['songs'][song]['title']

            dict_songs_neg[title] = lyrics


        # salva em json por artista indivdualmente
        file = './data/data_mus_neg/data_music_neg.json'
        with open(file, "w") as json_file:
            json.dump(dict_songs_neg, json_file, indent=4)