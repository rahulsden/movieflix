#This class defines the data structure for the Movie object
class Movie:

	#constructor with 3 arguments
	# 1) Movie Title
	# 2) Complete url for movie poster
	# 3) Complete youtube url for movie trailer
	def __init__(self, title, poster_url, trailer_url):
		self.title = title;
		self.poster_image_url = poster_url;
		self.trailer_youtube_url = trailer_url;
		self.imdb_rating = -1;  #to be used for future enhancement
