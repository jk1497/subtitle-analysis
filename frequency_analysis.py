import pandas as pd

# frequency_analysis.py reads the dataframe that contains the frequency for every word in every genre
# it targets words that are common in a given genre, but less common overall.
# the output is stored in uncommon_words.csv

my_df = pd.read_csv("frequency_df.csv")

genre_list = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama','Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery','Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'All']

current_genre = genre_list[0]

uncommon_words_df = pd.DataFrame(columns=['Genre','Word'])
tweek_words_df = pd.DataFrame(columns=['Genre','Word','Frequency','Overall'])

for j in genre_list:
    current_genre = j
    print(f"analysing {j}..")
    for i in my_df.index:
        curr_frequency = my_df.iloc[i][current_genre]
        total_frequency = my_df.iloc[i]["All"]

        if (curr_frequency > 0.0016) & (total_frequency < 0.001):
            uncommon_words_df.loc[len(uncommon_words_df)] = [current_genre,my_df.iloc[i]['word']]
            tweek_words_df.loc[len(tweek_words_df)] = [current_genre,my_df.iloc[i]['word'],curr_frequency,total_frequency]

uncommon_words_df.to_csv("uncommon_words.csv")
tweek_words_df.to_csv("tweek_words.csv")

    

