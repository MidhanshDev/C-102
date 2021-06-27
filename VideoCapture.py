import cv2

def take_snapshot():
    #Initializing cv2
    vcobj = cv2.VideoCapture(0)
    result = True
    while result:
        #Read the frames while the camera is on
        ret,frame = vcobj.read()
        print(ret)
        #cv2.imwrite()method is used to save an image to any storage device
        cv2.imwrite("newpic.jpg", frame)
        result = False

    #Release the camera
    vcobj.release()
    #Close all the windows that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()
