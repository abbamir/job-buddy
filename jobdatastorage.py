# -*- coding: utf-8 -*-
"""
This page is responsible only for storing job-related information 
and only communicates with jobadderwindow class. 

@author: Team Job Buddy
"""

import pandas as pd 

class JobData (object):
    
    try:
        lf = pd.read_csv("database/job_details.csv")
    except:
        lf = pd.DataFrame(columns=["jobtitle","company","location", 
                           "deadline","applicationstatus","jobdescription", "username"])
        lf.to_csv("database/job_details.csv")
    
    def __init__(self):
        pass
    
    def store(self, jobtitle, company, location, deadline, applicationstatus, jobdescription, email):
        self.lf = self.lf.append({"jobtitle":jobtitle,"company":company,
                                  "location":location, "deadline":deadline, 
                                  "applicationstatus":applicationstatus,
                                  "jobdescription":jobdescription, "username":email}, ignore_index=True) 
        self.lf.to_csv("database/job_details.csv", index=False)
    