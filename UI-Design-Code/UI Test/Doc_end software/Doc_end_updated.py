import cv2
import sys
import numpy as np
import time as t
import datetime
import os
import paramiko

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget, QDialog , QApplication
from PyQt5 import uic

cnt = 1
directory = "PATIENT000{}".format(cnt)
parent_dir = 'C:/Users/tejas/Capstone-Project-T229/UI-Design-Code/UI Test/Doc_end software'
paths = os.path.join(parent_dir, directory)
os.makedirs(paths)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.229.96', username='tejas', password='trp17kpl', port=22)
sftp_client = ssh.open_sftp()
sftp_client.get('/home/tejas/share/PATIENT0001/2.png','C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Doc_end software\\PATIENT0001\\1.png')
sftp_client.get('/home/tejas/share/PATIENT0001/Data.txt','C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Doc_end software\\PATIENT0001\\Data.txt')
sftp_client.get('/home/tejas/share/PATIENT0001/Symptoms.txt','C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Doc_end software\\PATIENT0001\\Symptoms.txt')
sftp_client.close()
ssh.close()

class main_1(QMainWindow):
    def __init__(self):
        super(main_1,self).__init__()
        uic.loadUi('First_1.ui',self)
        self.value=0
        self.NFCButton.clicked.connect(self.NFCscan)
        self.Next_doc.clicked.connect(self.NextPage)
        self.Exit_doc.clicked.connect(self.exit)
        x=datetime.datetime.now()
        x=str(x)
        x=x.split()
        self.DateTime1.setText(x[0]+'\n'+x[1])


    @pyqtSlot()

    def NFCscan(self): # add NFC scan function at the doc end
        print('NFC scanned')
    def NextPage(self):
        window2.show()
        self.close()
        window2.showDetails()

    def exit(self):
        self.close()

