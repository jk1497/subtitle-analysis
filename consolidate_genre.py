import pandas as pd

# consolodate_genre.py takes list of orignal list of movies with their genres and the new tokenized text with wordcount,
# it merges the two dataframes together and consolidates them in one large dataframe. 
# This dataframe has spereate rows for every word from every film in every genre.

movies_db = pd.read_csv('moviedb.csv')
movies_analysis = pd.read_csv('token_output.csv')

movies_analysis = movies_analysis.drop("Unnamed: 0",axis=1)

new_df = pd.merge(  movies_analysis,
                    movies_db,
                    on ='title',
                    how ='inner')

new_df_all_genres = pd.DataFrame(columns = ["title","word","count",'imdb_id','original_title','popularity','release_date','genre'])

GENRE_TOTAL = 7

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
            new_df_all_genres = pd.concat([new_df_all_genres,list_row])
        else:
            genre_count = GENRE_TOTAL
        genre_count += 1
    print(f"Consolidating genres... {(i/float(len(new_df.index))*100):.2f}%", end="\r")

new_df_all_genres.to_csv("all_genres.csv")

