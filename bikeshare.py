# TODO: import all necessary packages and functions

import  csv
import pandas as pd
import numpy as np
from datetime import datetime
import calendar
import time

# To color text color
class style:
    BOLD = '\033[1m'
    END = '\033[0m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    UNDERLINE = '\033[4m'


# Dataset filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

CITY_DATA = {'chicago':'chicago.csv',
             'new_york_city':'new_york_city.csv',
             'washington':'washington.csv'}

def load_data_month(city,time_period_month):
    '''Returns Dataframe filtered by month

     :param city: User selected city name
     :param time_period_month: User selected month name
     :Returns: Returns Dataframe for selected month
    '''
    # TODO: complete function
    # load CSV file into the dataframe
    month = time_period_month.lower()

    if city == 'new_york_city':
        df = pd.read_csv(CITY_DATA[city], nrows =4163571)
        df = df.dropna()
    else:
        df = pd.read_csv(CITY_DATA[city])
        df = df.dropna()

    # convert the Start time into the datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extracting month number and creating new column 'Start_Time_month'
    df['Start_Time_month'] = df['Start Time'].dt.month

    # Extracting month name and creating new column 'Start_Time_month_name'
    df['Start_Time_month_name'] = df['Start Time'].dt.month.apply(lambda x: calendar.month_name[x])

    # Extracting weekday name and creating new column 'Start_Time_day_of_week'
    df['Start_Time_day_of_week'] = df['Start Time'].dt.weekday_name

    # Extracting hour and creating new column 'Start_Time_hour'
    df['Start_Time_hour'] = df['Start Time'].dt.hour

    # Create new Dataframe,filter by month, if asked by user
    # use the index of the month list to get the corresponding int
    months = ['january','february','march','april','may','june']
    month = months.index(month) + 1
    #print("Inside Load data: {}".format(month))

    # filter by month to create the new dataframe
    df = df[df['Start_Time_month'] == month]
    return df

def load_data_2017_month_june(city):
    '''Returns Dataframe filtered by month

     :param city: User selected city name
     :param time_period_month: User selected month name
     :Returns: Returns Dataframe for selected month
    '''
    # TODO: complete function
    # load CSV file into the dataframe

    if city == 'new_york_city':
        df = pd.read_csv(CITY_DATA[city], nrows =5163571)
        df = df.dropna()
    else:
        df = pd.read_csv(CITY_DATA[city])
        df = df.dropna()

    #print("\n1. {}".format(df.head(3)))

    # convert the Start time into the datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert the Start time into the year
    df['Start_Time_year'] = df['Start Time'].dt.year
    # Extracting month name and creating new column 'Start_Time_month_name'
    df['Start_Time_month_name'] = df['Start Time'].dt.month.apply(lambda x: calendar.month_name[x])

    #print("\n2. {}".format(df.head(3)))
    #print("\n2. {}".format(df.info()))

    # filter by month to create the new dataframe
    month = 'June'
    df = df[(df.Start_Time_year == 2017) & (df.Start_Time_month_name == month)]

    df_final = df[['Trip Duration', 'Start_Time_year', 'Start_Time_month_name']].reset_index(drop=True)

    #print("\n3. {}".format(df.head(3)))

    return df_final

def load_data_day(city, time_period):
    '''Returns Dataframe filtered by day

     :param city: User selected city name
     :param time_period: User selected day name
     :Returns: Returns Dataframe filtered by day
     '''

    # TODO: complete function
    # load CSV file into the dataframe

    if city == 'new_york_city':
        df = pd.read_csv(CITY_DATA[city], nrows=2163571)
        df = df.dropna()
    else:
        df = pd.read_csv(CITY_DATA[city])
        df = df.dropna()

    # convert the Start time into the datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extracting year number and creating new column 'Start_Time_year'
    df['Start_Time_year'] = df['Start Time'].dt.year

    # Extracting month number and creating new column 'Start_Time_month'
    df['Start_Time_month'] = df['Start Time'].dt.month

    # Extracting month name and creating new column 'Start_Time_month_name'
    df['Start_Time_month_name'] = df['Start Time'].dt.month.apply(lambda x: calendar.month_name[x])

    # Extracting weekday name and creating new column 'Start_Time_day_of_week'
    df['Start_Time_day_of_week'] = df['Start Time'].dt.weekday_name

    # Extracting hour and creating new column 'Start_Time_hour'
    df['Start_Time_hour'] = df['Start Time'].dt.hour

    # filter by day of week if user ask for
    # filter by day of week to create the new dataframe
    df = df[df['Start_Time_day_of_week'] == time_period.title()]

    return df

def load_data_none(city):
    '''Returns Dataframe filtered by user choice 'none'

     :param city: User selected city name
     :param time_period_month: User selected month name
     :Returns: Returns Dataframe for selected month
    '''
    # TODO: complete function
    # load CSV file into the dataframe
    if city == 'new_york_city':
        df = pd.read_csv(CITY_DATA[city], nrows =2163571)
        df = df.dropna()
    else:
        df = pd.read_csv(CITY_DATA[city])
        df = df.dropna()

    # convert the Start time into the datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extracting year number and creating new column 'Start_Time_year'
    df['Start_Time_year'] = df['Start Time'].dt.year

    # Extracting month number and creating new column 'Start_Time_month'
    df['Start_Time_month'] = df['Start Time'].dt.month

    # Extracting month name and creating new column 'Start_Time_month_name'
    df['Start_Time_month_name'] = df['Start Time'].dt.month.apply(lambda x: calendar.month_name[x])

    # Extracting weekday name and creating new column 'Start_Time_day_of_week'
    df['Start_Time_day_of_week'] = df['Start Time'].dt.weekday_name

    # Extracting hour and creating new column 'Start_Time_hour'
    df['Start_Time_hour'] = df['Start Time'].dt.hour

    return df

def get_city():
    '''Asks the user for a city and returns user typed city name.

    Returns:(str) returns user typed city name
    '''
    print(style.BOLD + '\nPrompt:' + style.END +  'Hello! Let\'s explore some US bikeshare data!Would you like to see data for Chicago, New York, or Washington?')
    city = input(style.BOLD + 'User input:' + style.END)

    # TODO: handle raw input and complete function

    if city == 'Chicago' or city == 'chicago' or city == 'c':
        city = 'Chicago'
        return city.lower()
    elif city == 'Newyork' or city == 'newyork' or city == 'NYC' or city == 'nyc' or city == 'n':
        city = 'new_york_city'
        return city.lower()
    elif city == 'Washington' or city == 'washington' or city == 'w':
        city = 'Washington'
        return city.lower()
    else:
        print(style.RED + "Keyboard Type Error: Please check spelling and try again.\n" + style.END)
        return get_city()

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Returns:(str) specified filter string like month, day, or none.
    '''
    print(style.BOLD + 'Prompt:' + style.END + 'Would you like to filter the data by month,day,or not at all? Type \"none\" for no time filter.')
    time_period = input(style.BOLD + 'User input:' + style.END)
    # TODO: handle raw input and complete function

    time_period = time_period.lower()

    if time_period == 'month' or time_period == 'm':
        my_val = 'month'
    elif time_period == 'day'or time_period == 'd':
        my_val = 'day'
    elif time_period == 'none'or time_period == 'n':
        my_val = 'none'
    else:
        print(style.RED + "Keyboard Type Error: Please check spelling and try again.\n" + style.END)
        return get_time_period()

    return my_val

def get_month():
    '''Asks the user for a month and returns the specified month.

       Args: none.
       Returns:(str) month name for a city's bikeshare data.
       '''
    print(style.BOLD + 'Prompt:' + style.END + 'Which month? January, February, March, April, May, or June?')
    month = input(style.BOLD + 'User input:' + style.END)
    # TODO: handle raw input and complete function
    if month == 'January' or month == 'jan' or month == 'january':
        month_name = 'January'
    elif month == 'February' or month == 'Feb' or month == 'february':
        month_name = 'February'
    elif month == 'March' or month == 'Mar' or month == 'march':
        month_name = 'March'
    elif month == 'April' or month == 'Apr' or month == 'april' :
        month_name = 'April'
    elif month == 'May' or month == 'may':
        month_name = 'May'
    elif month == 'June' or month == 'Jun' or month == 'june':
        month_name = 'June'
    else:
        print(style.RED + "Keyboard Type Error: Please check spelling and try again.\n" + style.END)
        return get_month()

    return month_name

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args: none.
    Returns: (str) week day name.
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('Prompt:Which day? Type integer\n0 for Monday\n1 for Tuesday\n2 for Wednesday\n3 for Thursday\n4 for Friday\n5 for Saturday\n6 for Sunday\nPlease type your response as an integer.\n')
    day = int(day)
    week_day = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    return week_day[day]

def popular_month(city_file):
    '''Returns popular month

     :param city_file: Dataframe.
     :Returns:(str) Returns popular month.
    '''
    # TODO: complete function
    bikeshare_popular_month = city_file['Start_Time_month_name'].mode()
    bikeshare_popular_month = bikeshare_popular_month.to_string(header=False)
    bikeshare_popular_month = bikeshare_popular_month.lstrip('0 ').split('.')[0]
    return bikeshare_popular_month

def popular_day(city_file):
    '''Returns popular day
    :param city_file: Dataframe.
    :Returns:(str) Returns popular day.
    '''
    # TODO: complete function
    popular_day = city_file['Start_Time_day_of_week'].mode()
    return popular_day

def popular_hour(city_file):
    '''Returns popular day

     :param city_file: Dataframe.
     :Returns:(str) Returns popular hour.
     '''
    # TODO: complete function
    popular_hour = city_file['Start_Time_hour'].mode()
    return popular_hour

def convert_to_day_hour_min_sec(seconds):
    """Calculates day(s), hours, minutes, and second.

    :param seconds: Time in seconds
    :Returns:(tuple) day(s), hours, minutes, and second.
    """
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return (int(days), int(hours), int(minutes), seconds)


def trip_duration(city_file):
    '''Calculates day(s), hours, minutes, and second.

     :param city_file: Dataframe.
     :Returns:(tuple) day(s), hours, minutes, and second.
    '''
    total_trip_time_seconds = city_file['Trip Duration'].sum()
    average_trip_time_seconds = city_file['Trip Duration'].mean()

    convert_total_trip_time_seconds = convert_to_day_hour_min_sec(total_trip_time_seconds)
    convert_average_trip_time_seconds = convert_to_day_hour_min_sec(average_trip_time_seconds)

    return (convert_total_trip_time_seconds, convert_average_trip_time_seconds)


def popular_stations(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    popular_start_station = city_file['Start Station'].mode()
    popular_end_station = city_file['End Station'].mode()

    return  (popular_start_station,popular_end_station)

def popular_stations_start_end(city_file):
    """Return popular start station.

    :param seconds: Time in seconds
    :Returns:(str)Return popular start station.
    """
    popular_station_start_end = city_file.groupby(['Start Station', 'End Station'], sort=True).size().nlargest(1)

    return  popular_station_start_end

def users(city_file):
    """Returns count of users type

    :param city_file: City Dataframe
    :return:(int) Returns count of users by their category
    """
    # TODO: complete function
    users_breakdown = city_file.groupby('User Type').size()
    list_users_breakdown = users_breakdown.to_string(header=False).split()
    user_subscriber = 0
    user_customer = 0
    user_dependent = 0

    for i, e in enumerate(list_users_breakdown):
        if e == 'Subscriber' in list_users_breakdown:
            user_subscriber = list_users_breakdown[i + 1]
        elif e == 'Customer' in list_users_breakdown:
            user_customer = list_users_breakdown[i + 1]
        elif e == 'Dependent' in list_users_breakdown:
            user_dependent = list_users_breakdown[i + 1]

    return  (user_subscriber, user_customer, user_dependent)

def gender(city_file):
    '''Return gender count

    :param city_file: City Dataframe
    :return:(int) Returns gender count
    '''
    # TODO: complete function
    gender = city_file.groupby('Gender').size()
    list_gender = gender.to_string(header=False).split()
    for i, e in enumerate(list_gender):
        if e == 'Male' in list_gender:
            gender_male = list_gender[i + 1]
        elif e == 'Female' in list_gender:
            gender_female = list_gender[i + 1]

    return (gender_male,gender_female)

def birth_years(city_file):
    '''Returns Earliest and recent Birth Years.
    Question: What are the earliest, most recent, and most popular birth years?

    :param city_file: City Dataframe
    :return: Return gender count oldest, popular, and youngest
    '''
    # TODO: complete function

    birth_year_oldest = city_file.groupby(['Birth Year'], sort=True)['Birth Year'].count().sort_values().head(1)
    birth_year_oldest = birth_year_oldest.to_string(header=False).split()[0].split('.')[0]

    birth_year_popular = city_file['Birth Year'].mode()
    birth_year_popular = birth_year_popular.to_string(header=False)
    birth_year_popular = birth_year_popular.lstrip('0 ').split('.')[0]

    birth_year_youngest = city_file['Birth Year'].sort_values(ascending=False).iloc[0]
    birth_year_youngest = str(birth_year_youngest)
    birth_year_youngest = birth_year_youngest.split('.')[0]

    return (birth_year_oldest, birth_year_popular, birth_year_youngest)

def csv_read_dict(filename,num=5):
    """Displays five lines of data based on user selected ciyif the user specifies that th

    :param filename: City Filename in CSV
    :param num: Number of rows
    :return: Return next five rows
    """
    for chunk in pd.read_csv(filename, chunksize=num):
        print(style.BLUE,chunk,style.END)
        user_input = input("        Would you like to view next 5 line? "
                               "Type \'y\' or \'n\' \n")
        if user_input == 'Yes' or user_input == 'y' or user_input == 'yes':
            for chunk in pd.read_csv(filename, skiprows=5):
                bullet_empty_circle = u'\u006F\t'
                print("     {} {}".format(bullet_empty_circle,style.BLUE,chunk,style.END))
            #return csv_read_dict(filename,num)
        else:
            # Break for 'n' or any user input
            break

def display_data(city_name):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    :param city_name: City Dataframe

    :returns:Five rows of user chosen dataset
    '''
    display = input('       Would you like to view individual trip data? Type \'yes\' or \'no\'. ')
    # TODO: handle raw input and complete function
    display = display.lower()

    if display == 'yes' or  display == 'y':
        if city_name == 'Chicago':
            filename = chicago
            csv_read_dict(filename)
        elif city_name == 'Newyork':
            filename = new_york_city
            csv_read_dict(filename)
        else:
            filename = washington
            csv_read_dict(filename)
    else:
        pass


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    #print("==>You choose time period : {}.".format(time_period))

    if time_period == 'month':
        time_period_01 = time_period
        time_period = get_month()
        df = load_data_month(city, time_period)
        #print("DEBUG:When time_period is month:\n{}".format(df.head(3)))

        # dropping any NaN row entry
        #df = df.dropna()

        #print("Dropped NAN entries")
        #print(df.head(3))

        print("{}, {}, {}".format(city, time_period_01, time_period))

        #print("\nDEBUG:The time_period is: {}.".format(time_period))
        bullet_dark_circle = u'\u25CF\t'

        print("\n{}Q1:What is the most popular month for traveling?".format(bullet_dark_circle))
        bullet_dark_circle = u'\u25CF\t'
        start_time = time.time()
        bullet_empty_circle = u'\u006F\t'
        print("     {}{}".format(bullet_empty_circle,time_period))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))


        print("\n{}Q2:What is the most popular day for traveling?".format(bullet_dark_circle))
        bullet_dark_circle = u'\u25CF\t'
        start_time = time.time()
        bikeshare_popular_day = popular_day(df)
        bikeshare_popular_day = bikeshare_popular_day.to_string(header=False)
        bikeshare_popular_day = bikeshare_popular_day.lstrip('0 ')
        bullet_empty_circle = u'\u006F\t'
        print("     {}{}".format(bullet_empty_circle, bikeshare_popular_day))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))


    elif time_period == 'day':
        time_period_01 = time_period
        time_period = get_day()
        df = load_data_day(city, time_period)

        # dropping any NaN row entry
        #df = df.dropna()

        #print("Dropped NAN entries")
        #print(df.head(3))

        print("{}, {}, {}".format(city,time_period_01,time_period))

        bullet_dark_circle = u'\u25CF\t'
        print("\n{}Q1:What is the most popular month for traveling?".format(bullet_dark_circle))
        bikeshare_popular_month = popular_month(df)
        start_time = time.time()
        bullet_empty_circle = u'\u006F\t'
        print("     {}{}".format(bullet_empty_circle, bikeshare_popular_month))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

        bullet_dark_circle = u'\u25CF\t'
        print("\n{}Q2:What is the most popular day for traveling?".format(bullet_dark_circle))
        bikeshare_popular_day = time_period
        start_time = time.time()
        bullet_empty_circle = u'\u006F\t'
        print("     {}{}".format(bullet_empty_circle, bikeshare_popular_day))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

        print("\nThe time_period is: {}.".format(time_period))

    else:
        # for time_period == 'none'
        time_period = 'none'
        time_period_01 = time_period
        #df = load_data_none(city, time_period)
        df = load_data_none(city)
        #print("DEBUG:When time_period is day:\n{}".format(df.head(3)))

        # dropping any NaN row entry
        #df = df.dropna()

        #print("Dropped NAN entries")
        #print(df.head(3))

        print("{}, {}, {}".format(city, time_period_01, time_period))

        bullet_dark_circle = u'\u25CF\t'
        print("\n{}Q1:What is the most popular month for traveling?".format(bullet_dark_circle))
        bikeshare_popular_month = popular_month(df)
        start_time = time.time()
        bullet_empty_circle = u'\u006F\t'
        print("     {}{}".format(bullet_empty_circle, bikeshare_popular_month))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

        print("\n{}Q2:What is the most popular day for traveling?".format(bullet_dark_circle))
        bullet_dark_circle = u'\u25CF\t'
        start_time = time.time()
        bikeshare_popular_day = popular_day(df)
        bikeshare_popular_day = bikeshare_popular_day.to_string(header=False)
        bikeshare_popular_day = bikeshare_popular_day.lstrip('0 ')
        bullet_empty_circle = u'\u006F\t'
        print("     {}{}".format(bullet_empty_circle, bikeshare_popular_day))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

        print("\nThe time_period is: {}.".format(time_period))


    # Common Data Analysis

    bullet_dark_circle = u'\u25CF\t'
    print("\n{}Q3:What is the most popular hour of the day to start your travels?".format(bullet_dark_circle))
    start_time = time.time()
    bikeshare_popular_hour = popular_hour(df)
    bikeshare_popular_hour = bikeshare_popular_hour.to_string(header=False)
    bikeshare_popular_hour = bikeshare_popular_hour.lstrip('0 ')
    bullet_empty_circle = u'\u006F\t'
    print("     {}{}".format(bullet_empty_circle, bikeshare_popular_hour))
    print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))



    bullet_dark_circle = u'\u25CF\t'
    print("\n{}Q4:What is the most popular start and end stations respectively?".format(bullet_dark_circle))
    start_time = time.time()
    bikeshare_popular_start_end_stations = popular_stations(df)
    popular_start_station, popular_end_station = bikeshare_popular_start_end_stations

    popular_start_station = popular_start_station.to_string(header=False)
    popular_start_station = " ".join(popular_start_station.split())
    popular_start_station = popular_start_station.lstrip('0 ')

    popular_end_station = popular_end_station.to_string(header=False)
    popular_end_station = " ".join(popular_end_station.split())
    popular_end_station = popular_end_station.lstrip('0 ')

    bullet_empty_circle = u'\u006F\t'
    print("     {}Start Station | {}".format(bullet_empty_circle, popular_start_station))
    print("     {}End Station   | {}".format(bullet_empty_circle, popular_end_station))
    print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

    #print("\nDEBUG:City name : {}".format(city))

    bullet_dark_circle = u'\u25CF\t'
    print("\n{}Q5:What is the most popular trip from start to end?".format(bullet_dark_circle))

    start_time = time.time()
    bikeshare_popular_start_to_end_stations = popular_stations_start_end(df)

    bikeshare_popular_trip_start_to_end = bikeshare_popular_start_to_end_stations.to_string(header=False)
    bikeshare_popular_trip_start_to_end_01 = bikeshare_popular_trip_start_to_end[:-7]

    bikeshare_popular_trip_start_station = bikeshare_popular_trip_start_to_end_01[:22]
    bikeshare_popular_trip_end_station = bikeshare_popular_trip_start_to_end_01[23:]

    bullet_empty_circle = u'\u006F\t'
    print("     {}Start Station | {}".format(bullet_empty_circle, bikeshare_popular_trip_start_station))
    print("     {}End Station   | {}".format(bullet_empty_circle, bikeshare_popular_trip_end_station))
    print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

    #print("DEBUG: {}".format(city))


    if city == 'chicago' or city == 'new_york_city':
        bullet_dark_circle = u'\u25CF\t'
        print("\n{}Q6:What is the breakdown of gender?".format(bullet_dark_circle))

        start_time = time.time()
        bikeshare_gender_count = gender(df)
        gender_male_01, gender_female_01 = bikeshare_gender_count
        bullet_empty_circle = u'\u006F\t'
        print("     {}Male     | {}".format(bullet_empty_circle, gender_male_01))
        print("     {}Female   | {}".format(bullet_empty_circle, gender_female_01))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

        bullet_dark_circle = u'\u25CF\t'
        print("\n{}Q7:What is the oldest,youngest,and most popular year of birth,respectively?".format(bullet_dark_circle))

        start_time = time.time()
        bikeshare_birth_count = birth_years(df)
        birth_year_oldest, birth_year_popular, birth_year_youngest = bikeshare_birth_count
        bullet_empty_circle = u'\u006F\t'
        print("     {}Oldest     | {}".format(bullet_empty_circle, birth_year_oldest))
        print("     {}Yougest    | {}".format(bullet_empty_circle, birth_year_youngest))
        print("     {}Popular    | {}".format(bullet_empty_circle, birth_year_popular))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))

    else:
        # Pass for city == 'washington':
        bullet_dark_circle = u'\u25CF\t'
        print("\n{}Q7:What is the oldest,youngest,and most popular year of birth,respectively?".format(
            bullet_dark_circle))
        bullet_empty_circle = u'\u006F\t'
        print("     {}".format(bullet_empty_circle) + style.RED + "Skipping, No Gender Data for City:Washington.\n" + style.END)
        pass

    bullet_dark_circle = u'\u25CF\t'
    print("\n{}Q8:What is the breakdown of users?".format(bullet_dark_circle))

    start_time = time.time()
    bikeshare_users = users(df)
    user_subscriber, user_customer, user_dependent = bikeshare_users

    bullet_empty_circle = u'\u006F\t'
    print("     {}Subscriber    | {}".format(bullet_empty_circle, user_subscriber))
    print("     {}Customer      | {}".format(bullet_empty_circle, user_customer))
    print("     {}Dependent     | {}".format(bullet_empty_circle, user_dependent))
    print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))


    bullet_dark_circle = u'\u25CF\t'
    print("\n{}Q9:What is the total trip duration and average time spent on each trip ?".format(bullet_dark_circle))
    start_time = time.time()
    bikeshare_trip_duration = trip_duration(df)
    convert_total_trip_time_seconds, convert_average_trip_time_seconds = bikeshare_trip_duration

    total_trip_days, total_trip_hour, total_trip_min, total_trip_second = convert_total_trip_time_seconds
    average_trip_days, average_trip_hour, average_trip_min, average_trip_second = convert_average_trip_time_seconds

    bullet_empty_circle = u'\u006F\t'
    print("     {}Total trip time                      | {} days {} hours {} minutes {} seconds ".format(bullet_empty_circle, total_trip_days, total_trip_hour, total_trip_min, total_trip_second))
    print("     {}Average time spent on each trip      | {} days {} hours {} minutes {} seconds".format(bullet_empty_circle, average_trip_days, average_trip_hour, average_trip_min, average_trip_second))
    print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))



    bullet_dark_circle = u'\u25CF\t'
    print("\n{}Q10:What was the total traveling done for 2017 through June, and what was the average time spent on each trip ?".format(bullet_dark_circle))
    start_time = time.time()

    #print(city)

    try:
        df_final = load_data_2017_month_june(city)
    except MemoryError:
        bullet_empty_circle = u'\u006F\t'
        print("     {}".format(bullet_empty_circle),style.RED, "Exception: MemoryError - Skipping.", style.END)
    else:
        # print("Dropped NAN entries")
        #print(df_final.head(3))

        bikeshare_trip_duration_2017_june = trip_duration(df_final)
        convert_total_trip_time_seconds, convert_average_trip_time_seconds = bikeshare_trip_duration_2017_june

        total_trip_days, total_trip_hour, total_trip_min, total_trip_second = convert_total_trip_time_seconds
        average_trip_days, average_trip_hour, average_trip_min, average_trip_second = convert_average_trip_time_seconds

        bullet_empty_circle = u'\u006F\t'
        print("     {}Total trip time                 | {} days {} hours {} minutes {} seconds ".format(
            bullet_empty_circle, total_trip_days, total_trip_hour, total_trip_min, total_trip_second))
        print("     {}Average time spent on each trip | {} days {} hours {} minutes {} seconds".format(
            bullet_empty_circle, average_trip_days, average_trip_hour, average_trip_min, average_trip_second))
        print("     {}That took {} seconds.".format(bullet_empty_circle, (time.time() - start_time)))


        bullet_dark_circle = u'\u25CF\t'
        print("\n{}Q11:Print five lines for Data of chosen city?".format(bullet_dark_circle))
        start_time = time.time()
        bullet_empty_circle = u'\u006F\t'
        print(style.BOLD, "     {}City | {}.".format(bullet_empty_circle, city), style.END)
        display_data(city)

        print("\n")


    # Restart?
    restart = input('\n     Would you like to restart? Type \'yes\' or \'Stop by Pressing Any keyboard Button\'.')
    if restart.lower() == 'yes' or restart.lower() == 'Y':
        statistics()


if __name__ == "__main__":
	statistics()
