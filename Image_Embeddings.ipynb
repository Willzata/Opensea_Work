import image_embeddings #Will only run on linux 

path_images = r'/mnt/c/Users/wmang/Python Stuff/Opensea/Images_New/Images_New'
path_tfrecords = r'/mnt/c/Users/wmang/Python Stuff/Opensea/Images_New/TF_Records'
path_embeddings = r'/mnt/c/Users/wmang/Python Stuff/Opensea/Images_New/Embeddings'


#Write as tf record 
image_embeddings.inference.write_tfrecord(image_folder=path_images,
                                          output_folder=path_tfrecords,
                                          num_shards=10)
#Create inferences
image_embeddings.inference.run_inference(tfrecords_folder=path_tfrecords,
                                         output_folder=path_embeddings,
                                         batch_size=100)

#Build Faiss Index
[id_to_name, name_to_id, embeddings] = image_embeddings.knn.read_embeddings(path_embeddings)
index = image_embeddings.knn.build_index(embeddings)

#Pick a random index value --> display other images in folder with similar embeddings
p = 10111

print(id_to_name[p]) #displays the Hash name of that image, allows it to be referenced later if need be. 

image_embeddings.knn.display_picture(path_images, id_to_name[p])

results = image_embeddings.knn.search(index, id_to_name, embeddings[p])

image_embeddings.knn.display_results(path_images, results)


#Insert user Image here
path_user_image = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Images/User_Image'
path_user_image_tf = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Images/User_TF_Record'
path_user_image_embedding = f'/mnt/c/Users/wmang/Python Stuff/Opensea/Images/User_Embeddings'
#Create tf record for user image
image_embeddings.inference.write_tfrecord(image_folder=path_user_image,
                                          output_folder=path_user_image_tf,
                                          num_shards=1)
#Create embedding for user image
image_embeddings.inference.run_inference(tfrecords_folder=path_user_image_tf,
                                         output_folder=path_user_image_embedding,
                                         batch_size=1)
#Create index for user image
[user_image_id_to_name, user_image_name_to_id, user_image_embedding] = image_embeddings.knn.read_embeddings(path_user_image_embedding)
user_image_index = image_embeddings.knn.build_index(user_image_embedding)

#Compare the User image to the other Images in the database.
p=0#Display the user image
image_embeddings.knn.display_picture(path_user_image, user_image_id_to_name[p])

k_nearest = 5 #How many neighbours do you want


#Find similar embeddings in the main index
user_image_results = image_embeddings.knn.search(index, id_to_name, user_image_embedding[p],k=k_nearest)

#Display the k nearest neighbours from main index
image_embeddings.knn.display_results(path_images, user_image_results)
