init python:
    import math

    # Functions
    def damage_fighters(actor: Fighter, targets: list[Fighter], mult: float = 1, count: int = 1, crit: bool = False):
        for f in targets:
            for _ in range(count):
                f.hp -= actor.attack_points * mult * 1.5 if crit else actor.attack_points * mult

    def damage_over_time(actor: Fighter, targets: list[Fighter], mult: float = 1, turns: int = 1):
        for f in targets:
            f.damage_over_time.append(actor.attack_points * mult, turns)

    def random_damage_fighters(actor: Fighter, targets: list[Fighter], min_mult: float = 1, max_mult: float = 1, crit: bool = False):
        mult = max_mult if crit else renpy.random.uniform(min_mult, max_mult)
        for f in targets:
            f.hp -= actor.attack_points * mult * 1.5 if crit else actor.attack_points * mult

    def confuse_targets(actor: Fighter: targets: list[Fighter]):
        for f in targets:
            f.confused = True

    # Objects

    class Attack:
        def __init__(self, name: str, func: callable[[Fighter, list[Fighter], float, bool], None], mult: float = 1):
            self.name = name
            self.func = func
            self.mult = mult

        def run(self, fighters: list[Fighter], crit: bool = False):
            self.func(self, fighters, self.mult, crit)

    class Fighter:
        def __init__(self, name: str, enemy: bool, hp: int, ap: int, atk: int, attacks: list[Attack], multiplier: float = 1):
            self.name = name
            self.enemy = enemy
            self.health_points = int(hp * multiplier)
            self.max_health = int(hp * multiplier)
            self.armor_points = ap
            self.attack_points = int(atk * multiplier)
            self.attacks = attacks

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
                    self.normal.run(targets)
                elif style == "special":
                        self.special.run(targets)
                elif style == "psi":
                    self.psi.run(targets)
                else:
                    return

        def tick(self):
            if self.damage_over_time:
                for h, t in self.damage_over_time:
                    if t > 0:
                        self.health_points -= h
                    else:
                        self.damage_over_time.remove((h, t))

        @property
        def dead(self) -> bool:
            return self.health_points <= 0

    class Encounter:
        def __init__(self, fighters: list[Fighter], background: Displayable, music: str):
            self.fighters = fighters
            self.background = background
            self.music = music

        @property
        def allies(self) -> list[Fighter]:
            return [f for f in self.fighters if not f.enemy]

        @property
        def enemies(self) -> list[Fighter]:
            return [f for f in self.fighters if f.enemy]

    # Example Fighter object

    cs_fighter = Fighter("CS", False, 188, 5, 25, [
        Attack("Punch", damage_fighters),
        Attack("Bullet Spray", damage_fighters, 1.5)
    ])


    class RPGGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # Do some fancy things here!

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load


screen rpggame:
    default rpggame = RPGGameDisplayable()
    # Add a background or any static images here.
    add rpggame

label play_rpggame:
    window hide
    $ quick_menu = False
    call screen rpggame
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label rpggame_done:
    # Thing to do after the game if we reach here.
    pass
