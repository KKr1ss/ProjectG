init python:
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

    class Navigator:
        current_location = ""
        current_label = ""

        def set_navigation_data(self, current_location, current_label):
            self.current_location = current_location
            self.current_label = current_label
    
    class Inventory:
        money = 0

        def add_money(self, moneyToAdd):
            self.money += moneyToAdd
        
        def subtract_money(self, moneyToSubtract):
            if(self.money - moneyToSubtract < 0):
                return False
            self.money -= moneyToSubtract
            return True
        # label moneyPlus:
        #     $ Inventory.add_money(2000)
        #     "+ 2000$"
        #     jump nav_boysCollege_mcRoom 

        # label moneyMinus:
        #     if Inventory.subtract_money(1500):
        #         "-1500$"
        #     else:
        #         "Nincs péz"
        #     jump nav_boysCollege_mcRoom 
    
    class Inventory_Item:
        id = 0
        item_name = ""
        item_image = ""