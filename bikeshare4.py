import datetime
from datetime import datetime
import pandas as pd
import time
import sys


def get_city():
    """Asks the user to select a city from a list of options.
    If city is incorrect, restarts loop.
    """
    city_input = (input("Let's look at some bike share data! \nSelect Chicago, New York City, or Washington: \n")).lower()
    if city_input in ['chicago', 'washington', 'new york city']:
        city_file = city_input.replace(" ", "_") + '.csv'
        return city_file
    else:
        print("Incorrect city, please try again.")
        get_city()


def create_df(city_file):
    '''
    Args: city_file
    Returns: df with loaded city csv file
    '''
    df = pd.read_csv(city_file)
    df.rename(columns={'Start Time': 'Start', 'End Time': 'End', 'Trip Duration': 'Duration',
                           'Start Station': 'Start_Station', 'End Station': 'End_Station',
                           'User Type': 'User_Type', 'Birth Year': 'Birth_Year'}, inplace=True)
    df['Start'] = pd.to_datetime(df.Start)
    return df


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
        print("Okay, we will filter by a day.")

    elif time_period.lower() == 'none':
        print("Okay, no filter requested.")
    else:
        get_time_period()
    return time_period


def display_data(df):
    '''
    Arguments: df
    Returns: Dataframe with csv info, the first five lines of data for user to see.
    '''
    display_input = input('Would you like to see some of the data? Select Yes or No.\n')
    rows = 0

    while True:
        if display_input == 'yes':
            print(df.head(rows + 5))
            rows += 5
        if display_input == 'no':
            return
        display_input = input('Would you like to see some of the data? Select Yes or No.\n')


