# -*- coding: utf-8 -*-
"""
This class is responsible for rendering Sign in Window

@author: Team Job Buddy
"""

from PyQt5 import QtWidgets, uic, QtCore
import pandas as pd

class SigninWindow (QtWidgets.QMainWindow):
    switch_window4 = QtCore.pyqtSignal() #switching to Job listing page
    switch_window3 = QtCore.pyqtSignal() #switching to Sign up page
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self) # Call the inherited classes __init__ method
        uic.loadUi('pages\Window2.ui', self) # Load the .ui file
        
        # Setting Enter button invisible -> appears after validation
        self.enter = self.findChild(QtWidgets.QPushButton, 'enter')
        self.enter.setVisible(False)
        
        # Getting user input
        self.email_enter = self.findChild(QtWidgets.QLineEdit, 'email_enter')
        self.password_enter = self.findChild(QtWidgets.QLineEdit, 'password_enter')
        
        #Output label
        self.status = self.findChild(QtWidgets.QLabel, 'status')
        
        
        #Button Click for sign up page
        self.signUp_button = self.findChild(QtWidgets.QPushButton, 'signUp')
        self.signUp_button.clicked.connect(self.switch_window3)
        
        #Button Click for Job listing page
        self.signIn_button = self.findChild(QtWidgets.QPushButton, 'signIn')
        self.signIn_button.clicked.connect(self.verify_user)
    
    def verify_user(self):
        username = self.email_enter.text()
        password = self.password_enter.text()
        # Exception handling for if the file is not found
        try:
            pd.read_csv("database/user_details.csv")
        except:
            self.status = QtWidgets.QLabel("Please sign up!")
        else:
            data = pd.read_csv("database/user_details.csv")
            
        # Logic for verifying user credentials
        count_email = 0
        count_pass = 0
        # Chcking  for email
        for element in data['email']:
            if element == username:
                count_email = 1
            else:
                count_email = 0
        
        # Checking for password
        for element2 in data['password']:
            if element2 == password:
                count_pass = 1
            else:
                count_pass = 0
        
        # Verifying user
        if count_email > 0 and count_pass > 0:
            self.enter.setVisible(True)
            self.status.setText("Approved")
            self.enter.clicked.connect(self.switch_window4)
        else:
            self.status.setText("Wrong email or password")
   