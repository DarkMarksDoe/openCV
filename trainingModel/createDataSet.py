import glob
import os
import cv2 as cv
import numpy as np
from PIL import Image

recognizer = cv.face.LBPHFaceRecognizer_create()
globalpath = "./lfw"


def addImages(globalpath):
    images = []
    for fname in globalpath:
        print(globalpath + "/" + fname)
        images.append(np.array(Image.open(globalpath + "/" + fname)))
    train = np.array(images)

def getImageWithID(globalpath):
    imagePaths = [os.path.join(globalpath, f) for f in os.listdir(globalpath)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        try:
            facesImg = Image.open(imagePath)
            faceNP = np.array(facesImg, '.jpg')
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(faceNP)
            Ids.append(ID)
            cv.imshow("Adding faces for training ", faceNP)
            print('Ready!')
            cv.waitKey(10)
            return np.array(Ids), faces
        except Exception as e:
            s = str(e)
            print(s)


addImages(globalpath)
# Ids, faces = getImageWithID(globalpath)
# recognizer.train(faces, Ids)
# recognizer.save("images/trainingData.yml")
cv.destroyAllWindows()
