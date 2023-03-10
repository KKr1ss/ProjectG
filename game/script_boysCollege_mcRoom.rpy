screen boysCollege_mcRoom():
    imagebutton:
        xpos 0.5
        ypos 0.28
        idle "boysCollege_mcRoom/mc_bed.png"
        action Jump("boysCollege_mcRoom_sleep_in_bed")
    imagebutton:
        xpos 0.1
        ypos 0.28
        idle "shared/door_1.png"
        #action Jump("nav_boysCollege_2floor")
        action [Hide("boysCollege_mcRoom"), Jump("nav_boysCollege_2floor")]

label nav_boysCollege_mcRoom:
    $ current_location = "My room"
    $ current_label = "nav_boysCollege_mcRoom"
    scene bg mc room

    call screen boysCollege_mcRoom

label boysCollege_mcRoom_sleep_in_bed:
    menu:  
        "Do you want to sleep?"
        "Yes":       
            call advance_day() # advances time by 1 unit
        "No":
            "Im not sleepy."
    call nav_boysCollege_mcRoom