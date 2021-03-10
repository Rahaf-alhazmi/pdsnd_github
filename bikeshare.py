import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH=['january','february', 'march', 'april',  'may','june','all']
DAYS=['monday','tuesday', 'wednesday','thursday','friday','saturday', 'sunday','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
	print('Welcome :)')
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input=input("Please choose a city: chicago, new york city or washington :\n ").lower()
    while city_input not in CITY_DATA.keys():
            print('\n There is error in splling or you are not choose the correct city from the list.\n ')
            city_input=input("Please choose a city: chicago, new york city or washington :\n ").lower()
          
    print('You have chosen {} let\'s show the statistics \n'.format(city_input))
    

    # TO DO: get user input for month (all, january, february, ... , june)
    month_input=input('Please choose a month:January, February, March, April, May,June or All:\n').lower()
    while month_input not in MONTH:
        print('\n There is error in splling or you are not choose the correct month from the list.\n')
        month_input=input('Please choose a month:January, February, March, April, May,June or All:\n').lower()
        
    print('You have chosen {} let\'s show the statistics \n'.format(month_input.title())) 

      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input=input("all, monday,tuesday,wednesday,thursday,friday, saturday, sunday \n").lower()
    while day_input not in DAYS:
            print('\n There is error in splling or you aren\'t choose the correct day from the list.\n')
            day_input=input("all, monday,tuesday,wednesday,thursday,friday, saturday, sunday \n").lower()
        
    print('You have chosen {} let\'s show the statistics \n'.format(day_input.title())) 
            
    print('-'*40)
    return city_input, month_input, day_input


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #create hour data fram to extact hour   
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
     """Displays statistics on the most frequent times of travel."""

     print('\nCalculating The Most Frequent Times of Travel...\n')
     start_time = time.time()

    # to display the most common month i use mode() method 
     common_month= df['month'].mode()[0]
     print('\nthe most common month is:\n ',common_month)

    # TO display the most common day of week i use mode() method 
     common_Dayof_week=df['day_of_week'].mode()[0]
     print('\n The most common day in a week is:\n ',common_Dayof_week)

    # TO display the most common start hour i need use mode() method
    
     common_early_hour=df['hour'].mode()[0]
     print('\n The most common early hour on a day is: \n',common_early_hour)


     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO display most commonly used start station use mode() method
    common_start_station=df['Start Station'].mode()[0]
    print('\n The most commonly used start station :\n ',common_start_station)

    # TO display most commonly used end station i use mode()
    common_Stop_station=df['End Station'].mode()[0]
    print('\n The most commonly used stop station :\n ',common_Stop_station)


    # TO display most frequent combination of start station and end station trip i need to create new column combin of start+stop using str.cat() method columns then use mode()
    df['combin']=df['Start Station'].str.cat(df['End Station'],sep=" to ")
    combin_start_stop= df['combin'].mode()[0]
    print('\n The most commonly used both start and Stop station are :\n ',combin_start_stop)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time 
    total_trip_duration=round(df['Trip Duration'].sum())
    #show total_trip_duration in min and seconds by using divmod()
	minute, second = divmod(total_trip_duration, 60)
    #show total_trip_duration in hour and minute
	hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time in sec,min and hour
    mean_travel=round(df['Trip Duration'].mean())
    mins, sec = divmod( mean_travel, 60)
	#if mean_travel greater than 60 minutes convert into hour 
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe mean of travel time is: {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe mean of travel time is: {mins} minutes and {sec} seconds.")


        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nDisplaying User Type counts...\n',user_types)
    # TO DO: Display counts of genderprint('\n Displaying Gender counts...\n'
    #i put gender and birth year in handling error because these two coulmn are't exist in washington dataset
    try:
        gender=df['Gender'].value_counts()
        print('\nDisplaying count of gender\n',gender)
    except:
        print("\nThere is no 'Gender' column in this file.")      

    # TO DO: Display earliest year by using min() method.
    try:
        print('\nCalculating year of birth...\n')
        early_birth=df['Birth Year'].min()
        print('\nThe earliest year of birth:\n',early_birth)
		# to show the most recent birth year i used max() method 
        recent_birth=df['Birth Year'].max()
        print('\nThe most recent year of birth:\n',recent_birth)
		#to show the most common year of birth i used the mood() method.
        common_birth=df['Birth Year'].mode()[0]
        print('\n the most common year of birth :\n ',common_birth)
    except:
        print("\nThere is no 'Birth Year' column in this file.\n")

             

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_time = time.time()
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while True:
            if view_data=='yes':
                start_loc += 5
                print(df.iloc[start_loc:start_loc +5])
                review_display = input("Do you wish to continue?:Enter yes or no\n  ").lower()
                if review_display!='yes':
                    break
            elif view_data=='no':
                return
            elif view_data !='no' and view_data !='yes':
                print('\n There is error in splling .\n')
                view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
            

               
            
                       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)                                           

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)                     

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
		    print("Thank you for exploring bikeshare data GOODBYE !") 
            break


if __name__ == "__main__":
    main()
