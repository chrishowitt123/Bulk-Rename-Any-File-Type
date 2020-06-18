
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from pathlib import Path
import numpy
from datetime import datetime


path = input('Please paste the path of the files you wish to rename and press enter: \n')

os.chdir(path)

files = [f for f in listdir(path) if isfile(join(path, f))]


df = pd.DataFrame(files)

df['Files'] = pd.DataFrame(files)

df['Files'] 

file_names = list(df['Files'])
file_names = [ file for file in file_names if ".ipynb" not in file ]
files = file_names
df['Files'] = pd.DataFrame(files)

df['New File Names'] = df['Files'].str.split('.').str[0].str.split('(').str[0]

date_today = datetime.today().strftime('%Y-%m-%d')
date_today

document_type = input('What type of documents are these? (followed by press enter) \n').title()

df['New File Names'] = (date_today + '_' + df['New File Names'].str.title() + '_' + document_type).str.title()

df.columns

df.columns = (['old', 'Files', 'New File Names'])

del df['old']

df['New File Names'] = df['New File Names'] + '.txt'

df

path1 = Path(path)


files = [f for f in path1.iterdir() if f.is_file()]

for file in files:
    try:
        prefix = df.loc[df['Files'] == file.name, 'New File Names'].values[0]
        file.rename(f'{prefix}')
    except IndexError:
        pass
