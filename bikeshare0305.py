import csv
import datetime
from datetime import datetime
import time
import pandas as pd


def get_city():
    """Asks the user to select a city from a list of options.
    If city is incorrect, restarts loop.
    """
    city_input = (input("Let's look at some bike share data! \nSelect Chicago, New York, or Washington: \n"))
    if city_input.lower in ['Chicago', 'Washington']:
        k = city_input.lower() + '.csv'
        df = pd.read_csv(k)
        return k
    elif city_input.lower() in ['new york']:
        k = 'new_york_city.csv'
        df = pd.read_csv(k)
        return k
    elif city_input.lower() not in ['chicago', 'washington', 'new york']:
        print('Wrong city, try again.')
        get_city()


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

    while True:
        try:
            month = int(input('\nWhich month? Select 1: January, 2: February, 3: March, 4: April, 5: May, 6: June\n'))
        except ValueError:
            print("Enter a month between 1 and 6.")
        else:
            if 1 <= month < 7:
                break
            else:
                print("Enter a month between 1 and 6.")
    return month

    # TODO: handle raw input and complete function

def get_day():
    '''Asks the user for a day and returns the specified day.
    https://stackoverflow.com/questions/7854859/how-to-find-min-max-values-from-rows-and-columns-in-python

    Args:
        none.
    Returns:
        Returns day and month in 2017.
    '''
    input_date = input("Choose a day and month between 01/01/2017 and 06/01/2017 in the format of DD/MM/YY\n")
    day = pd.to_datetime(input_date)
    return day


def popular_month(k):
    '''
    Args:
        k=city_file
    Returns:
        Popular month without a time filter.
    '''
    for row in k:
        df = pd.read_csv(k)
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


def popular_day(k):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        Args:
        k=city_file
    Returns:
        Returns popular day without time period.
    '''

    for row in k:
        df = pd.read_csv(k)
        df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
        df['Start'] = pd.to_datetime(df.Start)
        popular = str(df.Start.dt.weekday_name.mode())
        print('Most Popular Day of Week: ' + popular)
        break

def popular_hour(k):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    Args:
        k=city_file
    Returns:
        Popular month without time period.
    '''
    for row in k:
        df = pd.read_csv(k)
        df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
        df['Start'] = pd.to_datetime(df.Start)
        popular = str(df.Start.dt.hour.mode())
        print('Popular Start Hour: ' + popular)
        break


def trip_duration(k, time_period):
    '''
    Question: What is the total trip duration and average trip duration?
    Args:
        k=city_file, time_period
    Returns:
        Returns trip duration using user selected city and time period.
    '''

    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = df['Start'].dt.weekday_name
        df.loc[df.day == + day]['Duration'].max() #how would I add the day argument into this. example: If day = 01/01/17 ?
        duration_max = (df.Duration.max())/60
        duration_avg = (df.Duration.mean())/60
        print('Maximum Trip Duration: ' + str(duration_max) + ' minutes')
        print('Minimum Trip Duration: ' + str(duration_avg) + ' minutes')
        return duration_max, duration_avg
    elif time_period == 'month':
        df['month'] = df['Start'].dt.to_period('M')
        df.loc[df.month == 'month']['Duration'].max()
        duration_max = (df.Duration.max())/60
        duration_avg = (df.Duration.mean())/60
        print('Maximum Trip Duration: ' + str(duration_max) + ' minutes')
        print('Minimum Trip Duration: ' + str(duration_avg) + ' minutes')
        return duration_max, duration_avg
    elif time_period == 'None':
        for row in k: # do I need this portion? Since there is no loop.
            duration_max = (df.Duration.max())/60
            duration_avg = (df.Duration.mean())/60
            print('Maximum Trip Duration: ' + str(duration_max) + ' minutes')
            print('Minimum Trip Duration: ' + str(duration_avg) + ' minutes')
            return duration_max, duration_avg

def popular_stations(k, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    Args:
        k=city_file, time_period
    Returns:
        Returns popular stations using user selected city file and time period.
    '''

    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    if time_period == 'None':
        for row in k:
            popular_start = (df.Start_Station.mode())
            popular_end = (df.End_Station.mode())
            print('Popular Start Station: ' + popular_start)
            print('Popular End Station: ' + popular_end)
            return popular_start, popular_end


def popular_trip(k, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function


def users(k, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    if time_period == 'None':
        for row in k:
            df = pd.read_csv(k)
            df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
            print("User Type Counts: \n")
            print(pd.value_counts(df['User_Type']))
            break


def gender(k, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    https://stackoverflow.com/questions/9247241/python-algorithm-of-counting-occurrence-of-specific-word-in-csv
    '''
    # TODO: complete function
    df = pd.read_csv(k)
    if time_period == 'None':
        for row in k:
            print("Gender Breakdown: \n")
            print(pd.value_counts(df['Gender']))
            break


def birth_years(k, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    if time_period == 'None':
        for row in k:
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
    k = get_city()

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

        popular_month(k)

        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        popular_day(k)

        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular hour of day for start time?
    popular_hour(k)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(k, time_period)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    popular_stations(k, time_period)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    popular_trip(k, time_period)

    print("That took %s seconds.\n" % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    users(time_period, k)

    print("That took %s seconds.\n" % (time.time() - start_time))

    if k != 'washington.csv':
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?
        gender(k, time_period)

        print("That took %s seconds.\n" % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        birth_years(k, time_period)

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
