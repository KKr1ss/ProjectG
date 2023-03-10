screen boysCollege_2floor():
    imagebutton:
        xpos 0.2
        ypos 0.5
        idle "shared/door_1_unhovered.png"
        hover "shared/door_1_hovered.png"
        action [Hide("boysCollege_2floor"), Jump("nav_boysCollege_outside")]
    imagebutton:
        xpos 0.7
        ypos 0.28
        idle "shared/door_1_unhovered.png"
        hover "shared/door_1_hovered.png"
        action [Hide("boysCollege_2floor"), Jump("nav_boysCollege_mcRoom")]

label nav_boysCollege_2floor:
    $ Navigator.set_navigation_data("Boys college: 2. floor", "nav_boysCollege_2floor")
    scene bg boysCollege 2floor
    call screen boysCollege_2floor