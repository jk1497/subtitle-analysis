from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from clean import cleanText
from collections import Counter
import pandas as pd 
import os

my_titles = []
string_array = []
stopwords = []

directory = 'subtitles'

with open('stopwords.txt') as f:
  stopwords = f.read().splitlines()
  f.close

print('Reading files.../n')

for filename in os.listdir(directory):
  my_titles.append(filename)
  with open(os.path.join("subtitles", filename), 'r') as f:
    string_array.append(f.read())
  f.close()

new_titles_array = []

for i in my_titles:
  new_titles_array.append(i[10:].rstrip(".srt"))

new_array = []

print('Cleaning subtitles.../n')

for i in string_array:
  new_array.append(cleanText(i))

token_filters = [POSKeepFilter(['名詞']), TokenCountFilter()]

a = Analyzer(token_filters=token_filters)

d = {'title': [],'word': [], 'count': []}
df = pd.DataFrame(data=d)

length = len(new_titles_array)
# length = 10

print('Creating dataframe.../n')

for i in range(length):
  print(f"Analysing {new_titles_array[i]}...")
  for k, v in a.analyze(new_array[i]):
    if k not in stopwords:
      df.loc[len(df.index)] = [new_titles_array[i],k,v]

print('Sorting dataframe.../n')

df = df.sort_values(by = ['count'], ascending = False)

df.to_csv('output.csv')

print('Done.')
