label csbiii_start:

    scene outside_ltt with fade
    show cs at left with moveinleft
    n "CS returns to LMG the next day."
    hide cs with moveoutright
    scene inside_ltt with fade
    show linus at center with moveinright
    linus "Welcome to Linus Media Group, come on in, I'll show you your desk."
    cs "Thanks Linus."
    scene black with fade
    n "Linus and CS walk to CS' new desk."
    scene csdesk with fade
    show linus at right with moveinright
    show cs at left with moveinleft
    cs "Wow! I thought this was an office, why do I get such a cool desk?"
    linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."
    cs "Holy shit, really? This is way better than any setup I've seen, let alone had."
    linus "You must've had really bad setups then, this only has 2080s, everyone else has 2080 TIs or GTX Titans."
    cs "I have absolutely no problem with 2080s."
    linus "Well, enjoy!"
    hide linus with moveoutright
    cs "I guess I better get to work on editing, let's see what videos I need to edit..."
    cs "Let's see, I have the new TechQuickie video on how live streaming works, or the video on how at least half of the keys on your keyboard should be macros..."
    cs "Dammit Taran, you can edit your own macro fetish content."
    cs "I guess I'll edit the livestreaming one."
    scene black with fade
    n "CS starts working on editing the TechQuickie video and Linus comes in to check on him."
    scene csdesk
    show cs at left
    with fade
    show linus at right with moveinright
    linus "Hey CS, how's the new video coming along?"
    cs "It's going well, I have the background all done and I'm working on adding graphics and fixing audio."
    linus "Wow! You're a fast worker, you'll get off of those old 2080s in no time."
    cs "Thanks Linus."
    linus "Speaking of live streaming, we need a new PC for the WAN Show, can you go and buy parts for one?"

    menu: 
        "What are you going to do?"
        "Go to the store.":
            jump microcenter
        "Help edit a video.":
            jump edit_video
label microcenter:
    cs "Sure, what parts do you need?"
    linus "We need eggs, milk..."
    linus "Just kidding."
    linus "I'll leave the details up to you since you've done a lot of live streaming, just get the highest end available."
    cs "Alright, I'll go get the parts."
    # Jumpcut, fade to black
    cs "I have your new streaming PC, it runs quite well too! Way better than my computer!"
    linus "Awesome! Lemme go move this into the othe-- WOAAAHHH!!!"
    n "Linus trips and falls, immediately destroying the insides and outsides of the PC that CS just built."
    cs "Oh damn, you okay there?"
    linus "No of course not! I just destroyed another one of these $20,000 computing machines! How the hell am I going to get another just like this?"
    cs "Well, you could just always buy more parts like these, I'm sure you have the budget for that."
    linus "No no, that's too expensive and wasteful, let me think…"
    linus "Hmmm….."
    linus "Wait! I just got a brilliant idea! Why don't you go buy more parts for me, we certainly have the budget to do that!"
    cs "Uhmm… I literally just said--"
    linus "Alright! The plan is settled! You can go fetch me some more parts for the ultimate streaming machine, and you get to decide what parts should belong in the computer!"
    cs "Okay but, are there any recommendations you would give me for building this? This is YOUR money, you know."
    linus "Nah, it's fine. I'm sure you will do well picking out parts, make sure to get the highest quality you can!"
    cs "Alrighty, I'll get going now."
    n "CS goes to Microcenter."
    cs "Okay gamers, we are buying some parts for our epic computing machine. Let's go inside the magical concrete structure to buy some computing parts."
    cs "Wow, this building looks a lot bigger than the places I would go shopping at near home."
    n "CS enters the building."
    cs "Woah! This place is huge!"
    cs "There are so many options to pick from! And I have as much money as I'll ever need too!"
    cs "Before I get too carried away though, I should probably start by buying the processor."
    n "CS goes to the CPU aisle."
    cs "My goodness, there are so many options."
    cs "I honestly don't know which one to pick."
    cs "Let's see here…"
    cs "I could get a super high-end Intel CPU since Linus still seems to default to Intel even after shilling for AMD…"
    cs "Or I could get a Threadripper, more cores would probably be better for streaming..."
    cs "Too many good options! I don't know what one to pick!"
    # REMEMBER TO CHANGE THIS
    cs "Whatever, I'll get *whatever choice since this doesn't change the path*"
    cs "Now for the GPU."

    menu:
        "Which card do you want to choose"
        "High end GPU":
            jump high_gpu
        "Low end GPU":
            jump low_gpu