def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        Returns index of month in Pandas DatetimeIndex 1=January, 2=February, etc.
    '''

    while True:
        try:
            month_or_day = int(input('\nChoose a month as an integer. '
                                     'Select 1: January, 2: February, 3: March, 4: April, 5: May, 6: June\n'))
        except ValueError:
            print("Enter a month between 1 and 6.")
        else:
            if 1 <= month_or_day < 7:
                break
            else:
                print("Enter a month between 1 and 6.")
    return month_or_day


def get_day():
    '''Asks the user for a day of week and returns the specified day.
    Args:
        none.
    Returns:
        Returns day of week (Monday-Sunday)
    '''
    while True:
        try:
            month_or_day = int(input('\nChoose a day as an integer. '
                                     'Select 0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday,'
                                     ' 4: Friday, 5: Saturday, 6: Sunday\n'))
        except ValueError:
            print("Enter an integer between 0 and 6.")
        else:
            if 0 <= month_or_day < 7:
                break
            else:
                print("Enter a month between 1 and 6.")
    return month_or_day


def popular_month(df):
    '''
    Args:
        df
    Returns:
        Popular month without a time filter.
    '''
    popular = df.Start.dt.month.mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_popular_month = months[popular - 1].capitalize()
    print("Popular Month: " + most_popular_month)


def popular_hour(df, time_period, month_or_day):
    '''
    Question: What is the most popular hour of day for start time?
    Args:
        df, time_period, month_or_day
    Returns:
        Popular month without time period.
    '''
    if time_period == 'day':
        day_dt = pd.to_datetime(month_or_day)
        df['day'] = pd.to_datetime(df['Start'].dt.dayofweek)
        period = df.loc[df.day == day_dt, :]
        popular = str(period.Start.dt.hour.mode()[0])
        print('Popular Start Hour: ' + popular)

    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        period = df.loc[df.month == month_dt, :]
        popular = str(period.Start.dt.hour.mode()[0])
        print('Popular Start Hour: ' + popular)

    elif time_period == 'none':
        popular = str(df.Start.dt.hour.mode()[0])
        print('Popular Start Hour: ' + popular)


def trip_duration(df, time_period, month_or_day):
    '''
    Question: What is the total trip duration and average trip duration?
    Args:
        df, time_period, month_or_day
    Returns:
        Returns trip duration using user selected city and time period.
    '''
    if time_period == 'day':
        day_dt = pd.to_datetime(month_or_day)
        df['day'] = pd.to_datetime(df['Start'].dt.dayofweek)
        duration = df.loc[df.day == day_dt, :]
        duration_max = duration.Duration.sum() // 60
        duration_mean = duration.Duration.mean() // 60
        print("Total Trip Duration: " + str(duration_max) + " minutes.")
        print("Average Trip Duration: " + str(duration_mean) + " minutes.")
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        duration = df.loc[df.month == month_dt, :]
        duration_max = duration.Duration.sum() // 60
        duration_mean = duration.Duration.mean() // 60
        print("Total Trip Duration: " + str(duration_max) + " minutes.")
        print('Average Trip Duration: ' + str(duration_mean) + " minutes.")
    elif time_period == 'none':
        duration_max = (df.Duration.max())//60
        duration_mean = (df.Duration.mean())//60
        print("Total Trip Duration: " + str(duration_max) + " minutes.")
        print("Average Trip Duration: " + str(duration_mean) + " minutes.")
    else:
        get_city()


def popular_stations(df, time_period, month_or_day):
    '''
    Question: What is the most popular start station and most popular end station?
    Args:
        df, time_period, month_or_day
    Returns:
        Returns popular stations using user selected city file and time period.
    '''
    if time_period == 'day':
        day_dt = pd.to_datetime(month_or_day)
        df['day'] = pd.to_datetime(df['Start'].dt.dayofweek)
        popular = df.loc[df.day == day_dt, :]
        popular_start = popular.Start_Station.mode()[0]
        popular_end = popular.End_Station.mode()[0]
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


def popular_trip(df, time_period, month_or_day):
    '''
    Question: What is the most popular trip?
    Args:
        df, time_period, month_or_day
    Returns:
        most popular trip
    '''
    if time_period == 'day':
        day_dt = pd.to_datetime(month_or_day)
        df['day'] = pd.to_datetime(df['Start'].dt.dayofweek)
        df = df[df['day'] == day_dt]
        popular = df.groupby(['Start_Station', 'End_Station']).size().sort_values(ascending=False)
        print("Popular Trip: ")
        print(popular.head(1))
    elif time_period == 'month':
        month_dt = pd.to_datetime(month_or_day)
        df['month'] = pd.to_datetime(df['Start'].dt.month)
        df = df[df['month'] == month_dt]
        popular = df.groupby(['Start_Station', 'End_Station']).size().sort_values(ascending=False)
        print("Popular Trip: ")
        print(popular.head(1))
    if time_period == 'none':
        popular = df.groupby(['Start_Station', 'End_Station']).size().sort_values(ascending=False)
        print("Popular trip: ")
        print(popular.head(1))


def users(df, time_period, month_or_day):
    '''
    Question: What are the counts of each user type?
    Arguments:
        df, time_period, month_or_day
    Returns:
        Counts of each user within time frame
    '''
    if time_period == 'day':
        day_dt = pd.to_datetime(month_or_day)
        df['day'] = pd.to_datetime(df['Start'].dt.dayofweek)
        day_period = df.loc[df.day == day_dt, :]
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
        users(df, time_period, month_or_day)


def gender(df, time_period, month_or_day):
    '''
    Question: What are the counts of gender?
    Arguments:
        df, time_period, month_or_Day
    Returns:
        Gender counts per time frame
    '''
    if time_period == 'day':
        day_dt = pd.to_datetime(month_or_day)
        df['day'] = pd.to_datetime(df['Start'].dt.dayofweek)
        day_period = df.loc[df.day == day_dt, :]
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
        gender(df, time_period, month_or_day)


def birth_years(df, time_period, month_or_day):
    '''
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Arguments:
        df, time_period, month_or_day
    Returns:
        Oldest User, Youngest User, Popular Birth
    '''
    if time_period == 'day':
        day_dt= pd.to_datetime(month_or_day)
        df['day'] = pd.to_datetime(df['Start'].dt.dayofweek)
        day_period = df.loc[df.day == day_dt, :]
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

def restart():
    '''
    Arg: None
    Returns: If user wants to restart program.  
    '''
    restart = input('Restart statistics? Select Yes or No.\n').lower()
    if restart == 'yes':
        statistics()
    elif restart == 'no':
        sys.exit()
    else:
        sys.exit()


def statistics():
    city_file = get_city()
    df = create_df(city_file)
    time_period = get_time_period()

    if time_period == 'none':
        month_or_day = 0
        popular_month(df)
        popular_hour(df, time_period, month_or_day)
        trip_duration(df, time_period, month_or_day)
        popular_stations(df, time_period, month_or_day)
        popular_trip(df, time_period, month_or_day)
        users(df, time_period, month_or_day)
        if city_file != 'washington.csv':
            gender(df, time_period, month_or_day)
            birth_years(df, time_period, month_or_day)
        display_data(df)
        restart()

    if time_period == 'month':
        month_or_day = get_month()
        popular_hour(df, time_period, month_or_day)
        trip_duration(df, time_period, month_or_day)
        popular_stations(df, time_period, month_or_day)
        popular_trip(df, time_period, month_or_day)
        users(df, time_period, month_or_day)
        if city_file != 'washington.csv':
            gender(df, time_period, month_or_day)
            birth_years(df, time_period, month_or_day)
        display_data(df)
        restart()

    if time_period == 'day':
        month_or_day = get_day()

        popular_hour(df, time_period, month_or_day)
        trip_duration(df, time_period, month_or_day)
        popular_stations(df, time_period, month_or_day)
        popular_trip(df, time_period, month_or_day)
        users(df, time_period, month_or_day)
        if city_file != 'washington.csv':
            gender(df, time_period, month_or_day)
            birth_years(df, time_period, month_or_day)
        display_data(df)
        restart()

statistics()