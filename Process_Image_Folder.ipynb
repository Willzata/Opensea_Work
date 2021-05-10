##For some reason in the database there will be various duplicates, and some files which may get corrupted during download etc.
#To counter this, we can iterate through the Assets_full table for filepath, and move these into a new folder if not None type.
#So we will create a new folder called Images_New or something similar to deposit these in. 


from PIL import Image
import sqlite3
import os
import shutil

#This shows the number of entries in both tables, will show a difference as certain 
#filetypes are not supported by our previous scripts.

conn = sqlite3.connect('/mnt/c/Users/wmang/Python Stuff/Opensea/Database/PC_Assets.db')
cursor = conn.cursor()
cursor.execute("select Distinct * from Assets")
results = cursor.fetchall()
cursor.execute("select Distinct  * from Assets_full")
results1 = cursor.fetchall()
print(len(results),len(results1))
cursor.close()


## This will give back the number of distinct results in both tables.
conn = sqlite3.connect('/mnt/c/Users/wmang/Python Stuff/Opensea/Database/PC_Assets.db')
cursor = conn.cursor()
cursor.execute("select Distinct * from Assets")
results = cursor.fetchall()
cursor.execute("select Distinct  * from Assets_full")
results1 = cursor.fetchall()
cursor.execute("select distinct filepath from Assets_full")
results2 = cursor.fetchall()
print("Number rows in Initial Table: Number of rows in Second Table(Downloaded) : Number of unique Filepaths in 2nd table")
print(len(results),len(results1),len(results2))
cursor.close()

## Append the pathnames from the distinct filepaths to a list. 
l1 = []
for i, m  in enumerate(results2):
    if m[i][0] is not None:
        l1.append(m[i][0])

#Move these Images to a seperate folder
for i in l1:
    im_path = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Images_New/Images/{i}.jpeg'
    new_path = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Images_New/Images_New/{i}.jpeg'
    shutil.move(im_path, new_path)
    
