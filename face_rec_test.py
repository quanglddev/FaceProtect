import face_recognition
import cv2
import numpy as np
import sys
import json

# NOTE: We could use packages for keyboard input (like "from pynput.keyboard import Key, Controller")
# NOTE: Press o to capture image, q to end face recognition


class faces:
    def __init__(self, imageLocation, name):
        self._imageLocation = imageLocation
        self._personName = name

    def load_image_file(self):
        return face_recognition.load_image_file(self._imageLocation)

    def face_encoding(self):
        return face_recognition.face_encodings(self.load_image_file())[0]

    def getName(self):
        return self._personName


def initializeFaceRecognition():
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        # print("ret", ret)
        # print("frame", frame)

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    knownFaceEncodings, face_encoding)
                name = "Unknown"

                # # If a match was found in knownFaceEncodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    knownFaceEncodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = knownFaceNames[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        imS = cv2.resize(frame, (960, 540))
        cv2.imshow('Video', imS)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


def getInput():
    print("Select from the actions below:")
    print("(a) Add data")
    print("(b) Start Face Recog")
    print("(c) Exit")
    inp = input("Enter a, b or c:\n").strip().lower()
    return inp


def getData():
    name = input("Enter name of the person whose data is to be entered.\n")
    getImage(name)
    # creating new object of face class and encoding the new image
    newImage = faces("images/%s.jpg" % (name), name)
    # adding the encoding and name to knownFaceEncodings and knownFaceNames lists.
    knownFaceEncodings.append(newImage.face_encoding())
    knownFaceNames.append(newImage.getName())
    initializeFaceRecognition()


def getImage(name):
    # captures image and saves it in the images folder with the entered name (name.jpg)
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('o'):
            # FIXME: Add an inspector to check if image exists with same name.
            out = cv2.imwrite('images/%s.jpg' % (name), frame)
            break

    cap.release()
    cv2.destroyAllWindows()


def takeAction(input):
    if input == 'a':
        getData()
    elif input == 'b':
        initializeFaceRecognition()
    elif input == 'c':
        sys.exit()
    else:
        print("Please enter the correct choice")
        inp = getInput()
        takeAction(inp)


if __name__ == "__main__":
    # FIXME: The datastructure is list and the program does not read form the images folder itself. The program should be able to read data from the images folder itself.
    obama = faces("images/obama.jpg", "Obama")
    quang = faces("images/quang.jpg", "Quang")
    knownFaceEncodings = [obama.face_encoding(), quang.face_encoding()]
    knownFaceNames = [obama.getName(), quang.getName()]
    # print(knownFaceEncodings[0])
    inp = ""
    while inp != "exit":
        inp = getInput()
        takeAction(inp)
