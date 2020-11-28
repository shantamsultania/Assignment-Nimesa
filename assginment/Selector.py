# This  class is responsible for the menu selection

from assginment import WeatherAPI, System_check, Validator


# To display the menu and get the user Choice

def choice_maker():
    while True:
        print("      Welcome to Weather Guide   ")
        print()
        print("      Press 1 : To get Temperature Details ")
        print()
        print("      Press 2  : To get Wind Speed ")
        print()
        print("      Press 3 : To get Pressure ")
        print()
        print("      Press 0 : To exit the program ")
        print()
        print("      Enter your choice ")
        choice = input()
        if '1' <= choice <= '3':
            print("  Enter Date in YYYY-MM-DD format  \n")
            # to Validate the Date
            while True:
                date = input()
                if Validator.valid_date(date):
                    break
                else:
                    print(" Please enter a Valid Date in a Valid Format Example 2019-03-28 ")
            print(" Enter Time in HH:MM:SS format ")
            # to Validate the time
            while True:
                time = input()
                if Validator.valid_time(time):
                    print()
                    WeatherAPI.get_data(date, time, choice)
                    print()
                    break
                else:
                    print(" Enter a Valid Time in a Valid Time Format Example 20:00:00 ")
        elif choice == '0':
            # To Exit from the program
            print(" Thank you for your time ")
            exit(0)
        else:
            # check fro valid choice
            print(" Please enter Valid choice ")
            print()
            print()