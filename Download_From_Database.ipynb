import sqlite3
import requests
import io 
from PIL import Image
import pathlib  
import hashlib

db_path = '/mnt/c/Users/wmang/Python Stuff/Opensea/Database/PC_Assets.db'

# This function will insert the data into the SQlite database.
def UpdateDB(processed_data): 
  #Connecting to sqlite
  conn = sqlite3.connect(db_path)

  #Creating a cursor object using the cursor() method
  curr = conn.cursor()

  a = processed_data['ids']
  b = processed_data['token_ids']
  c = processed_data['img_urls']
  d = processed_data['permalink_urls']
  e = processed_data['asset_contract_types']
  f = processed_data['art_name']
  g = processed_data['artist_name']
  h = processed_data['twitter']
  i = processed_data['filepath']


  SQL = "INSERT OR IGNORE INTO Assets_full (id,token_id,image_URL,auction_URL,asset_contract_type,art_name,artist_name,twitter,file_path) VALUES (?,?,?,?,?,?,?,?,?)"
  for z in range(len(a)):
    curr.execute(SQL, (a[z],b[z],c[z],d[z],e[z],f[z],g[z],h[z],i[z]))

  # Commit your changes in the database
  conn.commit()
  print("Records inserted........")
  
  # Closing the connection
  conn.close()

#This function will download the images from the URLs listed in the table, and assign them a 
#unique hash for the filepath. 
def DownloadImage(url):
  directory = '/mnt/c/Users/wmang/Python Stuff/Opensea/Images_New/Images'

   #Add content of link to a variable
  image_content = requests.get(url).content

    #creates a byte object out of image_content and point the variable image_file to it
  image_file = io.BytesIO(image_content)
    
    #use pillow to convert object to RGB img 
  image = Image.open(image_file).convert('RGB')
  
  #resize to 128,128 so embeddings can be taken
  image = image.resize((400,400), Image.ANTIALIAS)

  #create hash that can be used to refer back to image later(in DB)
  hash = hashlib.sha1(image_content).hexdigest()[:10]

  img_path = pathlib.Path(directory,hash + '.jpeg')

  #Image must be a jpeg...
  image.save(img_path,"JPEG",quality=80)

  #Convert from Path object to Str 
  img_path = str(img_path)

  return hash

# This function will insert the data into a new SQlite table, this time including the filepath.
#(If storage is an issue, can add code to delete existing table).
def UpdateDB(processed_data): 
  #Connecting to sqlite
  conn = sqlite3.connect(db_path)

  #Creating a cursor object using the cursor() method
  curr = conn.cursor()

  a = processed_data['ids']
  b = processed_data['token_ids']
  c = processed_data['img_urls']
  d = processed_data['permalink_urls']
  e = processed_data['asset_contract_types']
  f = processed_data['art_name']
  g = processed_data['artist_name']
  h = processed_data['twitter']
  i = processed_data['filepath']


  SQL = "INSERT OR IGNORE INTO Assets_full (id,token_id,image_URL,auction_URL,asset_contract_type,art_name,artist_name,twitter,filepath) VALUES (?,?,?,?,?,?,?,?,?)"
  for z in range(len(a)):
    curr.execute(SQL, (a[z],b[z],c[z],d[z],e[z],f[z],g[z],h[z],i[z]))

  # Commit your changes in the database
  conn.commit()
  print("Records inserted........")
  
  # Closing the connection
  conn.close()


#Function to retrieve data about a specific token_ID value from the first table in the database(no filepaths).
def RetrieveIDfromDB(token_id): 
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  cursor.execute(f'SELECT DISTINCT * FROM Assets WHERE token_id = {token_id}')
  results = cursor.fetchall()
  cursor.close()
  return results



def Script(id): 
  dataset = RetrieveIDfromDB(id)

  ##Data structure --> [0] = id(unique), [1] = token_id [2] = img_url 
  ##[3]= permalink [4] = asset type [5]= Art name [6]= Artist Name [7] = Twitter
  ##[8] = Filepath 

  img_urls= [] #Link to the image of the artwork being sold
  permalink_urls = [] #Link to the auction on opensea
  ids = [] #Unique identifier 
  token_ids = [] #Some other identifier (????)
  asset_contract_types = [] #Fungible / semi-fungible / non-fungible 
  art_name = []  #Artwork Name 
  artist_name = [] #Artist Name
  twitter = [] #Twitter Handle 
  filepath = [] #Filepath


  for data in dataset:
    #Use img_url to download image

    #PIL cannot support various formats so try
    try:
    #if "gif" not in data[2] and "gif" not in data[2] and "svg" not in data[2] and "json" not in data[2] and "webm" not in data[2]: 
      img_path = DownloadImage(data[2])

      #Append data to temp lists
      ids.append(data[0])
      token_ids.append(data[1])
      img_urls.append(data[2])
      permalink_urls.append(data[3])
      asset_contract_types.append(data[4])
      art_name.append(data[5])
      artist_name.append(data[6])
      twitter.append(data[7])
      filepath.append(img_path)
    except:
      continue


  #Convert this data to dict
  outdict = {'img_urls':img_urls,
             'permalink_urls':permalink_urls,
             'ids':ids,
             'token_ids':token_ids,
             'asset_contract_types':asset_contract_types,
             'art_name':art_name,
             'artist_name':artist_name,
             'twitter':twitter,
             'filepath':filepath
              }

  #Commit this data into a new table in database.
  UpdateDB(outdict)

  #Add one to counter and update counter document so next id can be read
  dir = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Database/DB_count.txt'
  next_id = id + 1
  UpdateCount(next_id,dir)
  return 

#These two functions serve to use counters to aid the script in case of timeout.
#They read and update an integer in a text file by 1, which serves as a counter.
dir = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Database/DB_count.txt'
def ReadCount(dir):
  with open(dir) as f:
      c = [int(x) for x in next(f).split()] # read first line
      c = c[0]
      f.close()
  return c

def UpdateCount(next_id,dir):
  with open(dir, 'r+') as f:
    f.truncate(0)
    f.write(str(next_id))
    f.close


def Main():
    ccc = 0
    working = True
    while working is True:
        id = ReadCount(dir)
        print(f"Downloading URLS from token_id: {id}")
        try:
            Script(id)
            ccc = 0 #Fail counter that will go to 3 before shutting script off. 
        except:
            ccc = ccc + 1
            if ccc == 3:
                working = False

if __name__ == '__main__':
    
  Main()

