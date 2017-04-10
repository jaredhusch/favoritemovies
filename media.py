#importing webbrowser module
import webbrowser

#Class movie
class Movie():
	"""This class provides a way to store movie related informaiton"""
	VALID_RATINGS = ["G","PG","PG-13","R"]

	def __init__(self, movie_title, movie_story, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
#instance method for shwoing trailers
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)