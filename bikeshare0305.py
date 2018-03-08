import csv
import datetime
from datetime import datetime
import time
import pandas as pd


def get_city():
    """Asks the user to select a city from a list of options.
    If city is incorrect, restarts loop.
    """
    while True:
        city_input = (input("Let's look at some bike share data! \nSelect Chicago, New York, or Washington: \n"))
        city_file = ''
        if city_input.lower() in ['chicago', 'washington']:
            city_file = city_input + ".csv"
        elif city_input.lower() in ['new york']:
            city_file = 'new_york_city.csv'
        else:
            print('Wrong city, try again.')
            get_city()
        return city_file

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        January - June
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function
    time_period = (input('\nWould you like to filter the data by month, day, or not at'
                             ' all? Type "none" for no time filter.\n'))
    if time_period.lower() == 'month':
        print("Okay, we will filter by month.")
    elif time_period.lower() == 'day':
        print("Okay, we will filter by a day of a month.")

    elif time_period.lower() == 'none':
        print("Okay, no filter requested.")
    else:
        get_time_period()
    return time_period

def get_month():
    '''Asks the user for a month and returns the specified month.
    https://stackoverflow.com/questions/14533709/basic-python-programming-to-convert-month-number-to-month-name-using-dictionary
    https://stackoverflow.com/questions/13774649/how-to-convert-a-month-number-into-a-month-name-in-python
    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DatetimeIndex.month.html

    Args:
        none.
    Returns:
        Returns index of month in Pandas DatetimeIndex 1=January, 2=February, etc.
    '''

    month = (input('\nWhich month? Select January, February, March, April, May, or June.\n'))
    if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june']:
        return month
    else:
        print('Please select a valid month.')
    get_month()

    # TODO: handle raw input and complete function

def get_day():
    '''Asks the user for a day and returns the specified day.
    https://stackoverflow.com/questions/7854859/how-to-find-min-max-values-from-rows-and-columns-in-python

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    input_date = input("Choose a day and month between 01/01/2017 and 06/01/2017 in the format of DD/MM/YY\n")
    day = pd.to_datetime(input_date)
    return day


def popular_month(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    for row in city_file:
        df = pd.read_csv(city_file)
        df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
        df['Start'] = pd.to_datetime(df.Start)
        popular = str(df.Start.dt.month.mode())
        if popular == '1':
            print('Popular Month: January')
            break
        elif popular == '2':
            print('Popular Month: February')
            break
        elif popular == '3':
            print('Popular Month: March')
            break
        elif popular == '4':
            print('Popular Month: April')
            break
        elif popular == '5':
            print('Popular Month: May')
            break
        elif popular == '6':
            print('Popular Month: June')
            break

    # TODO: complete function


def popular_day(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    for row in city_file:
        df = pd.read_csv(city_file)
        df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
        df['Start'] = pd.to_datetime(df.Start)
        popular = str(df.Start.dt.weekday_name.mode())
        print('Most Popular Day of Week: ' + popular)
        break



def popular_hour(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    for row in city_file:
        df = pd.read_csv(city_file)
        df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
        df['Start'] = pd.to_datetime(df.Start)
        popular = str(df.Start.dt.hour.mode())
        print('Popular Start Hour: ' + popular)
        break


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = df['Start'].dt.weekday_name
        df.loc[df.day == '*whatever day"]['Duration'].max()
            duration_max = (df.Duration.max())/60
            duration_avg = (df.Duration.mean())/60
            print('Maximum Trip Duration: ' + str(duration_max) + ' minutes')
            print('Minimum Trip Duration: ' + str(duration_avg) + ' minutes')
            return duration_max, duration_avg
    elif time_period == 'month':
        df['month'] = df['Start'].dt.weekday_name
        df.loc[df.month == '*whatever day"]['Duration'].max()
        duration_max = (df.Duration.max())/60
        duration_avg = (df.Duration.mean())/60
        print('Maximum Trip Duration: ' + str(duration_max) + ' minutes')
        print('Minimum Trip Duration: ' + str(duration_avg) + ' minutes')
        return duration_max, duration_avg
    elif time_period == 'None':
        for row in city_file:
            duration_max = (df.Duration.max())/60
            duration_avg = (df.Duration.mean())/60
            print('Maximum Trip Duration: ' + str(duration_max) + ' minutes')
            print('Minimum Trip Duration: ' + str(duration_avg) + ' minutes')
            return duration_max, duration_avg

def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function

    df = pd.read_csv(city_file)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    if time_period == 'None':
        for row in city_file:
            popular_start = (df.Start_Station.mode())
            popular_end = (df.End_Station.mode())
            print('Popular Start Station: ' + popular_start)
            print('Popular End Station: ' + popular_end)
            return popular_start, popular_end


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    if time_period == 'None':
        for row in city_file:
            df = pd.read_csv(city_file)
            df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
            print("User Type Counts: \n")
            print(pd.value_counts(df['User_Type']))
            break


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    https://stackoverflow.com/questions/9247241/python-algorithm-of-counting-occurrence-of-specific-word-in-csv
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    if time_period == 'None':
        for row in city_file:
            print("Gender Breakdown: \n")
            print(pd.value_counts(df['Gender']))
            break


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    if time_period == 'None':
        for row in city_file:
            oldest_user = int(datetime.now().year - (df.Birth_Year.min()))
            youngest_user = int(datetime.now().year - (df.Birth_Year.max()))
            popular_birth = int(datetime.now().year - (df.Birth_Year.mode()))
            print('Oldest User: ' + str(oldest_user))
            print('Youngest User: ' + str(youngest_user))
            print('Frequent User Age: ' + str(popular_birth))
            return oldest_user, youngest_user, popular_birth


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    '''

    # Filter by city (Chicago, New York, Washington) and load the file
    city_file = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'month':
        month = get_month()
    elif time_period == 'day':
        day = get_day()
    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        popular_month(city_file)

        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        popular_day(city_file)

        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular hour of day for start time?
    popular_hour(city_file)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(city_file, time_period)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    popular_stations(city_file, time_period)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    popular_trip(city_file, time_period)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    users(time_period, city_file)

    print("That took %s seconds.\n" % (time.time() - start_time))

    if city_file != 'washington.csv':
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?
        gender(city_file, time_period)

        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        birth_years(city_file, time_period)

        print("That took %s seconds.\n" % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like t

    # Restart?
    restart = input('\nWould you like to restart? Type \'Y\' or \'N\'.\n')
    if restart == 'Y':
        statistics()


if __name__ == "__main__":
    statistics()





#What is the most popular month for start time?
#What is the most popular day of week (Monday, Tuesday, etc.) for start time? Hint: datetime.weekday() (documentation here) may be helpful!
#What is the most popular hour of day for start time?
#What is the total trip duration and average trip duration?
#What is the most popular start station and most popular end station?
#What is the most popular trip?
#What are the counts of each user type?
#What are the counts of gender?
#What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years?