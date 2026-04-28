"""Movie class for storing movie information.

This module defines a Movie class that encapsulates movie data
including title, poster image URL, and trailer YouTube URL.
"""


class Movie:
    """A class to represent a movie.

    Attributes:
        title (str): The title of the movie.
        poster_image_url (str): URL to the movie's poster image.
        trailer_youtube_url (str): URL to the movie's trailer on YouTube.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Initialize a Movie object.

        Args:
            title (str): The title of the movie.
            poster_image_url (str): URL to the movie's poster image.
            trailer_youtube_url (str): URL to the movie's trailer on YouTube.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
