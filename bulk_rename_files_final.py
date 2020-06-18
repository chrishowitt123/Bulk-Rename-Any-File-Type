
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from pathlib import Path
import numpy
from datetime import datetime


path = input('\n Please paste the path to the the files you wish to rename and press enter: ')
os.chdir(path)
files = [f for f in listdir(path) if isfile(join(path, f))]

df = pd.DataFrame(files)
df['old_file_names'] = pd.DataFrame(files)
del df[0]

file_names = list(df['old_file_names'])
file_names = [ file for file in file_names if ".ipynb" not in file ]
files = file_names
df['old_file_names'] = pd.DataFrame(files)

df['new_file_names'] = df['old_file_names'].str.split('.').str[0].str.split('(').str[0]
exe = df['old_file_names'].str.split('.').str[-1].str.split('(').str[0]
date_today = datetime.today().strftime('%Y-%m-%d')

document_type = input('\n Enter your document identifier: ').title()

df['new_file_names'] = (date_today + '_' + df['new_file_names'].str.title() + '_' + document_type).str.title()


df['new_file_names'] = df['new_file_names'] + '.' + exe

df

path1 = Path(path)


files = [f for f in path1.iterdir() if f.is_file()]

for file in files:
    try:
        prefix = df.loc[df['old_file_names'] == file.name, 'new_file_names'].values[0]
        file.rename(f'{prefix}')
    except IndexError:
        pass


old = list(df['old_file_names'])
new = list(df['new_file_names'])

for o, n in zip(old, new):
    print('\n ' + o + '    ---------->    ' + n)



