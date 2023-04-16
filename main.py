#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import tkinter as tk
from tkinter import Message ,Text
from tkinter import * 
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from firebase import firebase
fixefixed_interval = 3
firebase = firebase.FirebaseApplication('https://criminal-7abf1-default-rtdb.firebaseio.com/', None)
window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("AUTOMATED ATTENDANCE SYSTEM ")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1368x768')
#window.configure(background='#496E7C')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
global key 

#path = "profile.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("img541.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) 
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)

img = ImageTk.PhotoImage(Image.open("./images/9.jpg"))
panel = Label(window, image = img)
panel.place(x = 0, y = 0)
    
message = tk.Label(window, text="AUTOMATED ATTENDANCE SYSTEM" ,bg="#496E7C"  ,fg="white"  ,width=50  ,height=2,font=('times', 30, 'bold')) 

message.place(x=80, y=10)
  
 
lbl = tk.Label(window, text="Enter ID",width=20  ,height=1  ,fg="white"  ,bg="#496E7C" ,font=('times', 15, ' bold ') ) 
lbl.place(x=100, y=200)

txt = tk.Entry(window,width=20  ,bg="#ced5db" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=400, y=200)

lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="white"  ,bg="#496E7C"    ,height=1 ,font=('times', 15, ' bold ')) 
lbl2.place(x=100, y=250)

txt2 = tk.Entry(window,width=20  ,bg="#ced5db"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=400, y=250)

lbl3 = tk.Label(window, text="Enter Age",width=20  ,height=1  ,fg="white"  ,bg="#496E7C" ,font=('times', 15, ' bold ') ) 
lbl3.place(x=100, y=300)

txt3 = tk.Entry(window,width=20  ,bg="#ced5db"  ,fg="black",font=('times', 15, ' bold ')  )
txt3.place(x=400, y=300)

lbl4 = tk.Label(window, text="Enter Gender",width=20  ,height=1  ,fg="white"  ,bg="#496E7C" ,font=('times', 15, ' bold ') ) 
lbl4.place(x=100, y=350)

txt4 = tk.Entry(window,width=20  ,bg="#ced5db"  ,fg="black",font=('times', 15, ' bold ')  )
txt4.place(x=400, y=350)

lbl3 = tk.Label(window, text="Notification",width=15  ,fg="white"  ,bg="#496E7C"  ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=200, y=475)

message = tk.Label(window, text="" ,bg="#ced5db"  ,fg="black"  ,width=50  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=400, y=475)

lbl3 = tk.Label(window, text="Student_Reports",width=15  ,fg="white"  ,bg="#496E7C"  ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=200, y=550)


message2 = tk.Label(window, text="" ,fg="black"   ,bg="#ced5db",activeforeground = "green",width=50  ,height=3  ,font=('times', 15, ' bold ')) 
message2.place(x=400, y=550)
 
 
 
 
 
def clear():
    txt.delete(0, 'end') 
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')
    txt4.delete(0, 'end')
    res = ""
    message.configure(text= res)

'''def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res) '''   
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    age=(txt3.get())
    gender=(txt4.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("Capturing_Images\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name +"Age :" + age + "Gender:" +gender
        row = [Id , name,age,gender]
        with open('Student_List\Student_List.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("Capturing_Images")
    recognizer.train(faces, np.array(Id))
    recognizer.save("Models\Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("Models\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("Student_List\Student_List.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time','Location']
    attendance = pd.DataFrame(columns = col_names)   
    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                  
            if(conf < 50):
                Location="College"
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa+"-"+"Student"
               
              
                
                
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp,Location]
                
                
               
                        
               
            else:
                Id='Not_MATCHED'                
                tt=str(Id)  
            
            if(conf > 75):
                noOfFile=len(os.listdir("Database"))+1
                cv2.imwrite("Database\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])  
            
            
            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
        
        cv2.imshow('Face_Recognize',im) 
        
        if ((cv2.waitKey(1)==ord('q'))):
            break
        
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Students_Reports\Students_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
   
    res=attendance
    message2.configure(text= res)
    data =  {"Id":Id,"Name":aa,"Date":date,"Time":timeStamp,"Location":Location}
    print(data)
   
   
 
    n=str(aa)
    l=str(Location)
    t=str(timeStamp)
    date=str(date)
 
   
    firebase.put('/', '/Student/Name', n)
    firebase.put('/', '/Student/Location', l)
    firebase.put('/', '/Student/time', t)
    firebase.put('/', '/Student/date', date)
    count=0
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="white"  ,bg="#496E7C"  ,width=10  ,height=1 ,activebackground = "white" ,font=('times', 15, ' bold '))
clearButton.place(x=300, y=400)
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="white"  ,bg="#496E7C"  ,width=15  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=750, y=200)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="white"  ,bg="#496E7C"  ,width=15  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=1000, y=200)
trackImg = tk.Button(window, text="Track Images", command=TrackImages  ,fg="white"  ,bg="#496E7C"  ,width=15  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=750, y=300)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="#496E7C"  ,width=15  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=300)
copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.insert("insert", "Python","", "TEAM", "superscript")
copyWrite.configure(state="disabled",fg="red"  )
copyWrite.pack(side="left")
copyWrite.place(x=800, y=750)

window.mainloop()


# In[ ]:





# In[ ]:




