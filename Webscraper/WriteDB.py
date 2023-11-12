import mysql.connector

#Izveidot savienojumu ar datubāzi

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="data"
)

# connection = sqlite3.connect("Webscraper/database.db")
cursor = mydb.cursor()

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
            product_info["rating"] = float(rating)
    elif "$" in line:
        price = line.strip().split("$")[1]
        if "price" not in product_info:
            product_info["price"] = float(price)
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

        cursor.execute("INSERT INTO products (title, rating, price) VALUES (%s, %s, %s)", (title, rating, price))

        product_info = {}

#Saglabā un aizver savienojumu
mydb.commit()
mydb.close()
cursor.close()
