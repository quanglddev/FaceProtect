import cv2

# importing os module  
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Path 
path = os.path.join(dir_path, "..", "images")

def takePictureUsingWebcam(personName):
    # Captures image and saves it in the images folder with the entered name (name.jpg)
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('o'):
            # FIXME: Add an inspector to check if image exists with same name.
            out = cv2.imwrite(os.path.join(path, ('%s.jpg' % (personName))), frame)
            return os.path.join(path, ('%s.jpg' % (personName)))
            
    cap.release()
    cv2.destroyAllWindows()
