import datetime
from datetime import datetime
import pandas as pd
import time


def get_city():
    """Asks the user to select a city from a list of options.
    If city is incorrect, restarts loop.
    """
    city_input = (input("Let's look at some bike share data! \nSelect Chicago, New York, or Washington: \n"))
    if city_input.lower() in ['chicago']:
        k = 'chicago.csv'
        return k
    elif city_input.lower() in ['washington']:
        k = 'washington.csv'
        return k
    elif city_input.lower() in ['new york']:
        k = 'new_york_city.csv'
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
    Args:
        none.
    Returns:
        Returns index of month in Pandas DatetimeIndex 1=January, 2=February, etc.
    '''

    while True:
        try:
            month_or_day = int(input('\nWhich month? Select 1: January, 2: February, 3: March, 4: April, 5: May, 6: June\n'))
        except ValueError:
            print("Enter a month between 1 and 6.")
        else:
            if 1 <= month_or_day < 7:
                break
            else:
                print("Enter a month between 1 and 6.")
    return month_or_day

    # TODO: handle raw input and complete function

def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        Returns day and month in 2017.
    '''
    input_date = input("Choose a day and month between 01/01/2017 and 06/01/2017 in the format of MM/DD/YY\n")
    month_or_day = pd.to_datetime(input_date)
    return month_or_day


def popular_month(k):
    '''
    Args:
        k=city_file
    Returns:
        Popular month without a time filter.
    '''

    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df.Start)
    popular = str(df.Start.dt.month.mode())
    print("Popular month: " + popular)


def popular_day(k):
    '''
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        Args:
        k=city_file
    Returns:
        Returns popular day without time period.
    '''

    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df.Start)
    popular = str(df.Start.dt.weekday_name.mode())
    print('Most Popular Day of Week: ' + popular)


def popular_hour(k):
    '''
    Question: What is the most popular hour of day for start time?
    Args:
        k=city_file
    Returns:
        Popular month without time period.
    '''
    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df.Start)
    popular = str(df.Start.dt.hour.mode())
    print('Popular Start Hour: ' + popular)


def trip_duration(k, time_period, month_or_day):
    '''
    Question: What is the total trip duration and average trip duration?
    Args:
        k=city_file, time_period, month_or_day
    Returns:
        Returns trip duration using user selected city and time period.
    '''

    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = pd.to_datetime(df['Start'].dt.date)
        duration = df.loc[df.day == month_or_day, :]
        duration_max = duration.Duration.max() // 60
        duration_mean = duration.Duration.mean() // 60
        print("Max Trip Duration: " + str(duration_max) + " minutes.")
        print("Average Trip Duration: " + str(duration_mean) + " minutes.")
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        duration = df.loc[df.month == month_dt, :]
        duration_max = duration.Duration.max() // 60
        duration_mean = duration.Duration.mean() // 60
        print("Maximum Trip Duration: " + str(duration_max) + " minutes.")
        print('Minimum Trip Duration: ' + str(duration_mean) + " minutes.")
    elif time_period == 'none':
        duration_max = (df.Duration.max())//60
        duration_mean = (df.Duration.mean())//60
        print("Maximum Trip Duration: " + str(duration_max) + " minutes.")
        print('Minimum Trip Duration: ' + str(duration_mean) + " minutes.")
    else:
        get_city()

def popular_stations(k, time_period, month_or_day):
    '''
    Question: What is the most popular start station and most popular end station?
    Args:
        k=city_file, time_period, month_or_day
    Returns:
        Returns popular stations using user selected city file and time period.
    '''

    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = pd.to_datetime(df['Start'].dt.date)
        popular = df.loc[df.day == month_or_day, :]
        popular_start = popular.Start_Station.mode()
        popular_end = popular.End_Station.mode()
        print('Popular Start Station: ' + popular_start)
        print('Popular End Station: ' + popular_end)
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        popular = df.loc[df.month == month_dt, :]
        popular_start = popular.Start_Station.mode()
        popular_end = popular.End_Station.mode()
        print('Popular Start Station: ' + popular_start)
        print('Popular End Station: ' + popular_end)
    if time_period == 'none':
        popular_start = (df.Start_Station.mode())
        popular_end = (df.End_Station.mode())
        print('Popular Start Station: ' + popular_start)
        print('Popular End Station: ' + popular_end)
        return popular_start, popular_end


def popular_trip(k, time_period, month_or_day):
    '''
    Question: What is the most popular trip?
    Args:
        k=city_file, time_period, month_or_day
    Returns:
        most popular trip
    '''
    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = pd.to_datetime(df['Start'].dt.date)
        popular = df.loc[df.day == month_or_day, :]
        popular_start = popular.df.groupby(["Group", "Size"]).size().reset_index(name="Time")
        popular_end = popular.End_Station.mode()
        print('Popular Start Station: ' + popular_start)
        print('Popular End Station: ' + popular_end)
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        popular = df.loc[df.month == month_dt, :]
        popular_start = popular.Start_Station.mode()
        popular_end = popular.End_Station.mode()
        print('Popular Start Station: ' + popular_start)
        print('Popular End Station: ' + popular_end)
    if time_period == 'none':
        popular_start = (df.Start_Station.mode())
        popular_end = (df.End_Station.mode())
        print('Popular Start Station: ' + popular_start)
        print('Popular End Station: ' + popular_end)
        return popular_start, popular_end


