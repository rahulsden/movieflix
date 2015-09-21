# This class defines the data structure for the Movie object
class Movie:

	# constructor with 5 arguments
	# 1) Movie Title
	# 2) Complete url for movie poster
	# 3) Complete youtube url for movie trailer
	# 4) IMDB Rating in string
	# 5) Release year of movie in 'yyyy' format
	def __init__(self, title, poster_url, trailer_url, rating, year):
		self.title = title
		self.poster_image_url = poster_url
		self.trailer_youtube_url = trailer_url
		self.imdb_rating = rating
		self.release_year = year
