from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QMessageBox
import os, sys, csv
from PyQt5.uic import loadUi

class Exin(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("transaction.ui", self)
        self.open_file()
        print(self.transaction)
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.transactData = []
        self.dateselected = QDate.currentDate().toPyDate()
        self.date.setDisplayFormat("d MMM yyyy")
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.savebutton.setEnabled(False)
        self.savebutton.setStyleSheet("background-color:rgb(226,226,226);border-width: 2px;border-radius: 20px;padding: 4px;")
        self.balancemoney.setText(str(self.balance))
        self.savebutton.clicked.connect(self.Save)
        self.confirmbutton1.clicked.connect(self.conf1)
        self.confirmbutton2.clicked.connect(self.conf2)
        self.date.dateChanged.connect(self.set_date)
        self.tabWidget.currentChanged.connect(self.tabChanged)

    def open_file(self):
        with open('income.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            self.balance = 0
            self.transaction = []
            self.header = []
            self.header = next(csv_reader)
            for row in csv_reader:
                self.balance = self.balance + int(row[1])
                self.transaction.append(row)

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
    
    def set_date(self):
        self.dateselected = self.date.date().toPyDate()

    def Save(self):
        note = self.note.text()
        if note == '':
            note = '-'  
        self.balance += self.trans 
        self.datepicked = str(self.dateselected)
        self.balancemoney.setText(str(self.balance))
        '''
        if self.trans < 0:
            trans =  "'" + str(self.trans)
        else:
            trans = str(self.trans)
            
        self.transactData.append(self.datepicked)
        self.transactData.append(trans)
        self.transactData.append(note)
        #transactData = self.datepicked+';'+trans+';'+note
        print(self.transactData)
        '''
        if self.transaction[0] == []:
            self.transaction[0] = [str(self.dateselected), str(self.trans), note]
        else:
            self.transaction.append([str(self.dateselected), str(self.trans), note])
        
        print(self.transaction)
        self.transaction.sort()
        self.transaction.reverse() 
        print(self.transaction)
        self.datepicked = None
        self.trans = 0
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.savebutton.setEnabled(False)
        self.savebutton.setStyleSheet("background-color:rgb(226,226,226);border-width: 2px;border-radius: 20px;padding: 4px;")
        self.popup()

    def record(self):
        with open('income.csv',mode='w', newline = '') as file:
            writer = csv.writer(file,delimiter=",")
            writer.writerow(self.header)
            for row in self.transaction:
                writer.writerow(row)
    def popup(self):
        msg = QMessageBox()
        msg.setWindowFlag(Qt.FramelessWindowHint)
        msg.setText("Transaksi Anda Telah Disimpan!")
        #msg.setStyleSheet("background-color:white;")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()

user = 1

app=QApplication(sys.argv)
window1=Exin()
window1.show()
try :
    sys.exit(app.exec_())
except :
    window1.record()
    #window1.open_file()

    

    
