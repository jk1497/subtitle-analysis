import pandas as pd
import json

# uncommon_to_json takes the uncommon words for each genre and creates a json file that can be pushed to the website

genre_list = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama','Family', 'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery','Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'All']

my_df = pd.read_csv("uncommon_words.csv")

other_list = []

for i in genre_list:
    my_list = []
    for j in my_df.index:
        if my_df.iloc[j]["Genre"] == i:
            curr = my_df.iloc[j]["Word"]
            my_list.append(curr)
    other_list.append(my_list)

for i in other_list:
    print(i)

words = {'jack': 4098, 'sape': 4139}

my_dict = {'Action': other_list[0],'Adventure': other_list[1], 'Animation': other_list[2], 'Comedy': other_list[3],'Crime': other_list[4],'Drama': other_list[5],'Family': other_list[6],'Fantasy': other_list[7], 'Foreign': other_list[8], 'History': other_list[9], 'Horror': other_list[10], 'Music': other_list[11], 'Mystery': other_list[12],'Romance': other_list[13], 'Science Fiction': other_list[14], 'TV Movie': other_list[15], 'Thriller': other_list[16], 'War': other_list[17]}

json_object = json.dumps(my_dict, indent = 4, ensure_ascii=False) 

f = open("my_genre.json", "w")
f.write(json_object)
f.close()
