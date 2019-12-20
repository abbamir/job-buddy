# -*- coding: utf-8 -*-
"""

This class is responsible for Webscrapign User Interface and methods related to
loading and processing data from indeed.com

@author: Team - Job Buddy
"""

from PyQt5 import QtWidgets, uic, QtCore
import pandasmodel 
import webscraper
import webbrowser 

class WebScrapingWindow (QtWidgets.QMainWindow):
    switch_window_to_JoblistWindow = QtCore.pyqtSignal()
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('pages\Window7.ui', self)
        
        # creating empty variable to store website name from get_results_from_web method
        # then use it in go_online method
        # even though interpreter thinks it's not used anywhere, it is used in the methods below
        website_name = str()
        
        #QTableView
        self.job_table_web = self.findChild(QtWidgets.QTableView,'job_table_web')
        
        #Getting inputs from QLineEdit
        self.job_title2 = self.findChild(QtWidgets.QLineEdit,'job_title2')
        self.location2 = self.findChild(QtWidgets.QLineEdit,'location2')
        
        #Button Click for JoblistWindow page
        self.check_online = self.findChild(QtWidgets.QPushButton,'check_online')
        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.switch_window_to_JoblistWindow)
        self.check_online.clicked.connect(self.go_online)
        
        # Button Click for initiating webscraping search
        self.find = self.findChild(QtWidgets.QPushButton,'find')
        self.find.clicked.connect(self.get_results_from_web)
        
    def get_results_from_web(self):
        
        # Getting input from user 
        job_title = self.job_title2.text()
        city = self.location2.text()
        
        # Initiating web-scraping class to get data from the web in tabular format
        web_searcher = webscraper.WebScraping()
        result_table = web_searcher.generate_result(job_title, city)
        
        # Converting result_table to QTableView format to represent in GUI
        model = pandasmodel.PandasModel(result_table)
        self.job_table_web.setModel(model)
        
        # Storing website name so that we will use in the method below
        self.website_name = web_searcher.website_name
        
    def go_online(self):
        webbrowser.open(self.website_name)
        