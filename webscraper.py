# -*- coding: utf-8 -*-
"""
    This class is designed to receive requests from Window7 (Web Scraping Page) and get 
    data from indeed.com.
    
    It generates dataframe as a result which is then processed by respective class to display it 
    in QTableView

@author: Team Job Buddy
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

class WebScraping:
    
    
    def __init__(self):
        website_name = str()
    
    def extract_job_title_from_result(self, soup): 
        jobs = []
        for div in soup.find_all(name="div", attrs={"class":"row"}):
            for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
                jobs.append(a["title"])
        return(jobs)
  
    def extract_company_from_result(self, soup): 
        companies = []
        for div in soup.find_all(name="div", attrs={"class":"row"}):
            company = div.find_all(name="span", attrs={"class":"company"})
            if len(company) > 0:
                for b in company:
                    companies.append(b.text.strip())
            else:
                sec_try = div.find_all(name="span", attrs={"class":"result-link-source"})
                for span in sec_try:
                    companies.append(span.text.strip())
        return(companies)
        
    def generate_result(self, job_title, city):
        
        # Parts of URL
        website_begin = "https://www.indeed.com/jobs?q="
        website_mid = "+%2420%2C000&l=" 
        website_end = "&start=10"
        job_title = job_title.replace(" ",  "+")
        city = city.replace(" ",  "+")
        
        # URL Combined
        URL = website_begin+job_title+website_mid+city+website_end
        # Storing it in Class attribute so that we can use it in another class
        
        self.website_name = URL
        # Conducting a request of the stated URL above:
        page = requests.get(URL)
        
        #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
        soup = BeautifulSoup(page.text, "html.parser")
        
        job_title = self.extract_job_title_from_result(soup)
        company = self.extract_company_from_result(soup)
        
        # Creating dataframe and storing results
        df = pd.DataFrame()
        df["company"] = company
        df["job_title"] = job_title
        df["location"] = city.replace("+"," ")
        
        return df