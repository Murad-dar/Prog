import sqlite3
from typing import List
from models import Movie, Director

class Database:
    def __init__(self, db_name: str = 'imdb.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS directors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                year INTEGER NOT NULL,
                rating REAL NOT NULL,
                duration INTEGER NOT NULL,
                director_id INTEGER NOT NULL,
                FOREIGN KEY (director_id) REFERENCES directors (id)
            )
        ''')
        self.conn.commit()
    
    def insert_directors(self, directors: List[Director]):
        query = '''
            INSERT INTO directors (id, name)
            VALUES (:id, :name)
        '''
        self.cursor.executemany(query, [director.__dict__ for director in directors])
        self.conn.commit()
    
    def insert_movies(self, movies: List[Movie]):
        query = '''
            INSERT INTO movies (title, year, rating, duration, director_id)
            VALUES (:title, :year, :rating, :duration, :director_id)
        '''
        self.cursor.executemany(query, [movie.__dict__ for movie in movies])
        self.conn.commit()
    
    def close(self):
        self.conn.close()