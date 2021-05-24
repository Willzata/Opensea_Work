#Importing libraries
import requests 
import requests 
import sqlite3
from PIL import Image
import pathlib  
import hashlib
import io 


#Setting API URL
url = "https://api.opensea.io/api/v1/assets"
#Function to get a set of data from the API 
def GetApiData(offset,limit,id):
  #Arguments for API request
  #In this instance returning in order of token-id, starting from 0.
  #Max limit is 50, max offset is 10,000.

  querystring = {"order_direction":"asc",
                 "offset":offset,
                 "limit":limit,
                 "token_ids":id
                 } 

  #Carry out request 
  response = requests.request("GET", url, params=querystring)

  #Convert to .json
  response_data = response.json()

  #Useful data in an array named 'assets'
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
            'twitter':twitter
            }      

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
  else: #This means there are no nested lists present
      output = input
      return output

  while NoNestedLists is False:
    #remove nestings from all the lists. (These nested lists arrise during the iteration of offset)
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
            'twitter':twitter
            }

  return output




def DownloadImage(url):
  directory = r'/mnt/c/Users/wmang/Python Stuff/Opensea_2/images/images'

  #Add content of link to a variable
  image_content = requests.get(url).content

  #creates a byte object out of image_content and point the variable image_file to it
  image_file = io.BytesIO(image_content)
    
  #use pillow to convert object to RGB img 
  image = Image.open(image_file).convert('RGB')
  
  #resize all images to equal size, so embeddings can be taken
  image = image.resize((128,128), Image.ANTIALIAS)

  #create hash that can be used to refer back to image later(in DB)
  hash = hashlib.sha1(image_content).hexdigest()[:12]
  img_path = pathlib.Path(directory,hash + '.jpeg')

  #Image must be a jpeg...
  image.save(img_path,"JPEG",quality=90)

  #Convert from Path object to Str 
  img_path = str(img_path)

  return hash #The name of the image in the image directory 


def AddFilePathsToDictAndDownload(data):
    #Some filetypes are unable to be processed via the PIL process above. Therefore an error will ge thrown up
    #And the process will not work, so must 'try' each image url.
    a1,b1,c1,d1,e1,f1,g1,h1,i1 = [],[],[],[],[],[],[],[],[]
    print(f"This token_id returned {len(data['img_urls'])} URLs to try and download... ")


    for index,z in enumerate(data['img_urls']):
        try:
            hash = DownloadImage(z)
            if hash is not None:
                a1.append(data['ids'][index])
                b1.append(data['token_ids'][index])
                c1.append(data['img_urls'][index])
                d1.append(data['permalink_urls'][index])
                e1.append(data['asset_contract_types'][index])
                f1.append(data['art_name'][index])
                g1.append(data['artist_name'][index])
                h1.append(data['twitter'][index])
                i1.append(hash)
        except:
            continue
    print(f"{len(a1)} URLs returned valid images, these are now saved to disc...")    
    output = {'img_urls':c1,
            'permalink_urls':d1,
            'ids':a1,
            'token_ids':b1,
            'asset_contract_types':e1,
            'art_name':f1,
            'artist_name':g1,
            'twitter':h1,
            'filepath':i1 
            }      

    return output




# This function will insert the data into the SQlite database.
def CommitToDb(processed_data): 
  #Connecting to sqlite
  conn = sqlite3.connect(r'/mnt/c/Users/wmang/Python Stuff/Opensea_2/database/assets.db')

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

  SQL = "INSERT OR IGNORE INTO Assets (id,token_id,image_URL,auction_URL,asset_contract_type,art_name,artist_name,twitter,filepath) VALUES (?,?,?,?,?,?,?,?,?)"
  for z in range(len(a)):
    curr.execute(SQL, (a[z],b[z],c[z],d[z],e[z],f[z],g[z],h[z],i[z]))

  # Commit your changes in the database
  conn.commit()
  print("Records inserted........")
  
  # Closing the connection
  conn.close()

   

dir = r'/mnt/c/Users/wmang/Python Stuff/Opensea_2/database/count.txt'
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

#This runs through each offset possible (max 10,000) for a given ID. 
#Then calls the checknesting function to ensure no list nestings exist.
#Then calls the CommitToDB function to put all of that data into DB.
def IDtoDB(id):
  
  input = IterateOffset(id)

  data = CheckNestings(input)
  print("Downloading....")
  processed_data = AddFilePathsToDictAndDownload(data)
  CommitToDb(processed_data)

  id = ReadCount(dir)
  next_id = id+1
  UpdateCount(next_id,dir)





def Main():
  working = True
  fail_counter = 0
  while working is True:
    id = ReadCount(dir)
    print(f"Trying to retrieve token_ID: {id} ")
    try:
      IDtoDB(id)
      fail_counter = 0
    except:
      print(f"This program failed on token_ID: {id}")
      fail_counter = fail_counter + 1
      if fail_counter == 5:
        working = False


if __name__ == '__main__':
    Main()
    
