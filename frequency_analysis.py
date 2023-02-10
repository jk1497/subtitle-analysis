import pandas as pd

my_df = pd.read_csv("frequency_df.csv")

current_genre = "Action"

uncommon_words = []

my_df = my_df.sort_values(by=[current_genre], ascending=False)

for i in my_df.index:
    curr_frequency = my_df.iloc[i][current_genre]
    total_frequency = my_df.iloc[i]["All"]

    if (curr_frequency > 0.001) & (total_frequency < 0.001):
        print(f"{my_df.iloc[i]['word']}\t{round(curr_frequency,4)}\t{round(total_frequency,4)}")
        uncommon_words.append(my_df.iloc[i]['word'])

print(uncommon_words)
    

