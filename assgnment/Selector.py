# This  class is responsible for the menu selection

from assgnment import WeatherAPI, System_check, Validator


def choice_maker():
    while True:
        print("  Welcome to Weather Guide   ")
        print("  Please choose from one of the options below ")
        print()
        print()
        print("  To Know The Temperature Please Press 1 : ")
        print()
        print("  To Know The Wind Speed  Please Press 2  : ")
        print()
        print("  To Know The Pressure    Please Press 3 : ")
        print()
        print("  To Exit The Program     Please Press 0 : ")
        print()
        print(" Enter your choice now ")
        choice = input()
        if choice == '1':
            print(" To know Temperature please Enter Date in YEAR-MONTH-DAY format a sample can be found below ")
            print("  Sample Date : 2019-03-28 ")
            print()
            while True:
                date = input()
                if Validator.valid_date(date):
                    break
                else:
                    print(" Please Enter a Valid Date in a Valid Date Format ")
                    print(" Sample Date : 2019-03-28 ")
            print( " To know the Temperature please Enter Time in the format as given in sample below ")
            print("  Sample Time : 20:00:00 ")
            while True:
                time = input()
                if Validator.valid_time(time):
                    WeatherAPI.get_data(date, time, choice)
                    break
                else:
                    print(" Please Enter a Valid Time in a Valid Time Format ")
                    print("  Sample Time : 20:00:00 ")

        elif choice == '2':
            print(" To know Wind Speed please Enter Date in YEAR-MONTH-DAY format a sample can be found below ")
            print("  Sample Date : 2019-03-28 ")
            print()
            while True:
                date = input()
                if Validator.valid_date(date):
                    break
                else:
                    print(" Please Enter a Valid Date in a Valid Date Format ")
                    print(" Sample Date : 2019-03-28 ")
            print(" To know the Wind Speed please Enter Time in the format as given in sample below ")
            print("  Sample Time : 20:00:00 ")
            while True:
                time = input()
                if Validator.valid_time(time):
                    WeatherAPI.get_data(date, time, choice)
                    break
                else:
                    print(" Please Enter a Valid Time in a Valid Time Format ")
                    print("  Sample Time : 20:00:00 ")
        elif choice == '3':
            print(" To know Pressure please Enter Date in YEAR-MONTH-DAY format a sample can be found below ")
            print("  Sample Date : 2019-03-28 ")
            print()
            while True:
                date = input()
                if Validator.valid_date(date):
                    break
                else:
                    print(" Please Enter a Valid Date in a Valid Date Format ")
                    print(" Sample Date : 2019-03-28 ")
            print(" To know the Pressure please Enter Time in the format as given in sample below ")
            print("  Sample Time : 20:00:00 ")
            while True:
                time = input()
                if Validator.valid_time(time):
                    WeatherAPI.get_data(date, time, choice)
                    break
                else:
                    print(" Please Enter a Valid Time in a Valid Time Format ")
                    print("  Sample Time : 20:00:00 ")
        elif choice == '0':
            print(" Thank you for your time ")
            exit(0)
        else:
            print(" Please enter Valid choice ")
