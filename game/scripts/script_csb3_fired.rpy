label new_plan:
    scene outside_ltt
    show cs angry at center
    with fade
    cs "This really sucks. One of my favorite YouTubers just kicked me out of my dream job and told me to never come back!"
    show cs
    cs "I would be acting super emotional right now, but the years of angry YouTube comments against me have already worn me down."
    cs "Well, I guess I have no other choice than to look for another job."
    n "CS sulks away in defeat."

    scene alley with fade
    show cs disappointed with moveinright
    cs "Ugh, what am I going to do now?"
    cs "I don't even know what other job I could get."
    cs "I've spent most of my life editing..."
    n "Before CS can spend much time thinking about alternatives, someone comes running up to CS."
    show arceus at right with moveinright
    arceus "CS!"
    show cs scared
    cs "Ah! Arceus?!"
    arceus "CS, we gotta get outta here, fast."
    cs "OK, what? What's going on?"
    arceus "Cops. They're still after us."
    cs "Oh, come on, really?! Today has sucked bad enough already."
    arceus "What happened to you? I just thought you were out here for a smoke break."
    cs "Arc, I don't smoke."
    arceus "Man, I don't know."
    show cs disappointed
    cs "No, I got fired."
    arceus "Aw, man. That sucks. I'm sure we'll figure it out."
    arceus "Come on, let's go back to the hotel. We can think of something, I'm sure."
    cs "Alright man, thanks. Let's go."

    # scene hotel_lobby
    show cs at right
    show arceus at left
    with fade
    arceus "Come on up to my room, we'll workshop where to go from here."
    cs "Alrighty then. Not like I'll be able to pay for my own much longer..."
    arceus "Oh come on, don't talk like that. Come on."

    # scene hotel_room
    show arceus at right
    show cs at left
    with fade
    arceus "OK, let's think. We have two big problems. The cops, and money."
    cs "Right."
    arceus "Let's tackle these one at a time."
    cs "The cops, first."
    arceus "Nah, I don't think tackling the cops is going to work."
    show cs angry
    arceus "I'm thinking we need to convince them to give it up."
    show cs
    cs "How would we do that?"
    n "A knock is heard at the door."
    anno "Can I come in?"
    arceus "Yeah, of course."
    show anno at mid_left
    anno "Hey, CS, what are you doing here?"
    cs "I got fired. And the cops are still after us."
    anno "Ah, fuck. What's the plan?"
    arceus "Nothing yet... wait. Anno, I just got an idea."
    anno "What's up?"
    arceus "You know AI stuff, right?"
    anno "Well, yeah, but I don't see--"
    arceus "We AI generate a message to the cops. Tell them they don't need to go after us anymore."
    anno "From who?"
    arceus "HoH SiS."
    anno "Wait, yeah, I can totally do that, I have the models ready for that and everything."
    n "Anno starts typing away at his laptop, and within a few minutes, a voice plays out of the speaker."
    ed "I think CS is a pretty good guy. You shouldn't arrest him."
    cs "Oh my god, that's amazing! But what about you two?"
    anno "Gotcha covered."
    # IDEA: Maybe have an actual AI-generated clip here?
    obama "I'm officially pardoning Annorexorcist and Arceus3251, for helping me out of a pickle."
    arceus "Incredible as always, Anno."
    anno "I try."
    cs "But what about money? I'm still out of a job and I'd like to keep having a roof over my head."
    arceus "I don't know man, I can't think after all that. Let's take a bit and relax. Clear our heads."
    cs "Good call. Wanna play some Guitar Hero?"
    anno "I'm down, but, do you have controllers?"
    cs "Do I?"
    hide cs with moveoutleft
    n "Anno and Arc look at each other confused."
    show cs with moveinleft
    n "CS comes back holding two guitar controllers and a drum kit."
    cs "Saw em on the side of the road. Couldn't pass em up."
    jump guitar_hero

