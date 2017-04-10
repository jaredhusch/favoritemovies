#importing media and fresh tomatoes files
import media
import fresh_tomatoes

#Instances of the class Movies
avatar = media.Movie("Avatar",
					 "Marine on an alien planet.",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://youtu.be/5PSNL1qE6VY")

shawshank_redemption = media.Movie("Shawshank Redemption",
								 "A story about a banker who is sentenced to life in Shawshank State Penitentiary for the murder of his wife and her lover, despite his claims of innocence.",
								 "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
								 "https://youtu.be/6hB3S9bIaco")

braveheart = media.Movie("Braveheart",
						 "The story of the legendary thirteenth century Scottish hero named William Wallace as he rallies the Scottish against the English monarch.",
						 "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
						 "https://youtu.be/j53_WxqPZ7c")

good_will_hunting = media.Movie("Good Will Hunting",
								"Will Hunting has a genius-level IQ but chooses to work as a janitor at MIT.",
								"https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
								"https://youtu.be/QSMvyuEeIyw")

gladitor = media.Movie("Gladiator",
					   "Commodus takes power and strips rank from Maximus, one of the favored generals of his predecessor and father, Emperor Marcus Aurelius",
					   "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
					   "https://youtu.be/owK1qxDselE")

forrest_gump = media.Movie("Forrest Gump",
						   "Slow-witted Forrest Gump has never thought of himself as disadvantaged, and thanks to his supportive mother he leads anything but a restricted life.",
						   "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
						   "https://youtu.be/uPIEn0M8su0")

#create list of instances
movies = [avatar, shawshank_redemption, braveheart, good_will_hunting, gladitor, forrest_gump]

#build my favorite movies webpage
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)






