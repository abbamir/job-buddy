## Desktop Application Development using Python

Good day! I would like to talk about how I used Python programming language to develop great desktop application. However, before I talk about the development process, I wanted to talk about why Python is a great tool to employ.

### Little bit about Job Buddy
![Imgur](https://i.imgur.com/cJa7Wab.png)

As an international student in the US, I realized that it's not easy to land a job in a very competitive market where you have hundreds of companies and millions of applications. As the competition is fierce and candidates compete on hundreds of companies, it is important to have one place where a candidate can store his/her details on applications submitted. The application can then help the application see what company s/he applied and what was the verdict and sort the results by the applied date. 

#### Overall Structure
![Imgur](https://i.imgur.com/1qw9WVO.png)

The picture above presents the overall structure of the Deskop application and how interaction happens among pages. 

#### Advanced function -> Web Scraping
![Imgur](https://i.imgur.com/LOXDOVx.png)
Job Buddy also has advanced feature of web scraping that takes Job Position and Location as inputs and returns the results by search on Indeed.com platform. 

### Technologies used
#### 1. Frontend - PyQT

Python is an Object Oriented Programming (OOP) language and thus efforts are concentrated around objects that represent real world objects. In order to develop desktop application, we should use a framework that can objectify front-end of our application. There are many GUI frameworks for Python but I chose to work on [PyQT](https://riverbankcomputing.com/software/pyqt/intro). 

#### 2. Backend - DataFrame

As I primarily used Python for Data Analysis, it's no wonder why I used Data Frames to store user details and Job details. 
