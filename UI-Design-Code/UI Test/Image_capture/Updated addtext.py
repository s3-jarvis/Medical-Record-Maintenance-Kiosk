<<<<<<< HEAD
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import logging
from logging.handlers import RotatingFileHandler

logger1 = logging.getLogger('general_logger')
logger2 = logging.getLogger('some_other_logger')

log_handler1 = logging.handlers.RotatingFileHandler('Doctor_Report.log', maxBytes = 2000, backupCount = 10)
log_handler2 = logging.handlers.RotatingFileHandler('Symptoms.log', maxBytes = 2000, backupCount = 10)

logger1.addHandler(log_handler1)
logger2.addHandler(log_handler2)


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add a title
        self.setWindowTitle("Text Box")
        #Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())
        #Create a Label
        my_label = qtw.QLabel("The symptoms captured are :")
        my_label.setFont(qtg.QFont('Times New Roman',22))
        self.layout().addWidget(my_label)
        
        symptoms = ["cough","cold","fever"]
        logger2.warning(symptoms)

        #Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("Text_box")
        my_entry.setText("{}".format(symptoms))
        self.layout().addWidget(my_entry)

        new_label = qtw.QLabel("Doctor's Remarks: ")
        new_label.setFont(qtg.QFont('Times New Roman',22))
        self.layout().addWidget(new_label)

        #Create a new entry box
        new_entry = qtw.QLineEdit()
        new_entry.setObjectName("Write_box")
        new_entry.setText("")
        self.layout().addWidget(new_entry)

        #Create a button for new entry box
        new_button = qtw.QPushButton("Enter",
        clicked = lambda: press_it())
        #my_entry.setObjectName("Text_box")
        #my_entry.setText("")
        self.layout().addWidget(new_button)
           

        #Show the designed window
        self.show()

        def press_it():
            #Add name to label
            print(new_entry.text())
            logger1.warning(new_entry.text())
            #Clear the entry box
            new_entry.setText("")



app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
=======
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import logging

logging.basicConfig(filename="Doctor's Report.log",format='%(message)s',filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add a title
        self.setWindowTitle("Text Box")
        #Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())
        #Create a Label
        my_label = qtw.QLabel("The symptoms captured are :")
        my_label.setFont(qtg.QFont('Times New Roman',22))
        self.layout().addWidget(my_label)
        
        symptoms = ["cough","cold","fever"]

        #Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("Text_box")
        my_entry.setText("{}".format(symptoms))
        self.layout().addWidget(my_entry)

        new_label = qtw.QLabel("Doctor's Remarks: ")
        new_label.setFont(qtg.QFont('Times New Roman',22))
        self.layout().addWidget(new_label)

        #Create a new entry box
        new_entry = qtw.QLineEdit()
        new_entry.setObjectName("Write_box")
        new_entry.setText("")
        self.layout().addWidget(new_entry)

        #Create a button for new entry box
        new_button = qtw.QPushButton("Enter",
        clicked = lambda: press_it())
        #my_entry.setObjectName("Text_box")
        #my_entry.setText("")
        self.layout().addWidget(new_button)
           

        #Show the designed window
        self.show()

        def press_it():
            #Add name to label
            print(new_entry.text())
            logger.info(new_entry.text())
            #Clear the entry box
            new_entry.setText("")



app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
>>>>>>> 09ff8d409de241e21b0f8990ec25be810d9fa0d9
