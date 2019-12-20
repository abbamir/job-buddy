# -*- coding: utf-8 -*-
"""
This class is responsible for loading JobAdder window and has 
all methods related to this page.

@author: Team Job Buddy
"""
from PyQt5 import QtWidgets, uic, QtCore
import jobdatastorage # internal class

class JobAdderWindow (QtWidgets.QMainWindow):
    switch_window_to_JoblistWindow = QtCore.pyqtSignal()
    # Creating here because we come back to this page several times and 
    # we want this object to be active so that data can be stored 
    
    def __init__(self, email):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('pages\Window6.ui', self)
        self.email = email
        
        #Getting input data
        self.job_title_edit = self.findChild(QtWidgets.QLineEdit, 'job_title_edit')
        self.company_edit = self.findChild(QtWidgets.QLineEdit, 'company_edit')
        self.location_edit = self.findChild(QtWidgets.QLineEdit, 'location_edit')
        self.application_date = self.findChild(QtWidgets.QDateTimeEdit, 'application_date')
        self.status = self.findChild(QtWidgets.QComboBox, 'status')
        self.job_description = self.findChild(QtWidgets.QPlainTextEdit, 'job_description')
        
        #Button Click for JoblistWindow page
        self.save = self.findChild(QtWidgets.QPushButton, 'save')
        self.save.clicked.connect(self.store_job_data)
        self.save.clicked.connect(self.switch_window_to_JoblistWindow)
    
    def store_job_data(self):
        data = jobdatastorage.JobData()
        data.store(self.job_title_edit.text(),
                   self.company_edit.text(),
                   self.location_edit.text(),
                   self.application_date.dateTime().toString(),
                   self.status.currentText(),
                   self.job_description.toPlainText(),
                   self.email)  