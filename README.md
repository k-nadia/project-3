# **WeatherWise** 

<br>

![GitHub last commit](https://img.shields.io/github/last-commit/k-nadia/project-3?color=red&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/k-nadia/project-3?color=orange&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/k-nadia/project-3?color=yellow&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/k-nadia/project-3?color=green&style=for-the-badge)

<hr>

# **Introduction**


Portfolio Project 2 - Code Institute Full Stack Development Diploma

WeatherWise is a Python-based command line application that offers current, daily and historic weather insights based on the user's location. The application utilises API to retrieve up-to-date accurate weather data and runs via a mock terminal on Heroku. JSON is used in this project to retrieve, parse and present weather API data to the user.

WeatherWise was designed as an ultra-efficient solution for users who require access to weather information at a moments notice. The no-frills, data-driven interface eliminates elements typical of a traditional weather info site which can hinder data delivery speed and negatively impact the user expierience, such as: ads, slow-loading graphics, unrelated content, cookies and complex navigation menus.

Deployed website can be be found here:

<p align="center">
<img src ="assets/images/am-i-responsive-placeholder-image.JPG" width="auto" height="auto" alt="AmIResponsive placeholder image showing the following viewports: desktop, laptop, tablet, mobile">
</p>

# Table of Contents

- [Design](#design)
	- [Colours](#colours)
- [User Experience - UX](#user-experience---ux)
	- [User Stories](#user-stories)
- [Logic](#logic)
	- [Flow Charts](#flow-charts)
- [Features](#features)
	- [Navigation](#navigation)
- [Testing](#testing)
    - [General App Testing](#general-app-testing)
    - [PEP8 Validator Service](#pep8-validator-service)
    - [Google Chrome Lighthouse Tool](#google-chrome-lighthouse-tool)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Deployment Steps](#deployment-steps)
    - [Forking Steps](#forking-steps)
    - [Cloning Steps](#cloning-steps)    
- [Technologies Used](#technologies-used)
	- [Languages Used](#languages-used)
    - [Python Packages](#python-packages)
	- [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
- [Credits](#credits)
	- [Content Sources](#content-sources)
    - [Information Resources](#information-resources)
    - [Special Thanks](#special-thanks)

<hr>

## **Design**

### **Colours**

<hr>

## **User Experience - UX**

### **User Stories**

As a user, I wish to:

- Immediately understand the purpose of the application, so I can quickly determine if it meets my needs.
- Receive clear feedback on invalid inputs, so I can quickly correct my entries and proceed with using the application.
- Input my country and city easily, so I can get localized weather information relevant to my area.
- View the current weather forecast, so I can plan my immediate activities accordingly.
- See the daily weather forecast, so I can plan my week and make informed decisions about upcoming events.
- Be notified of any national weather alerts, so I can stay safe and prepared for potential severe weather conditions.
- Access historical weather data, so I can compare current conditions with past trends and make long-term plans.
- Use a simple and intuitive interface, so I can navigate the application easily without needing extensive instructions.

As a developer, I wish to: 

- Access a README file so that I can understand the scope and purpose of the project and locate essential information regarding the application
- Access deployment information so I can follow step-by-step instructions on how to deploy the project

<hr>

## **Logic**

### **Flow Charts**

[LucidChart](https://www.lucidchart.com/) was used create a flowchart to visualise the programming sequence.
![LucidChart Flowchart Image](./assets/images/README/flowchart.png)

<hr>

## **Features**

### **Navigation**

<hr>

## **Testing**

### **General App Testing**

### **PEP8 Validator Service**
![PEP8](https://img.shields.io/badge/PEP8-0078D7?style=for-the-badge&logo=pep8&logoColor=white)

### **Google Chrome Lighthouse Tool**

### **Unfixed Bugs**

<hr>

## **Deployment**

### **Deployment Steps**
Deploy this project using the following steps:

#### **Heroku Log In**
1. Log in to [Heroku](https://id.heroku.com/login) or create a new Heroku account [here](https://signup.heroku.com/).
2. Click 'Create New App' and enter a unique app name.
3. Select your region from the drop-down menu.
4. Click on the 'Create App' button.

#### **Adjust Settings**
5. Navigate to the 'Settings' tab.
6. Scroll down to 'Config Vars' and select 'Reveal Config Vars'.
7. Type 'PORT' into the key box and '8000' into the value box, then click 'Add'.
8. Enter a second config var: enter 'CREDS' into the key box, copy and paste the contents of your creds.JSON file into the value box, then click 'Add'.
9. Scroll down to 'Buildpack'and click 'Add Buildpack'.
10. Select 'Python' and click 'Save Changes'.
11. Select 'NODE.js' and click 'Save Changes (note: buildpacks must be in this order).

#### **Deploy Application**
12. Click on the 'Deploy' tab and select 'GitHub'.
13. Confirm you wish to connect to GitHub.
14. Search for the repository name and then click 'Connect'.
15. Scroll down and either select 'Enable Automatic Deploys' (for automatic deployment of any changes made to GitHub repository) or select 'Deploy Branch' (for manual deployment).

### **Forking Steps**
Fork this project using the following steps:
1. Open the respository at [PP3 Github](https://github.com/k-nadia/project-3).
2. Select the 'Fork' button near the top of the page.
3. After a few minutes the newly forked repository will be created under your GitHub account.

### **Cloning Steps**
Clone this project using the following steps:
1. Open the respository at [PP3 Github](https://github.com/k-nadia/project-3).
2. Select the green 'Code' button near the top of the page.
3. Choose from one of the 3 cloning options: HTTPS, SSH, GitHub CLI.
4. Click on the clipboard icon to copy the URL.
5. Open a new GitPod terminal.
6. Type 'git clone' and paste in the URL copied earlier.
7. Press enter to complete the cloning process. 


<hr>

## **Technologies Used**

### **Languages Used**
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### **Python Packages**
- [Colorama:](https://pypi.org/project/colorama/) enables coloured text display in the terminal
- [DateTime:](https://pypi.org/project/DateTime/) provides DataTime data type
- [PPrint:](https://docs.python.org/3/library/pprint.html) enables python output to be properly formatted 
- [Requests:](https://pypi.org/project/requests/) allows HTTP requests to be sent

### **Frameworks - Libraries - Programs Used**

- ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) - Version control system used to track file versions within the project.
- ![Github](https://img.shields.io/badge/github-121013?style=for-the-badge&logo=github&logoColor=white) - Cloud-based version control developer platform used in this project to host the repository, manage code and track code changes.
- ![Gitpod](https://img.shields.io/badge/gitpod-f06611.svg?style=for-the-badge&logo=gitpod&logoColor=white) - Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. Used for version control. 
- ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) - Cloud platform used to deploy the live project.
- ![Lucidchart](https://img.shields.io/badge/Lucidchart-FF7139?style=for-the-badge) - Web-based diagramming application used to create the flowchart which will visualise the project code excecution process.
- ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) - Open-source Javascript runtime environment used for asynchronous programming.
- ![PEP8](https://img.shields.io/badge/PEP8-0078D7?style=for-the-badge&logo=pep8&logoColor=white) - Python style checker used to validate all the Python code within the project.
- ![VS Code](https://img.shields.io/badge/VS%20Code%20-35b393.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) - Code editor platform used to create and edit the project code.

<hr>

## **Credits**

### **Content Sources**

### **Information Resources**

### **Special Thanks**