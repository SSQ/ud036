import media
import fresh_tomatoes

toy_story = media.Movie("T S",
                        "A story about ",
                        "http://",
                        "https://github.com/")
#print(toy_story.storyline)

#toy_story.show_trailer()
movies = [toy_story]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
