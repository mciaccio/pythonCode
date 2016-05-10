import webbrowser

class Movie():
    """ Move class documentation """
    
    # Class variable - not instance variable
    # Constant - All CAPS 
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method 
    def show_trailer(self):
        print("Begin show_trailer function")
        print('\tself.trailer_youtube_url is -> {}'.format(self.trailer_youtube_url))
        
        webbrowser.open(self.trailer_youtube_url)

        print("End show_trailer function")
