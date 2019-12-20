# -*- coding: utf-8 -*-
"""
This class is responsible for initiating all windows stored as separate classes.

It's called Controller class because it controls what page should come up after
particular button click or is responsible for inter-page communication

@author: Team Job Buddy
"""

from PyQt5 import QtWidgets
import sys

#local classes
import mainwindow, signupwindow, signinwindow, joblistwindow, jobadderwindow, webscrapingwindow

class Controller:
    
    # Username variable should be accessible by all classes because it is used
    # by many classes
    username = str()
    
    def __init__(self):
        pass
    
    # Method for initializing Main window
    def show_MainWindow(self):
        self.mainWindow = mainwindow.MainWindow()
        self.mainWindow.switch_window.connect(self.show_SignupWindow)
        self.mainWindow.switch_signinwindow.connect(self.show_SigninWindow)
        self.mainWindow.show()
    
    # Method for initializing sign up window
    def show_SignupWindow(self):
        self.signupWindow = signupwindow.SignupWindow()
        self.mainWindow.close()
        
        try:
            self.signinWindow
        except:
            self.mainWindow.close()
        else:
            self.signinWindow.close()
            
        self.signupWindow.switch_window.connect(self.show_JoblistWindow)
        self.signupWindow.switch_to_window_2.connect(self.show_SigninWindow)
        self.signupWindow.show()
        
    # Method for initializing sign in window
    def show_SigninWindow(self):
        self.signinWindow = signinwindow.SigninWindow()
        # Exception handling to correctly identify what page should be closed
        try:
            self.signupWindow
        except:
            self.mainWindow.close()
        else:
            self.signupWindow.close()
            
        self.signinWindow.switch_window3.connect(self.show_SignupWindow)
        self.signinWindow.switch_window4.connect(self.show_JoblistWindow)
        self.signinWindow.show()
        
    # Method for initializing job adder window    
    def show_JobAdderWindow(self):
        # Storing username from signup window or sign in window
        # dependending on which class was instantiated.
        try:
            self.username = self.signupWindow.email_enter.text()
        except:
            self.username = self.signinWindow.email_enter.text()
        else:
            self.username = self.signupWindow.email_enter.text()
        
        self.jobadderWindow = jobadderwindow.JobAdderWindow(self.username)
        self.joblistWindow.close()
        self.jobadderWindow.switch_window_to_JoblistWindow.connect(self.show_JoblistWindow)
        self.jobadderWindow.show()
        
    # Method for initializing webscraping window    
    def show_WebScrapingWindow(self):
        self.webscrapingWindow = webscrapingwindow.WebScrapingWindow()
        self.joblistWindow.close()
        self.webscrapingWindow.switch_window_to_JoblistWindow.connect(self.show_JoblistWindow)
        self.webscrapingWindow.show()   
        
    def show_JoblistWindow(self):
        # Storing username from signup window or sign in window
        # dependending on which class was instantiated.
        try:
            self.username = self.signupWindow.email_enter.text()
        except:
            self.username = self.signinWindow.email_enter.text()
        else:
            self.username = self.signupWindow.email_enter.text()
            
        self.joblistWindow = joblistwindow.JoblistWindow(self.username)
        
        # Exception handling for page switching - since this is a central page
        # - it has many exceptions
        try: #SigninWindow
            self.signinWindow
        except:
            try: #SignUpWindow
                self.signupWindow
            except:
                try: #JobAdderWindow
                    self.jobadderWindow
                except:
                    try:
                        self.webscrapingWindow
                    except:
                        pass
                    else:
                        self.webscrapingWindow.close()
                else:
                    self.jobadderWindow.close()
            else:
                self.signupWindow.close()
        else:
            self.signinWindow.close()
            
        self.joblistWindow.switch_window_JobAdderWindow.connect(self.show_JobAdderWindow)
        self.joblistWindow.switch_window_WebScrapingWindow.connect(self.show_WebScrapingWindow)
        self.joblistWindow.show()
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_MainWindow()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()