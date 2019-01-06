import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)

def InsertAndUpdate(Id,name):
    conn=sqlite3.connect("People.db")
    cmd="SELECT * FROM facial WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    ifrecordexist=0
    for row in cursor:
        ifrecordexist=1

    if(ifrecordexist==1):
        cmd="UPDATE facial SET Names="+str(name)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO facial(ID,Names) Values("+str(Id)+","+str(name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()


id=raw_input("Enter User id: ")
name=raw_input("Enter your name: ")
InsertAndUpdate(id,name)

sampleNum=0

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100);

    cv2.imshow('detector',img);
    cv2.waitKey(10);
    if(sampleNum>250):
        break
cam.release()
cv2.destroyAllWindows()
