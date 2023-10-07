screen skip_car():
    zorder 100
    layer "music"
    style_prefix "skip_car"

    frame at t_skip_car:
        imagebutton idle "images/skip_now.png" hover_sound "sfx-select.wav":
            action Play("sound", "sfx-valid.wav"), Hide("skip_car", Fade(1.0)), Jump("back_home")

transform t_skip_car:
    xanchor 1.0 xpos 0.95
    yanchor 0.0 ypos 0.05
    on show:
        alpha 0.0
        time 3.0
        linear 30 alpha 1.0

style skip_car_frame is empty

label car_dialogue:
    scene car plains
    show billy car
    with fade
    cs "Well Arceus, it has been quite a ride."
    arceus "It sure has. We've been through quite a lot haven't we?"
    cs "Yeah, I'm so tired. I can't wait to get some actual rest."

    show screen skip_car

    pause 1.0

    cs "So, Arc?"
    arceus "Yeh?"
    cs "Are you a furry?"
    arceus "I mean, I {i}am{/i} furry."
    cs "You know what I mean."
    arceus "Is it really being a furry if I'm literally not a human?"
    cs "Fair point."

    pause 1.0

    cs "You know, I can drive, Billy."
    billy "This is my car!"
    cs "Well, yeah, but if you don't want to drive the whole way..."
    billy "No, I'm good. You're in my car, and that means I'll drive!"
    cs "Alright man, I just don't feel like we paid you enough for this."
    billy "Everything I sell, it's always $19.95!"
    cs "Well, thanks man."
    billy "That's the power of friendship!"

    pause 1.0

    cs "So Arc, where'd you learn to hack like that?"
    arceus "College."
    cs "You went to college? I thought you'd been in prison for five years!"
    arceus "And...?"
    cs "How... how old are you?"
    n "Arc locks eyes with CS."
    cs "I forgot what I was saying, never mind."
    arceus "Yeah, that's fine."

    pause 1.0

    cs "How long is this drive?"
    arceus "You sound like a child asking their mom if they're at Disney World yet."
    cs "I'm sorry man, I just want to get home."
    billy "It's quite a ways away still!"
    cs "Aw man..."
    arceus "Listen, at least the cops aren't after us this time."
    billy "What?"
    cs "Don't worry about it."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    carla "Hey Billy, it's Carla!"
    billy "What are you doing in my car?"
    carla "I'm not in your car, I'm on the phone. You're using the Jupiter Jack, remember?"
    billy "Oh yeah."
    carla "We have a meeting in twenty minutes."
    billy "I'm in the fucking Northeast!"
    carla "What? What are you doing there?"
    billy "It's my car!"
    n "Billy hangs up the phone."
    billy "Unbelievable."
    
    pause 1.0

    arceus "CS, why do you still pay for Adobe Premiere?"
    cs "Well, I pay for the whole Creative Cloud."
    arceus "You know, I can get you the whole suite for free."
    cs "No, no, I know, I just don't feel like I should."
    arceus "Yarr."
    cs "No, thank you, I understand what you were insinuating."
    arceus ";)"
    billy "How much are you paying for it?"
    cs "Like $50 a month..."
    billy "Unbelievable! I wouldn't pay more than $19.95!"
    billy "And buy one get one free!"
    cs "What would I do with two Adobe suites?"
    billy "What would you do with two Grater Platers?"
    cs "Fair enough."

    pause 1.0

    cs "Hey Arceus?"
    arceus "Hmm?"
    cs "Ever heard of the Butterfly Effect?"
    arceus "Yeah, that's like where one little thing can effect something big later down the line."
    cs "Yeah, I've been thinking, what if like I took the other job Linus gave me?"
    arceus "What do you mean?"
    cs "Oh, Linus wanted me to build him a stream machine."
    arceus "Ah I see, that sounds cool."
    cs "I was thinking about if I would've done that."
    cs "I might've like, gotten into a fight and went to the hospital or something."
    cs "And then travelled the world!"
    arceus "That's very... descriptive."
    cs "That's what I love about the Butterfly Effect, is that it might've actually happened!"

    pause 1.0

    cs "Have you heard of Genshin Impact? Start your adventure on the continent of Teyvat, and--{w=0.5}"
    arceus "{b}No.{/b}"
    billy "I'm a pitchman, and even I won't stoop that low."
    n "CS shuts up."

    pause 1.0

    arceus "Okay so, CS, what is up with the catmaid outfit?"
    pause 3.0
    arceus "CS?"

    pause 3.0

    n "Billy gets a call on his Jupiter Jack."
    billy "Hi, it's Billy!"
    linus "Hey Billy, CS is with you, right?"
    cs "Oh hey Linus, it's me, CS!"
    cs "I'm sorry about the cop scenario. I had an issue with a company called HoH SiS where they scammed me, and I kinda beat up their workers."
    linus "It's all good, I heard that the cops were looking for them anyways."
    linus "I'm sorry to hear about all that, I hope you are doing well."
    cs "We are doing okay!"
    linus "That's good, I hope to hear from you again."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    iris "Arceus?"
    arceus "How did you-- who is this?"
    iris "We need to talk later."
    pause 1.0
    iris ":3"
    n "The phone hangs up from the other end."

    pause 1.0

    arceus "Hey remember that pizza place we went to?"
    cs "Yeah, why?"
    arceus "Well we spent the night there, and I swore there was someone watching us."
    cs "Oh really? Like when we were sleeping?"
    arceus "Yeah, I think I saw this dude with a funky hat, and he had a camera."
    cs "That's really creepy."

    pause 1.0

    arceus "Did you ever change the Mount Rushmore thing back?"
    cs "Nope!"
    cs "Why would I? It looks cool now!"
    arceus "..."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    billy "Hi, it's Billy!"
    pakoo "What did the dog say after a long day of work?"
    pause 3.0
    pakoo "That was ruff."
    n "Billy immediately hangs up."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    billy "Hi, it's Billy!"
    tv_billy "Hi, it's Billy!"
    tv_billy "Introducing the New Craptop that isn't sentient at all, from me, Billy Mays!"
    billy "What the actual fuck?"
    tv_billy "Hello? Did I get a new signal?"
    billy "You aren't Billy! I am Billy!"
    tv_billy "No! I am Billy! I died long ago and I'm now in Super Heaven, selling pointless products!"
    billy "No, fuck you! I am the real Billy!"
    cs "Yeah, dude from the radio, you sound like an imposter."
    arceus "sus{w=0.25}{nw}"
    tv_billy "And you sound like that one guy who I sold a laptop to from his old ass TV!"
    cs "No clue what are you talking about."
    n "Billy turns off the Jupiter Jack for a while."

    pause 1.0

    cs "Who called asking for you earlier, Arc?"
    arceus "No clue."
    cs "Huh."

    pause 1.0

    cs "Man, we should have a podcast or something."
    arceus "No, no we shouldn't."
    cs "What do you mean? We're just chatting right now and I think it's pretty funny!"
    arceus "You only think it's funny because we're the ones talking."
    arceus "Every group of idiot friends thinks their funny enough to have a podcast, and 99 percent of the time, they're wrong."
    billy "Yeah, I gotta agree with him on this one. I don't think anyone would find this funny."
    n "Arceus glances at the top-right corner of the screen."
    cs "What are you looking at?"
    arceus "Nothing."

    pause 1.0

    n "Arceus sniffs the air."
    cs "What do you smell, Arc?"
    arceus "Gas."
    cs "Oh, jeez, I hope the tank isn't leaking!"
    arceus "No, like, gas. Like, passed gas."
    cs "Oh, that was me."
    n "Billy rolls down the window for a bit."
    
    pause 1.0

    $ renpy.music.set_pause(True, "music")
    play music2 "moving_right_along.mp3"
    $ renpy.pause(5.0, hard = True)
    # 0:05.0
    cs "{cps=30}{image=note_small1.png}Moving right along, in search of good times and good news{image=note_small2.png}{w=0.8}{nw}"
    # 0:08.9
    cs "{cps=30}{image=note_small1.png}With good friends you can't lose{image=note_small2.png}{w=0.8}{nw}"
    # 0:11.4
    arceus "{cps=30}{image=note_small1.png}This could become a habit!{image=note_small2.png}{w=0.8}{nw}"

    stop music2
    $ renpy.music.set_pause(False, "music")

    pause 1.0

    cs "I spy with my little eye something blue."
    arceus "Is it the car?"
    cs "Yeah..."

    pause 1.0

    cs "Did you know you can buy 500,000 plastic straws on AliBaba for like $50?"
    arceus "Why... would you?"
    cs "I don't know, you just can."
    billy "That's an amazing deal!"
    arceus "I think that's for like, resturaunts."
    cs "I guess, but like, that'd be funny to do, right?"
    arceus "...no?"
    cs "Yeah, you're probably right."

    pause 1.0

    cs "I wonder what would've happened if we went south."
    arceus "Back at Compass Road?"
    cs "Yeah. Who knows how far we might've gotten..."

    pause 1.0

    cs "Let's play 20 Questions!"
    arceus "Sure."
    cs "OK, it's an object."
    arceus "Is it bigger than a breadbox?"
    cs "Nope."
    arceus "Um, is it useful?"
    cs "Yep!"
    arceus "Hmm, uh, do you use it with your hands?"
    cs "Yeah."
    arceus "Is it... uh, frick, is it in my house?"
    cs "Probably."
    arceus "Is it in a drawer?"
    cs "Usually?"
    arceus "Is it shiny?"
    cs "Typically, yeah."
    arceus "Is it a knife?"
    cs "Nope!"
    arceus "Dang it, uh, is it a tool?"
    cs "Yes?"
    arceus "OK, OK, is it in the kitchen?"
    cs "Yes!"
    arceus "OK, so is it a fork?"
    cs "Nope!"
    arceus "How many questions have I done?"
    cs "You're halfway in."
    arceus "A... spoon?"
    cs "That's the one!"
    arceus "Welp, yay."

    pause 1.0

    n "Arceus is reading a book."
    arceus "{i}Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much."
    cs "Arc? Are you... reading Harry Potter?"
    arceus "Yeah."
    arceus "{i}They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't hold with such nonsense."
    cs "Do you... have to read out loud?"
    arceus "Oh shit, I'm reading out loud?"
    cs "How do you not notice that?"
    arceus "{i}Mr. Dursley was the director of a firm called Grunnings, which made drills."
    cs "Yeah, you're doing it again."
    arceus "Sorry."

    pause 1.0

    cs "{i}First of all, let me get something straight: This is a journal, not a diary. I know what it says on the cover, but when Mom went out to buy this thing I specifically told her to get one that didn't say “diary” on it."
    arceus "OK, OK, I get it."

    pause 1.0

    cs "The fog is coming."
    arceus "The fog is coming, CS?"
    cs "The fog is coming, Arc."
    billy "Crap, the fog is coming!"
    cs "The fog is coming, Billy."
    n "The phone rings."
    digi "The fog is coming."
    arceus "Fuck, the fog is coming, Digi?!"
    digi "The fog is coming, Arceus."
    billy "The fog is coming."
    n "Billy hangs up the phone."
    cs "The fog is coming."

    pause 1.0

    n "CS hears something from the back of the car. It sounds like the fumbling of plastic."
    n "CS turns around."
    n "Arceus is mumbling under his breath."
    arceus "Right, up, right inverted, up inverted..."
    cs "Are you... solving a Rubik's cube?"
    arceus "Yeah, it's a hobby of mine."
    cs "Where the fuck did you get a Rubik's cube?"
    arceus "Man, we've been a lot of places the last few days. I don't remember exactly where I got a Rubik's cube."
    cs "I need to learn to stop asking questions."
    arceus "That you do."

    pause 1.0

    n "Billy turns on the Jupiter Jack again."
    tv_billy "Hi, Billy Mays here for Smacid!"
    billy "What the actual fuck?"
    tv_billy "The fast and easy way to smash stomach pain from the source!"
    billy "What is this shit? I would never sell this scammy crap!"
    n "Billy changes the channel on the Jupiter Jack."

    pause 1.0

    cs "Wouldn't it be funny if someone was listening to all of this?"
    arceus "Well they'd be really bored by now."

    $ achievement_manager.unlock("Bored")

    hide screen skip_car

    jump back_home
