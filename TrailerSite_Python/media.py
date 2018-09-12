import webbrowser


class Movie():
    """This class contains information regarding various movies."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_synopsis, poster_image,
                 trailer_youtube):
        """Constructor for the class Movie.

            Arguments
            _________


            self:
                It is the instance for which the method (constructor)
                is being called.

            movie_title:
                Title of the movie.

            movie_synopsis:
                Summary of the movie.

            poster_image:
                Url of the poster of the movie.

            trailer_youtube:
                Url of the youtube trailer of the movie."""

        self.title = movie_title
        self.synopsis = movie_synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
