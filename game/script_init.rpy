init python:
    from datetime import datetime, timedelta

default current_location = ""
default current_label = ""

#characters


#day cycle
default s = '2023/03/01'
default day = datetime.strptime(s, "%Y/%m/%d")
default time_of_day = ["morning", "noon", "evening"] #edit this list to rename, add or delete time of days
default end_of_day = time_of_day[-1] # this can automatically pick up the last element of time_of_day as above, remove above line if you want to use this.

#week cycle
default week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
default end_of_week_days = week_days[-1]

#call advance() # advances time by 1 unit
#"Day [day] [time_of_day[0]]"
#call advance(2) # advances time by 2 units
label advance_day(increment = 1):
    python:
        while increment > 0:
            #if time_of_day[0] == end_of_day:
                #day += 1
                #day = day + timedelta(days=1)
            #time_of_day.append(time_of_day.pop(0))
            while time_of_day[2] != end_of_day:
                time_of_day.append(time_of_day.pop(0))
            week_days.append(week_days.pop(0))
            increment -= 1       
    return

label advance_timeOfDay(increment = 1):
    python:
        while increment > 0:
            if time_of_day[0] != end_of_day:
                time_of_day.append(time_of_day.pop(0))
            increment -= 1 
    return