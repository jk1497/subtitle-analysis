import pandas as pd
import os
import requests
from os import listdir
from os.path import isfile, join

f = open(".credentials", "r")
credentials = f.read().splitlines()
f.close() 

username = credentials[0]
password = credentials[1]
api_key = credentials[2]

# define appropriate language code, first pass of analysis is for Japanese films, languages = 'ja'
languages = 'ja'

# connection.py attempts to download a subtitle file for every relevent film:
#     1. login() into opensubtitles API with credentials
#     2. download_subs() reads the movies with their imdb id from moviedb.csv
#     3. get_subtitle_id() takes the imdb id and checks the api for a subtitle file with matching opensubs id, the opensubs id is returned
#     4. download_subs() checks if a subtitle file has already been downloaded for that movie in the directory, if a file doesn't exist yet, 
#        get_download_url() returns a url for the file and it is downloaded.

def login(username,password,api_key):

    url = "https://api.opensubtitles.com/api/v1/login"

    payload = {
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json",
        "Api-Key": api_key
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

def get_subtitle_id(imdb_id,api_key):
    url = "https://api.opensubtitles.com/api/v1/subtitles"
    order_by = 'download_count'
    order_direction = 'desc'

    headers = {
        "Content-Type": "application/json",
        "Api-Key": api_key
    }
    querystring = {
        "imdb_id":imdb_id,
        "languages":languages,
        "order_by":order_by,
        "order_direction":order_direction
    }

    response = requests.request("GET", url, headers=headers,params=querystring)
    my_json = response.json()

    if bool(my_json['data']):
        subtitle_id = int(my_json['data'][0]["attributes"]["files"][0]["file_id"])
        return subtitle_id
    else:
        return 0

def get_download_url(subtitle_id,api_key):
    url = "https://api.opensubtitles.com/api/v1/download"

    payload = {
        "file_id": subtitle_id
    }
    headers = {
        "Content-Type": "application/json",
        "Api-Key": api_key
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    my_json = response.json()
    link = my_json['link']

    return(link)

def download_subs():

    output_directory = '/Users/jonny/Developer/SRT_Analysis/subtitles'

    filelist = [f for f in listdir(output_directory) if isfile(join(output_directory, f))]

    filelistbrief = []

    for i in filelist:
        filelistbrief.append(i[0:9].lstrip('t').lstrip('0'))

    movies_df = pd.read_csv('moviedb.csv')

    id_list = []

    for i in movies_df.index:
        id_list.append(movies_df['imdb_id'][i].lstrip('t').lstrip('0'))

    movies_df['imdb_id_trim'] = id_list

    for i in movies_df.index:
        try:
            subtitle_id = get_subtitle_id(movies_df.at[i, 'imdb_id_trim'],api_key)
        except:
            subtitle_id = 0

        curr_id = movies_df.at[i, 'imdb_id_trim']

        # Create a file path by joining the directory name with the desired file name
        file_path = os.path.join(output_directory, f"{movies_df.at[i, 'imdb_id']}_{movies_df.at[i, 'title']}.srt")

        if curr_id in filelistbrief:
            print(f"i = {i}: File already exists for {movies_df.at[i,'title']}")
        elif subtitle_id != 0: 
            try:
                my_url = get_download_url(subtitle_id,api_key)
                response = requests.get(my_url)
                with open(file_path, 'wb') as output:
                    output.write(response.content)
                print(f"i = {i}: Download successful for {movies_df.at[i,'title']}")
                counter_pass+=1
            except:
                print(f"i = {i}: No subtitle ID for {movies_df.at[i, 'title']}")
            
login(username=username,password=password,api_key=api_key)
download_subs()




