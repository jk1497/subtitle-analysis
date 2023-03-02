from janome.analyzer import Analyzer
from janome.tokenfilter import *
from clean_text import cleanText
import pandas as pd 
import os


# tokenize_ja.py takes all text from the subtitle files and returns a dataframe with each word and that word's count
#   1. tokenize_ja.py reads the text from each subtitle file.
#   2. cleanText() removes any non-japanese characters. (timecodes, punctuation, etc)
#   3. The text is tokenized, ie split from a large block of text into indivual words.
#   4. Stopwords (common words that aren't relavent to the analysis) are removed
#   5. The words along with their count and the film they were mined from, are compiled into a dataframe and stored in 'output.csv'

my_titles = []
string_array = []

directory = 'subtitles'

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

print('Creating dataframe.../n')

stopwords = []

with open('stopwords.txt') as f:
  stopwords = f.read().splitlines()
  f.close

for i in range(length):
  print(f"Analysing {new_titles_array[i]}...")
  for k, v in a.analyze(new_array[i]):
    if k not in stopwords:
      df.loc[len(df.index)] = [new_titles_array[i],k,v]

print('Sorting dataframe.../n')

df = df.sort_values(by = ['count'], ascending = False)

df.to_csv('token_output.csv')

print('Done.')




