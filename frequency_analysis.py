import pandas as pd

my_df = pd.read_csv("frequency_df.csv")

genre_list = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama','Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery','Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'All']

current_genre = genre_list[0]

uncommon_words = []

uncommon_words_df = pd.DataFrame(columns=['Word','Genre'])

my_df = my_df.sort_values(by=[current_genre], ascending=False)


for j in genre_list:
    current_genre = j
    print(f"analysing {j}..")
    for i in my_df.index:
        curr_frequency = my_df.iloc[i][current_genre]
        total_frequency = my_df.iloc[i]["All"]

        if (curr_frequency > 0.001) & (total_frequency < 0.001):
            # print(f"{my_df.iloc[i]['word']}\t{round(curr_frequency,4)}\t{round(total_frequency,4)}")
            uncommon_words.append(my_df.iloc[i]['word'])
            uncommon_words_df.loc[len(uncommon_words_df)] = [my_df.iloc[i]['word'],current_genre]

uncommon_words_df.to_csv("uncommon_words.csv")

    

