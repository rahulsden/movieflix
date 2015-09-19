#import statements
from media import Movie
from fresh_tomatoes import *

#function to add the favourite movies in the list
def add_fav_movies(movie_list):
	movie_list.append(Movie("The Shawshank Redemption",
					  "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1__SX727_SY685_.jpg",
					  "https://www.youtube.com/watch?v=6hB3S9bIaco"
					  ))

	movie_list.append(Movie("The Godfather",
					  "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1__SX727_SY685_.jpg",
					  "https://www.youtube.com/watch?v=sY1S34973zA"
					  ))


	movie_list.append(Movie("The Dark Knight",
					  "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1__SX727_SY685_.jpg",
					  "https://www.youtube.com/watch?v=EXeTwQWrcwY"
					  ))


#create a favourite movie list
my_fav_movie_list = [];

# call function to add the movies in the list
add_fav_movies(my_fav_movie_list)

# call to generate html and render in browser
open_movies_page(my_fav_movie_list)