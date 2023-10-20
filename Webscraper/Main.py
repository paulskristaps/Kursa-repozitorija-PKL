import sqlite3

connection = sqlite3.connect("Webscraper/database.db")
cursor = connection.cursor()

#Paņem visu produktu informāciju no datubāzes
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# Izprintē informāciju
i = 0
for row in rows:
    i+= 1
    print("Product #" +str(i)+ " -- " + row[0] + " has a rating of " + str(row[1]) + ", and it costs $" + str(row[2]) +"\n")

connection.commit()
connection.close()