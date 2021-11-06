from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QMessageBox
import os, sys, csv
from PyQt5.uic import loadUi

class Exin(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("expenditurecube1.ui", self)
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.balance = 200000
        self.date.setDisplayFormat("MMM d yyyy")
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.savebutton.setEnabled(False)
        self.savebutton.setStyleSheet("background-color:rgb(226,226,226);border-width: 2px;border-radius: 20px;padding: 4px;")
        self.balancemoney.setText(str(self.balance))
        self.savebutton.clicked.connect(self.Save)
        self.confirmbutton1.clicked.connect(self.conf1)
        self.confirmbutton2.clicked.connect(self.conf2)
        self.date.dateChanged.connect(self.set_date)
        self.tabWidget.currentChanged.connect(self.tabChanged)

    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.expline.clear()
            self.note.clear()
            self.date.setDateTime(QtCore.QDateTime.currentDateTime())
            print(self.tabWidget.currentIndex())
        elif self.tabWidget.currentIndex() == 1:
            self.incline.clear()
            self.note.clear()
            self.date.setDateTime(QtCore.QDateTime.currentDateTime())
            print(self.tabWidget.currentIndex())
        else:
            print("What?!!!")

    def conf1(self):
        income = self.incline.text()
        try:
            income = int(income)
            self.trans = int(income)
            self.savebutton.setEnabled(True)
            self.savebutton.setStyleSheet("background-color: rgb(85, 255, 0);border-width: 2px;border-radius: 20px;padding: 4px;")
        except:
            warn = QMessageBox()
            warn.setWindowFlag(Qt.FramelessWindowHint)
            #warn.setStyleSheet("background-color:white;")
            warn.setText("Invalid Input!")
            warn.setIcon(QMessageBox.Warning)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setDefaultButton(QMessageBox.Ok)
            x = warn.exec_()
            pass
        
    def conf2(self): 
        expenditure = self.expline.text()
        try:
            expenditure = int(expenditure)
            self.trans = int(expenditure)*-1
            self.savebutton.setEnabled(True)
            self.savebutton.setStyleSheet("background-color: rgb(85, 255, 0);border-width: 2px;border-radius: 20px;padding: 4px;")
        except:
            warn = QMessageBox()
            warn.setWindowFlag(Qt.FramelessWindowHint)
            #warn.setStyleSheet("background-color:white;")
            warn.setText("Invalid Input!")
            warn.setIcon(QMessageBox.Warning)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setDefaultButton(QMessageBox.Ok)
            x = warn.exec_()
            pass
    
    def set_date(self, qDate):
        self.dateselected = self.date.date().toString()
        self.datepicked = self.dateselected[4::]

    def Save(self):
        note = self.note.text()  
        self.balance += self.trans 
        self.balancemoney.setText(str(self.balance))
        transactData = self.datepicked+';'+str(self.trans)+';'+str(self.balance)+';'+note
        print(transactData)
        self.datepicked = None
        self.trans = 0
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.savebutton.setEnabled(False)
        self.popup()
    
    def popup(self):
        msg = QMessageBox()
        msg.setWindowFlag(Qt.FramelessWindowHint)
        msg.setText("Transaksi Anda Telah Disimpan!")
        msg.setStyleSheet("background-color:white;")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()
        
app=QApplication(sys.argv)
window1=Exin()
window1.show()
sys.exit(app.exec_())
    
        
    
