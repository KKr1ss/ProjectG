screen boysCollege_mcRoom():
    imagebutton:
        xpos 0.5
        ypos 0.28
        idle "boysCollege_mcRoom/mc_bed.png"
        action Jump("boysCollege_mcRoom_sleep_in_bed")
    imagebutton:
        xpos 0.1
        ypos 0.28
        idle "shared/door_1_unhovered.png"
        hover "shared/door_1_hovered.png"
        #action Jump("nav_boysCollege_2floor")
        action [Hide("boysCollege_mcRoom"), Jump("nav_boysCollege_2floor")]

label nav_boysCollege_mcRoom:
    $ Navigator.set_navigation_data("My room", "nav_boysCollege_mcRoom")
    scene bg mc room
    call screen boysCollege_mcRoom

label boysCollege_mcRoom_sleep_in_bed:
    menu:  
        "Do you want to sleep?"
        "Yes":       
            $ DateTime_Handler.advance_day() # advances time by 1 unit
        "No":
            "Im not sleepy."
    call nav_boysCollege_mcRoom