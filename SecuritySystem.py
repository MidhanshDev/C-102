from os import access
import cv2
import random
import time
import dropbox
startTime=time.time()
def take_snapshot():
    number = random.randint(0,100)
    #Initializing cv2
    vcobj = cv2.VideoCapture(0)
    result = True
    while result:
        #Read the frames while the camera is on
        ret,frame = vcobj.read()
        imgName = "img"+str(number)+".jpg"

        print(ret)
        #cv2.imwrite()method is used to save an image to any storage device
        cv2.imwrite(imgName, frame)
        startTime=time.time
        result = False
    
    return imgName
    print("Snapshot taken")

    #Release the camera
    vcobj.release()
    #Close all the windows that might be opened while this process
    cv2.destroyAllWindows()
    
def uploadFiles(imgName):
    access_token = "sl.AzhdBzuwKG7tGIUBhwRwc7Upwtvq3LQxDXkG8iqtfB7TMt9FaI7dycD8-MDecchjkADwUxu1wGLWLXxgJW_JfWStIlilcZyjDjrhWc8c3C3kmz1aFZcil2mPqqgguq67bFQgSb4"
    file_from = imgName
    file_to = "/midhansh/captures/"+imgName
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while True:
        if time.time()-startTime>=300:
            name = take_snapshot()
            uploadFiles(name)
            
main()
