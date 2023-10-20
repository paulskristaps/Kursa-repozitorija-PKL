import sqlite3

#Izveidot savienojumu ar datubāzi

connection = sqlite3.connect("Webscraper/database.db")
cursor = connection.cursor()

#Izveido jaunu tabulu, ja tāda jau nēeksistē
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    title TEXT,
    rating REAL,
    price REAL
)''')

#Nolasa informāciju no faila, kur saglabāti web-skrapotie dati
with open('Webscraper/Bestselling items.txt', 'r') as file:
    data = file.readlines()

product_info = {}

#Izfiltrē ārā titulu, reiting un cenu, ieliek datubāzē
for line in data:
    if "out of" in line:
        rating = line.strip().split(" out of ")[0]
        if "rating" not in product_info:
            product_info["rating"] = rating
    elif "$" in line:
        price = line.strip().split("$")[1]
        if "price" not in product_info:
            product_info["price"] = price
    else:
        if len(line) <= 1:
            continue
        else:
            title = line.strip()
            product_info["title"] = title

    if len(product_info) == 3:
        title = product_info.get("title", "NONE SUPPLIED")
        rating = product_info.get("rating", "NONE SUPPLIED")
        price = product_info.get("price", "NONE SUPPLIED")

        cursor.execute("INSERT INTO products (title, rating, price) VALUES (?, ?, ?)", (title, rating, price))

        product_info = {}

#Saglabā un aizver savienojumu
connection.commit()
connection.close()