class main_2(QWidget):
    def __init__(self):
        super(main_2,self).__init__()
        uic.loadUi('second_2.ui',self)
        self.value1=0
        self.saveButton.clicked.connect(self.saveData)
        self.printButton.clicked.connect(self.printData)
        self.reportGenButton.clicked.connect(self.reportGenerate)
        self.cons_details.setAcceptRichText(False)
        self.med_history.setAcceptRichText(False)
        self.vitals.setAcceptRichText(False)
        self.medication.setAcceptRichText(False)
        self.LB.setAcceptRichText(False)

    def showDetails(self):
        x=datetime.datetime.now()
        x=str(x)
        x=x.split()
        self.DateTime2.setText(x[0]+'\n'+x[1])
        Date=x[0]
        self.pic.setScaledContents(True)
        px=QPixmap(id+'/1.png')
        self.pic.setPixmap(px)
        self.pdetails.setText('\n'.join(new_lis))
        self.fo_med.setText('Format:'+'\n'+'Medicine Name'+'\n'+'1A(BF) 0B(LU) 0B(DN)'+'-Duration(only after breakfast)'+'\n'+'1/day-Dosage')


    def saveData(self):
        doc_data=open(id+'/doc_data.txt','w')
        text1=self.cons_details.toPlainText()
        text2=self.med_history.toPlainText()
        text3=self.vitals.toPlainText()
        text4=self.medication.toPlainText()
        text5=self.LB.toPlainText()
        doc_data.writelines(str(datetime.datetime.now()).split()[0]+'\n')
        doc_data.writelines(text1+'\n')# we need write the details from GUI to file
        doc_data.writelines(text2+'\n')
        doc_data.writelines(text3+'\n')
        doc_data.writelines(text5+'\n')
        doc_data.writelines(text4)
        doc_data.close()



    def reportGenerate(self):
        import os
        from PIL import Image
        doc_input=open(id+'/doc_data.txt','r')
        info=[]
        for i in doc_input:
            i.split()
            info.append(i.strip())


        d=os.getcwd() #path of current working dir
        d1=os.path.join(d,id) #go to particular folder
        f=os.path.join(d1,'Data.txt')
        image = os.path.join(d1,'1.png')
        image= Image.open(image)
        image=image.resize((150,120))
        fh=open(f,'r')
        pos=['Name = ','Birth Date = ','Gender = ','Aadhar No = ']
        Details=[]
        for i in fh:
            Details.append(i.strip())
        filename=os.path.join(d1,id+'.pdf')#
        documentTitle = 'Document title!'
        title = 'ABC Hospital'
        subTitle = 'Report'
        fh.close()

        from reportlab.pdfgen import canvas

        pdf = canvas.Canvas(filename)
        pdf.setTitle(documentTitle)

        from reportlab.pdfbase.ttfonts import TTFont #libraries
        from reportlab.pdfbase import pdfmetrics

        #title of Report
        pdf.setFont('Courier-Bold', 36)
        pdf.drawCentredString(300, 770, title)

        #subtitle of 'Report'
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290,720, subTitle)

        pdf.line(40, 710, 590, 710)

        from reportlab.lib import colors

        textn = pdf.beginText(46, 680)
        textn.setFont("Courier", 14)
        textn.setFillColor(colors.black)
        n=len(pos)
        for i in range(n):
            textn.textLine(pos[i]+Details[i])
        pdf.drawText(textn)

        pdf.line(40, 540, 590, 540)
        pdf.drawInlineImage(image, 440, 570)

        txt=pdf.beginText(46,520)
        txt.setFont("Courier",14)
        txt.setFillColor(colors.black)
        txt.textLine("History, Examination, Investigation, Treatment and Progress")
        pdf.drawText(txt)
        pdf.line(40,510,590,510)

        txt=pdf.beginText(46,490)
        txt.setFont("Courier-Bold",14)
        txt.setFillColor(colors.black)
        txt.textLine("Consultation Details : "+ info[1])
        pdf.drawText(txt)

        txt=pdf.beginText(46,460)
        txt.setFont("Courier-Bold",14)
        txt.setFillColor(colors.black)
        txt.textLine("Medical History(if any) : " + info[2])
        pdf.drawText(txt)

        txt=pdf.beginText(46,400)
        txt.setFont("Courier-Bold",14)
        txt.setFillColor(colors.black)
        txt.textLine("Vitals : " + info[3])
        pdf.drawText(txt)

        txt=pdf.beginText(46,370)
        txt.setFont("Courier-Bold",14)
        txt.setFillColor(colors.black)
        txt.textLine("LAB test : "+info[4])
        pdf.drawText(txt)

        txt=pdf.beginText(46,320)
        txt.textLine("Medication Name")
        pdf.drawText(txt)

        txt=pdf.beginText(450,320)
        txt.textLine("Dosage")
        pdf.drawText(txt)

        txt=pdf.beginText(280,320)
        txt.textLine("Duration")
        pdf.drawText(txt)

        pdf.line(42,340,540,340)
        pdf.line(42,300,540,300)
        pdf.line(42,260,540,260)
        pdf.line(42,220,540,220)
        pdf.line(42,180,540,180)

        pdf.line(42,180,42,340)
        pdf.line(230,180,230,340)
        pdf.line(440,180,440,340)
        pdf.line(540,180,540,340)

        txt= pdf.beginText(46,280)
        txt.textLine(info[5])
        pdf.drawText(txt)

        txt= pdf.beginText(240,280)
        txt.textLine(info[6])
        pdf.drawText(txt)

        txt= pdf.beginText(450,280)
        txt.textLine(info[7])
        pdf.drawText(txt)
        k=0
        if len(info)>8:
            j=len(info)-8
            k=j/3

        if(k==1):
            txt= pdf.beginText(46,240)
            txt.textLine(info[8])
            pdf.drawText(txt)

            txt= pdf.beginText(240,240)
            txt.textLine(info[9])
            pdf.drawText(txt)

            txt= pdf.beginText(450,240)
            txt.textLine(info[10])
            pdf.drawText(txt)
        if(k==2):
            txt= pdf.beginText(46,240)
            txt.textLine(info[8])
            pdf.drawText(txt)

            txt= pdf.beginText(240,240)
            txt.textLine(info[9])
            pdf.drawText(txt)

            txt= pdf.beginText(450,240)
            txt.textLine(info[10])
            pdf.drawText(txt)

            txt= pdf.beginText(46,200)
            txt.textLine(info[11])
            pdf.drawText(txt)

            txt= pdf.beginText(240,200)
            txt.textLine(info[12])
            pdf.drawText(txt)

            txt= pdf.beginText(450,200)
            txt.textLine(info[13])
            pdf.drawText(txt)

        txt=pdf.beginText(46,150)
        txt.setFont("Courier-Bold",14)
        txt.setFillColor(colors.black)
        txt.textLine("Dr.XYZ")
        pdf.drawText(txt)
        doc=['MBBS,MD(specialisation)','ABC Hospital']
        txt=pdf.beginText(46,130)
        txt.setFont("Courier",14)
        txt.setFillColor(colors.black)
        for j in doc:
            txt.textLine(j)
        txt.textLine('Date = '+info[0])
        pdf.drawText(txt)

        txt=pdf.beginText(46,50)
        txt.setFont("Courier",12)
        txt.setFillColor(colors.black)
        txt.textLine("Note : Consulatation by appointment only")
        txt.textLine("Clinic No : 080-XXXXX001")
        pdf.drawText(txt)

        pdf.save()


    def printData(self): # add print function to print function
        import webbrowser
        path = 'C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Doc_end software\\PATIENT0001\\PATIENT0001.pdf'
        webbrowser.open_new(path)
        print('Printed')
        self.saveData()
        self.close()



"""import PyPDF2

file=open('PATIENT0100/PATIENT0100.pdf','rb')
pdf_read=PyPDF2.PdfFileReader(file)
read=pdf_read.getPage(0)
ex_read=read.extractText()
lis=ex_read.split('\n')
new_lis=[]
for i in range(len(lis)):
    if i>=2 and i<6:
        new_lis.append(lis[i])
        if lis[i]=='Aadhar No = 23135XX76886':
            new_lis.append('\n')
            new_lis.append('SYMPTOMS : ')
sym_f=open('PATIENT0100/Symptoms.txt','r')
for j in sym_f:
    new_lis.append(j.strip())
"""

id = input('Enter id: ') # take id from NFC read
new_lis=[]
file=open(id+'/Data.txt','r')
for i in file:
    new_lis.append(i.strip())
new_lis.append('\n')
new_lis.append('SYMPTOMS : ')
sym_f=open(id+'/Symptoms.txt','r')
for j in sym_f:
    new_lis.append(j.strip())
Date=str()
app=QApplication(sys.argv)
window1=main_1()
window1.show()
window2=main_2()
print(Date)


try:
    sys.exit(app.exec_())
except:
    print('exiting')
