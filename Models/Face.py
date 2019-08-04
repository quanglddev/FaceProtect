class Face:
    def __init__(self, imagePath, full_name):
        self.imagePath = imagePath
        self.full_name = full_name

    # def load_image_file(self):
    #     return face_recognition.load_image_file(self.imagePath)

    # def face_encoding(self):
    #     return face_recognition.face_encodings(self.load_image_file())[0]

    def getName(self):
        return self.full_name