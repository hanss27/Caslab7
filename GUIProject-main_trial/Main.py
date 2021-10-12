from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, math, csv
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
        login.clear()
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupbtn(self):
        print("Sign up Button") 
        signup.clear()
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+2)

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.co = 1
    
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.login)
        self.createaccbutton.clicked.connect(self.signup) 
        self.visiblebutton.clicked.connect(self.visible)
        self.visiblebutton.setStyleSheet("background-image : url(invisible.png);")

        
        #SET PASSWORD
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet('lineedit-password-character: 9679')

    def clear(self):
        print("test clear")
        self.username.clear()
        self.password.clear()
        self.cond.clear()

    def visible(self):
        self.co +=1
        if (self.co%2 == 0):
            print("Invisible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.visiblebutton.setStyleSheet("background-image : url(visible.png);")

        else:
            print("Visible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password.setStyleSheet('lineedit-password-character: 9679')      
            self.visiblebutton.setStyleSheet("background-image : url(invisible.png);")

    def login(self):
        print("Login Button")
        counter = 0
        user = self.username.text()
        password = self.password.text()
        self.cond.setStyleSheet("color: red;")

        for i in rows :
            if i[0] == user:
                print("Username is correct")
                counter += 1
                if i[1] == password:
                    print("Access Granted")
                    self.cond.setStyleSheet("color: green;")
                    self.cond.setText("Login Successful!")
                    counter += 1
                    break
                else:
                    self.cond.setText("Password is incorrect")
                    break         
        if counter == 0:
            self.cond.setText("Username or Password is incorrect")

        if self.cond.text() == "Login Successful!":
                
                widget.setFixedHeight(686)
                widget.setFixedWidth(660)
                widget.setCurrentIndex(widget.currentIndex()+2)

    def signup(self):
        print("Sign up Button") 
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Signup(QtWidgets.QMainWindow): #QtWidgets.QDialog
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("signup.ui", self)
        self.mainbutton.clicked.connect(self.main)
        self.signupbutton.clicked.connect(self.Signup)
        self.visiblebutton.clicked.connect(self.visible)
        self.visiblebutton.setStyleSheet("background-image : url(invisible.png);")
        self.visiblebutton_2.clicked.connect(self.visible_cpw)
        self.visiblebutton_2.setStyleSheet("background-image : url(invisible.png);")
        self.co = 1

        #SET PASSWORD
        self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwsignup.setStyleSheet('lineedit-password-character: 9679')
        self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpwsignup.setStyleSheet('lineedit-password-character: 9679')

    def clear(self):
        print("test clear")
        self.unsignup.clear()
        self.pwsignup.clear()
        self.cpwsignup.clear()
        self.cond.clear()

    def visible(self):
            self.co +=1
            if (self.co%2 == 0):
                print("Invisible")
                self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.visiblebutton.setStyleSheet("background-image : url(visible.png);")

            else:
                print("Visible")
                self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
                self.pwsignup.setStyleSheet('lineedit-password-character: 9679')         
                self.visiblebutton.setStyleSheet("background-image : url(invisible.png);")

    def visible_cpw(self):
            self.co +=1
            if (self.co%2 == 0):
                print("Invisible")
                self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.visiblebutton_2.setStyleSheet("background-image : url(visible.png);")

            else:
                print("Visible")
                self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
                self.cpwsignup.setStyleSheet('lineedit-password-character: 9679')      
                self.visiblebutton_2.setStyleSheet("background-image : url(invisible.png);")

    def Signup(self):
        print("Signup Button")
        user = self.unsignup.text()
        password = self.pwsignup.text()
        password2 =self.cpwsignup.text()
        self.cond.setStyleSheet("color: red;")

        with open('database.csv',mode='a', newline='') as Fileappend:
            Writer = csv.writer(Fileappend,delimiter=",")
            
            for line in rows : 
                if line[0] != user:
                    print("Username allowed")
                    if password == password2:
                        Writer.writerow([user,password])
                else:
                    print("Username existed!")
                    self.cond.setStyleSheet("color: red;")
                    self.cond.setText("Username already existed!")

    def main(self):
        print("Back to main")        
        widget.setFixedHeight(201)
        widget.setFixedWidth(421)
        widget.setCurrentIndex(widget.currentIndex()-2)

    

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("main.ui", self)

#Load Database
file = open('database.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

#Call Qt
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
greet= Greet()
login = Login()
signup = Signup()
widget.addWidget(greet)
widget.addWidget(login)
widget.addWidget(signup)
widget.setFixedHeight(201)
widget.setFixedWidth(421)
widget.show()

try :
    sys.exit(app.exec_())
except:
    print("Exiting")