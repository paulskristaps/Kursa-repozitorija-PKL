import mysql.connector
import logging
import logging.config
import yaml
import os

#atver konfigurācijas failu
with open("Webscraper/logging_config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

logging.config.dictConfig(config)

logger = logging.getLogger("my_logger")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="data"
)

cursor = mydb.cursor()

#Paņem visu produktu informāciju no datubāzes
logger.debug("Selecting data from DB...")
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# Loggo informāciju
i = 0
for row in rows:
    i+= 1
    logger.info("Product #" +str(i)+ " -- " + row[0] + " has a rating of " + str(row[1]) + ", and it costs $" + str(row[2]) +"\n")

logger.debug("COMPLETED!")

with open("Webscraper/logfile.log", "r") as printout:
    for row in printout:
        print(row)

mydb.commit()
mydb.close()

cursor.close()