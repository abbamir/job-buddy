# -*- coding: utf-8 -*-
"""
This class renders JobList Window UI and is responsible for method attached to 
button of this page.

It uses local class pandasmodel to convert dataframe to QTableView format.

@author: Team Job Buddy
"""

import pandas as pd
import pandasmodel  # Internal class
from PyQt5 import QtWidgets, uic, QtCore

class JoblistWindow (QtWidgets.QMainWindow):
    
    data = pd.DataFrame()
    
    switch_window_JobAdderWindow = QtCore.pyqtSignal()
    switch_window_WebScrapingWindow = QtCore.pyqtSignal()
    
    def __init__(self, email):
        QtWidgets.QWidget.__init__(self) # Call the inherited classes __init__ method
        uic.loadUi('pages\Window4.ui', self) # Load the .ui file
        
        # Getting QTableView
        self.job_table = self.findChild(QtWidgets.QTableView, 'job_table')
        
        #Button Click for Load Data Button
        self.load_data = self.findChild(QtWidgets.QPushButton, 'load_data')
        self.load_data.clicked.connect(self.load_info)
        
        #Button Click for Job Adder page
        self.add_job = self.findChild(QtWidgets.QPushButton, 'add_job')
        self.add_job.clicked.connect(self.switch_window_JobAdderWindow)
        
        #Button Click for Web Scraping page
        self.find_job = self.findChild(QtWidgets.QPushButton, 'find_job')
        self.find_job.clicked.connect(self.switch_window_WebScrapingWindow)
        
        self.email = email
        
    def load_info(self):
        self.data = pd.read_csv("database/job_details.csv")
        self.data = self.data[self.data['username'] == self.email]
        
        model = pandasmodel.PandasModel(self.data.iloc[:,[0,1,2,3,4,5]])
        self.job_table.setModel(model) 