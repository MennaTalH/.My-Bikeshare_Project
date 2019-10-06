import time
import pandas as pd
import numpy as np

CITY_DATA = { 'CHICAGO': 'chicago.csv',
              'NEW YORK CITY ': 'new_york_city.csv',
              'WASHINGTON ': 'washington.csv' }

MONTHS = ['JANUARY:-', 'FEBRUARY ', 'MARCH ', 'APRIL', 'MAY', 'JANE']
WEEKDAYS = ['MONDAY', ' TUESDAY', 'WEDNESDAY', 'THURSDAY', ' FRIDAY', 'SATURDAY', 'SUNDAY']
  

LINE_LEN = 70
    # print long string with repeating char ...
    # used to separate sections of output ...

print_line = lambda char: print(char[0] * LINE_LEN)

def print_processing_time(start_time):
    time_str = "[... %s seconds]" % round((time.time() - start_time), 3)
    print(time_str.rjust(LINE_LEN))
    print_line('--')


def get_filter_city():
    
    # build and display the list of cities for which we have datasets ...
    cities_list = []
    num_cities = 0

    for a_city in CITY_DATA:
        cities_list.append(a_city)
        num_cities += 1
        print('        {0:20}. {1}'.format(num_cities, a_city.title()))

    # ask user to insert a number for a city from the list
    while True:
        try:
            city_num = int(input("\n   PLEASE  ENTER A NUMBER FOR THE CITY (1 - {}):  ".format(len(cities_list))))
        except:
            continue

        if city_num in range(1, len(cities_list)+1):
            break
     # get the city's name in string format from the list ...
    city = cities_list[city_num - 1]
    return city


def get_filter_month():
   
    while True:
        try:
<<<<<<< HEAD
            month = input("  \n  PLEASE ENTER THE MONTH WHITH   JANUARY =1, JUNE=6 or 'a' for all:-  ")
||||||| merged common ancestors
            month = input("   PLEASE ENTER THE MONTH WHITH     January=1, June=6 or 'a' for all:-  ")
=======
            month = input("   PLEASE ENTER THE MONTH WHITH     January=1, June=6 or 'a' for All:-  ")
>>>>>>> refactoring
        except:
            print("        ---->>  Valid input:  1 - 6, A")
            continue

        if month == 'A':
            month = 'All'
            break
        elif month in {'1', '2', '3', '4', '5', '6'}:
      # reassign the string name for the month ...
            month = MONTHS[int(month) - 1]
            break
        else:
            continue
    
    return month


def get_filter_day():
    
    while True:
        try:
<<<<<<< HEAD
            day = input("  PLEASE ENTER  THE DAY WITH  MONDAY=1, SUNDAY=7 or 'a' for all:  ")
||||||| merged common ancestors
            day = input("  PLEASE ENTER  THE DAY WITH Monday=1, Sunday=7 or 'a' for all:  ")
=======
            day = input("  PLEASE ENTER  THE DAY WITH Monday=1, Sunday=7 or 'A' for All:  ")
>>>>>>> refactoring
        except:
            print("        ---->>  Valid input:  1 - 7, A")
            continue

        if day == 'A':
            day = 'All'
            break
        elif day in {'1', '2', '3', '4', '5', '6', '7'}:
      # reassign the string name for the day ...
            day = WEEKDAYS[int(day) - 1]   
            break
        else:
            continue

    return day


def get_filters():
  
    print_line('=')
<<<<<<< HEAD
    print('\n  Hello! Let\'s EXPLORE  US BIKESHARE BIKESHARE DATA!\n')
    
||||||| merged common ancestors
    print('\n  Hello! Let\'s explore US bikeshare data!\n')
    
=======
    print('\n  Hello!(: Let\'s explore US bikeshare data! \n')
      # get user input for city ...
>>>>>>> refactoring
    city = get_filter_city()
    # get user input for month ...
    month = get_filter_month()
   # get user input for day of week ... 
    day = get_filter_day()

    return city, month, day

def filter_summary(city, month, day, init_total_rides, df):
 
    start_time = time.time()

    filtered_rides = len(df)
    num_stations_start = len(df['Start Station'].unique())
    num_stations_end = len(df['End Station'].unique())

    print('   Gathering Statistics For:                ', city)
    print('   Filters (Month, Day):        ', month, ', ', day)
    print('   Total Rides In Dataset:      ', init_total_rides)
    print('   Rides In Filtered Set:         ', filtered_rides)
    print('   Number Of Start Stations:    ', num_stations_start)
    print('   Number Of End Stations:       ', num_stations_end)

    print_processing_time(start_time)


def load_data(city, month, day):
   
    start_time = time.time()
   # load data file into a dataframe ...
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime ...
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')

   
    df['month'] = df['Start Time'].dt.month                
    df['day_of_week'] = df['Start Time'].dt.dayofweek       
    df['hour'] = df['Start Time'].dt.hour                  

    init_total_rides = len(df)
    filtered_rides = init_total_rides   
     
     # filter by month if applicable

    if month != 'All':
        
        month_i = MONTHS.index(month) + 1    
    
     # filter by month to create the new dataframe

        df = df[df.month == month_i]
        month = month.title()
   # filter by day of week if applicable ...
    if day != 'All':
     
        day_i = WEEKDAYS.index(day)        

        df = df[df.day_of_week == day_i]
        day = day.title()

    print_processing_time(start_time)

    filter_summary(city.title(), month, day, init_total_rides, df )

    return df

