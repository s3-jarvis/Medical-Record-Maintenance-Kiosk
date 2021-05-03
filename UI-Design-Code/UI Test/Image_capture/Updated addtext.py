
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit,QPushButton

from PyQt5.QtGui import QFont  
import logging
from logging.handlers import RotatingFileHandler

logger1 = logging.getLogger('general_logger')
logger2 = logging.getLogger('some_other_logger')

log_handler1 = logging.handlers.RotatingFileHandler('Doctor_Report.log', maxBytes = 2000, backupCount = 10)
log_handler2 = logging.handlers.RotatingFileHandler('Symptoms.log', maxBytes = 2000, backupCount = 10)

logger1.addHandler(log_handler1)
logger2.addHandler(log_handler2)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #Add a title
        #self.setWindowTitle("Text Box")
        #Set Vertical Layout
        self.setLayout(QVBoxLayout())
        #Create a Label
        """my_label = QLabel("The symptoms captured are :")
        my_label.setFont(QFont('Times New Roman',22))
        self.layout().addWidget(my_label)"""
        
        symptoms = ["cough","cold","fever"]
        logger2.warning(symptoms)

        #Create an entry box
        my_entry = QLineEdit()
        my_entry.setObjectName("Text_box")
        self.my_entry.setText("{}".format(symptoms))
        self.layout().addWidget(my_entry)
        
        """new_label = QLabel("Doctor's Remarks: ")
        new_label.setFont(QFont('Times New Roman',22))
        self.layout().addWidget(new_label)

        #Create a new entry box
        new_entry = QLineEdit()
        new_entry.setObjectName("Write_box")
        new_entry.setText("")
        self.layout().addWidget(new_entry)

        #Create a button for new entry box
        new_button = QPushButton("Enter",
        clicked = lambda: press_it())
        #my_entry.setObjectName("Text_box")
        #my_entry.setText("")
        self.layout().addWidget(new_button)"""
           

        #Show the designed window
        self.show()

        """def press_it():
            #Add name to label
            print(new_entry.text())
            logger1.warning(new_entry.text())
            #Clear the entry box
            new_entry.setText("")"""



app = QApplication([])
mw = MainWindow()

app.exec_()
