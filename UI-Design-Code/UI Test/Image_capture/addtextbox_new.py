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
