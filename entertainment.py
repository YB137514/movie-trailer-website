import media
import fresh_tomatoes

# Creating 3 instances from the class movie by calling constructor
# located in media.py file.
ex_machina = media.Movie("Ex Machina", "AI at it's best",
                         "http://www.impawards.com/2015/posters/ex_machina_ver4_xxlg.jpg",
                         "https://www.youtube.com/watch?v=XYGzRB4Pnq8", "04/10/2015")


iob = media.Movie("The Internet's own boy", "Hacker",
                  "http://ia.media-imdb.com/images/M/MV5BMjgwOTgwNjQ5MV5BMl5BanBnXkFtZTgwMzk1NTQ2MTE@._V1_SX640_SY720_.jpg",
                  "https://www.youtube.com/watch?v=RvsxnOg0bJY", "06/27/2014")

pitch_perfect = media.Movie("Pitch Perfect", "A story about girls...",
                            "http://www.joblo.com/posters/images/full/pitch-perfect-movie-poster3.jpg",
                            "https://www.youtube.com/watch?v=amFjSha7iqM", "10/05/2012")
# using a list data structure for 3 objects of the class movie
# created above
movies = [ex_machina, iob, pitch_perfect]
# pass the movie list to the open movies function
# to generate HTML document.
fresh_tomatoes.open_movies_page(movies)
