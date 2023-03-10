class DateTime_Handler:
    # s = '2023/03/01'
    # day = datetime.strptime(s, "%Y/%m/%d")
    
    time_of_day = ["morning", "noon", "evening"] #edit this list to rename, add or delete time of days
    end_of_day = time_of_day[-1]

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    end_of_week_days = week_days[-1]

    def advance_day(self):
        increment = 1
        while increment > 0:
            #if time_of_day[0] == end_of_day:
                #day += 1
                #day = day + timedelta(days=1)
            #time_of_day.append(time_of_day.pop(0))
            while self.time_of_day[2] != self.end_of_day:
                self.time_of_day.append(self.time_of_day.pop(0))
            self.week_days.append(self.week_days.pop(0))
            increment -= 1       

    def advance_timeOfDay(self):
        increment = 1
        while increment > 0:
            #if time_of_day[0] != .end_of_day:
            self.time_of_day.append(self.time_of_day.pop(0))
            increment -= 1