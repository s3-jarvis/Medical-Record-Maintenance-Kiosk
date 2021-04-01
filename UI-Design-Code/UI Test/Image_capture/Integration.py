import cv2
import sys
import numpy as np
import pytesseract
import time as t
from PIL import Image
import os
import speech_recognition as sr

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget, QDialog , QApplication
from PyQt5 import uic

class main(QWidget):
    def __init__(self):
        super(main,self).__init__()
        uic.loadUi('First.ui',self)
        self.logic=0
        self.value=0
        self.pushButton.clicked.connect(self.first_click)
    @pyqtSlot()
    
    def first_click(self):
        open(1)
        self.close()
        cap=cv2.VideoCapture(0)
        start=t.perf_counter()
        stop=t.perf_counter()
        #i=0
        while(cap.isOpened()):
            ret,frame=cap.read()
            if ret==True: 
                window2.display(frame,1)
                cv2.waitKey()
                stop=t.perf_counter()
                if  stop-start>5: # photo taken after 5s.
                    break
                
            else:
                print('Return not found')
        window2.value1=window2.value1+1
        cv2.imwrite('C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Image_capture/%s.png' % (window2.value1), frame)
        cap.release()
        #cv2.destroyAllWindows()
       
    


class main1(QWidget):
    def __init__(self):
        super(main1,self).__init__()
        uic.loadUi('second_page.ui',self)
        self.logic1=0
        self.value1=1
        self.Next.clicked.connect(self.second_next)
        self.Retry.clicked.connect(self.retry)
    def display(self,img,window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape)==3:
            if (img.shape[2])==4:
                qformat =QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1],img.shape[0], qformat)
        img = img.rgbSwapped()
        self.Camera_box.setPixmap(QPixmap.fromImage(img))
        self.Camera_box.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    def second_next(self):
        window3.show()
        self.close()
        """cap=cv2.VideoCapture(0)
        while(cap.isOpened()):
            ret,frame=cap.read()
            if ret==True:
                window3.display(frame,1)
                cv2.waitKey()"""
                
    def retry(self):
        open(1)
        #we don't need this to show again same page so it does same function as first_click.
        windo=main()
        windo.first_click()

class main2(QWidget):
    def __init__(self):
        super(main2,self).__init__()
        uic.loadUi('third.ui',self)
        self.logic2=0
        self.value2=0
        self.Next.clicked.connect(self.third_next)
        #self.Retry.clicked.connect(self.retry)
        self.Capture.clicked.connect(self.capture)

    def capture(self):
        #counter3=0
        cap=cv2.VideoCapture(0)
        start=t.perf_counter()
        stop=t.perf_counter()
        #i=0
        while(cap.isOpened()):
            ret,frame=cap.read()
            if ret==True: 
                window3.display(frame,1)
                cv2.waitKey()
                stop=t.perf_counter()
                if  stop-start>7: # photo taken after 5s.
                    break
                
            else:
                print('Return not found')
        window3.value2=window3.value2+1
        cv2.imwrite('C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Image_capture/OCR_%s.jpg' % (window3.value2), frame)
        cap.release()
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        img = cv2.imread('C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Image_capture/Aadhar.jpg')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    
    #detecting words
        hImg,wImg,_ = img.shape
        boxes = pytesseract.image_to_data(img)
        a=list(boxes.split("\n"))
    #print(boxes)
        main = []
        e = ""
    
        for i in range(len(a)):
          for j in range(len(a[i])):
            if a[i][j] != '\t':
              e += a[i][j]
          main.append(e)
    
        name = main[21][496:] + " " + main[22][521:]
        DOB = main[29][675:]
        gender = main[33][766:]
        aadhar = main[41][-4:] + main[42][-4:] + main[43][-4:]
        print("\n")
        print("OCR OUTPUT")
        print("Name = ",name)
        print("DOB = ",DOB)
        print("Gender = ",gender)
        print("Aadhar = ",aadhar)
        """Dfile = open('C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Image_capture/Data.txt','w')
        Dfile.writelines(name+"\n")
        Dfile.writelines(DOB+"\n")
        Dfile.writelines(gender+"\n")
        Dfile.writelines(aadhar+"\n")
        Dfile.close()  
        for x,b in enumerate(boxes.splitlines()):
            if x!=0:
                b = b.split()
            #print(b)
                if len(b)==12:
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
                    cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(50,50,255),3)
    
        #imS = cv2.resize(img, (800, 800))
        #window3.display(img,1)
        #cv2.imshow('Result',imS)
        #cv2.waitKey()"""

    """def retry(self):
        window3.show()
        window2.second_next()"""
        
    def display(self,img,window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape)==3:
            if (img.shape[2])==4:
                qformat =QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1],img.shape[0], qformat)
        img = img.rgbSwapped()
        self.imagelabel.setPixmap(QPixmap.fromImage(img))
        self.imagelabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    def third_next(self):
        window4.show()
        self.close()

        
class main3(QWidget):
    def __init__(self):
        super(main3,self).__init__()
        uic.loadUi('fourth.ui',self)
        self.logic3=0
        self.value3=1
        self.Next.clicked.connect(self.fourth_next)
        self.Retry.clicked.connect(self.retry)
        self.Start.clicked.connect(self.Start_recording)

    def Start_recording(self):
        
        print('Test')
        file1 = open("SYMPTOMS.txt","a")
        r = sr.Recognizer()
        m = sr.Microphone()

        speechData = []
        Data = ""
        sym_dataset = ['cough', 'cold', 'headache', 'pain', 'fever']
        symptoms = []

        print("\n")
        print("Speech Data")
        print("Please Start Speaking...")
        self.Text.setText('Please Start Speaking')

        while 'stop' not in Data.split():
            with m as source:
                r.adjust_for_ambient_noise(source)
                Data = r.recognize_google(r.listen(source))
                print(">>" + Data)
                speechData.append(Data)

        for i in speechData:
            for j in sym_dataset:
                if j in i:
                    file1.writelines(j + '\n')
                    symptoms.append(j)



        #return symptoms
        self.Text.setText('Your Voice has been recorded.')
        self.Text.setText(symptons)
    def retry(self):
        window4.start_recording()

    def fourth_next(self):
        print('Hello')
        


        
app=QApplication(sys.argv)
windo=main()
windo.show()
window2=main1()
window3=main2()
window4=main3()


def open(r):
    if r==1:
        window2.show()
    
try:
    sys.exit(app.exec_())
except:
    print('existing')
        
        
    
