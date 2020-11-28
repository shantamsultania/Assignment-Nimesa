#  Coding Assignment for Nimesa Technologies Pvt. Ltd.

# About the Assignment

Write a program to get the option from the user and print the result based on the [API](https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22).

1. Get weather
2. Get Wind Speed
3. Get Pressure
0. Exit

If the user press 1, Prompt the user for the date then print the temp of the input date.
If the user press 2, Prompts the user for the date then print the wind speed of the input date.
If the user press 3, Prompt the user for the date then print the pressure of the input date.
If the user press 0, Terminate the program.

The program should not terminate until the user press 0.

# Solution

## Developing Environment Used 

### Python 

for downloading python just go to https://www.python.org/ and click download click or you can use this link this will download the latest version of python for you https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
after that, a .exe file will be downloaded just go through it and your Python is installed.

### Pycharm

To install Pycharm 

just go through this link and do the needful installation you can also refer to this video tutorial given below for reference 

https://www.jetbrains.com/pycharm/download/
[Video reference](https://www.youtube.com/watch?v=AUiM1UaRCPc) 

### Version control

1. Python 3.7
2. Pycharm 2020.1.0

## Libraries and other dependencies 

1) Request (To handle the request from the API)

3) JSON (to clean and organize the JSON data received from the API)

4) CSV (To store and retrieve the data in CSV format)

3) Pandas (To filter out the data)


##  JSON Data Analysis

After analysis of the data it was found that the date contains files as following:

1. cod -> Status Code of API 
2. message - > Status message for the API
3. cnt -> connection code
4. list - > This contains multiple data for multiple Dates 
5. city -> Name of City for which the API has been called example London 


## Source Code 

The whole code is divided into multiple subparts as followed:

1) SystemCheck.py 

Responsible to check for the installation of Libraries and Python Environment

2) Selector.py

Responsible to Display the Menu and accept user choice

3) Validator.py

Responsible for Validating the user input that is if the user has inputted a valid date and time in proper formate or not

4) WeatherAPI.py

Responsible for getting the JSON data from the API and filtering out the data in the proper format that has been sent to the user as well as saving the data in a CSV file.

5) Main.py

to execute the program

## OutPut 

1. Menu 

2. User input = 1

3. User input = 2

4. User input = 3

5. User input = 4







