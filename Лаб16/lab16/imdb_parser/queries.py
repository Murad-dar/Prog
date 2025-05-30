from pypika import Query, Table, functions as fn

def get_movies_with_directors():
    movies = Table('movies')
    directors = Table('directors')
    
    return (
        Query.from_(movies)
        .join(directors)
        .on(movies.director_id == directors.id)
        .select(movies.title, movies.year, movies.rating, directors.name.as_('director'))
        .orderby(movies.rating, order=Query.desc)
    )

def get_avg_rating_by_director():
    movies = Table('movies')
    directors = Table('directors')
    
    return (
        Query.from_(movies)
        .join(directors)
        .on(movies.director_id == directors.id)
        .groupby(directors.name)
        .select(directors.name, fn.Avg(movies.rating).as_('avg_rating'))
        .having(fn.Count(movies.id) > 1)
        .orderby(fn.Avg(movies.rating), order=Query.desc)
    )

def get_movies_count_by_year():
    movies = Table('movies')
    
    return (
        Query.from_(movies)
        .groupby(movies.year)
        .select(movies.year, fn.Count('*').as_('movies_count'))
        .orderby(movies.year)
    )

def get_total_duration_by_director():
    movies = Table('movies')
    directors = Table('directors')
    
    return (
        Query.from_(movies)
        .join(directors)
        .on(movies.director_id == directors.id)
        .groupby(directors.name)
        .select(directors.name, fn.Sum(movies.duration).as_('total_duration'))
        .orderby(fn.Sum(movies.duration), order=Query.desc)
    )

def get_top_rated_movies(limit=5):
    movies = Table('movies')
    
    return (
        Query.from_(movies)
        .select(movies.title, movies.rating)
        .orderby(movies.rating, order=Query.desc)
        .limit(limit)
    )