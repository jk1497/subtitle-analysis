Target language immersion is an important part of learning any natural language.
It's a lot easier to spend time immersing in a language if you enjoy the content you're consuming.
At the moment I'm learning Japanese and I love Japanese horror movies. 
I decided it would be useful to do an analysis of different movie genres to determine what vocabulary to prioritize if I wanted to watch a lot of Japanese horror movies.

This analysis started by sourcing a list of movies archived on imdb with their imdb_id, orginal language and genres considered esssential data. 
I then connected to the opensubtitles.org api and downloaded all available Japanese language subtitles for each movie in my target list from imdb.
After obtaining the dataset, I cycled through every file, cleaning the subtitles of any misc. characters and storing them as individual, long strings.
The strings are then tokenized. For Japanese text I use the Janome python package. This splits the text from one long paragraphs and sentence into individual words.
The words can then be counted. 
Once I have a file of every word in every movie and the count, I can add in the genres for each movie from the imdb dataset.
I can then perform a frequency analysis on every word to see how common it is in a given movie.
Once I have the word frequency, I compare that to a broad frequency across all genres.
I consider any word that is common in a certain genre, reletively uncommon overall an esssential word to understand movies in a given genre.
These esssential words are then compiled into a JSON file with an object for each genre of movie.
I push this JSON file to my react app which displays the esssential vocabulary on jonnykidd.com

Currently this analysis is focused on Japanese language movies as Japanese is my target language.
However this analysis could be expanded to include movies from other languages. 
The only method that would need tweeking is the method of Tokenization as the Janome package is used exclusively for Japanese.

