# -*- coding: utf-8 -*-
"""
This class is responsible for rendering Main page with sign in and sign up buttons

Methods are responsible for button click events.

@author: Team Job Buddy
"""
from PyQt5 import QtWidgets, uic, QtCore

class MainWindow(QtWidgets.QMainWindow):
    
    # Initializing switch window signal for SignUp
    switch_window = QtCore.pyqtSignal()
    # Initializing switch window signal for SignIn
    switch_signinwindow = QtCore.pyqtSignal()
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self) # Call the inherited classes __init__ method
        uic.loadUi('pages\Window1.ui', self) # Load the .ui file
        
        #SignInbutton
        self.SignIn_button = self.findChild(QtWidgets.QPushButton, 'SignIn')
        self.SignIn_button.clicked.connect(self.signIn_clicked)
        
        #SignUpbutton
        self.SignUp_button = self.findChild(QtWidgets.QPushButton, 'SignUp')
        self.SignUp_button.clicked.connect(self.signUp_clicked)

        self.show() # Show the GUI
        
    # method to emit signal for SignUp    
    def signUp_clicked(self):
        self.switch_window.emit()
        
    # method to emit signal for SignIn  
    def signIn_clicked(self):
        self.switch_signinwindow.emit()
