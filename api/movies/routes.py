from flask import Blueprint, render_template, request
from api.models import Movie

movies = Blueprint('movies', __name__)


@movies.route('/movie/<title>', methods=['GET','POST'])
def show_movie(title):
    movie = Movie.query.filter_by(title=title).first_or_404()
    print(movie)
    return render_template('movie.html', movie=movie)


@movies.route('/movies', methods=['GET','POST'])
def show_all_movie():
    movie = Movie.query.all()
    return render_template('all_movies.html', movie=movie)