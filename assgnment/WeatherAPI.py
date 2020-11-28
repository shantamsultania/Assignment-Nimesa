import csv
import requests
import pandas as pd


def set_data():
    complete_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London," \
                   "us&appid=b6907d289e10d714a6e88b30761fae22 "

    response = requests.get(complete_url)

    x = response.json()

    z = x['list']
    imp_data = []
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

    fields = ['index', 'date', 'time', 'wind speed', 'Temperature', 'wind Pressure']
    with open("records.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(imp_data)


def get_data(date, time, choice):
    df = pd.read_csv("records.csv")
    count = 0
    flag = 0
    for i in df['date']:
        if i == date:
            if choice == '1':
                if time == df.iloc[count, 2]:
                    flag += 1
                    print("date : ", str(i), "time", df.iloc[count, 2], "   temperature ", df.iloc[count, 4])
            elif choice == '2':
                if time == df.iloc[count, 2]:
                    flag += 1
                    print("date : ", str(i), "time", df.iloc[count, 2], "   wind speed ", df.iloc[count, 3])
            elif choice == '3':
                if time == df.iloc[count, 2]:
                    flag += 1
                    print("date : ", str(i), "time", df.iloc[count, 2], "   Pressure ", df.iloc[count, 5])
            else:
                print(" Not Valid Choice ")
            count += 1
