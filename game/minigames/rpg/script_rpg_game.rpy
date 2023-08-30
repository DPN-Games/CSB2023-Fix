python early:
    import math
    from copy import copy
    from typing import Callable

    # Functions
    def damage_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
        """Damage a list of fighters.
        Valid options:
        - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
        - `count: int`: The number of times to hit the targets."""
        mult = options.get("mult", 1)
        count = options.get("count", 1)
        for f in targets:
            for _ in range(count):
                hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
                hit *= 1 - (f.armor_points / 100)
                f.health_points -= hit

    def heal_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
        """Heal a list of fighters.
        Valid options:
        - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with."""
        mult = options.get("mult", 1)
        for f in targets:
            hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
            hit *= 1 - (f.armor_points / 100)
            f.health_points -= hit

    def damage_over_time(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
        """Set a damage over time for a list of fighters.
        Valid options:
        - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
        - `turns: int`: The number of turns to hit the targets for."""
        mult = options.get("mult", 1)
        turns = options.get("turns", 1)
        for f in targets:
            f.damage_per_turn.append(subject.attack_points * mult, turns)

    def random_damage_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
        """Damage a list of fighters for a value between two multiples..
        Valid options:
        - `min_mult: float`: The minimum multiplier on top of `subject`'s ATK to hit the targets with.
        - `max_mult: float`: The maximum multiplier on top of `subject`'s ATK to hit the targets with."""
        min_mult = options.get("mult", 1)
        max_mult = options.get("count", 1)
        mult = max_mult if crit else renpy.random.uniform(min_mult, max_mult)
        for f in targets:
            hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
            hit *= 1 - (f.armor_points / 100)
            f.health_points -= hit

    def confuse_targets(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
        """Confuse a list of targets."""
        for f in targets:
            f.confused = True

    def change_stat(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
        """Damage a list of fighters.
        Valid options:
        - `stat: str`: The stat to affect ("hp", "ap", or "atk")
        - `mult: float`: The multiplier on change the stat by."""
        mult = options.get("mult", 1)
        stat = options["stat"]

        for f in targets:
            if stat == "hp":
                f.health_points *= mult
            elif stat == "ap":
                f.armor_points *= mult
            elif stat == "atk":
                f.attack_points *= mult
            else:
                pass

    # Objects

    class Attack:
        def __init__(self, name: str, func: Callable[[Fighter, list[Fighter], dict], None], target_count = 1, auto_target: str = None, cooldown: int = 0, **kwargs):
            self.name = name
            self.func = func
            self.target_count = target_count
            self.auto_target = auto_target
            self.cooldown = cooldown
            self.options = kwargs

            self._turns_until_available = 0


        def run(self, subject: Fighter, fighters: list[Fighter], crit: bool = False):
            self.func(subject, fighters, crit, self.options)
            self._turns_until_available = self.cooldown

        @property
        def available(self) -> bool:
            return self._turns_until_available == 0

    class Fighter:
        def __init__(self, name: str, enemy: bool, hp: int, ap: int, atk: int, attacks: list[Attack], sprite: Displayable, multiplier: float = 1):
            self.name = name
            self.enemy = enemy
            self.health_points = int(hp * multiplier)
            self.max_health = int(hp * multiplier)
            self.armor_points = ap
            self.attack_points = int(atk * multiplier)
            self.attacks = [copy(a) for a in attacks]
            self.sprite = sprite

            self.damage_per_turn: list[tuple] = []
            self.confused: bool = False

        @property
        def normal(self) -> Attack:
            return self.attacks[0]

        @property
        def special(self) -> Attack:
            return self.attacks[1]

        @property
        def psi(self) -> Attack | None:
            return self.attacks[2] if len(self.attacks) >= 3 else None

        def attack(self, style: Literal["normal", "special", "psi"], targets: list[Fighter]):
            hit = renpy.random.choice(True, False) if self.confused else True
            if hit:
                if style == "normal":
                    self.normal.run(self, targets)
                elif style == "special":
                        self.special.run(self, targets)
                elif style == "psi":
                    self.psi.run(self, targets)
                else:
                    return

        def tick(self):
            if self.damage_per_turn:
                for h, t in self.damage_per_turn:
                    if t > 0:
                        self.health_points -= h
                    else:
                        self.damage_per_turn.remove((h, t))
            if self.confused:
                self.confused = renpy.random.choice(True, False)
            for a in self.attacks:
                a._turns_until_available -= 1
                a._turns_until_available = max(0, a._turns_until_available)

        @property
        def dead(self) -> bool:
            return self.health_points <= 0

    class Encounter:
        def __init__(self, fighters: list[Fighter], background: Displayable, music: str):
            self.fighters = [copy(f) for f in fighters]
            self.background = background
            self.music = music

        @property
        def allies(self) -> list[Fighter]:
            return [f for f in self.fighters if not f.enemy]

        @property
        def enemies(self) -> list[Fighter]:
            return [f for f in self.fighters if f.enemy]

        @property
        def turn_order(self) -> list[Fighter]:
            return self.allies + self.enemies

        @property
        def won(self) -> bool | None:
            if len(self.allies) == 0:
                return False
            elif len(self.enemies) == 0:
                return True
            else:
                return None

    class Attacks:
        PUNCH = Attack("Punch", damage_fighters)
        BULLET_SPRAY = Attack("Bullet Spray", damage_fighters, target_count = 0, auto_target = "enemies", cooldown = 3, mult = 1.5)

    class Fighters:
        CS = Fighter("CS", False, 188, 5, 25, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"))
        COP = Fighter("Cop", True, 150, 15, 30, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/copguy.png"))

    encounter = Encounter([], Image("images/bg/casino1.png"), "audio/card_castle.mp3")

    # This is the displayable that controls what's happening in the boxes at the bottom of the screen

    class StatBlockDisplayable(renpy.Displayable):
        def __init__(self, fighter: Fighter):
            self.text_size = 50
            self.fighter = fighter
            self.fighter_name = Text(self.fighter.name, color="#0000FF", size=50)
            self.health_text = Text("HP: "+str(self.fighter.health_points)+"/"+str(self.fighter.max_health), color="#FFFFFF", size=self.text_size)
            self.AP_text = Text("AP: "+str(self.fighter.armor_points), color="#FFFFFF", size=self.text_size)
            self.ATK_text = Text("ATK: "+str(self.fighter.attack_points), color="#FFFFFF", size=self.text_size)
            self.stat_back = Image("minigames/rpg/statbox.png")
            super().__init__(self)

        def render(self, width, height, st, at):
            x_al = 25
            y_al = 65
            spacing = 10
            self.health_text = Text("HP: "+str(self.fighter.health_points)+"/"+str(self.fighter.max_health), color="#FFFFFF", size=self.text_size)
            self.AP_text = Text("AP: "+str(self.fighter.armor_points), color="#FFFFFF", size=self.text_size)
            self.ATK_text = Text("ATK: "+str(self.fighter.attack_points), color="#FFFFFF", size=self.text_size)
            r = renpy.Render(370, 270)
            r.place(self.stat_back)
            r.place(self.fighter_name, x=25, y=5)
            r.place(self.health_text, x=x_al, y=y_al)
            r.place(self.AP_text, x=x_al, y=y_al*2)
            r.place(self.ATK_text, x=x_al, y=y_al*3)
            renpy.redraw(self, 0)
            return r
        
        def event(self, ev, x, y, st):
            pass

        def visit(self):
            return [self.health_text, self.AP_text, self.ATK_text, self.stat_back, self.fighter_name]

    # These are the enemy displayables. They display the enemy and the enemies health
    class EnemyDisplayable(renpy.Displayable):
        def __init__(self, fighter: Fighter):
            self.fighter = fighter
            self.red_part = Solid("#FF0000", xsize = 0, ysize = 0)
            self.green_part = Solid("#00FF00", xsize = 0, ysize = 0)
            self.size = renpy.image_size(self.fighter.sprite)
            super().__init__(self)
        
        def render(self, width, height, st, at):
            r = renpy.Render(640, self.size[1])
            r.place(self.fighter.sprite, x=0, y=0)
            # Making the health bar
            self.red_part = Solid("#FF0000", xsize=1920//9, ysize=1920//54)
            self.green_part = Solid("#00FF00", xsize=int((1920//9)*((self.fighter.health_points)/(self.fighter.max_health))), ysize=1920//54)
            r.place(self.red_part, x=(self.size[0]//2)-((1920//9)//2), y=int(25))
            r.place(self.green_part, x=(self.size[0]//2)-((1920//9)//2), y=int(25))
            renpy.redraw(self, 0)
            return r

        def visit(self):
            return [self.fighter.sprite, self.red_part, self.green_part]

    class RPGGameDisplayable(renpy.Displayable):
        def __init__(self, encounter: Encounter):
            self.encounter = encounter
            super().__init__(self)
            self.start_time = None
            self.win = None

            self.enemy_displayables: list[Displayable] = []
            self.statblock_displayables: list[Displayable] = []

            for e in self.encounter.enemies:
                self.enemy_displayables.append(EnemyDisplayable(e))

            for a in self.encounter.allies:
                self.statblock_displayables.append(StatBlockDisplayable(a))

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # These are the enemies
            for i, e in enumerate(self.enemy_displayables):
                if not e.fighter.dead:
                    r.place(e, x=(1920*(i*0.33)), y=(1080-e.size[1])//2)

            # This adds in the allies
            for i, s in enumerate(self.statblock_displayables):
                if not s.figher.dead:
                    r.place(s, x=(1920*(i*0.25)+55), y=810)

            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return self.enemy_displayables + self.statblock_displayables # Assets needed to load

    rpggame = RPGGameDisplayable(encounter)

    # Custom encounter statement

    def parse_rpg(lexer):
        lexer.require(":")
        lexer.expect_eol()
        lexer.expect_block("rpg")

        # block
        l = lexer.subblock_lexer()
        l.advance()
        l.keyword("bg")
        bg = l.string()
        l.advance()
        l.keyword("music")
        music = l.string()
        
        # fighters: subblock
        l.advance()
        l.require(":")
        l.expect_eol()
        l.expect_block("fighters")

        fighters = []
        ll = l.subblock_lexer()
        while ll.advance():
            fighters.append(ll.rest())
            ll.expect_eol()

        fighters = [f.upper() for f in fighters]

        return (bg, music, fighters)

    def execute_rpg(parsed_object):
        b, m, f = parsed_object
        global encounter
        encounter = Encounter(
            [getattr(Fighters, fighter) for fighter in f],
            Image(b),
            m
        )
        renpy.jump("play_rpggame")

    def lint_rpg(parsed_object):
        pass

    renpy.register_statement("rpg",
        parse = parse_rpg,
        lint = lint_rpg,
        execute = execute_rpg,
        block = True)

screen rpggame():
    $ global encounter
    # Add a background or any static images here.
    add encounter.background
    add rpggame

label game_loop:
    python:
        global encounter
        while encounter.won is None:
            # First phase, get the user inputs of what each fighter should do.
            actions = []
            for c in range(len(encounter.allies)):
                curr_fighter = encounter.allies[c]
                if not curr_fighter.dead:
                    valid_move = False
                    normal_name = curr_fighter.normal.name if curr_fighter.normal._turns_until_available == 0 else f"{curr_fighter.normal.name} [[{curr_fighter.normal._turns_until_available} turns remaining]"
                    special_name = curr_fighter.special.name if curr_fighter.special._turns_until_available == 0 else f"{curr_fighter.special.name} [[{curr_fighter.special._turns_until_available} turns remaining]"
                    while not valid_move:
                        selected_move = renpy.display_menu([("What will "+curr_fighter.name+" do?", None), (normal_name, "normal"), (special_name, "special")])
                        curr_attack = getattr(curr_fighter, selected_move)
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
                    actions.append((curr_fighter, selected_move, targets))
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
    play music encounter.music
    show screen rpggame
    jump game_loop

label rpggame_done:
    stop music
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label test_rpg:
    rpg:
        bg "images/bg/casino1.png"
        music "audio/card_castle.mp3"
        fighters:
            cs
            cop
            cop
            cop