label low_gpu:
    cs "I should probably try to save Linus some money. Most of the expensive parts he gets are from sponsors, he's not actually that rich."
    n "CS flags down an employee."
    cs "I'm trying to get a graphics card, and I want to save money, what do you have?"
    worker "Everything here is pretty expensive, lemme check the back…"
    n "The worker comes back."
    worker "Alright, I got this. It's pretty old, and it's covered in dust, but it's like $50."
    cs "Sounds great, I'll take it."

label edit_video:
    cs "Nah, I wanna finish this video first. That way I can help you pump out videos faster."
    linus "Alright, that's fine. I'll probably send Colton to get the parts instead, he's good at sucking up to those kinda things."
    cs "Alright haha, yeah I definitely wasn't using this as an excuse to get out of shopping!"
    linus "...ok? Whatever, just keep editing."
    cs "Yeah, no, don't worry I got this."
    hide linus with moveoutright
    n "Linus leaves the room."
    cs "Hmm, this video looks pretty great so far, I'm practically almost done at this point."
    cs "I wonder what the others will think of this though? I should probably get opinions from some of the other employees."
    show taran at right with moveinright
    taran "Need any help with anything?"
    cs "Hey Taran! You wanna check out my video so far?"
    taran "Sure, let it roll."
    scene csvideo with fade
    n "CS and Taran watch CS's video."
    scene csdesk
    show cs worried at left
    show taran at right
    with fade
    cs "Well, you think it's good?"
    taran "Hey hey! That's not half bad!"
    show cs happy
    cs "Thanks! I guess my many years of video editing is finally paying off after all."
    taran "They definitely have."
    taran "You know what? I think this video is so good, I don't even think Linus needs to check this."
    taran "He will be so surprised when you upload it, he will wonder how well you put it together in such little time."
    show cs
    cs "You really think so? I mean I don't want him to be upset with me."
    taran "Don't worry about it. If he thinks it is that bad, I'll take the blame on it."
    cs "That's nice and all, but do you think that's a good idea? I mean, I don't want to mess up my first chance at this."
    taran "Nah, don't worry about it."
    taran "Even if something dumb happens, he usually never gets mad at us for doing silly things like that."
    taran "Besides, he plays practical jokes on us half the time, so even if the video was dumb, I doubt he would be mad at all."
    cs "Well if you say so, I guess it's fine."
    cs "Let's wait and see how he reacts."
    taran "Alrighty then, I'll catch you later!"
    cs "For tonight, this{w=0.1} is{w=0.1} CS,{cps=*0.1} signing{cps=*10} out!"
    taran "...What did you say?"
    cs "Huh? I totally didn't say that, I'm just gonna leave."
    taran "..."
    n "..."
    taran "... This is {i}your{/i} office.."
    n "..."
    taran "Okay, I'll see you later then!"
    show taran flipped at right
    hide taran with moveoutright
    n "Taran goes back to his office."
    cs "Well, I guess since this video is already good enough, I can upload it now."
    cs "It's so crazy having the ability to access the LTT channels. There is so much crazy shit going on here!"
    cs "Oh well, time to upload this."
    n "CS pauses for a moment."
    cs "I don't know, I really feel like I shouldn't upload this yet."
    cs "It doesn't feel complete. Something is missing from it…"
    cs "Lemme go look at the project file and run through the video again."
    n "Just as CS was about to watch his video, an idea kicked in."
    cs "I got it! I know exactly what to do!"
    cs "If Taran really does mean what he says about Linus, then I'm sure he'll love this!"
    cs "I'm gonna turn this video into a YTP!"
    cs "It will be perfect! No one will expect it because they probably don't even know what I even did with my life for the past 13 years!"
    cs "As always, I should make sure it's as good as possible so at least Linus will enjoy it, along with his fans."
    cs "But I also don't have much time before Linus comes back and notices, so I need to hurry!"
    cs "Welp, time to get to work!"
    menu:
        "Good":
            hide cs
            hide csdesk
            show black
            with fade
            jump boost
        "Bad":
            hide cs
            hide csdesk
            show black
            with fade
            jump fired

