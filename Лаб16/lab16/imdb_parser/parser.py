from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from models import Movie, Director
import time
from collections import defaultdict

class IMDBParser:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "https://www.imdb.com/chart/top/"
        self.directors_map = defaultdict(int)
        self.next_director_id = 1
    
    def parse_directors(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        
        directors = set()
        director_elements = self.driver.find_elements(By.XPATH, '//td[@class="titleColumn"]/a[@title]')
        
        for element in director_elements:
            director_name = element.get_attribute('title').split(' (dir.)')[0]
            directors.add(director_name)
        
        directors_list = []
        for name in directors:
            self.directors_map[name] = self.next_director_id
            directors_list.append(Director(id=self.next_director_id, name=name))
            self.next_director_id += 1
        
        return directors_list
    
    def parse_movies(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        
        movies = []
        movie_rows = self.driver.find_elements(By.XPATH, '//tbody[@class="lister-list"]/tr')
        
        for row in movie_rows[:50]:  # парсим только 50 фильмов для примера
            title = row.find_element(By.XPATH, './/td[@class="titleColumn"]/a').text
            year = int(row.find_element(By.XPATH, './/td[@class="titleColumn"]/span').text[1:-1])
            rating = float(row.find_element(By.XPATH, './/td[@class="ratingColumn imdbRating"]/strong').text)
            director_name = row.find_element(By.XPATH, './/td[@class="titleColumn"]/a[@title]').get_attribute('title').split(' (dir.)')[0]
            
            # Переходим на страницу фильма для получения продолжительности
            movie_link = row.find_element(By.XPATH, './/td[@class="titleColumn"]/a').get_attribute('href')
            duration = self._get_movie_duration(movie_link)
            
            movies.append(Movie(
                title=title,
                year=year,
                rating=rating,
                duration=duration,
                director_id=self.directors_map[director_name]
            ))
        
        return movies
    
    def _get_movie_duration(self, url):
        self.driver.get(url)
        time.sleep(2)
        
        try:
            duration_text = self.driver.find_element(By.XPATH, '//li[@data-testid="title-techspec_runtime"]/div').text
            duration = int(duration_text.split(' ')[0])
        except:
            duration = 0
        
        return duration
    
    def close(self):
        self.driver.close()