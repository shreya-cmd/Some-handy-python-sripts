import os
import cv2

data = "D:/shreya/datasets/kth dataset" #directory to your dataset 
listing = os.listdir(data)
count = 0
index = 0
for folder in listing: #looping through different classes
    os.makedirs("data_frames/"+ folder+"/") #directory to store video frames of each class
    for videoname in os.listdir(data + str("/") + folder): 
        video = cv2.VideoCapture(data + str("/") + folder + "/" + videoname) #capturing video
        framerate = 1 #it will capture frames in every 1 second
        index=50 #index is the number of frames
        os.makedirs("data_frames/" + folder+"/"+videoname.replace(".avi","")) #creating a folder to store frames of each video inside the class folder
        while(index>0):
            # Extract images
            ret, frame = video.read()
            # end of frames
            if not ret: 
                break
            # Saves images
            name =  "data_frames/" + folder+"/"+videoname.replace(".avi","")+"/"+videoname.replace('.avi', '')+ '_' + str(index) + '.jpg'
            cv2.imwrite(name, frame)
        #video.release()
            print('done')
            # next frame
            index -=1