def users(k, time_period, month_or_day):
    '''
    Question: What are the counts of each user type?
    Arguments:
        k=city_file, time_period, month_or_day
    Returns:
        Counts of each user within time frame
    '''
    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = pd.to_datetime(df['Start'].dt.date)
        day_period = df.loc[df.day == month_or_day, :]
        user_count = pd.value_counts(day_period['User_Type'])
        print("User Types: \n")
        print(user_count)
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        month_period = df.loc[df.month == month_dt, :]
        user_count = pd.value_counts(month_period['User_Type'])
        print("User Types: \n")
        print(user_count)
    elif time_period == 'none':
        print("User Types: \n")
        print(pd.value_counts(df['User_Type']))
    else:
        users(k, time_period, month_or_day)


def gender(k, time_period, month_or_day):
    '''
    Question: What are the counts of gender?
    Arguments:
        k, time_period, month_or_Day
    Returns:
        Gender counts per time frame
    '''
    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = pd.to_datetime(df['Start'].dt.date)
        day_period = df.loc[df.day == month_or_day, :]
        gender_count = pd.value_counts(day_period['Gender'])
        print("Gender Breakdown: \n")
        print(gender_count)
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        month_period = df.loc[df.month == month_dt, :]
        gender_count = pd.value_counts(month_period['Gender'])
        print("Gender Breakdown: \n")
        print(gender_count)
    elif time_period == 'none':
        print("Gender Breakdown: \n")
        print(pd.value_counts(df['Gender']))
    else:
        gender(k, time_period, month_or_day)


def birth_years(k, time_period, month_or_day):
    '''
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Arguments:
        k, time_period, month_or_day
    Returns:
        Oldest User, Youngest User, Popular Birth
    '''
    df = pd.read_csv(k)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                       'Start Station': 'Start_Station', 'End Station': 'End_Station',
                       'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    if time_period == 'day':
        df['day'] = pd.to_datetime(df['Start'].dt.date)
        day_period = df.loc[df.day == month_or_day, :]
        oldest_user = int(datetime.now().year - day_period.Birth_Year.min())
        youngest_user = int(datetime.now().year - day_period.Birth_Year.max())
        popular_birth = int(datetime.now().year - day_period.Birth_Year.mode())
        print('Oldest User: ' + str(oldest_user))
        print('Youngest User: ' + str(youngest_user))
        print('Frequent User Age: ' + str(popular_birth))
        return oldest_user, youngest_user, popular_birth
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        month_period = df.loc[df.month == month_dt, :]
        oldest_user = int(datetime.now().year - month_period.Birth_Year.min())
        youngest_user = int(datetime.now().year - month_period.Birth_Year.max())
        popular_birth = int(datetime.now().year - month_period.Birth_Year.mode())
        print('Oldest User: ' + str(oldest_user))
        print('Youngest User: ' + str(youngest_user))
        print('Frequent User Age: ' + str(popular_birth))
        return oldest_user, youngest_user, popular_birth
    elif time_period == 'none':
        oldest_user = int(datetime.now().year - (df.Birth_Year.min()))
        youngest_user = int(datetime.now().year - (df.Birth_Year.max()))
        popular_birth = int(datetime.now().year - (df.Birth_Year.mode()))
        print('Oldest User: ' + str(oldest_user))
        print('Youngest User: ' + str(youngest_user))
        print('Frequent User Age: ' + str(popular_birth))
        return oldest_user, youngest_user, popular_birth


def statistics():
    '''
    Arguments:
        None
    Returns:
        Bikeshare statistics
    '''
    k = get_city()
    time_period = get_time_period()
    if time_period == 'month':
        month_or_day = get_month()
        trip_duration(k, time_period, month_or_day)
        popular_stations(k, time_period, month_or_day)
        #popular_trip(k, time_period, month_or_day)
        users(k, time_period, month_or_day)
        if k != 'washington.csv':
            gender(k, time_period, month_or_day)
            birth_years(k, time_period, month_or_day)
    if time_period == 'day':
        month_or_day = get_day()
        trip_duration(k, time_period, month_or_day)
        popular_stations(k, time_period, month_or_day)
        #popular_trip(k, time_period, month_or_day)
        users(k, time_period, month_or_day)
        if k != 'washington.csv':
            gender(k, time_period, month_or_day)
            birth_years(k, time_period, month_or_day)
    if time_period == 'none':
        month_or_day = 0
        popular_month(k)
        popular_hour(k)
        trip_duration(k, time_period, month_or_day)
        popular_stations(k, time_period, month_or_day)
        #popular_trip(k, time_period, month_or_day)
        users(k, time_period, month_or_day)
        if k != 'washington.csv':
            gender(k, time_period, month_or_day)
            birth_years(k, time_period, month_or_day)


statistics()











