screen boysCollege_outside():
    imagebutton:
        xpos 0.6355
        ypos 0.55
        idle "shared/door_boyscollege_outside_unhovered.png"
        hover "shared/door_boyscollege_outside_hovered.png"
        action [Hide("boysCollege_outside"), Jump("nav_boysCollege_2floor")]

label nav_boysCollege_outside:
    $ Navigator.set_navigation_data("Boys college", "nav_boysCollege_outside")
    scene bg boyscollege outside day
    call screen boysCollege_outside
    
