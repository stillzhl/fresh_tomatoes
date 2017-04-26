#!/usr/bin/env python
# coding: utf-8

import httplib

# entertainment center
import entm_cnt

from flask import Flask

app = Flask(__name__) 


@app.route("/")
def fresh_tomatoes():
    return "index.html"


@app.route("/movie/<title>")
def movie(title):
    resource = None
    movie = entm_cnt.movies.get(title, None)
    if not movie:
        status_code = httplib.NOT_FOUND
    else:
        status_code = httplib.OK
        resource = movie.toJson()
    return resource


if __name__ == '__main__':
    app.run()
