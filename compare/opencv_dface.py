from django.conf import settings
from requests import get
import numpy as np
import cv2
from imageio import imread,imwrite 
from PIL import Image as Im
from IPython.display import display,Image
from scipy.linalg import norm
from django.db import connection

def download(url, file_name):
    with open(file_name, "wb") as file:   
        response = get(url)               
        file.write(response.content)

download("https://www.udrop.com/9mq/haarcascade_frontalface_default.xml",'f.xml')
face_classifier = cv2.CascadeClassifier('f.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return None
    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face

def sim(image1, image2):
    A = np.array(image1, dtype=object )
    B = np.array(image2, dtype=object )

    Aflat = np.hstack(A)
    Bflat = np.hstack(B)
    sim=np.dot(Aflat,Bflat)/(norm(Aflat)*norm(Bflat))
    return sim

def change_size(image):
    height=image.shape[0]
    wideth=image.shape[1]
    h_min=100
    w_min=100
    for i in range(100,1000,100):
        if(abs(i-height)<h_min):
            h_min=abs(i-height)
            h_index=i
        if(abs(i-wideth)<w_min):
            w_min=abs(i-wideth)
            w_index=i
    return cv2.resize(image,(h_index,w_index))

def compare(character_image, user_image):
    img1=imread(character_image)
    img2=imread(user_image)
    img2=face_extractor(img2)
    character=change_size(img1)
    face=change_size(img2)

    gray_character = cv2.cvtColor(character, cv2.COLOR_BGR2GRAY)
    gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    h1= gray_character.shape[0]/100
    h1=int(h1)
    w1=gray_character.shape[1]/100
    w1=int(w1)
    h2=gray_face.shape[0]/100
    h2=int(h2)
    w2=gray_face.shape[1]/100
    w2=int(w2)
    image1=[]
    image2=[]
    sum1=0
    sum2=0

    for p in range(0,100):
        image1.append([])
        for q in range(0, 100): 
            for r in range(0,h1):
                for s in range(0,w1):
                    sum1+=gray_character[r+h1*q][s+w1*q]
            mean1=sum1/(h1*w1)
            image1[p].append(mean1)
            sum1=0
        
    for p in range(0,100):
        image2.append([])
        for q in range(0, 100): 
            for r in range(0,h2):
                for s in range(0,w2):
                    sum2+=gray_face[r+h2*q][s+w2*q]
            mean2=sum2/(h2*w2)
            image2[p].append(mean2)
            sum2=0
    return sim(image1,image2)

def main(user_image):
    sim=0
    sql1="SELECT name FROM compare_charac WHERE id=%s"
    sql2="SELECT imgurl FROM compare_charac WHERE name=%s"

    for i in range (1,10):
        with connection.cursor() as cursor:
            cursor.execute(sql1,[i])
            name=cursor.fetchall()
        for j in name:
            with connection.cursor() as cursor:
                cursor.execute(sql2,[j[0]])
                imgurl=cursor.fetchone()
                imgurl=imgurl[0]
            if(compare(imgurl,user_image)>sim):
                sim=compare(imgurl,user_image)
                best_character=name[0][0]
    
    user=imread(user_image)
    user=face_extractor(user)
    user=cv2.resize(user,(200,200))
    with connection.cursor() as cursor:
                cursor.execute(sql2,[best_character])
                imgurl=cursor.fetchone()
    character=imread(imgurl[0])
    character=cv2.resize(character,(200,200))
    result=cv2.hconcat([user,character])
    imwrite(user_image,result)
    sim=sim*100
    return (sim,best_character,user_image)
    
def opencv_dface(path):    
    main(path)

