# Compulsory Task 2

import spacy

nlp = spacy.load('en_core_web_md')

# Write 'movies.txt' file to list
movies = []

with open ("movies.txt", "r", encoding = "utf-8") as f:
    for line in f:
        line = line.strip()
        movies.append(line)

# Extract decription only from movies list and omit movie number/letter
movies_desc = []

for i in movies:
    movies_desc.append(i[9:])

# Create tokens from my movie
my_movie_title = "Planet Hulk"
my_movie_desc = [ "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator." ]

# Find similarity and append to list
similarity_list = []

for token in my_movie_desc:
    token = nlp(token)
    for token_ in movies_desc:
        token_ = nlp(token_)
        similarity_list.append(token.similarity(token_))

# Find index of max similarity
max_similarity_index = similarity_list.index(max(similarity_list))

print(f"The title of the most similar movie is: {movies[max_similarity_index][0:7]}")