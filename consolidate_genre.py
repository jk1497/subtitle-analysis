import pandas as pd

movies_db = pd.read_csv('moviedb.csv')
movies_analysis = pd.read_csv('output.csv')

movies_analysis = movies_analysis.drop("Unnamed: 0",axis=1)

new_df = pd.merge(  movies_analysis,
                    movies_db,
                    on ='title',
                    how ='inner')

new_df_all_genres = pd.DataFrame(columns = ["title","word","count",'imdb_id','original_title','popularity','release_date','genre'])

GENRE_TOTAL = 7

# test_df = new_df.head(100)

for i in new_df.index:
    genre_count = 1
    while genre_count<=GENRE_TOTAL:
        if str(new_df.iloc[i][f"Genre_{genre_count}"])!="nan":
            list_row = pd.DataFrame({   "title":[new_df.iloc[i]["title"]], 
                                        "word":[new_df.iloc[i]["word"]],
                                        "count":[new_df.iloc[i]["count"]],
                                        "imdb_id":[new_df.iloc[i]["imdb_id"]],
                                        "original_title":[new_df.iloc[i]["original_title"]],
                                        "popularity":[new_df.iloc[i]["popularity"]],
                                        "release_date":[new_df.iloc[i]["release_date"]],
                                        "genre":[new_df.iloc[i][f"Genre_{genre_count}"]]
            })
            # new_df_all_genres = new_df_all_genres.append(list_row)
            new_df_all_genres = pd.concat([new_df_all_genres,list_row])
        else:
            genre_count = GENRE_TOTAL
        genre_count += 1
    print(f"Consolidating genres... {(i/float(len(new_df.index))*100):.2f}%", end="\r")

new_df_all_genres.to_csv("new_df_all_genres.csv")

