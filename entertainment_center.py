"""Entertainment center for displaying favorite movies.

This module creates instances of movies and generates an HTML webpage
to display them using the fresh_tomatoes module.
"""

import fresh_tomatoes
from media import Movie

# Create instances of movies with their details
# Format: Movie(title, poster_image_url, trailer_youtube_url)

toy_story = Movie(
    "Toy Story 3",
    "https://m.media-amazon.com/images/I/71M5v4cCsFL._AC_UF894,1000_QL80_.jpg",
    "https://www.youtube.com/watch?v=v-2BlMNH1QTeE")

the_matrix = Movie(
    "The Matrix",
    "https://m.media-amazon.com/images/M/MV5BN2NmN2VhMTQtMDNiOS00NDlhLTliMjgtODE2ZTY0ODQyNDRhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")

inception = Movie(
    "Inception",
    "https://m.media-amazon.com/images/M/MV5BMjExMjkwNTQ0Nl5BMl5BanBnXkFtZTcwNTY0OTk1Mw@@._V1_.jpg",
    "https://www.youtube.com/watch?v=YoHD3HAjGGA")

interstellar = Movie(
    "Interstellar",
    "https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

dark_knight = Movie(
    "The Dark Knight",
    "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

gladiator = Movie(
    "Gladiator 2",
    "https://friedrichsbau-kino.de/fileadmin/friedrichsbau/import/_processed_/a/3/csm_fw27big_13_10941174f6.jpg",
    "https://www.youtube.com/watch?v=4rgYUipGJNo")

# Create a list of movies
movies = [toy_story, the_matrix, inception, interstellar, dark_knight, gladiator]

# Generate the HTML page with the movies
fresh_tomatoes.open_movies_page(movies)
