#Setting API URL and importing library 
import requests 
url = "https://api.opensea.io/api/v1/assets"

#Function to get a set of data from the API 
def GetApiData(offset,limit,id):
  #Arguments include offset and limit(number of requests returned)
  querystring = {"order_direction":"asc",
                 "offset":offset,
                 "limit":limit,
                 "token_ids":id
                 } 

  #Carry out request 
  response = requests.request("GET", url, params=querystring)

  #Convert to .json
  response_data = response.json()

  #Find useful data
  data = response_data['assets']
  
  #Turn data to a list and split so each part of request is accessible 
  data = list(map(str,data))
  for i in range(len(data)):
    data[i] = data[i].split(",")
  
  #When commas are found in the description this makes a new row. We must delete 
  for i in range(len(data)):
    if data[i][12][2:15] == "external_link":
      continue
    else:
      for j in range(len(data[i])):
        if data[i][j][2:15] == "external_link":
          tmp = j
          while tmp != 12:
            del data[i][tmp-2]
            tmp = tmp - 1 
          break
      continue
  #For some reason the description comes up twice, so must be deleted again so 
  #we can consistently get the correct permalink data 
  for i in range(len(data)):
    if  "permalink" in data[i][40]:
      continue
    else:
      for j in range(len(data[i])):
        if data[i][j][2:11] == "permalink":
          tmp = j
          while tmp != 40:
            del data[i][tmp-1]
            tmp = tmp - 1 
          break
      continue

  return data



def GetUrls(data):
  img_urls= [] #Link to the image of the artwork being sold
  permalink_urls = [] #Link to the auction on opensea
  ids = [] #Unique identifier 
  token_ids = [] #Some other identifier (????)
  asset_contract_types = [] #Fungible / semi-fungible / non-fungible 
  art_name = []  #Artwork Name 
  artist_name = [] #Artist Name
  twitter = [] #Twitter Handle 
  

  #Finds assets that we want to scrape within the API dataset. 

  for i in range(len(data)):
    if "https" in data[i][4] and ".mp4" not in data[i][4]:
      if "permalink" in data[i][40] and "assets" in data[i][40]:

        #append img_url links
        img_urls.append(data[i][4][15:-1])
        
        #append permalinks
        permalink_urls.append(data[i][40][15:-1])
        
        #append ids
        ids.append(int(data[i][0][7:-1]))

        #append token_ids
        token_ids.append(int(data[i][1][14:-1]))

        #append contract type
        asset_contract_types.append(data[i][14][25:-1])

        #append art name
        art_name.append(data[i][10][10:-1])

        #append artist name
        artist_name.append(data[i][16][10:-1])

        #append twitter username 
        for j in range(len(data[i])):
          if "twitter_username" in data[i][j]:
            twitter.append(data[i][j][21:-1])
    else:
      continue

  output = {'img_urls':img_urls,
            'permalink_urls':permalink_urls,
            'ids':ids,
            'token_ids':token_ids,
            'asset_contract_types':asset_contract_types,
            'art_name':art_name,
            'artist_name':artist_name,
            'twitter':twitter} 

  return output 

def IterateOffset(id):
  start = 0
  stop = 10000
  num_vals = 200
  delta = int((stop-start)/(num_vals-1))
  fifty_list = [start + i * delta for i in range(num_vals)]

  img_urls= [] #Link to the image of the artwork being sold
  permalink_urls = [] #Link to the auction on opensea
  ids = [] #Unique identifier 
  token_ids = [] #Some other identifier (????)
  asset_contract_types = [] #Fungible / semi-fungible / non-fungible 
  art_name = []  #Artwork Name 
  artist_name = [] #Artist Name
  twitter = [] #Twitter Handle 


  for offset in fifty_list:
    try:
        input = GetUrls(GetApiData(offset,50,id))

        img_urls.append(input['img_urls'])
        permalink_urls.append(input['permalink_urls'])
        ids.append(input['ids'])
        token_ids.append(input['token_ids'])
        asset_contract_types.append(input['asset_contract_types'])
        art_name.append(input['art_name'])
        artist_name.append(input['artist_name'])
        twitter.append(input['twitter'])

    except:
      break
    
  output = {'img_urls':img_urls,
            'permalink_urls':permalink_urls,
            'ids':ids,
            'token_ids':token_ids,
            'asset_contract_types':asset_contract_types,
            'art_name':art_name,
            'artist_name':artist_name,
            'twitter':twitter
             } 

  return output
# function used for removing nested 
# lists in python. 
def RemoveNestings(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return flat_list

#Function to check if the lists have nestings     
def CheckNestings(input):

  if type(input['img_urls'][0]) == list:   
    NoNestedLists = False


  while NoNestedLists is False:

    img_urls = RemoveNestings(input['img_urls'])
    permalink_urls = RemoveNestings(input['permalink_urls'])
    ids = RemoveNestings(input['ids'])
    token_ids = RemoveNestings(input['token_ids'])
    asset_contract_types = RemoveNestings(input['asset_contract_types'])
    art_name =  RemoveNestings(input['art_name'])
    artist_name = RemoveNestings(input['artist_name'])
    twitter =  RemoveNestings(input['twitter'])

    if type(img_urls[0]) == list:
      NoNestedLists = False
    else:
      NoNestedLists = True

  output = {'img_urls':img_urls,
            'permalink_urls':permalink_urls,
            'ids':ids,
            'token_ids':token_ids,
            'asset_contract_types':asset_contract_types,
            'art_name':art_name,
            'artist_name':artist_name,
            'twitter':twitter}

  return output



import sqlite3

# This function will insert the data into the SQlite database.
def CommitToDb(processed_data): 
  #Connecting to sqlite
  conn = sqlite3.connect('/mnt/c/Users/wmang/Python Stuff/Opensea/Database/PC_Assets.db')

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


  SQL = "INSERT OR IGNORE INTO Assets (id,token_id,image_URL,auction_URL,asset_contract_type,art_name,artist_name,twitter) VALUES (?,?,?,?,?,?,?,?)"
  for i in range(len(a)):
    curr.execute(SQL, (a[i],b[i],c[i],d[i],e[i],f[i],g[i],h[i]))

  # Commit your changes in the database
  conn.commit()
  print("Records inserted........")
  
  # Closing the connection
  conn.close()

#This runs through each offset possible (max 10,000) for a given ID. 
#Then calls the checknesting function to ensure no list nestings exist.
#Then calls the CommitToDB function to put all of that data into DB.
def IDtoDB(id):
  
  input = IterateOffset(id)

  processed_data = CheckNestings(input)


  l = len(processed_data['img_urls'])

  print(f"ID {id} returned {l} images. Attempting to commit to DB... ")
  

  CommitToDb(processed_data)

 

dir = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Database/count.txt'
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
