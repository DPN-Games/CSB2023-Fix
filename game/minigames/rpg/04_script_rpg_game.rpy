screen rpggame():
    add rpggame.encounter.background
    add rpggame

label game_loop:
    python:
        global rpggame
        encounter = rpggame.encounter
        while encounter.won is None:
            # First phase, get the user inputs of what each fighter should do.
            actions = []
            for c in range(len(encounter.allies)):
                curr_fighter = encounter.allies[c]
                if not curr_fighter.dead:
                    valid_move = False
                    attacks = []
                    for n, a in enumerate(curr_fighter.attacks):
                        name = a.name if a._turns_until_available == 0 else f"{a.name} [[{a._turns_until_available} turns remaining]"
                        attacks.append((name, str(n)))
                    while not valid_move:
                        selected_move = renpy.display_menu([("What will " + curr_fighter.name + " do?", None)] + attacks)
                        curr_attack = curr_fighter.attacks[int(selected_move)]
                        valid_move = curr_attack.available
                    target_count = curr_attack.target_count
                    targets = []
                    auto_target = curr_attack.auto_target
                    if auto_target:
                        if auto_target == "enemies":
                            targets = encounter.enemies
                    else:
                        for _ in range(target_count):
                            targets.append(renpy.display_menu([("Who will "+curr_fighter.name+" attack? ("+str(target_count)+")", None)]+[(e.name, e) for e in encounter.enemies]))
                    actions.append((curr_fighter, int(selected_move), targets))
            # Execute the attacks
            for c in range(len(actions)):
                actions[c][0].attack(actions[c][1], actions[c][2])
            renpy.redraw(rpggame, 0)
            for f in encounter.turn_order:
                f.tick()
                if f.dead:
                    encounter.fighters.remove(f)
            renpy.redraw(rpggame, 0)

    jump rpggame_done

label play_rpggame:
    window hide
    $ quick_menu = False
    play music rpggame.encounter.music
    show screen rpggame
    jump game_loop

label rpggame_done:
    stop music
    $ quick_menu = True
    window show
    hide screen rpggame

    if rpggame.encounter.won == True:
        $ renpy.jump(rpggame.encounter.goto)
    else:
        pass
        # Thing for lose condition
