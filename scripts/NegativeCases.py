from lyricsgenius import Genius
import json

# cria acesso a API

token = 'SRY7bkiOpAIaIm6Uh_fz0xyv3cEpKzph9RTpe6bQ4xVRfnwPdEeoCZ1oTeesYR7a'

genius = Genius(token, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
genius.verbose = True
genius.remove_section_headers = True
genius.skip_non_songs = True

# busca artista 
artist = genius.search_artist("a", sort="title") #, max_songs=50, sort="title")
print(artist)