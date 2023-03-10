screen boysCollege_2floor():
    imagebutton:
        xpos 0.25
        ypos 0.28
        idle "shared/door_1.png"
    imagebutton:
        xpos 0.7
        ypos 0.28
        idle "shared/door_1.png"
        action [Hide("boysCollege_2floor"), Jump("nav_boysCollege_mcRoom")]

label nav_boysCollege_2floor:
    $ current_location = "Boys college: 2. floor"
    $ current_label = "nav_boysCollege_2floor"
    
    scene bg boysCollege 2floor
    call screen boysCollege_2floor
