# This  class is responsible for the menu selection

from assginment import WeatherAPI, System_check, Validator


# To display the menu and get the user Choice

def choice_maker():
    while True:
        print("      Welcome to Weather Guide   ")
        print()
        print("      To Know The Temperature Please Press 1 : ")
        print()
        print("      To Know The Wind Speed  Please Press 2  : ")
        print()
        print("      To Know The Pressure    Please Press 3 : ")
        print()
        print("      To Exit The Program     Please Press 0 : ")
        print()
        print("      Enter your choice when ready")
        choice = input()
        if choice == '1':
            print(" To know Temperature please Enter Date in YEAR-MONTH-DAY format a sample can be found below ")
            print("  Sample Date : 2019-03-28 ")
            print()
            # to Validate the Date
            while True:
                date = input()
                if Validator.valid_date(date):
                    break
                else:
                    print(" Please Enter a Valid Date in a Valid Date Format ")
                    print(" Sample Date : 2019-03-28 ")
            print(" To know the Temperature please Enter Time in the format as given in sample below ")
            print("  Sample Time : 20:00:00 ")
            # to Validate the time
            while True:
                time = input()
                if Validator.valid_time(time):
                    WeatherAPI.get_data(date, time, choice)
                    print()
                    print()
                    break
                else:
                    print(" Please Enter a Valid Time in a Valid Time Format ")
                    print("  Sample Time : 20:00:00 ")

        elif choice == '2':
            print(" To know Wind Speed please Enter Date in YEAR-MONTH-DAY format a sample can be found below ")
            print("  Sample Date : 2019-03-28 ")
            print()
            # to Validate the Date
            while True:
                date = input()
                if Validator.valid_date(date):
                    break
                else:
                    print(" Please Enter a Valid Date in a Valid Date Format ")
                    print(" Sample Date : 2019-03-28 ")
            print(" To know the Wind Speed please Enter Time in the format as given in sample below ")
            print("  Sample Time : 20:00:00 ")
            # to Validate the Time
            while True:
                time = input()
                # calling the Validator to check the time
                if Validator.valid_time(time):
                    # calling the WeatherAPI to display the Required data
                    WeatherAPI.get_data(date, time, choice)
                    print()
                    print()
                    break
                else:
                    print(" Please Enter a Valid Time in a Valid Time Format ")
                    print("  Sample Time : 20:00:00 ")
        elif choice == '3':
            print(" To know Pressure please Enter Date in YEAR-MONTH-DAY format a sample can be found below ")
            print("  Sample Date : 2019-03-28 ")
            print()
            # to Validate the Date
            while True:
                date = input()
                if Validator.valid_date(date):
                    break
                else:
                    # if The Date is not Valid the program will ask for a valid date
                    print(" Please Enter a Valid Date in a Valid Date Format ")
                    print(" Sample Date : 2019-03-28 ")
            print(" To know the Pressure please Enter Time in the format as given in sample below ")
            print("  Sample Time : 20:00:00 ")
            # to Validate the Time
            while True:
                time = input()
                if Validator.valid_time(time):
                    WeatherAPI.get_data(date, time, choice)
                    print()
                    print()
                    break
                else:
                    print(" Please Enter a Valid Time in a Valid Time Format ")
                    print("  Sample Time : 20:00:00 ")
        elif choice == '0':
            # To Exit from the program
            print(" Thank you for your time ")
            print()
            print()
            exit(0)
        else:
            # check fro valid choice
            print(" Please enter Valid choice ")
            print()
            print()
