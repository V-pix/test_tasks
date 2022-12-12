import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    city_id INTEGER
);
''')

cur.execute('''     
CREATE TABLE IF NOT EXISTS cities(
    id INTEGER PRIMARY KEY,
    name TEXT
);
''')

con.commit()

customers = [
    (1, 'Иванов', 3),
    (2, 'Пановко', 2),
    (3, 'Черненко', 3),
    (4, 'Пановко', 2),
    (5, 'Иванова', 1),
]
cities = [
    (1, 'Москва'),
    (2, 'Санкт-Петербург'),
    (3, 'Пермь'),
    (4, 'Воронеж'),
    (5, 'Липецк'),
]

# cur.executemany('INSERT INTO customers VALUES(?, ?, ?);', customers)
# cur.executemany('INSERT INTO cities VALUES(?, ?);', cities)

# con.commit()
# con.close()

cur.execute('''
SELECT name, 
    city_id
FROM customers
UNION ALL
SELECT id, 
    name
FROM cities;
''')

for result in cur:
    print(result)

con.close()