import pandas as pd

anal_df = pd.read_csv("new_df_all_genres.csv")

# for i in anal_df.index:
#     print(i)

# anal_df = anal_df.drop("Unnamed: 0",axis=1)

anal_df = pd.pivot_table(anal_df, values="count", index=["word"], columns=["genre"], aggfunc=sum, fill_value=0, margins=True)

anal_df = anal_df.sort_values(by=['All'], ascending=False)

# print(anal_df.head(5))
# print(len(anal_df.index))

genre_list = []

for i in anal_df.columns:
    genre_list.append(i)

total_list = []

for i in genre_list:
    total_list.append(anal_df[i][0])

# print(genre_list)
genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'All']


# frequency_df = pd.DataFrame(columns = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'All'])
# frequency_df = pd.Series(['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'All'])
frequency_df = anal_df.copy().astype(float)

for i in range(0,len(frequency_df.index)):
    for j in range(0,len(frequency_df.columns)):
        frequency_df.iloc[i][j] = frequency_df.iloc[i][j]/total_list[j]
    print(f"calculating row {i}")

frequency_df.drop(index=frequency_df.index[0],axis=0,inplace=True)

# for i in genre_list:
#     sorted_frequency_df = frequency_df.sort_values(by=[i], ascending=False)
#     sorted_frequency_df.head(250).to_csv(f"Sorted/{i}_sorted.csv")

frequency_df.to_csv("frequency_df.csv")