label fired:
    $ renpy.movie_cutscene("movies/mymovie_cs.mpg")
    scene inside_ltt with fade
    n "The next day."
    n "CS walks into LMG to greet Linus."
    show cs at left with moveinleft
    cs "Hey guys! Did you all check out the new video?"
    show linus at right with moveinright
    linus "Yes, and we need to talk."
    cs "Don't worry, I already know it's perfect. It's so great, isn't it?"
    linus "It's actually the very opposite of that. You're fired."
    show cs disappointed
    cs "Wait, what?"
    linus "Look, I don't care how much you really wanted to humiliate me, just leave."
    cs "I don't understand, I didn't think you would be this upse-{nw}"
    linus "Just get out of here you stupid dumb animal!!"
    cs "..."
    n "CS turns around and stomps out of the building."
    show cs angry with hpunch
    hide cs with moveoutleft
    scene black with fade
    scene outside_ltt with fade
    show cs angry at center
    cs "This really sucks. One of my favorite YouTubers just kicked me out of my dream job and told me to never come back!"
    show cs
    cs "I would be acting super emotional right now, but the years of angry YouTube comments against me have already worn me down."
    cs "Well, I guess I have no other choice than to look for another job."
    return
label boost:
    n "The next day."
    scene inside_ltt with fade
    show cs at offscreenleft
    n "CS walks into LMG to greet Linus."
    show cs at left with moveinleft
    show linus at offscreenright
    cs "Hey guys! Did you all check out the new video?"
    show linus at right with moveinright
    linus "Yes we did."
    linus "It was…"
    cs "Oh shoot, it was awful wasn't it?"
    cs "Yeah, I should've realized my style is too crazy, I guess I should leave…"
    show cs flipped at left
    show linus behind cs at left with ease
    show linus at center with ease
    n "As CS turns around, Linus friendly punches him in the back. "
    linus "Dude what are you talking about? That video was awesome!"
    show cs at left
    cs "Woah wait, you actually like YTPs?"
    linus "Yeah man, you think I just hired you on the spot because of your obviously fake visa?"
    linus " I love your videos! I've been secretly hoping you would YTP one of mine for the longest time!"
    show linus at left with ease
    show linus at center with ease
    n "CS's frown fades in a big grin, as they both high-five."
    cs "Hell yeah! I would've never thought YTPs would help me in a business setting, nevermind that my BOSS enjoyed them!"
    cs "Alright! Well, I guess I better get back to poopin'!"
    show cs flipped at left
    show cs flipped at offscreenleft with ease
    n "Before CS heads out of the room, Linus shouts to him."
    linus "Hey, later today, I got a big surprise to show you. I'll stop by your office and we can check it out."
    cs "Sure thing!"
    scene csdesk
    show cs at center
    with fade
    n "When CS gets back to his setup, he starts letting his mind race with ideas."
    cs "Oh man, where do I even start now?"
    cs "I have so many ideas of videos to poop, I could even try to teach Linus how to YTP…"
    cs " I mean, with the amount of tech he drops on a daily basis, he kinda already is a YTP."
    cs "Alright well, back to editing!"
    n "The time flies by as CS dumps his ideas into Premiere."
    cs "Doo dee doo…"
    show linus at offscreenright
    n "Linus barges in. "
    show linus at center with ease
    with hpunch
    show cs at left
    show linus at right
    with ease
    linus "CS!!!"
    cs "WOAH SHi- you scared the crap out of me!"
    linus "Hah sorry, I'm just excited to show you this!"
    n "Linus holds out a rectangular box that reads on the front in black bold text DO NOT USE."
    cs "Umm, you sure this is the right box? It literally says-"
    linus "Yeah I know what it says, I just wrote this on here so no one else uses it."
    linus "Don't worry, I didn't like, buy it from some creepy dude at a garage sale that claims it's haunted."
    n "CS looks unnerved."
    linus "Look just, open the box. I'm sure you'll like it."
    n "CS cautiously takes the box, and opens the top. "
    n "Inside is what looks to be a graphics card, but with a brown youtube logo engraved into the side."
    cs "Woah, what is this Linus? A Youtube-brand graphics card?"
    linus "Not exactly. It's an experimental piece of hardware that we have never used before, and it's custom made."
    n "Linus holds the card into the air."
    linus "Behold! {w=0.5} The- WOAH SHIT {w=0.5}{nw}"
    with vpunch
    n "Linus loses grip of the card as it tumbles down onto the table next to him."
    n "CS facepalms, while you can hear Luke laughing in the background."
    cs "Goodness Linus, you should maybe not do that next time."
    linus "Yeah, I'm sorry. Maybe you should hold it." 
    linus "This card is called the YTX-9001 Ti, a PCI add-in for enhancing and optimizing Youtube Poops."
    n "CS's eyes widen."
    cs "Wait whaaat? That's awesome! How does this even work?"
    linus "We don't even know, we haven't even tested it yet."
    linus "It also apparently has Poop-tracing, which I'm curious to see how that works."
    cs "Well, what are we waiting for? Let's get this thing hooked up!"
    n "Linus and CS take apart CS's PC and put the card in."
    n "They then start the computer, and everything boots up as normal."
    linus "Alright, now that it's up and working, we need to install the drivers. The card came with a flash drive that includes them."
    n "As Linus inserts the flashdrive, a window off the side of the screen pops up saying \"Your new Peeforce Experience drivers are available\"."
    n "CS chuckles a bit."
    cs "Peeforce? I must admit, even these drive names are a bit silly."
    n "Linus Laughs."
    linus "If you want, we can wipe them later."
    cs "Wipe! Now you're in on it!"
    n "They both laugh as the drivers install, and once they're finished, CS boots up Premiere."
    scene csvideo with fade
    cs "Alrighty, let's see here. Why don't we try this on that YTP I just made?"
    linus "Go to the settings real quick, and find the YTP features. turn YTP mode ON to allow the poop-tracing."
    cs "Alright, here goes nothing."
    n "A loading bar appears as the timeline starts shifting and different edits are created in the process."
    cs "Holy crap! This is amazing! It optimized every part of my YTP!"
    linus "That's pretty cool, but let's try it on a completely new source."
    linus "Open the video that we just took yesterday."
    n "CS opens the video, and enables YTP ON again. The source starts already making edits to start with."
    linus "And hey, if you don't like the edits it makes, you can always turn it off or tweak the settings in that tab."
    scene csdesk
    show cs at left
    show linus at right
    with fade
    cs "Wow, thank you so much Linus for this!"
    linus "No problem! This was my gift to you. Now, we should make a review video of it before the day ends."
    cs "Sure thing, let's take the card out real quick."
    show black with fade
    n "Linus goes and gets the cameras set up, and they start to film the video."
    n "After they finish recording, CS goes up to Linus's office."
    #Todo get linus's office
    cs "Hey Linus?"
    linus "What's up CS? What do you need help with?"
    menu:
        "What does CS need help with?"
        "I want to work on YTPs.":
            jump ytp_edit
        "I want to do reviews":
            jump reviews
    
