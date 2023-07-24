init python:
    import math

    TOTAL_ROUNDS = 20
    SCISSOR_SPEED = 800 # px/s
    WIN_PERCENTAGE = 0.75
    SCISSOR_WIDTH = 158

    class EditGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None
            self.started = False
            self.scissors = Image("minigames/editing/scissors.png")
            self.hit_width = 100
            self.hit_position = 200
            self.scissors_place = 1000
            self.successes = 0
            self.attempts = 0

            self.last_frame_time = 0
            self.scissors_direction = False

            self.hit = False
            self.cut_positions = []

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
                self.hit_position = renpy.random.randint(self.hit_width, 1920 - self.hit_width)
                self.last_frame_time = st
                dt = 1 / 60
            else:
                dt = st - self.last_frame_time
            current_time = st - self.start_time
            r = renpy.Render(1920, 1080)

            #Entry point
            if not self.started:
                if 0 < current_time < 1:
                    # Display 3
                    countdown_renderer = renpy.render(Text("3", color="FF0000", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif 1 < current_time < 2:
                    # Display 2
                    countdown_renderer = renpy.render(Text("2", color="FFFF00", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif 2 < current_time < 3:
                    # Display 1
                    countdown_renderer = renpy.render(Text("1", color="00FF00", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif current_time > 3:
                    # Yell Go at the player
                    self.started = True

            # Move scissors back and forth
            if self.scissors_direction:
                self.scissors_place += (SCISSOR_SPEED * dt)
                if self.scissors_place >= 1920:
                    self.scissors_direction = False
            else:
                self.scissors_place -= (SCISSOR_SPEED * dt)
                if self.scissors_place < 0:
                    self.scissors_direction = True

            # Cuts
            for p in self.cut_positions:
                rr = renpy.render(Solid("#313131", xysize=(2, 115)), 1920, 1080, st, at)
                r.blit(rr, (p, 454))
                rr = renpy.render(Solid("#FFFFFF4D", xysize=(2, 115)), 1920, 1080, st, at)
                r.blit(rr, (p + 3, 454))

            # Green hitbox rectangle visual
            rectangle_renderer = renpy.render(Solid("#00FF00", xysize=(self.hit_width, 115)), 1920, 1080, st, at)
            r.blit(rectangle_renderer, (self.hit_position, 454))

            # Scissor visual
            scissor_renderer = renpy.load_image(self.scissors)
            r.blit(scissor_renderer, (self.scissors_place - (SCISSOR_WIDTH / 2), 154))

            # Score visual
            score_renderer = renpy.render(Text(str(self.successes)+"/"+str(TOTAL_ROUNDS), size=72), 1920, 1080, st, at)
            r.blit(score_renderer, (50, 950))
            left_renderer = renpy.render(Text(str(TOTAL_ROUNDS - self.attempts) + " cuts left!", size=72), 1920, 1080, st, at)
            r.blit(left_renderer, (50, 1000))

            # Hit the space bar
            if self.hit:
                # In box
                if self.hit_position <= self.scissors_place <= self.hit_position + self.hit_width:
                    self.successes += 1
                self.attempts += 1
                self.hit_position = renpy.random.randint(self.hit_width, 1920 - self.hit_width)
                self.hit = False
                self.cut_positions.append(self.scissors_place)

            # Return if game over
            if self.attempts >= TOTAL_ROUNDS:
                self.win = self.successes / self.attempts

            renpy.redraw(self, 0)
            self.last_frame_time = st
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and self.started:
                if ev.key == pygame.K_END:
                    self.win = 1
                if ev.key == pygame.K_SPACE:
                    self.hit = True
                if self.win is not None:
                    return self.win

        def visit(self):
            return [] # Assets needed to load

screen edit_game:
    default edit_game = EditGameDisplayable()
    # Add a background or any static images here.
    add "minigames/editing/bg.png"
    add edit_game

label play_edit_game:
    window hide
    $ quick_menu = False
    call screen edit_game
    $ quick_menu = True
    window show

    if _return >= 0.75:
        arceus "Ween."
        pause
    else:
        arceus "Lose :("
        pause

label edit_game_done:
    # Thing to do after the game if we reach here.
