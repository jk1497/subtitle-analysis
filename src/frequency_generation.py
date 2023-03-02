import pandas as pd

# frequency_generation.py reads the dataframe that contains the wordcount for every word in every genre
# and calculates how common that word is within it's own genre
# the output is stored in frequency_df.csv

analysis_df = pd.read_csv("all_genres.csv")

# analysis_df = analysis_df.drop("Unnamed: 0",axis=1)

analysis_df = pd.pivot_table(analysis_df, values="count", index=["word"], columns=["genre"], aggfunc=sum, fill_value=0, margins=True)

analysis_df = analysis_df.sort_values(by=['All'], ascending=False)

genre_list = []

for i in analysis_df.columns:
    genre_list.append(i)

total_list = []

for i in genre_list:
    total_list.append(analysis_df[i][0])

genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'All']

frequency_df = analysis_df.copy().astype(float)

for i in range(0,len(frequency_df.index)):
    for j in range(0,len(frequency_df.columns)):
        frequency_df.iloc[i][j] = frequency_df.iloc[i][j]/total_list[j]
    print(f"calculating row {i}")

frequency_df.drop(index=frequency_df.index[0],axis=0,inplace=True)

frequency_df.to_csv("frequency_df.csv")
