import sqlite3

# Data from the provided table
landing_data = [
    {"spacecraft_name": "Луна-9", "country": "СССР", "landing_date": "1966-02-03", "site_name": "Океан Бурь"},
    {"spacecraft_name": "Сервейер-1", "country": "США", "landing_date": "1966-06-02", "site_name": "Океан Бурь"},
    {"spacecraft_name": "Луна-13", "country": "СССР", "landing_date": "1966-12-24", "site_name": "Океан Бурь"},
    {"spacecraft_name": "Сервейер-3", "country": "США", "landing_date": "1967-04-20", "site_name": "Океан Бурь"},
    {"spacecraft_name": "Сервейер-5", "country": "США", "landing_date": "1967-09-11", "site_name": "Море Спокойствия"},
    {"spacecraft_name": "Сервейер-6", "country": "США", "landing_date": "1967-11-10", "site_name": "Центральный Залив"},
    {"spacecraft_name": "Сервейер-7", "country": "США", "landing_date": "1968-01-10", "site_name": "Кратер Тихо"},
    {"spacecraft_name": "Луна-16", "country": "СССР", "landing_date": "1970-09-20", "site_name": "Море Изобилия"},
    {"spacecraft_name": "Луна-17", "country": "СССР", "landing_date": "1970-10-17", "site_name": "Море Дождей"},
    {"spacecraft_name": "Луна-20", "country": "СССР", "landing_date": "1972-02-21", "site_name": "Море Изобилия"},
    {"spacecraft_name": "Луна-21", "country": "СССР", "landing_date": "1973-01-15", "site_name": "Кратер Лемонье"},
    {"spacecraft_name": "Луна-23", "country": "СССР", "landing_date": "1974-11-06", "site_name": "Море Кризисов"},
    {"spacecraft_name": "Луна-24", "country": "СССР", "landing_date": "1976-08-18", "site_name": "Море Кризисов"},
    {"spacecraft_name": "Чанъэ-3", "country": "Китай", "landing_date": "2013-12-14", "site_name": "Залив Радуги"},
    {"spacecraft_name": "Чанъэ-4", "country": "Китай", "landing_date": "2019-01-03", "site_name": "Кратер Кармана"},
    {"spacecraft_name": "Чанъэ-5", "country": "Китай", "landing_date": "2020-12-01", "site_name": "Океан Бурь"},
    {"spacecraft_name": "Чандраян-3", "country": "Индия", "landing_date": "2023-08-23", "site_name": "Полярный регион"},
    {"spacecraft_name": "SLIM", "country": "Япония", "landing_date": "2024-01-19", "site_name": "Кратер Кирилл"},
    {"spacecraft_name": "Одиссей", "country": "США", "landing_date": "2024-02-23", "site_name": "Кратер Малаперт"},
]

# Connect to SQLite database
conn = sqlite3.connect('moon_landings.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT UNIQUE
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Spacecraft (
    spacecraft_id INTEGER PRIMARY KEY AUTOINCREMENT,
    spacecraft_name TEXT,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS LandingSites (
    site_id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_name TEXT UNIQUE
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Landings (
    landing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    spacecraft_id INTEGER,
    site_id INTEGER,
    landing_date DATE,
    FOREIGN KEY (spacecraft_id) REFERENCES Spacecraft(spacecraft_id),
    FOREIGN KEY (site_id) REFERENCES LandingSites(site_id)
)''')

# Dictionaries to store IDs
countries = {}
sites = {}

# Insert data into tables
for entry in landing_data:
    # Insert or get country_id
    country_name = entry["country"]
    if country_name not in countries:
        cursor.execute("INSERT OR IGNORE INTO Countries (country_name) VALUES (?)", (country_name,))
        cursor.execute("SELECT country_id FROM Countries WHERE country_name = ?", (country_name,))
        countries[country_name] = cursor.fetchone()[0]
    
    # Insert or get site_id
    site_name = entry["site_name"]
    if site_name not in sites:
        cursor.execute("INSERT OR IGNORE INTO LandingSites (site_name) VALUES (?)", (site_name,))
        cursor.execute("SELECT site_id FROM LandingSites WHERE site_name = ?", (site_name,))
        sites[site_name] = cursor.fetchone()[0]
    
    # Insert spacecraft
    cursor.execute("INSERT INTO Spacecraft (spacecraft_name, country_id) VALUES (?, ?)",
                   (entry["spacecraft_name"], countries[country_name]))
    spacecraft_id = cursor.lastrowid
    
    # Insert landing
    cursor.execute("INSERT INTO Landings (spacecraft_id, site_id, landing_date) VALUES (?, ?, ?)",
                   (spacecraft_id, sites[site_name], entry["landing_date"]))

# Commit changes
conn.commit()

# Execute SQL queries
# Query 1: Top 5 countries by number of landings
print("Топ 5 стран по числу прилунений:")
cursor.execute('''SELECT c.country_name, COUNT(l.landing_id) as num_landings
                  FROM Countries c
                  JOIN Spacecraft s ON c.country_id = s.country_id
                  JOIN Landings l ON s.spacecraft_id = l.spacecraft_id
                  GROUP BY c.country_name
                  ORDER BY num_landings DESC
                  LIMIT 5''')
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} прилунений")

# Query 2: Landings grouped by countries
print("\nПрилунения с группировкой по странам:")
cursor.execute('''SELECT c.country_name, s.spacecraft_name, l.landing_date, ls.site_name
                  FROM Countries c
                  JOIN Spacecraft s ON c.country_id = s.country_id
                  JOIN Landings l ON s.spacecraft_id = l.spacecraft_id
                  JOIN LandingSites ls ON l.site_id = ls.site_id
                  ORDER BY c.country_name, l.landing_date''')
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} прилунился {row[2]} в {row[3]}")

# Query 3: Landings grouped by sites
print("\nПрилунения с группировкой по местам:")
cursor.execute('''SELECT ls.site_name, s.spacecraft_name, l.landing_date, c.country_name
                  FROM LandingSites ls
                  JOIN Landings l ON ls.site_id = l.site_id
                  JOIN Spacecraft s ON l.spacecraft_id = s.spacecraft_id
                  JOIN Countries c ON s.country_id = c.country_id
                  ORDER BY ls.site_name, l.landing_date''')
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} прилунился {row[2]} ({row[3]})")

# Close connection
conn.close()