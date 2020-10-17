from api.models import Movie


def test_movies_should_be_in_db():
       movies = Movie.query.all()
       assert len(movies) != 0
