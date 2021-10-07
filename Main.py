from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, math
from PyQt5.uic import loadUi


class Greet(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("Greet.ui", self)
        #If the button is pushed
        self.button1.clicked.connect(self.loginbtn)
        self.button2.clicked.connect(self.signupbtn)
    
    def loginbtn(self):
        print("Login Button")
        widget.setFixedHeight(542)
        widget.setFixedWidth(421)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupbtn(self):
        print("Sign up Button") 
    


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("login.ui", self)

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
greet= Greet()
login = Login()
widget.addWidget(greet)
widget.addWidget(login)
widget.setFixedHeight(201)
widget.setFixedWidth(421)
widget.show()

try :
    sys.exit(app.exec_())
except:
    print("Exiting")