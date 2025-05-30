from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    year: int
    rating: float
    duration: int  # в минутах
    director_id: int

@dataclass
class Director:
    id: int
    name: str