import cv2
import sys
import numpy as np
import time as t

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
        cv2.imwrite('C:/Users/Mahesh M/Desktop/Python/CapstoneProject/%s.png' % (window2.value1), frame)
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
        print('Hello')
    def retry(self):
        open(1)
        #we don't need this to show again same page so it does same function as first_click.
        cap=cv2.VideoCapture(0)
        start=t.perf_counter()
        stop=t.perf_counter()
        #i=0
        while(cap.isOpened()):
            ret,frame=cap.read()
            if ret==True: # photo taken after 5s.
                self.display(frame,1)
                cv2.waitKey()
                stop=t.perf_counter()
                if  stop-start>5:
                    break
                
            else:
                print('Return not found')
        self.value1=self.value1+1
        cv2.imwrite('C:/Users/Mahesh M/Desktop/Python/CapstoneProject/%s.png' % (self.value1), frame)
        cap.release()
        
app=QApplication(sys.argv)
windo=main()
windo.show()
window2=main1()

def open(r):
    if r==1:
        window2.show()
    
try:
    sys.exit(app.exec_())
except:
    print('existing')
        
        
    
