#The API can return the same image twice, 
#Create the database

import sqlite3

path = 'db_path'
conn = sqlite3.connect(path)
print('Established Connection')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping Assets table if already exists.
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
   twitter text
   #filepath text
)'''

cursor.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()


#Create the second database table, containing the filepath 
path = 'db_path'
conn = sqlite3.connect(path)
print('Established Connection')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping Assets_full table if already exists.
cursor.execute("DROP TABLE IF EXISTS Assets_full")

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
