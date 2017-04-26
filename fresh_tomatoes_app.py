#!/usr/bin/env python
# coding: utf-8

import httplib

from entertainment import movies

from flask import Flask
from flask import render_template

app = Flask(__name__) 


@app.route("/")
def fresh_tomatoes():
    return render_template("index.html")


@app.route("/movie/<title>")
def movie(title):
    resource = None
    movie = movies.get(title, None)
    if not movie:
        status_code = httplib.NOT_FOUND
    else:
        status_code = httplib.OK
        resource = movie.toJson()
    return resource


if __name__ == '__main__':
    app.run()