label ytp_edit:
    cs "I have a question about what I want to do here at LTT."
    n "Linus stands up and walks over to him."
    show linus at center with ease
    linus "Sure. I mean, what do you want to do?"
    cs "I really want to make more YTPs for you guys."
    n "Linus laughs a bit."
    linus "Oh, CS, When I gave you the YTP card that was meant for use on your own channel, not the LTT one."
    cs "I know, but--{w=0.25}{nw}"
    linus "I mean, for example.{w=0.5} TARAN! GET IN HERE!"
    n "Taran rushes up to Linus's office."
    show taran at right with moveinright
    taran "{i}panting{/i} Yes, {w=0.5}Linus? {w=0.5}What is it?"
    linus "Taran, have you ever seen a YTP?"
    taran "Other than the one CS made the other day? Not really."
    linus "See, CS? Not only will our audience be super confused, but our employees will be as well."
    cs "Alright... I see..."

    menu:
        "What will CS do?"
        "Show everyone more YTPs":
            jump both_fan
        "Ignore them and keep making your own YTPs.":
            jump ytp_fan

label both_fan:
    cs "You know what? Why don't you all come down to my office."
    linus "I mean.. Sure. Let's see what you have in stock."
    linus "Come on guys, let's go"
    hide taran with moveoutright
    hide linus with moveoutright
    hide cs with moveoutright
    scene csdesk with fade
    n "Linus gathers more employees as they follow CS to his office."
    show cs at left with moveinright
    show linus at mid_left with moveinright
    show taran at center with moveinright
    show luke at mid_right with moveinright
    show colton at right with moveinright
    luke "What is this all about Linus? I was just about to go home."
    linus "Boohoo, Luke, you probably don't even do anything at home."
    luke ":("
    colton "Hi guys! What did I miss? I thought we were going to build a streaming machine?"
    linus "Look Colton, we can do that tomorrow."
    cs "Hey guys~ CS Here! Showing you the wonderful world of YTPs!"
    linus "Oh no.."
    colton "A... what?"
    cs "Alright! Strap in because YouTube is where the poop is!"
    show black with fade
    play sound "ytpintro.ogg"
    n "After half an hour passes, CS has shown LTT what YTPs are all about."
    hide black with fade
    cs "Welp. Those are some of the best ones that I could find."
    taran "Hey, those were actually really funny. Linus, didn't you tell me about how much you actually liked YTPs?"
    linus "Nooooo….?"
    luke "Now that you say that…"
    linus "Alright fine! I guess if you all like it too, we could put some on our channel from time to time."
    cs "Hell yeah!"
    linus "But you still have to help with some other videos as well, not just YTPs."
    cs " Alright, that's fair."
    linus "Well, the rest of you can go back to what you were doing."
    colton "Oh yeah Linus? Before I go, I was told someone was banging on the door to enter just a minute ago."
    colton "They were dressed up like a furry or something."
    linus "Great CS, did you attract your furry fanbase to work here as well?"
    cs "I swear, I know, this doesn't have anything to do with my community."
    linus "Wait what do you mean I know? I was just joking about the furry fanbase."
    cs "..."
    linus "Whatever, let's just go check out who it is."
    n "CS and Linus rush to the front door."
    n "Linus goes to open the door."
    linus "Who's there? Is anyone here?"
    n "Suddenly, Arceus rushes in through the doors."
    arceus "CS! There you are! We need to go ASAP!"
    linus "So you DO have a furry fanbase who wants to join LTT! Damnit CS, I should've known."
    cs "Shut up Linus!"
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look CS, we don't have much time. I know that you got your citizenship with Anno here, but the cops are still looking for you, and they are headed to LTT to search for you!"
    linus "WHAAAAT? CS, why are the cops chasing you? This could seriously damage our reputation more than the time I mentioned I dropped hard R's as a kid!"

    menu:
        "What will CS do?"
        "I'm going to stay with LTT.":
            jump cops_ltt
        "Escape with Arceus.":
            jump arc_escape

label arc_escape:
    cs "Look I'm sorry Linus, I wish I could explain, but Arceus is right. I need to get going."
    linus "I am like, so confused and frustrated, this better not ruin the LMG."
    cs "I'm sorry guys, I'll try to catch you guys up after this."
    cs "This is CS, signing out."
    arceus "C'mon CS! We need to go!"
    n "CS and Arceus run out of the building, and try to find cover while they escape."
    n "As they are making their way away from the building, they can hear sirens grow in volume as flashing lights rush towards the LTT building."
    cs "This is awful, I was just starting to get along well with Linus and the gang."
    arceus "I'm sure they'll forgive you in due time, but for now, we need to lose the sight of the cops and get back to the United States."

label high_gpu:
    jump secret
