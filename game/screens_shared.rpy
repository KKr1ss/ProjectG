screen main_HUD_day_bar:
    frame:
        xpos 0 ypos 0
        xsize 500
        hbox:
            text "[week_days[0]]"
    frame:
        xpos 0 ypos 0.05
        xsize 500
        hbox:
            text "[current_location]"

screen main_HUD_time_of_day_bar:
    frame:
        xpos 0.7 ypos 0
        xsize 300
        hbox:
            text "[time_of_day[0]]"
    frame:
        xpos 0.9 ypos 0
        xsize 50
        ysize 50
        imagebutton:
            idle "shared/advance_timeOfDay.jpg"
            action Jump("shared_advance_TimeOfDay")

label shared_advance_TimeOfDay:
    if (time_of_day[0] == end_of_day):
            "I cant advance time..."
    else:
        menu:
            "Do you want to advance the time of the day?"
            "Yes":       
                call advance_timeOfDay() # advances time by 1 unit
            "No":
                "I would rather not."
    jump expression current_label
    

screen main_HUD:
    use main_HUD_day_bar
    use main_HUD_time_of_day_bar
    
