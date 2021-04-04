import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add a title
        self.setWindowTitle("Text Box")
        #Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())
        #Create a Label
        my_label = qtw.QLabel("The symptoms capture are :")
        my_label.setFont(qtg.QFont('Times New Roman',22))
        self.layout().addWidget(my_label)

        symptoms = ["cough","cold","fever"]

        #Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("Text_box")
        my_entry.setText("{}".format(symptoms))
        self.layout().addWidget(my_entry)

        """#Create a button
        my_button = qtw.QPushButton("Enter",
        clicked = lambda: press_it())
        #my_entry.setObjectName("Text_box")
        #my_entry.setText("")
        self.layout().addWidget(my_button)"""
           

        #Show the designed window
        self.show()

        #def press_it():
            #Add name to label
            #my_label.setText(f'{my_entry.text()}!')
            #Clear the entry box
            #my_entry.setText("")



app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
