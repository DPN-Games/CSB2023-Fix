from __future__ import annotations

import renpy
import renpy.random  # noqa
from renpy.display.core import Displayable
from renpy.display.im import Image
from renpy.display.imagelike import Solid
from renpy.text import Text

"""renpy
python early:
"""

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
            print(f"Dealing {hit} damage to {f.name}.")

def heal_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Heal a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `overheal: bool`: Whether to allow targets to heal over their max health."""
    mult = options.get("mult", 1)
    overheal = options.get("overheal", False)
    for f in targets:
        hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
        hit *= 1 - (f.armor_points / 100)
        f.health_points += hit
        if not overheal:
            f.health_points = min(f.health_points, f.max_health)
        print(f"Healing {hit} damage from {f.name}.")

def damage_over_time(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Set a damage over time for a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `turns: int`: The number of turns to hit the targets for."""
    mult = options.get("mult", 1)
    turns = options.get("turns", 1)
    for f in targets:
        f.damage_per_turn.append((subject.attack_points * mult, turns))
        print(f"Added {subject.attack_points * mult} DOT to {f.name} for {turns} turns.")

def random_damage_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Damage a list of fighters for a value between two multiples..
    Valid options:
    - `min_mult: float`: The minimum multiplier on top of `subject`'s ATK to hit the targets with.
    - `max_mult: float`: The maximum multiplier on top of `subject`'s ATK to hit the targets with."""
    min_mult = options.get("min_mult", 1)
    max_mult = options.get("max_mult", 1)
    mult = max_mult if crit else renpy.random.uniform(min_mult, max_mult)
    for f in targets:
        hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
        hit *= 1 - (f.armor_points / 100)
        f.health_points -= hit
        print(f"Dealing {hit} damage to {f.name}.")

