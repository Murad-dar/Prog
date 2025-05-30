from parser import IMDBParser
from database import Database
from queries import (
    get_movies_with_directors,
    get_avg_rating_by_director,
    get_movies_count_by_year,
    get_total_duration_by_director,
    get_top_rated_movies
)

def main():
    # Инициализация парсера и БД
    parser = IMDBParser()
    db = Database()
    
    try:
        # Парсинг режиссёров
        directors = parser.parse_directors()
        db.insert_directors(directors)
        print(f"Добавлено {len(directors)} режиссёров")
        
        # Парсинг фильмов
        movies = parser.parse_movies()
        db.insert_movies(movies)
        print(f"Добавлено {len(movies)} фильмов")
        
        # Выполнение запросов
        print("\nРезультаты запросов:")
        
        # 1. JOIN: Фильмы с режиссёрами
        print("\n1. Фильмы с режиссёрами (первые 5):")
        query = get_movies_with_directors()
        print(query.get_sql())
        results = db.cursor.execute(query.get_sql()).fetchmany(5)
        for row in results:
            print(f"{row[0]} ({row[1]}) - {row[3]}, рейтинг: {row[2]}")
        
        # 2. JOIN: Средний рейтинг по режиссёрам (у которых >1 фильма)
        print("\n2. Средний рейтинг по режиссёрам:")
        query = get_avg_rating_by_director()
        print(query.get_sql())
        results = db.cursor.execute(query.get_sql()).fetchall()
        for row in results:
            print(f"{row[0]}: {row[1]:.1f}")
        
        # 3. Группировка: Количество фильмов по годам
        print("\n3. Количество фильмов по годам:")
        query = get_movies_count_by_year()
        print(query.get_sql())
        results = db.cursor.execute(query.get_sql()).fetchall()
        for row in results:
            print(f"{row[0]}: {row[1]} фильмов")
        
        # 4. JOIN: Общая продолжительность фильмов по режиссёрам
        print("\n4. Общая продолжительность по режиссёрам:")
        query = get_total_duration_by_director()
        print(query.get_sql())
        results = db.cursor.execute(query.get_sql()).fetchall()
        for row in results:
            print(f"{row[0]}: {row[1]} минут")
        
        # 5. Топ-5 фильмов по рейтингу
        print("\n5. Топ-5 фильмов по рейтингу:")
        query = get_top_rated_movies()
        print(query.get_sql())
        results = db.cursor.execute(query.get_sql()).fetchall()
        for row in results:
            print(f"{row[0]}: {row[1]}")
        
    finally:
        parser.close()
        db.close()

if __name__ == "__main__":
    main()