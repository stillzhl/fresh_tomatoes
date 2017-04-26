# coding: utf-8

import json
import re


class Movie:
    """ The movie that I love :)

    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """ the constructor.

        :param str title: the movie title
        :param str poster_image_url: the image url of poster of movie
        :param str trailer_youtube_url: the youtube url of the movie trailer
        """
        self.title = title
        self.poster_image = poster_image_url
        self.trailer_youtube = self.__ext_embed_id(trailer_youtube_url)

    def __ext_embed_id(self, youtube_url):
        """ Extract the id for embedding a youtube audio to a frame.

        :param str youtube_url: the youtube url of the movie trailer
        :return str youtube_id: the id of the youtube audio
        """
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        return trailer_youtube_id


    def toJson(self):
        movie_dict = {'title': self.title,
                      'poster_image': self.poster_image,
                      'trailer_youtube': self.trailer_youtube}
        return json.dumps(movie_dict)


movies = dict()
title = 'Blue Velvet'
movies[title] = Movie(title,
                      "http://dl9fvu4r30qs1.cloudfront.net/f3/fa/adf49af84d49ad18a041a74b458f/blue-velvet-30th-anniversary-poster.jpg",
                      "https://www.youtube.com/watch?v=k_BybDB_phY")

title = "The Social Network"
movies[title] = Movie(title,
                      "http://fr.web.img2.acsta.net/medias/nmedia/18/78/52/54/19534550.jpg",
                      "https://www.youtube.com/watch?v=lB95KLmpLR4")

title = "Matrix"
movies[title] = Movie(title,
                     "http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=kYzz0FSgpSU")
