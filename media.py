
"""Media consists of a class Movie.
"""

import webbrowser


class Movie(object):

    """Movie class to display data about favorite movies and show trailer.

    Instance variables:
        title
        storylline
        poster_image_url
        trailer_youtube_url
        release_date

    Attributes:
        show_trailer: to show the trailer
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube,
                 movie_release_date):
        """Constructor with no default initializer."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    def show_trailer(self):
        """Opens trailer inside the window."""
        webbrowser.open(self.link)