def hour_12_str(hour):
   
    if hour == 0:
        str_hour = '11 AM'
    elif hour == 12:
        str_hour = '11 PM'
    else:
        str_hour = '{} AM'.format(hour) if hour < 12 else '{} PM'.format(hour - 11)

    return str_hour


def time_stats(df):
   
    print('  Most Frequent Times of Travel...')
    start_time = time.time()

     # display the most common month; convert to string ...

    month = MONTHS[df['month'].mode()[0] - 1].title()
    print('  Month:-               ', month)
   
   
     # display the most common day of week ...
    common_day = df['day_of_week'].mode()[0]      
    common_day = WEEKDAYS[common_day].title()
    print('    Day of the week:     ', common_day)

    # display the most common start hour; convert to 12-hour string ...

    hour = hour_12_str(df['hour'].mode()[0])
    print('    Start hour:          ', hour)

    print_processing_time(start_time)


def station_stats(df):
   

    print('  Most Popular Stations and Trip...')
    start_time = time.time()

    filtered_rides = len(df)

     # display most commonly used start station ...

    start_station = df['Start Station'].mode()[0]
    start_station_trips = df['Start Station'].value_counts()[start_station]

    print('    Start station:       ', start_station)
    print('{0:30}{1}/{2} trips'.format(' ', start_station_trips, filtered_rides))
    
     # display most commonly used end station ...

    end_station = df['End Station'].mode()[0]
    end_station_trips = df['End Station'].value_counts()[end_station]

    print('    End station:         ', end_station)
    print('{0:30}{1}/{2} trips'.format(' ', end_station_trips, filtered_rides))

   # group the results by start station and end station ...

    df_start_end_combination_gd = df.groupby(['Start Station', 'End Station'])
    most_freq_trip_count = df_start_end_combination_gd['Trip Duration'].count().max()
    most_freq_trip = df_start_end_combination_gd['Trip Duration'].count().idxmax()

    print('    Frequent trip:        {}, {}'.format(most_freq_trip[0], most_freq_trip[1]))
    print('{0:30}{1} trips'.format(' ', most_freq_trip_count))

    print_processing_time(start_time)


def seconds_to_HMS_str(total_seconds):
    
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    
    day_hour_str = ''
    if weeks > 0:
        day_hour_str += '{} weeks, '.format(weeks)
    if days > 0:
        day_hour_str += '{} days, '.format(days)
    if hours > 0:
        day_hour_str += '{} hours, '.format(hours)
    if minutes > 0:
        day_hour_str += '{} minutes, '.format(minutes)

    # always show the seconds, even 0 secs when total > 1 minute ...
    if total_seconds > 59:
        day_hour_str += '{} seconds'.format(seconds)

    return day_hour_str


def trip_duration_stats(df):

    print('  Trip Duration...')
    start_time = time.time()

    total_travel_time = int(df['Trip Duration'].sum())
    print('    Total travel time:-    ', total_travel_time, 'seconds')
    print('               ', seconds_to_HMS_str(total_travel_time))

    mean_travel_time = int(df['Trip Duration'].mean())
    print('    Mean travel time:    ', mean_travel_time, 'seconds')
    print('               ', seconds_to_HMS_str(mean_travel_time))

    print_processing_time(start_time)


def user_stats(df):
   
    print('  User Stats...')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    for idx in range(len(user_types)):
        val = user_types[idx]
        user_type = user_types.index[idx]
        print('    {0:21}'.format((user_type + ':')), val)

    # 'Gender' and 'Birth Year' is only available for Chicago and New York City ... 
   
    if 'Gender' in df.columns:
  
        genders = df['Gender'].value_counts()
        for idx in range(len(genders)):
            val = genders[idx]
            gender = genders.index[idx]
            print('    {0:21}'.format((gender + ':')), val)

    if 'Birth Year' in df.columns:
     # Display earliest, most recent, and most common year of birth...
        print('    Year of Birth...')
        print('        Earliest:        ', int(df['Birth Year'].min()))
        print('        Most recent:     ', int(df['Birth Year'].max()))
        print('        Most common:     ', int(df['Birth Year'].mode()))

    print_processing_time(start_time)

def display_raw_data(df):
    
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    

    print('\n    Would you like to see some raw data from the current dataset?')
    while True:
        raw_data = input('      (YES or NO):  ')
        if raw_data.lower() == 'YES':
        # display show_rows number of lines, but display to user as starting from row as 1 ...
            print('\n    Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))

            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

            print_line('.')
            print('\n    Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\n    WOULD YOU LIKE TO START AGIAN  ? (YES or NO):  ')
        if restart.lower() != 'YES':
            break

if __name__ == "__main__":
   main()
