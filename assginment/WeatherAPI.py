import csv
import requests
import pandas as pd


#  This function is to get the data from the API and Save it in a CSV file
def set_data():
    complete_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London," \
                   "us&appid=b6907d289e10d714a6e88b30761fae22 "

    # Request Response from the API provided
    response = requests.get(complete_url)
    # Get the Response from the API in json format
    x = response.json()
    # Get the Required field from the Json DATA
    z = x['list']
    # create an Array of Array of the data provided
    imp_data = []
    # to keep teh count of data
    j = 0
    for i in z:
        temp = []
        j1 = i['main']
        j2 = i['wind']
        j3 = i['dt_txt']
        date = j3.split()
        j += 1
        date.append(date[0])
        temp.append(j)
        temp.append(date[0])
        temp.append(date[1])
        temp.append(j2['speed'])
        temp.append(j1['temp'])
        temp.append(j1['pressure'])
        imp_data.append(temp)
    # column names
    fields = ['index', 'date', 'time', 'wind speed', 'Temperature', 'wind Pressure']
    # to create a new CSV file names records.csv
    with open("records.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(imp_data)


# This is to get the data from the CSV file
def get_data(date, time, choice):
    # importing the CSV files
    df = pd.read_csv("records.csv")
    count = 0
    flag = 0
    # checking if date is present or not
    for i in df['date']:
        if i == date:
            flag = +1
            # if date is present check for choice
            if choice == '1':
                # then check for Time
                if time == df.iloc[count, 2]:
                    flag += 1
                    print("Date : ", str(i), " Time : ", df.iloc[count, 2], "   Temperature(in Fahrenheit) : ", df.iloc[count, 4])
            elif choice == '2':
                if time == df.iloc[count, 2]:
                    flag += 1
                    print("Date : ", str(i), " Time : ", df.iloc[count, 2], "   Wind Speed(in KMPH ) ", df.iloc[count, 3])
            elif choice == '3':
                if time == df.iloc[count, 2]:
                    flag += 1
                    print("Date : ", str(i), " Time: ", df.iloc[count, 2], "   Pressure(in atm) ", df.iloc[count, 5])
            count += 1
    if flag == 0:
        print("Data for the current date or Time if not present in teh API for now ")
