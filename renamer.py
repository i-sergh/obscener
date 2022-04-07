import os
import re
obscene_names = [

    ]

good_names = [

    ]

danger_names= [

    ]

def renamer ():
    for name in os.listdir():
    if re.search( 'Новый текстовый документ', name):
        os.rename(name, re.sub( 'Новый текстовый документ', '123', name))
