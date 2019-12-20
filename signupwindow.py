# -*- coding: utf-8 -*-
"""
This class is resposible for rendering SignUp window and is responsible for Sign up 
related methods

@author: Team Job Buddy
"""
from PyQt5 import QtWidgets, uic, QtCore
import storage

class SignupWindow (QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal() #Switching to Joblistview window
    switch_to_window_2 = QtCore.pyqtSignal() #Switching to SignIn window
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self) # Call the inherited classes __init__ method
        uic.loadUi('pages\Window3.ui', self) # Load the .ui file
        
        #Getting input data
        self.firstname_enter = self.findChild(QtWidgets.QLineEdit, 'firstname_enter')
        self.lastname_enter = self.findChild(QtWidgets.QLineEdit, 'lastname_enter')
        self.school_enter = self.findChild(QtWidgets.QLineEdit, 'school_enter')
        self.degree_enter = self.findChild(QtWidgets.QComboBox, 'degree_enter')
        self.jobtitle_enter = self.findChild(QtWidgets.QLineEdit, 'jobtitle_enter')
        self.company_enter = self.findChild(QtWidgets.QLineEdit, 'company_enter')
        self.email_enter = self.findChild(QtWidgets.QLineEdit, 'email_enter')
        self.password_enter = self.findChild(QtWidgets.QLineEdit, 'password_enter')
        
        #Click for Create Account Button and switch to Joblistview Page
        self.create_account = self.findChild(QtWidgets.QPushButton, 'create_account')
        self.create_account.clicked.connect(self.store_data)
        self.create_account.clicked.connect(self.switch_window)
                
        #Click for Sign in Button
        self.sign_in = self.findChild(QtWidgets.QPushButton, 'SignIn')
        self.sign_in.clicked.connect(self.switch_to_window_2)
    
    def send_username(self):
        self.switch_window_username.emit(self.email_enter.text())
    
    def store_data(self):
        data = storage.Authorization()
        data.store(self.firstname_enter.text(),
                   self.lastname_enter.text(),
                   self.school_enter.text(),
                   self.degree_enter.currentText(),
                   self.jobtitle_enter.text(),
                   self.company_enter.text(),
                   self.email_enter.text(),
                   self.password_enter.text()) 