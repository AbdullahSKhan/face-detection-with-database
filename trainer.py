import os
import cv2
import numpy as np
from PIL import Image
recognizer=cv2.createLBPHFaceRecognizer();
path='dataSet'

def getimages(path):
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagepath in imagepaths:
        faceImg=Image.open(imagepath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(faceNp)
        print ID
        IDs.append(ID)
        cv2.imshow("trainers",faceNp)
        cv2.waitKey(10)
    return IDs, faces

Ids,faces=getimages(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
