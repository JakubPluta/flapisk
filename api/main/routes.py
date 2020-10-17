from flask import Blueprint, render_template, request
from api.models import Movie

main = Blueprint('main', __name__)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/')
@main.route("/home")
def home():
    movie = Movie.query.all()
    return render_template('home.html', movie=movie)
