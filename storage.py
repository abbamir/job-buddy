# -*- coding: utf-8 -*-
"""
Data storage class for storing data from Sign up page

@author: Team Job Buddy
"""

import pandas as pd 

class Authorization(object):
    
    try:
        lf = pd.read_csv("database/user_details.csv")
    except:
        lf = pd.DataFrame(columns=["firstname","lastname","school", 
                           "degree","job_title","company","email","password"])
        lf.to_csv("database/user_details.csv")
        
    def __init__(self):
        pass
    
    def store(self, firstname, lastname, school, degree, job_title, company, email, password):
        self.lf = self.lf.append({"firstname":firstname,"lastname":lastname,
                                  "school":school, "degree":degree, "job_title":job_title,
                                  "company":company, "email":email, "password":password}, ignore_index=True) 
        self.lf.to_csv("database/user_details.csv", index=False)