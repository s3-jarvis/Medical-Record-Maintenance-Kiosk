import logging
import os
import sys
import time as t
from logging.handlers import RotatingFileHandler
import paramiko


import cv2
import numpy as np
import pytesseract
import speech_recognition as sr
from PIL import Image
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton
from gtts import gTTS
from playsound import playsound

cnt = 1
directory = "PATIENT000{}".format(cnt)
parent_dir = 'C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Final UI Design'
paths = os.path.join(parent_dir, directory)
os.makedirs(paths)
logger1 = logging.getLogger('general_logger')
logger2 = logging.getLogger('some_other_logger')
        
log_handler1 = logging.handlers.RotatingFileHandler('C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Final UI Design\\PATIENT0001\\Data.log', maxBytes = 2000, backupCount = 10)
log_handler2 = logging.handlers.RotatingFileHandler('C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Final UI Design\\PATIENT0001\\Symptoms.log', maxBytes = 2000, backupCount = 10)

logger1.addHandler(log_handler1)
logger2.addHandler(log_handler2)

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
        audio = gTTS("Please hold still in front of the camera, capturing face in 5 seconds.")
        audio.save("textaudio.mp3")
        playsound("textaudio.mp3")
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
        #window2.value1=window2.value1+1
        cv2.imwrite('C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Final UI Design/PATIENT0001/%s.png' % (window2.value1), frame)
        cap.release()
        audioc = gTTS(" If picture is out of frame,press retry. else press next to continue .")
        audioc.save("textaudioc.mp3")
        playsound("textaudioc.mp3")
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
        audio1 = gTTS("Please press Capture button to capture your ID card, your ID will be captured in 7 seconds")
        audio1.save("textaudio1.mp3")
        playsound("textaudio1.mp3")
                
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
        cv2.imwrite('C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Final UI Design/PATIENT0001/OCR_%s.jpg' % (window3.value2), frame)
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
        logger1.warning(name)
        logger1.warning(DOB)
        logger1.warning(gender)
        logger1.warning(aadhar)
        self.textEdit.setText("{}".format(name))
        self.textEdit1.setText("{}".format(DOB))
        self.textEdit2.setText("{}".format(gender))
        self.textEdit3.setText("{}".format(aadhar))
        audio2 = gTTS("captured data will appear on Data captured column, if the captured data is incorrect please press retry button. else press next button to continue")
        audio2.save("textaudio2.mp3")
        playsound("textaudio2.mp3")
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

    def retry(self):
        window3.capture()
        
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
        audio3 = gTTS("Please press start button to start recording your voice, say stop to end the recording")
        audio3.save("textaudio3.mp3")
        playsound("textaudio3.mp3")
        

        
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
        #file1 = open("SYMPTOMS.txt","a")
        r = sr.Recognizer()
        m = sr.Microphone()

        speechData = []
        Data = ""
        sym_dataset = ['cough', 'cold', 'headache', 'pain', 'fever']
        symptoms = []

        print("\n")
        print("Speech Data")
        print("Please Start Speaking...")
        #self.Text.setText('Please Start Speaking')

        while 'stop' not in Data.split():
            with m as source:
                r.adjust_for_ambient_noise(source)
                Data = r.recognize_google(r.listen(source))
                print(">>" + Data)
                speechData.append(Data)

        for i in speechData:
            for j in sym_dataset:
                if j in i:
                    #file1.writelines(j + '\n')
                    symptoms.append(j)

        
        print(symptoms)
        logger2.warning(symptoms)
        self.lineEdit.setText("{}".format(symptoms))
        return symptoms
        audios = gTTS("if the speech data is not identified correctly,please press retry else press next to continue")
        audios.save("textaudios.mp3")
        playsound("textaudios.mp3")
        
        

    def retry(self):
        window4.Start_recording()

    def fourth_next(self):
        window5.show()
        self.close()
        audio4 = gTTS("Please place the NFC Card from the pile on the reader marked as given below.Please wait while the Write Process completes.After successful Write Process, you have come to final stage of the process.Please Press Next button")
        audio4.save("textaudio4.mp3")
        playsound("textaudio4.mp3")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.89.96', username='tejas', password='trp17kpl', port=22)
        sftp_client = ssh.open_sftp()
        sftp_client.put("C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Final UI Design\\PATIENT0001\\1.png",'/home/tejas/share/PATIENT0001/1.png')
        sftp_client.put("C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Final UI Design\\PATIENT0001\\OCR_1.jpg",'/home/tejas/share/PATIENT0001/OCR_1.jpg')
        sftp_client.put("C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Final UI Design\\PATIENT0001\\Data.log", '/home/tejas/share/PATIENT0001/Data.txt')
        sftp_client.put("C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Final UI Design\\PATIENT0001\\Symptoms.log", '/home/tejas/share/PATIENT0001/Symptoms.txt')

        
class main4(QWidget):
    def __init__(self):
        super(main4,self).__init__()
        uic.loadUi('fifth.ui',self)
        self.logic4=0
        self.value4=1
        self.NFCnext.clicked.connect(self.fifth_next)

    def fifth_next(self):
        window6.show()
        self.close()
        audio5 = gTTS("Registration is completed. Kindly head over to the Consultation Doctor after generating a Token Number outside the kiosk.")
        audio5.save("textaudio5.mp3")
        playsound("textaudio5.mp3")


class main5(QWidget):
    def __init__(self):
        super(main5, self).__init__()
        uic.loadUi('sixth.ui', self)
        self.logic5 = 0
        self.value5 = 1
        #self.NFCnext.clicked.connect(self.fifth_next)



        
app=QApplication(sys.argv)
windo=main()
windo.show()
audio0 = gTTS("Welcome to Patient registration kiosk , press next to continue")
audio0.save("textaudio0.mp3")
playsound("textaudio0.mp3")
window2=main1()
window3=main2()
window4=main3()
window5=main4()
window6=main5()


def open(r):
    if r==1:
        window2.show()
    
try:
    sys.exit(app.exec_())
except:
    print('existing')
        
        
    