label guitar_hero:
    # scene guitar_hero with fade
    n "CS, Anno, and Arc relax by playing some Guitar Hero."
    arceus "Man, we're all pretty good at this."
    cs "Wait, this gives me an idea."
    anno "What?"
    arceus "No, you're not thinking..."
    cs "Let's start a band!"
    arceus "Man, there's no way that'll work. Playing a video game isn't the same thing as making real music."
    cs "Come on! Anno knows AI, Arc is actually a really good percussionist, and I have millions of scrobbles, so I know my music."
    anno "He has a point..."
    arceus "Does he?"
    cs "What's the worst that happens? We need money, don't we?"
    arceus "We do..."
    cs "Then let's do this!"
    anno "I'm down!"
    cs "Arc?"
    arceus "What do I have to lose?"
    cs "Woohoo!"  # haha I did it too Pakoo

    # scene hotel_room
    cs "Maybe we should call Blank. He's like, an actual musician."
    n "CS calls Blank on Discord."
    blank "CS? Where the heck have you been?"
    cs "Don't worry about it, I'll explain soon. I need tips on making music."
    blank "Man, I don't know, I just open FL Studio and kinda click shit until music comes out."
    cs "Wait, that's it?"
    blank "I mean, that's not {i}it{/i}, but--"
    cs "Awesome, thanks Blank!"
    n "CS hangs up."
    cs "Well, you heard the man. Anno, do you have FL Studio?"
    anno "Just got it."
    cs "Well let's get to work, boys!"
    jump write_song

label write_song:
    # scene black with dissolve
    n "After some time, the gang have their first song written."

    # scene hotel_room with dissolve
    show arceus at right with moveinright
    arceus "You know, that's not half bad."
    show anno at left with moveinright
    anno "I like it a lot!"
    show cs at center with moveinbottom
    cs "Wanna play it again one more time?"
    anno "Can do!"
    n "Anno hits play on the track."
    # IDEA: Actual instrumental here? I'm thinking rock-themed. Kinda Foo Fighters-y?
    n "{cps=15}{image=note_small1.png}We broke the chains, now we're free to fly,{w=1.5}\nEscaped concrete, and now we see blue skies{w=1.5}\nBecome brand new, we'll leave the past behind,{w=1.5}\nPrisoners no more, 'cause a new life we'll find{image=note_small2.png}"
    cs "Yeah, that's really good!"
    arceus "Well I guess all we have to do now is upload it."
    anno "Alright boys, what do we call it?"
    $ song_name = renpy.input("What should we call the song?", "Prison Break")
    cs "How about [song_name]?"
    anno "That's awesome."
    arceus "I like it!"
    cs "Alright, it's settled! Let's upload [song_name] to streaming services!"
    arceus "Are you going to plug it in the Discord?"
    cs "I guess I should, but people are going to be really confused as to why I'm not streaming still..."
    anno "I think they're used to you not streaming for a while."
    cs "Fair, but a music career?"
    arceus "Just say it's a side project."
    cs "Fair enough."
    n "Anno uploads the song, and CS tells the CSCord about it."
    discord "What the heck is this?"
    discord "Huh, this is pretty good."
    discord "CS can sing?!"
    cs "It's going well! People seem to like it."
    arceus "Let's hit the hay and check in on it in the morning."
    anno "Yeah, I'm getting tired."
    cs "Sounds good to me!"

    scene black with dissolve
    n "While they sleep, the song accumulates streams..."
    jump hotel_next_day

label hotel_next_day:
    # scene hotel_room with dissolve
    show cs at left with moveinleft
    cs "Let's go get breakfast."
    show anno with moveinleft
    anno "Free waffles, hell yeah."
    show arceus flipped at right with moveinleft
    arceus "Those sausages are amazing."

    # scene hotel_elevator
    show anno at left
    show arceus at right
    show cs
    with dissolve
    # play music elevator_music
    pause 2.0
    cs "So, see any good shows lately?"
    arceus "You watch TV?"
    cs "Not really."
    arceus "Mmm."

    pause 2.0
    cs "Do you have any ideas for{nw}"
    arceus "Man I {i}just{/i} woke up."
    cs "Yeah, sorry."

    pause 2.0
    # play sound elevator_ding

    # scene hotel_breakfast with dissolve
    show cs at center with moveinleft
    cs "Ah, nothing like a hotel breakfast to wake me up."
    n "The other two groggily join CS."
    show anno at left behind cs
    show arceus flipped at right behind cs
    with moveinleft
    n "They all sit down to eat."

    # show hotel_tabel behind cs with dissolve
    n "As they eat, CS check the stream numbers on [song_name]."
    # show cs surprised
    cs "Guys?"
    arceus "Mmm?"
    n "Arceus and Anno are stuffing their face."
    cs "The song has like, a hundred thousand streams."
    n "Arceus nearly spits out his food."
    arceus "It has what?!"
    n "CS shows Arc the phone."
    arceus "Holy shit!"
    anno "Wait, that's crazy actually."
    cs "This is amazing! We might have a ticket out of here! We won't have to run from the cops anymore!"
    n "A random patron turns to look at CS."
    cs "Uh... metaphorically, of course."
    