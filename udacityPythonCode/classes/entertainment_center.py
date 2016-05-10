
# import the media.py file
# media.py and entertainment_center.py - two files SAME directory 
import media
import fresh_tomatoes

# use the Movie class defined in the imported media.py file 
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#toy_story.title

print('\n\ttoy_story.title is -> {}'.format(toy_story.title))
print('\ttoy_story.storyline is -> {}'.format(toy_story.storyline))
print('\ttoy_story.poster_image_url is -> {}'.format(toy_story.poster_image_url))
print('\ttoy_story.trailer_youtube_url is -> {}\n'.format(toy_story.trailer_youtube_url))

"""
avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                     # "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
"""

# print('\tavatar.title is -> {}'.format(avatar.title))
# print('\tavatar.storyline is -> {}'.format(avatar.storyline))
# print('\tavatar.poster_image_url  is -> {}'.format(avatar.poster_image_url))
# print('\tavatar.trailer_youtube_url is -> {}\n'.format(avatar.trailer_youtube_url))

# print('\tavatar is -> {}'.format(avatar))
# print ("\tavatar.__class__ is %s" % avatar.__class__)
# print ("\tavatar.__class__.__name__ is %s\n" % avatar.__class__.__name__)

# print('\tdir(avatar) is -> {}\n'.format(dir(avatar)))

# toy_story.show_trailer()

# def open_movies_page(movies):
# movies = [avatar, toy_story]

# fresh_tomatoes.open_movies_page(movies)

# toy_story.valid_ratings

# OK Access class variable in an instance  
print('\tclass variable toy_story.VALID_RATINGS are -> {}'.format(toy_story.VALID_RATINGS))

# OK Access class variable - note class name NOT instance name  
print('\tclass variable media.Movie.VALID_RATINGS are -> {}\n'.format(media.Movie.VALID_RATINGS))

print('\tclass variable media.Movie.__doc__ is -> {}'.format(media.Movie.__doc__))
print('\tclass variable media.Movie.__name__ is -> {}'.format(media.Movie.__name__))
print('\tclass variable media.Movie.__module__ is -> {}'.format(media.Movie.__module__))
print('\tclass variable media.Movie.__bases__ is -> {}\n'.format(media.Movie.__bases__))








                     



