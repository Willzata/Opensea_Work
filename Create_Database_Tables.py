#Create the database

import sqlite3


path = '/mnt/c/Users/wmang/Python Stuff/Opensea_2/database/assets.db'

conn = sqlite3.connect(path)
print('Established Connection')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping Assets table if already exists.
cursor.execute("DROP TABLE IF EXISTS Assets")

#Creating table as per requirement
sql = '''CREATE TABLE Assets (
   id integer PRIMARY KEY,
   token_id integer,
   image_URL text,
   auction_URL text,
   asset_contract_type text,
   art_name text,
   artist_name text,
   twitter text,
   filepath text
)'''

cursor.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