def confuse_targets(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Confuse a list of targets."""
    for f in targets:
        f.confused = True
        print(f"Confusing {f.name}.")

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
            print(f"Setting {f.name} HP to {f.health_points}.")
        elif stat == "ap":
            f.armor_points *= mult
            print(f"Setting {f.name} AP to {f.armor_points}.")
        elif stat == "atk":
            f.attack_points *= mult
            print(f"Setting {f.name} ATK to {f.attack_points}.")
        else:
            pass

def enemy_ai_neutral(subject: Fighter, encounter: Encounter):
    """Just kinda, choose a random guy and hit them."""
    attack_chosen = False
    while not attack_chosen:
        attack_idx = renpy.random.randint(0, len(subject.attacks) - 1)
        attack = subject.attacks[attack_idx]
        if not attack.available:
            continue
        else:
            attack_chosen = True
    targets = []
    if attack.target_count == 0:
        target_type = {"enemies": "allies", "allies": "enemies", "all": "all"}[attack.target_type]
        targets = getattr(encounter, target_type)
    else:
        for _ in range(attack.target_count):
            if attack.target_type == "enemies":
                targets.append(renpy.random.choice(encounter.allies))
            elif attack.target_type == "allies":
                targets.append(renpy.random.choice(encounter.enemies))
            elif attack.target_type == "all":
                targets.append(renpy.random.choice(encounter.fighters))
    print(f"[NEUTRAL AI] {subject.name} running attack {attack.name} on {[t.name for t in targets]}...")
    renpy.notify(f"{subject.name} running attack {attack.name} on {[t.name for t in targets]}...")
    renpy.pause(1.0)
    subject.attack(attack_idx, targets)

def enemy_ai_target_weak(subject: Fighter, encounter: Encounter):
    """Just kinda, choose a random guy and hit them."""
    attack_chosen = False
    while not attack_chosen:
        attack_idx = renpy.random.randint(0, len(subject.attacks) - 1)
        attack = subject.attacks[attack_idx]
        if not attack.available:
            continue
        else:
            attack_chosen = True
    targets = []
    target_type = {"enemies": "allies", "allies": "enemies", "all": "all"}[attack.target_type]
    targets = getattr(encounter, target_type)
    if attack.target_count != 0:
        targets.sort(key = lambda x: x.health_points)
        targets = targets[:attack.target_count]
    print(f"[TARGET WEAK AI] {subject.name} running attack {attack.name} on {[t.name for t in targets]}...")
    renpy.notify(f"{subject.name} running attack {attack.name} on {[t.name for t in targets]}...")
    renpy.pause(1.0)
    subject.attack(attack_idx, targets)

def enemy_ai_target_strong(subject: Fighter, encounter: Encounter):
    """Just kinda, choose a random guy and hit them."""
    attack_chosen = False
    while not attack_chosen:
        attack_idx = renpy.random.randint(0, len(subject.attacks) - 1)
        attack = subject.attacks[attack_idx]
        if not attack.available:
            continue
        else:
            attack_chosen = True
    targets = []
    target_type = {"enemies": "allies", "allies": "enemies", "all": "all"}[attack.target_type]
    targets = getattr(encounter, target_type)
    if attack.target_count != 0:
        targets.sort(key = lambda x: x.health_points, reverse = True)
        targets = targets[:attack.target_count]
    print(f"[TARGET STRONG AI] {subject.name} running attack {attack.name} on {[t.name for t in targets]}...")
    renpy.notify(f"{subject.name} running attack {attack.name} on {[t.name for t in targets]}...")
    renpy.pause(1.0)
    subject.attack(attack_idx, targets)

class AI:
    NEUTRAL = enemy_ai_neutral
    TARGET_WEAK = enemy_ai_target_weak
    TARGET_STRONG = enemy_ai_target_strong

# Objects

class Attack:
    def __init__(self, name: str, func: Callable[[Fighter, list[Fighter], dict], None], target_count = 1, target_type: str = "enemies", cooldown: int = 0, **kwargs):
        self.name = name
        self.func = func
        self.target_count = target_count
        self.target_type = target_type
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
    def __init__(self, name: str, enemy: bool, hp: int, ap: int, atk: int, attacks: list[Attack], sprite: Displayable, multiplier: float = 1, ai: callable = None):
        self.name = name
        self.enemy = enemy
        self._health_points = int(hp * multiplier)
        self._max_health = int(hp * multiplier)
        self._armor_points = ap
        self._attack_points = int(atk * multiplier)
        self.attacks = [copy(a) for a in attacks]
        self.ai = ai
        self.sprite = sprite

        self.damage_per_turn: list[tuple] = []
        self.confused: bool = False

    @property
    def health_points(self) -> int:
        return int(self._health_points)
    
    @health_points.setter
    def health_points(self, v):
        self._health_points = int(v)

    @property
    def max_health(self) -> int:
        return int(self._max_health)
    
    @max_health.setter
    def max_health(self, v):
        self._max_health = int(v)

    @property
    def armor_points(self) -> int:
        return int(self._armor_points)
    
    @armor_points.setter
    def armor_points(self, v):
        self._armor_points = int(v)

    @property
    def attack_points(self) -> int:
        return int(self._attack_points)
    
    @attack_points.setter
    def attack_points(self, v):
        self._attack_points = int(v)

    @property
    def normal(self) -> Attack:
        return self.attacks[0]

    @property
    def special(self) -> Attack:
        return self.attacks[1] if len(self.attacks) >= 2 else None

    @property
    def psi(self) -> Attack | None:
        return self.attacks[2] if len(self.attacks) >= 3 else None

    def attack(self, style: int, targets: list[Fighter]):
        hit = renpy.random.choice(True, False) if self.confused else True
        if hit:
            self.attacks[style].run(self, targets)

    def attack_ai(self, encounter: Encounter):
        self.ai(self, encounter)

    def tick(self):
        # DOT
        if self.damage_per_turn:
            for h, t in self.damage_per_turn:
                if t > 0:
                    print(f"{self.name}: Taking {h} DOT damage...")
                    self.health_points -= h
                else:
                    self.damage_per_turn.remove((h, t))
        # Confusion
        if self.confused:
            self.confused = renpy.random.choice(True, False)
            if self.confused:
                print(f"{self.name}: I'm still confused...")
            else:
                print(f"{self.name}: No longer confused!")
        # Cooldowns
        for a in self.attacks:
            report = False
            if a._turns_until_available != 0:
                report = True
            a._turns_until_available -= 1
            a._turns_until_available = max(0, a._turns_until_available)
            if report:
                if a._turns_until_available == 0:
                    print(f"{self.name}: {a.name} now available!")
                else:
                    print(f"{self.name}: {a.name} available in {a._turns_until_available} turns!")

    @property
    def dead(self) -> bool:
        return self.health_points <= 0

class Encounter:
    def __init__(self, fighters: list[Fighter], background: Displayable, music: str, scale: float, on_win: str, on_lose: str = "start"):
        self.fighters = [copy(f) for f in fighters]
        self.background = background
        self.music = music
        self.scale = scale
        self.on_win = on_win
        self.on_lose = on_lose

        for a in self.allies:
            a.health_points *= scale
            a.max_health *= scale
            a.attack_points *= scale

    @property
    def allies(self) -> list[Fighter]:
        return [f for f in self.fighters if not f.enemy]

    @property
    def enemies(self) -> list[Fighter]:
        return [f for f in self.fighters if f.enemy]
    
    @property
    def all(self) -> list[Fighter]:
        return self.fighters

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
    BULLET_SPRAY = Attack("Bullet Spray", damage_fighters, target_count = 0, target_type = "enemies", cooldown = 3, mult = 1.5)
    SLASH = Attack("Slash", damage_over_time, mult = 0.5)
    LIGHT_CAST = Attack("Light Cast", random_damage_fighters, cooldown = 3, min_mult = 1, max_mult = 1, mult = 3)
    INSIGHT = Attack("Insight", change_stat, stat = "atk", mult = 0.75)
    SHOTGUN = Attack("Shotgun", damage_fighters, target_count = 2, cooldown = 3, mult = 2)
    ENCOURAGE = Attack("Encourage", heal_fighters, target_count = 0, target_type = "allies", mult = 3)
    HIGH_NOON = Attack("High Noon", damage_fighters, target_count = 3, cooldown = 3, mult = 1)
    SCRATCH = Attack("Scratch", damage_fighters)
    ARMOUR = Attack("Armour", change_stat, stat = "ap", target_count = 0, target_type = "allies", cooldown = 3, mult = 2.5)
    DAMAGE_SCREM = Attack("Damage Screm", damage_fighters, target_count = 0, target_type = "enemies", mult = 0.5)
    SCREM = Attack("Screm", heal_fighters, target_count = 0, target_type = "allies", cooldown = 3, mult = 1)
    ELDRITCH_BLAST = Attack("Eldritch Blast", damage_fighters, mult = 1.5)
    RAINBOW_VOMIT = Attack("Rainbow Vomit", damage_over_time, cooldown = 3, mult = 1)
    ROBOPUNCH = Attack("RoboPunch", damage_fighters, mult = 1.25)
    HOLOSHIELD = Attack("HoloShield", change_stat, stat = "ap", target_count = 0, target_type = "allies", cooldown = 3, mult = 2.5)
    MUSIC_BOOST = Attack("Music Boost", change_stat, stat = "ap", target_count = 0, target_type = "allies", mult = 1)
    RAVE = Attack("Rave", change_stat, stat = "ap", cooldown = 3, mult = 0.5)
    SAMPLE_BLAST = Attack("Sample Blast", random_damage_fighters, min_mult = 1, max_mult = 4, mult = 1)
    GNOMED = Attack("Gnomed", confuse_targets, target_count = 0, target_type = "enemies", cooldown = 3)
    NUDGE = Attack("Nudge", random_damage_fighters, min_mult = 0.1, max_mult = 10, mult = 1)
    DRAW_IN = Attack("Draw in", change_stat, stat = "atk", target_count = 0, target_type = "allies", cooldown = 3, mult = 2)
    CONFIDENCE = Attack("Confidence", change_stat, stat = "atk", target_count = 0, target_type = "allies", mult = 1.5)
    PEP_TALK = Attack("Pep Talk", change_stat, stat = "ap", target_count = 0, target_type = "allies", mult = 1.5)
    RADS_ATTACK = Attack("RADS Attack", damage_over_time, mult = 0.5)
    AI_MIMIC = Attack("AI Mimic", confuse_targets, target_count = 0, target_type = "enemies", cooldown = 3, mult = 1)
    SHELL = Attack("Shell", random_damage_fighters, min_mult = 1, max_mult = 2, mult = 1)

class Fighters:
    CS = Fighter("CS", False, 188, 5, 25, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"))
    CS_WEAK = Fighter("CS", False, 188, 5, 25, [Attacks.PUNCH], Image("images/characters/cs/neutral.png"))
    ARCEUS = Fighter("Arceus", False, 160, 15, 35, [Attacks.SLASH, Attacks.LIGHT_CAST], Image("images/characters/arc/arceus.png"))
    PAKOO = Fighter("Pakoo", False, 145, 20, 30, [Attacks.INSIGHT, Attacks.SHOTGUN], Image("images/characters/pakoo.png"))
    MIKA = Fighter("Mika", False, 165, 20, 30, [Attacks.ENCOURAGE, Attacks.HIGH_NOON], Image("images/characters/mika.png"))
    KITTY = Fighter("Kitty", False, 155, 15, 20, [Attacks.SCRATCH, Attacks.ARMOUR], Image("images/characters/kitty.png"))
    TATE = Fighter("Tate", False, 170, 5, 30, [Attacks.DAMAGE_SCREM, Attacks.SCREM], Image("images/characters/tate.png"))
    ARIA = Fighter("Aria", False, 200, 10, 45, [Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT], Image("images/characters/aria.png"))
    DIGI = Fighter("Digi", False, 150, 20, 25, [Attacks.ROBOPUNCH, Attacks.HOLOSHIELD], Image("images/characters/digi.png"))
    NOVA = Fighter("Nova", False, 150, 0, 30, [Attacks.MUSIC_BOOST, Attacks.RAVE], Image("images/characters/nova.png"))
    BLANK = Fighter("Blank", False, 180, 5, 35, [Attacks.SAMPLE_BLAST, Attacks.GNOMED], Image("images/characters/blank.png"))
    MIDGE = Fighter("Midge", False, 165, 10, 25, [Attacks.NUDGE, Attacks.DRAW_IN], Image("images/characters/midge.png"))
    DB05 = Fighter("Db05", False, 9001, 9001, 50, [Attacks.CONFIDENCE, Attacks.PEP_TALK], Image("images/characters/db.png"))
    ANNO = Fighter("Anno", False, 220, 30, 40, [Attacks.RADS_ATTACK, Attacks.AI_MIMIC], Image("images/characters/anno.png"))
    FANBOYA = Fighter("Fanboy",True, 50, 0, 15, [Attacks.PUNCH], Image("images/characters/nvidiafanboy.png"), ai = AI.NEUTRAL)
    FANBOYB = Fighter("Fanboy",True, 50, 0, 15, [Attacks.PUNCH], Image("images/characters/amdfanboy.png"), ai = AI.NEUTRAL)
    COP = Fighter("Cop", True, 150, 15, 30, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/cop.png"), ai = AI.NEUTRAL)
    COPGUYGODMODE = Fighter("Copguy", True, 9001, 9001, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/copguy.png"), ai = AI.TARGET_WEAK)
    COPGUY1 = Fighter("Copguy", True, 300, 20, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/copguy.png"), ai = AI.TARGET_WEAK)
    GUARD = Fighter("Guard", True, 250, 25, 40, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/guard_soldier.png"), ai = AI.NEUTRAL)
    SML_TANK = Fighter("Sherman", True, 500, 60, 120, [Attacks.SHELL], Image("images/characters/sherman.png"), ai = AI.TARGET_STRONG)

encounter = Encounter([], Image("images/bg/black.png"), "audio/legosfx.mp3", 1, "start", "secret")

# This is the displayable that controls what's happening in the boxes at the bottom of the screen

class StatBlockDisplayable(renpy.Displayable):
    def __init__(self, fighter: Fighter):
        self.text_size = 50
        self.fighter = fighter
        self.fighter_name = Text(self.fighter.name, color = "#FFCC00", size = 50)
        self.health_text = Text("HP: " + str(self.fighter.health_points) + "/" + str(self.fighter.max_health), color = "#FFFFFF", size = self.text_size)
        self.AP_text = Text("AP: " + str(self.fighter.armor_points), color = "#FFFFFF", size = self.text_size)
        self.ATK_text = Text("ATK: " + str(self.fighter.attack_points), color = "#FFFFFF", size = self.text_size)
        self.stat_back = Image("minigames/rpg/statbox.png")
        super().__init__(self)

    def render(self, width, height, st, at):
        x_al = 25
        y_al = 65
        spacing = 10
        self.health_text = Text("HP: " + str(self.fighter.health_points) + "/" + str(self.fighter.max_health), color = "#FFFFFF", size = self.text_size)
        self.AP_text = Text("AP: " + str(self.fighter.armor_points), color = "#FFFFFF", size=self.text_size)
        self.ATK_text = Text("ATK: " + str(self.fighter.attack_points), color = "#FFFFFF", size=self.text_size)
        r = renpy.Render(370, 270)
        r.place(self.stat_back)
        r.place(self.fighter_name, x = 25, y = 5)
        r.place(self.health_text, x = x_al, y = y_al)
        r.place(self.AP_text, x = x_al, y = y_al * 2)
        r.place(self.ATK_text, x = x_al, y = y_al * 3)
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
        r.place(self.fighter.sprite, x = 0, y = 0)
        # Making the health bar
        # THIS IS GARBAGE FULL OF MAGIC NUMBERS
        self.red_part = Solid("#FF0000", xsize = 1920 // 9, ysize = 1920 // 54)
        self.green_part = Solid("#00FF00", xsize = int((1920 // 9) * ((self.fighter.health_points) / (self.fighter.max_health))), ysize = 1920 // 54)
        r.place(self.red_part, x = (self.size[0] // 2)-((1920 // 9) // 2), y = int(25))
        r.place(self.green_part, x = (self.size[0] // 2)-((1920 // 9) // 2), y = int(25))
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

        self.reset()

    def reset(self):
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
                r.place(e, x = (1920 * (i * 0.33)), y = (1080 - e.size[1]) // 2)

        # This adds in the allies
        for i, s in enumerate(self.statblock_displayables):
            if not s.fighter.dead:
                r.place(s, x = (1920 * (i * 0.25) + 55), y = 810)

        return r

    def event(self, ev, x, y, st):
        import pygame  # noqa
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
    l.expect_block("fighters")

    fighters = []
    ll = l.subblock_lexer()
    while ll.advance():
        fighters.append(ll.rest())
        ll.expect_eol()

    l.advance()
    l.keyword("scale")
    scale = l.string()

    # goto
    l.advance()
    l.keyword("on_win")
    label = l.string()
    l.advance()
    l.keyword("on_lose")
    label2 = l.string()

    fighters = [f.upper() for f in fighters]

    return (bg, music, fighters, scale, label, label2)

def execute_rpg(parsed_object):
    b, m, f, s, l, ll = parsed_object
    global rpggame
    rpggame.encounter = Encounter(
        [getattr(Fighters, fighter) for fighter in f],
        Image(b),
        m,
        float(s),
        l,
        ll
    )
    rpggame.reset()
    renpy.jump("play_rpggame")

def lint_rpg(parsed_object):
    # I should probably do this at some point.
    pass

"""
rpg:
    bg "images/bg/X.png"
    music "audio/Y.mp3"
    fighters:
        cs
        cop
        etc...
    on_win "label"
    on_lose "label2"
"""
renpy.register_statement("rpg",
    parse = parse_rpg,
    lint = lint_rpg,
    execute = execute_rpg,
    block = True)
