from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
import os, sys, csv
from PyQt5.uic import loadUi
from win2 import Ui_Dialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("win1.ui", self)
        self.pushButton.clicked.connect(self.open_window)
    
    def open_window(self):
        self.window = Dialog() 
        self.window.show()

class Dialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("win2.ui", self)
        self.nextButton.clicked.connect(self.open_calendar)

    def open_calendar(self):
        self.window = Calendar()
        self.window.show()

class Calendar(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("calendar.ui", self)  
        self.cal = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        self.lab = self.findChild(QLabel, "label")
        self.cal.selectionChanged.connect(lambda:self.pick_date())
        self.selectButton.clicked.connect(lambda:self.select())
        #self.show()

    def pick_date(self):
        self.dateSelected = self.cal.selectedDate()
        self.lab.setText(str(self.dateSelected.toString()))
        
    def select(self):
        print(self.dateSelected)
        self.close()

app=QApplication(sys.argv)
window1=MainWindow()
window1.show()
sys.exit(app.exec_())
