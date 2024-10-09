from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

display_current_datetime()


days = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date():
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days)
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(future_date)

calculate_future_date()