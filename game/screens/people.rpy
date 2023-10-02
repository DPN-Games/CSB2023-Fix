
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    global name_map
    name_map = {"cs": "cs188",
        "nova": "ItsNovaHere",
        "carguy": "CarGuy",
        "doug": "Doug McMillon",
        "cashier": "Cashier",
        "ed": "Ed",
        "wesley": "Wesley",
        "rich": "Richard",
        "michael": "Michael Rosen",
        "phil": "Phil Swift",
        "hoh_worker": "HoH SiS Workers",
        "digi": "DigiDuncan",
        "copguy": "Copguy",
        "arceus": "Arceus3251",
        "anno": "Annorexorcist",
        "border_guard": "Canadaian Border Guard",
        "linus": "Linus Sebastian",
        "mohs": "Mr. Mohs",
        "csgod": "CSGod",
        "luke": "Luke Lafreniere",
        "taran": "Taran Van Hemert",
        "colton": "Colton Potter",
        "sheriff": "Sheriff",
        "billy": "Billy Mays",
        "cultist": "Cultist Leader",
        "cultist2": "Cultists",
        "pakoo": "Pakoo",
        "peppino": "Peppino Spaghetti",
        "scott": "Scott Wozniak",
        "terry": "Terry Lesler",
        "lego": "Lego NXT Minifigure",
        "trailtrash": "Trailer Trash",
        "green": "Mr. Green",
        "jerma": "Jermey Elbertson",
        "pencil": "Pencil Greeter",
        "mettaton": "Mettaton",
        "tsa": "TSA Agent",
        "luigi": "Luigi Mario",
        "mika": "Mikapara",
        "bubble": "Bub Ble",
        "lancer": "Lancer",
        "tate": "alleZSoyez",
        "kitty": "Undead Kitty",
        "obama": "Barack Obama",
        "blank": "Blank Named",
        "aria": "Aria",
        "cop": "Copdude",
        "midge": "Midgalicis",
        "db": "DB05",
        "benrey": "Benrey",
        "guest": "Estatic Fan",
        "mean": "Meancarnavor",
        "howie": "Howie Mandell",
        "ges": "Ges",
        "gordon": "Gordon Ramsay",
        "scott_pres": "Scott Oelkers",
        "miku": "Hatsune Miku",
        "hammond": "The Top Gear Crew",
        "tom": "Tom Scott",
        "sayori": "Sayori",
        "round": "Mr. Round",
        "iris": "???"

    }

screen people_nav():
    add Color('#323e42', alpha=0.75)
    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350
            for k in name_map.keys():
                if k in persistent.seen:
                    if k == "iris":
                        textbutton name_map[k] action ShowMenu("person", k), ShowMenu("fake_error", "people.rpy", 126, "`bios/iris.txt` could not be rendered as a Text object.", "Hi, I'm Iris, a cosmic being with interest in the happenings of this reality, as well as some of the people involved in this story.\nDoes that sound too formal? I don't know. Hey, Digi, writing this shit's hard. You can fill in the rest from here.", _transition = determination)
                    else:
                        textbutton name_map[k] action ShowMenu("person", k)

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen people_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use people_nav

    style_prefix "codex"
    python:
        bio_count = len(name_map.keys())
        unlocked_bio_count = len(persistent.seen)
    vbox:
        xsize 850
        xalign 0.5 yalign 0.5
        xoffset 200
        text "View bios about all the wacky characters you've seen!"
        text "([unlocked_bio_count]/[bio_count] unlocked)"
        # TODO: Arc, can you center this? Thanks.


##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen person(l):

    style_prefix "codex"
    label name_map[l]

    tag menu
    use people_nav

    viewport:

        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 305 
        yoffset 200
        side_yfill True
        mousewheel True
        draggable True
        pagekeys True
        
        hbox:
            vbox:
                xsize 800
                ysize 800
                python:
                    try:
                        fetched = renpy.file(f"bios/{l}.txt").read().decode('utf-8').replace("\r", "")
                    except:
                        fetched = "The bio didn't load correctly. Ask Digi to fix the game."

                text (fetched)
            # MCs
            if l == "cs":
                add "images/characters/cs/neutral.png" xalign 1.0 yalign 1.0 zoom 0.75 xzoom -1
            elif l == "arceus":
                add "images/characters/arc/arceus.png" xalign 1.0 yalign 1.0 zoom 0.75
            elif l == "anno":
                add "images/characters/anno/anno.png" xalign 1.0 yalign 1.0 zoom 0.75
            # SECRET
            elif l in ["iris", "bubble", "lancer", "howie", "round"]:
                add f"secret/{l}.png" xalign 1.0 yalign 1.0 zoom 0.75
            elif l == "hoh_worker":
                add "images/characters/hoh_worker.png" xalign 1.0 yalign 1.0 zoom 0.50
            else:
                add f"images/characters/{l}.png" xalign 1.0 yalign 1.0 zoom 0.75
