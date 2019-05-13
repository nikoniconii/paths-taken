# You can place the script of your game in this file.

# Declare characters used by this game.
define c = Character('Cordelian', color="#c8ffc8", show_two_window= True, image="cordelian")
define maid = Character('Maid', color="#fff", show_two_window= True)
define e = Character('[pname]', color="#E8C8C8", show_two_window= True, image="emory")
define en = Character(' ', color="#E8C8C8", show_two_window= True, image="emory", what_prefix='{i}', what_suffix='{/i}')
define l = Character('Lisia', color="#D9799B", show_two_window= True, image="lisia")
define m = Character('Marco', color="#8489DB", show_two_window= True, image="marco")
define k = Character('Katherine', color="#E8665F", show_two_window= True, image="katherine")
define mother = Character('Mother', color="#FFF", show_two_window= True, image="mother")


define queen = Character('Queen', color="#fff", show_two_window= True)
define king = Character('King', color="#fff", show_two_window= True)
define aunt = Character('Auntie', color="#fff", show_two_window= True)
define uncle = Character('Uncle', color="#fff", show_two_window= True)
define vendor = Character('Vendor', color="#fff", show_two_window= True)
define c1 = Character('Cousin', color="#fff", show_two_window= True)
define tv = Character('TV', color="#9CBAF7", show_two_window= True)
define g = Character('Guest', color="#FFF", show_two_window= True)
define minister = Character('Minister', color="#FFF", show_two_window= True)
define stablehand = Character('Stable hand', color="#FFF", show_two_window= True)
define el = Character('[pname] & Lisia', color="#FFF", show_two_window= True)
define gm = Character('[gmname]', color="#FFF", show_two_window= True)
define gmm = Character('Guild Member 2', color="#FFF", show_two_window= True)
define na = Character('???', color="#FFF", show_two_window= True)

define fade = Fade(1.0, 0.0, 1.0, color="#000")
define fadee = Fade(1.0, 1.0, 1.0, color="#000")
define flash = Fade(1.0, .0, 1.0, color="#fff")


define gmname = "Guild Member 1"


transform rightt:
    xalign 0.80
    yalign 1.0
    
transform leftt:
    xalign 0.20
    yalign 1.0

transform closeright:
    xalign 0.70
    yalign 1.0
    
transform closeleft:
    xalign 0.30
    yalign 1.0


transform closerright:
    xalign 0.90
    yalign 0.30
    zoom 1.3
    
transform closerleft:
    xalign 0.15
    yalign 0.30
    zoom 1.3



##############################################################################
# Splashscreen
#
#
#
label splashscreen:

    scene black

    show companylogo:
        yalign 0.4
        xalign 0.5
    with fade

    $ renpy.pause(2.5)

    return


# The game starts here.
label start:
    
    scene black
    with fade
    
    call screen genders
    
label startgame:

    $ cordelian = 1
    $ lisia = 1
    $ marco = 1
    $ katherine = 1

    default overworld_choice1 = ""
    default overworld_choice2 = ""
    default overworld_choice3 = ""

    scene black
    with fade
    
    "{i}Hmm...? Where did I place that book?{/i}"
    
    scene bg castleinside1
    with fade

    show emory down frown
    with dissolve

    play music "Dash.wav" fadeout 1 
    queue music "Dash.wav"    

    "{i}Miss Renne will be upset if I don't finish my homework before tonight. But, she'll be even angrier if I show up without my textbook.{/i}"
    "{i}...{/i}"
    
    show emory up smile

    "{i}Ah, here it is!{/i}"

    show emory unsure frown 

    "{i}Wait... but there's another one over here...{/i}"
    "{i}...It must be Cordelian's! I forgot to bring it back to him.{/i}"
    "{i}Let me write my name in mine before I get them mixed up again...{/i}"

    python:
        pname = renpy.input("Sign your name.", length=15)
        pname = pname.strip()

        if not pname:
             pname = "Emory"

    show emory up smile 

    e "There we go..."
    e "Alright, time to bring it back to him. He should be home by now."

    scene bg castle
    with fade 
    
    show emory up smile at leftt
    with dissolve 

    show emory talk 

    e "Cordelian! There you are."

    show emory smile

    show cordelian up at rightt
    with dissolve
    
    show cordelian talk
    
    c "Oh, [pname]! Don't tell me you've been waiting here all day just to see me."
        
    show cordelian up smile
    show emory down talk
    
    e "No, I was at home! Next time you go off somewhere, I hope you remember your manners and actually call someone every once in a while."

    show emory down frown

    "{i}Just like him, forgetting to tell his best friend when his parents are shipping him off somewhere else!{/i}"

    show emory up talk

    e "Here, I brought you your textbook I borrowed."

    show emory smile 
    show cordelian unsure talk

    c "You could have kept it, really."

    show emory talk 
    show cordelian smile

    e "Where did you go, anyway?"
    
    show cordelian down talk
    show emory up smile
    
    c "Don't you remember? I told you the other day my parents sent me to meet Katherine again."
    
    show cordelian up frown
    
    "{i}Oh, of course. The princess from a nearby country who's around our age.{/i}"
    
    show emory down frowntalk
    
    e "Well, did anything important happen?"
    
    show cordelian down talk
    show emory up smile
    
    c "Not really. They were still trying to negotiate trading laws and stuff."
    c "I mainly just read."
    c "I don't see why I had to be there for it though, I had no business being there."
    
    show cordelian down smile
    show emory up talk
    
    e "They probably just wanted you there for appearances."
    
    show cordelian down talk
    show emory up smile
    
    c "Yes, mayb-"
    
    show cordelian up frown
    show emory down frown 
    
    "{size=36}CORDELIAN!{/size}"
    
    c "..."
    
    show cordelian down frowntalk
    
    c "I think I'll see you later..."

    show cordelian frown
    
    hide cordelian
    with Dissolve(1.0)
    
    show emory unsure smile
    
    e "{i}He can't evade classes forever, I suppose...{/i}"
    
    show emory up frown
    
    m "Cordelian!"

    show emory down smile at leftt
    show marco down frown at rightt
    with Dissolve(0.5)
    
    show marco up talk
    
    m "[pname], have you seen Cordelian?"
    
    show emory up talk
    show marco frown
    
    e "Sorry Marco, his teacher found him before you did."
    
    show emory up smile
    
    "{i}Marco has always been an over-worrier when it comes to Cordelian... Of course, as his servant, if anything happened to him it would be Marco's fault.{/i}"
    
    show marco up talk
    
    m "I guess that's good... I haven't seen him in almost a week, ever since he left for his trip."
    m "His parents sent a group of agents with him and I just stayed here on a small 'break'."
    m "I haven't seen you around here this past week though. Where have you been?"
    
    show emory up talk
    show marco down frown
    
    e "I figured staying around here while Cordelian was away would be boring, so I just stayed at my house."
    e "I actually forgot he was leaving for so long... I thought he had said he was going to be seeing someone for a couple of days, but I didn't hear the part where he said he was going to be gone for a lot longer..."
    
    show emory up smile
    show marco up talk
    
    m "Yes, young master's parents have been making him take extensive trips to Dersion."
    m "They used to be day trips that I could accompany him on, but more recently they've been getting longer and longer, to his last few trips spanning from weekend to weekend."
    m "I suppose it's just to promote better relations with them, but still..."
    
    show emory unsure talk
    show marco down frown
    
    e "But what?"
    
    show emory up frown
    show marco frowntalk
    
    m "...Nothing."
    m "Ask Cordelian why he thinks he's been going, if you want to know."
    m "...Maybe there isn't any ulterior motives here..."
    
    show marco down frown
    
    "{i}Marco is unusually quiet and keeping to himself today... He's always been a soft spoken person, but not like this...{/i}"

    show emory unsure 

    "{i}And what does he mean by 'ulterior motives'?{/i}"
    
    show emory up talk
    
    e "I'll ask him when I see him later, after his class."
    e "He has World Economics to study today, so the class shouldn't be too long."
    
    show emory up smile
    show marco up talk
    
    m "That's good. I'm glad to hear his teachers aren't pressing him with too much right after his trip."
    m "Ah... By the way, I was talking to Lisia earlier today and she said she had a letter for you."
    
    show emory up talk
    show marco down frown
    
    e "Really? I'll go see what it is then."
    e "See you later!"
    
    show emory up smile
    show marco up talk
    
    m "Goodbye."

    show marco frown
    
    scene bg castionmanorinside
    with fade
    
    l "[pname]! Over here!"

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"
    
    show emory up smile at leftt
    show lisia up smile at rightt
    with Dissolve(0.5)
    
    show emory up talk
    
    e "There you are! Marco told me you had a letter for me." 
    
    show emory up smile
    show lisia down frowntalk
    
    l "I- well, I did find a letter addressed to you, but I-"
    l "I think I might have misplaced it while cleaning...?"
    
    show emory unsure smile
    show lisia down frown
    
    "{i}Lisia has always been a bit... absent-minded since I met her. But, as my personal servant, she is very loyal, just maybe not as trustworthy with feelings as with objects...{/i}"
    
    show emory frowntalk
    
    e "Well, we can just look for it. Where were you cleaning last?"
    
    show emory up frown
    show lisia down frowntalk
    
    l "I was cleaning in the study room, but really, you don't have to look for it. I lost it, I'll find it..."
    
    show emory down frowntalk
    show lisia down frown

    e "In {i}my{/i} study room?"

    show lisia down frown
    show emory down frown

    l "..."

    show emory frowntalk

    e "I told you not to worry about that room. I'll clean it up."

    show emory frown
    show lisia frowntalk

    l "But, your mother..."

    show emory up talk
    show lisia frown 

    e "It's alright."
    e "Come, I'll help you."
    
    show emory up frown
    show lisia down frowntalk
    
    l "Fine... Let's go upstairs to find it then."
    
    show lisia down frown

    scene bg emorystudy 
    with fade 

# label imagemap1:

# scene emorystudy
# show tsw
# with fade

# call screen emorystudy

# label historybook:

#     e "I think that's Cordelian's history book that I borrowed. I should probably return that soon."
    
#     $ book1 = 'found'
    
#     jump imagemap1
    
# label knife1: 
    
#     e "Is that a... knife?"
#     e "W-what's a thing like that doing around here?!"
    
#     $ knife1 = 'found'
    
#     jump imagemap1
    
# label mathbook:
    
#     e "Well, I found my math book, but I don't need that right now."
    
#     $ book2 = 'found'
    
#     jump imagemap1
    
# label letter:
    
    "{i}Ah, what a mess.{/i}"
    "{i}I hate asking Lisia to clean up after me, but maybe sometimes I should let someone with better skills in here...{/i}"
    "{i}I try to shuffle a few papers around in embarrassment.{/i}"
    
    e "Wait, what's this under here?"
    e "Hey Lisia, I found it!"

    show emory up smile at left:
        zoom 1.50
        yalign 0.35
    show lisia up smile at right:
        zoom 1.60
        yalign 0.35
    with Dissolve(0.5)
    
    show lisia up talk
    
    l "Wow, I can't believe it fell under there... I'm glad you found it, though!"
    l "What does it say?"
    
    show lisia up smile
    
    "{i}*shriiiip*{/i}"
    
    show emory unsure frown
    
    "{i}The letter is a light blue, which is Cordelian's favorite color. Does this have something to do with him?{/i}"
    e "..."
    
    show lisia down frowntalk
    
    l "What's wrong?"
    
    show lisia down frown
    show emory down frowntalk
    
    e "It's a cordial letter from the King."
    
    show emory up frown
    
    "{i}Wouldn't it have been faster to hand-deliver it to me while I was there earlier today...?{/i}"
    "{i}Ah, but nothing is that simple any more it seems...{/i}"
    
    show emory up talk
    
    e "It says there's a ball next week at the castle, and I'm invited."
    
    show emory up smile
    show lisia up talk
    
    l "Well, I would {i}hope{/i} you'd be invited..."
    
    show lisia up talk
    
    l "What's the occasion?"
    
    show lisia up smile
    show emory up talk
    
    e "The princess from Dersion will be visiting the country for the first time. I suppose I'll finally get to meet her then."
    
    show lisia up talk
    show emory up smile
    
    l "Ooo, that sounds exciting! I wish I could meet her!"
    l "I bet she wears flowing dresses enveloped in lace, and has fancy butlers waiting on her every whim, and wears only the finest jewelry from her country, and-"
    
    show lisia down frown
    show emory up talk
    
    e "Okay, I think that's enough day dreaming for today."
    
    show lisia down frowntalk
    show emory up smile
    
    l "Okay..."
    l "But, doesn't it say to RSVP in person?"
    
    show lisia up smile
    show emory up talk
    
    e "It does, yes."
    
    show lisia down frowntalk
    show emory up smile
    
    l "Shouldn't you go ahead and do so?"
    
    show lisia down frown
    show emory unsure talk
    
    e "Ah, but it's a hassle..."

    show emory smile

    "{i}She starts tapping her foot against the wood and glaring at me.{/i}"
    
    show lisia down frowntalk
    show emory up frown
    
    l "...Go."
    
    show lisia down frown
    show emory up frown
    
    e "..."
    
    show emory down frowntalk
    
    e "...I'm going to go RSVP right now..."
    
    show emory up frown
    show lisia up talk
    
    l "That sounds like a good idea."
    
    scene bg castle
    with fade

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"
    
    show cordelian smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)

    show cordelian up talk
    
    c "What's this? I barely finish signing these letters and you're giving me the {i}honor{/i} of another?"
    
    show cordelian smile
    show emory up talk
    
    e "Well, I had thought it was obvious I would be going, but Lisia persisted I RSVP."
    
    show cordelian up talk
    show emory up smile
    
    c "Why, you didn't have to do that. If you weren't there, I would have walked over and stolen you away anyway."
    c "And besides, your mother RSVP'd last night."
    c "While your here, why don't you sit down? I'm not busy for the next hour, so it'd be nice to sit down and take a break."
    
    show cordelian smile
    
label menu1:
menu: 
    "Sit Down with Him":
        $ sit = 'sat'
        
    "Go Home":
        $ sit = 'left'
        
if sit == 'sat':
    
    $ cordelian += 1
    
    show emory up talk
    
    e "Of course!"

    show emory at left:
        zoom 1.40
        yalign 0.28
    show cordelian at right:
        zoom 1.40
        yalign 0.35

    e "So..."
    
    stop music
    
    #play music "emotionalmusic.mp3" fadeout 1
    #queue music "emotionalmusic.mp3"
    
    show cordelian up frown
    show emory unsure frowntalk
    
    e "What's been troubling you recently?"
    
    show cordelian down talk
    show emory up frown
    
    c "That's really forward of you..."
    
    show cordelian up frown
    show emory down frowntalk
    
    e "I mean, you've been rather distant lately. After all your trips, you've been spending days seemingly avoiding the sunlight."
    e "Is there something wrong?"
    
    show cordelian down talk
    show emory down frown
    
    c "It's... it's nothing, really..."
    c "Just that, my parents..."

    show cordelian frown
    
    "{i}*knock knock knock*{/i}"
    
    show marco frown at center:
        xzoom -1
    with Dissolve(0.5)
    
    show marco frowntalk
    
    m "I'm sorry your Highness, was I disrupting something?"
    
    show marco frown at center
    show cordelian down talk
    
    c "No, it's fine. Come in."
    c "What is it?"
    
    show marco talk at center
    show cordelian down smile
    
    m "Your father has moved the meeting thirty minutes earlier, making it in about ten minutes."
    
    show marco frown at center
    show cordelian down frowntalk
    
    c "What-? Why would he do a thing like that?"
    
    show marco talk at center
    show cordelian up frown
    
    m "He did not say."
    
    show marco frown at center
    show cordelian down frown
    
    c "..."

    show cordelian frowntalk

    c "{i}Sigh...{/i} Tell him I'll be down in five minutes."
    
    show marco talk at center
    show cordelian frown
    
    m "I will be on my way then."
    
    hide marco
    with Dissolve(0.5)
    
    show cordelian down talk
    
    c "I'm sorry about this, it looks like I'll have to go... I'll see you another time, [pname]."
    
    stop music
    
    #play music "vnmusic.mp3" fadeout 1
    #queue music "vnmusic.mp3"
    
    jump night1
    
    
if sit == 'left':
    
    show emory up talk
    
    e "No, I'm afraid I need to be going now. I only had time to drop off the book, sorry."
    
    show emory down frowntalk
    
    e "But maybe we can talk tomorrow or some other time...?"
    
    show emory up frown
    show cordelian down frowntalk
    
    c "No, it's fine, it's fine..."
    c "Have a good day then."
    
    show cordelian down frown
    
    jump night1
    
label night1:
    scene bg bedroomnight
    with fade

    stop music fadeout 1
    
    "{i}What a long day...{/i}"
    "{i}I feel rather tired, though I guess I didn't do too much besides read and walk from my house to Cordelian's.{/i}"
    "{i}I'm a little worried about him... It seems his parents are overloading him with work.{/i}"
    "{i}He may be an adult now but even adults can have too much to work on and get crushed with the weight.{/i}"
    "{i}Maybe it'll be better tomorrow.{/i}"
    
    scene bg bedroomday
    with fadee

    "{i}Phew, a fresh new start to a new day!{/i}"
    "{i}I somewhat feel like bugging Cordelian again... I hope I won't be a bother.{/i}"
      
    scene bg castle
    with fade 
    
    show emory up smile
    with Dissolve(0.5)
    
    show emory up talk
    
    e "Cordelian! Are you around?"

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"
    
    show emory up smile at leftt
    show cordelian smile at rightt
    with moveinright
    
    show cordelian up talk
    
    c "Yes, I'm here of course, this is my house."
    c "How are you today?"
    
    show emory up talk
    show cordelian smile
    
    e "I was beginning to ask you the same thing. I'm fine, but are you okay?"
    
if sit == 'sat':
    show emory smile
    show cordelian down talk
    
    c "Why are you asking me that again?"
    
    jump notthatbad
    
if sit == 'left':
    
    show emory smile
    show cordelian up talk
    
    c "That's on odd question to ask me. What's the occasion?"
    
    jump notthatbad
    
label notthatbad:
    
    show emory unsure talk
    show cordelian down frown
    
    e "I'm worried about how you're doing. Your parents have been filling up every waking minute of your schedule, leaving you without any time to rest."
    
    show emory frown
    show cordelian down talk
    
    c "It's not that bad! I'm busy because it takes a lot of effort in order for me to be fit to become the king."
    c "I always knew that eventually the time would come when my studies became more rigorous. Seeing how I deal with the stress is part of my training."
    c "If I can't make it through this, then I definitely won't be able to make it through the tougher choices that come with ruling a country."
    c "Thank you for worrying about me, but I'm fine, really."
    
    show emory down frowntalk
    show cordelian down smile
    
    e "That's good..."
    e "Marco told me to ask you about something else, though..."
    
    show emory up frown
    show cordelian down talk
    
    c "Oh? What is it?"
    
    show emory up frowntalk
    show cordelian up frown
    
    stop music
    
    #play music "emotionalmusic.mp3" fadeout 1
    #queue music "emotionalmusic.mp3"
    
    e "He told me that your trips have been getting longer for a reason."
    
    show emory frown
    show cordelian down
    
    c "..."
    
    show cordelian down frowntalk
    
    c "We're still trying to work out partnerships with Dersion. Trade relations with them have been fine the past few years, but my parents want to make something a bit more lasting..."
    c "In the past, Sharan and Dersion have had rocky relations, which even resulted in conflicts centuries ago."
    c "This is a wealthy country now, but only because of innovations and new technologies made after the turmoil those conflicts caused."
    c "As the Prince of Sharan, my parents think it should be my duty to try and rectify good relations with Dersion so they don't turn sour again in our future."
    c "No matter what that entails."
    
    show emory unsure frowntalk
    show cordelian frown
    
    e "And what does that mean?"
    
    show emory frown
    show cordelian talk
    
    c "Don't worry about it."
    
    show cordelian down smile
    
    e "{i}That doesn't sound too good.{/i}"
    
    show cordelian down talk
    
    c "I have everything under control, everything's going to be alright."
    c "It's nothing bad, it's just..."
    c "...I can't tell you. You'll find out soon, though."
    
    show emory down frowntalk
    show cordelian down smile
    
    e "Why can't you tell me? I'm your best friend!"
    
    show emory frown
    show cordelian down frowntalk
    
    c "It's my parents idea, not mine..."
    c "They forbid me to talk about it for now, until everything is set in stone."
    c "Even from you. I'm sorry."
    
    show cordelian frown
    
    e "{i}This is the first time he's kept something big like this from me... And I've got a sneaking suspicion it isn't good, regardless of what he says.{/i}"
    e "..."
    
    show emory down frowntalk
    
    e "I trust you."
    e "You'll tell me when the time is right, so I'll go with that. I won't pry about it anymore."
    
    show emory up frown
    show cordelian down talk
    
    c "Thank you for that. I appreciate your trust and honesty."
    
    show cordelian smile
    
    stop music
    
    #play music "vnmusic.mp3" fadeout 1
    #queue music "vnmusic.mp3"
    
    show cordelian up

    c "I guess we should change this to a lighter subject..."
    c "Have you heard about the new outdoor cafe that opened up in town?"
    
    show emory unsure talk
    show cordelian smile
    
    e "I'm not taking you there."
    
    show emory smile
    show cordelian up talk
    
    c "Oh come on, why not? We need to check this place out! They might have good food, you never know!"
    
    show emory talk
    show cordelian smile
    
    e "You just want to sneak out of the castle, and make me your accomplice..."
    
    show emory smile
    show cordelian down talk
    
    c "Of course I want to get out of this place every once in a while!"
    c "And didn't you say it was good to take breaks and relax? This will be relaxing!"
    
    show cordelian up smile
    
    "{i}I don't quite remember saying that, and this will be a lot more nerve-racking for me than for him. I'll be the one in trouble if we were caught!{/i}"
    e "..."
    
    show emory unsure talk
    
    e "...Fine, I'll take you."
    
    show emory smile
    
    "{i}The only bad thing about being the Prince's friend is that I'm his first choice for helping him sneak off to the town, without his guards.{/i}"
    "{i}We don't usually get caught, as long as we don't spend hours gone, so we'll have to make this even quicker than usual due to his tight schedule...{/i}"
    "{i}But he is right, getting out and taking a break will be good for him, so I guess I should take him.{/i}"
    
    show emory talk
    
    e "Okay, get dressed. Meet me in the forest in thirty minutes."
    
    show emory up smile
    
    scene bg bedroomday
    with fade

    play music "Irreplacable Warmth.mp3" fadeout 1 
    queue music "Irreplacable Warmth.mp3"
    
    show emory frown 
    with dissolve 
    
    e "{i}I guess I'll need to change into my disguise, too...{/i}"
    l "[pname]!"
    
    show lisia up smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show lisia talk
    
    l "[pname], your parents have sent me to fetch you."
    
    show lisia up smile
    show emory talk 
    
    e "Oh? What do they want?"
    
    show emory smile
    show lisia talk
    
    l "They want to remind you that your mother's parents will be visiting and that you need to attend dinner with them here at 6 promptly."
    
    show emory frown
    show lisia up smile

    "{i}Oh, just great... Looks like that's going to cut into I and Cordelian's time in town. Looks like we'll have to be even more quick about it today than usual.{/i}"
    
    show emory talk
    
    e "Sure, tell them I'll be there. I need to catch up on some reading for now though, so could I have a couple hours of peace?"
    
    show emory smile
    show lisia talk
    
    l "Yes sir."
    
    show lisia up smile
    
    hide lisia
    with Dissolve(0.5)
    
    "{i}It's been almost a half hour, so I should be heading out.{/i}"
    
    scene bg forest
    with fade
    
    c "[pname]! Are you here?"
    e "Yes, I'm over here. ...Are the sunglasses really necessary?"
    c "Of course they are! Now come on, let's get moving."
    e "I have dinner with my grandparents tonight so we'll have to be even quicker than normal."
    c "...Fine."
    
    scene bg town
    with fade

    "{i}The city, as usual, is a bustling, fast-paced area.{/i}"
    "{i}Today is the weekly farmer's market, so vendors are lined against the street hoping to sell their crops.{/i}"
    "{i}Cordelian walks slowly, taking in every sight.{/i}"
    "{i}We walk shoulder to shoulder so as not to get separated in the crowd.{/i}"

    show cordelian disguise sunglasses smile:
        zoom 1.50
        yalign 0.33
        xalign 0.82
    show emory disguise smile:
        zoom 1.50 
        yalign 0.30
    with dissolve 

    show emory talk 
    
    e "Where did you say this place was again?"

    show emory smile 
    show cordelian talk 

    c "It was right down the street from here I believe..."

    show emory unsure talk 
    show cordelian smile

    e "You {i}believe{/i}? You brought me all the way out here on an assumption?"

    show emory smile 
    show cordelian talk 

    c "Not an assumption, it {i}is{/i} down here."

    show emory up talk 
    show cordelian smile 

    e "Well, even if it's not, it is a nice day out."

    show emory smile 
    show cordelian talk 

    c "I suppose it is. The weather has been mild this time of year."
    c "The past few months when I've visited Dersion it's been below freezing every time, so coming back home has constantly been a shock to my system."
    c "But still, it's pretty there. The land is littered with trees and nature, and the people there seem to build towns in accordance to nature."
    c "Here we've built sprawling cities almost wherever. It's a bit of a shame, really."
    c "I'm starting to notice a lot more of these types of things now, as time moves close to my inaugural ceremony. Obviously I'm not going to become King till both my parents die or step down, but my training will end soon."
    c "Still, I've just started noticing these small things. Some of them I might like to change, some I might not. I really don't know as of yet."

    show emory talk 
    show cordelian smile 

    e "It's good to notice those sort of things, since you'll be the ruler eventually."
    e "Being aware of your surroundings and people you're serving is good, and going to make you a great King."

    show emory smile 
    show cordelian blush talk 

    c "...Thank you."
    c "These few months have been hectic, but I'll make it through them. I won't let them crush me."

    show emory talk 
    show cordelian -blush smile 

    e "That's a good outlook on things."
    e "Say, is this the outdoor cafe you were talking about?"
    e "This cafe that says \"closed\"?"

    show emory unsure frown 
    show cordelian down frowntalk 

    c "...Damnit."
    c "...Look, I just found out the location, not the hours they were open!"

    show emory frowntalk 
    show cordelian frown 

    e "Good going. Now we just wasted an entire day of sneaking out for nothing."

    show emory frown 
    show cordelian talk 

    c "It's not for nothing, whenever I can escape the castle without my guards I'm grateful."
    c "I understand it's for my own protection, but I need just a bit of freedom and space. Thank you for coming out here with me."

    show cordelian smile 

    e "{i}*sigh...*{/i}"

    show emory up talk 

    e "It's no problem... Let's head back for now. I need to get going anyway, since I need to get ready for dinner tonight."
    
    show emory smile 
    show cordelian up talk 

    c "Plans?"

    show emory unsure talk 
    show cordelian smile 

    e "Yes- well, my mother's plans."

    show emory smile
    show cordelian talk 

    c "I see."
    c "I'm sure she's planned something {i}fun{/i} for you..."

    show cordelian smile
    show emory talk 

    e "Oh, for sure! Just dinner with my visiting relatives. Would you like to go in my place?"

    show cordelian talk 
    show emory smile 

    c "No, no, I couldn't possibly take some of your fun away."

    show cordelian smile 
    show emory talk

    e "Of course..."

    show emory smile 

    hide emory 
    hide cordelian 
    with dissolve 

    "{i}We continue down the road, heading back to the castle, making small comments at the sights.{/i}"
    "{i}He really does love visiting the town... but when he does with his guards, it always becomes a political stunt.{/i}"
    "{i}They are always trying to capitalize on parading him around in good faith...{/i}"
    "{i}As we walk further, he grabs my arm.{/i}"

    show cordelian disguise sunglasses down frown at rightt
    show emory disguise unsure frown at center
    with dissolve 

    show cordelian frowntalk

    c "Come on, quickly!"

    show cordelian frown 
    show emory frowntalk 

    e "H-Huh...?"

    show cordelian frowntalk 
    show emory frown 

    c "It's the guards! They must be making patrols- or... or... they realize I'm not in the castle..."

    show cordelian frown 
    show emory frowntalk 

    e "Then where should we go?"

    show cordelian frowntalk 
    show emory frown 

    c "I..."

    show cordelian frown 

    "{i}He bites his lip.{/i}"
    "{i}If they catch us, it'll be nigh impossible for him to leave the castle unattended again...{/i}"
    "{i}Despite this, he's at a loss for words. It's not typical for him to be in a panic-inducing situation.{/i}"

    show emory frowntalk

    e "We'll..."

    menu:
        "Hide in the Cathedral":
            $ hide = "cathedral"
        "Blend into the crowd":
            $ hide = "crowd"

if hide == "cathedral":
    e "We'll hide in the Cathedral until they pass. If they take too long then we can slip out the back."

    show cordelian frowntalk
    show emory smile 

    c "Yes... yes, that's a good idea. Let's go."

    show cordelian frown 

    stop music fadeout 1

    scene bg cathedral
    with fade 

    play sound "cathedralbells.mp3"

    "{i}The Cathedral is surprisingly empty, despite it being the middle of the day. Only a few clergymen and such roam the halls.{/i}"
    "{i}Still, the bells ring loud and clear through the halls.{/i}"
    "{i}It's a spectacle to behold- Cordelian could stay here for hours looking around, and tries to soak up as much as he can.{/i}"
    "{i}I clasp my hand around his wrist and tug him towards the back of the building.{/i}"
    "{i}Here, even less people are walking around. A nun grabs a book and heads out the door to the room, leaving us alone.{/i}"
    "{i}It's also... a bit crowded in here.{/i}"

    show cordelian disguise sunglasses at right:
        zoom 1.70
        ypos 1.61
    show emory disguise at left:
        zoom 1.70
        ypos 1.65
    with dissolve

    show cordelian talk

    c "Ah... we should be able to avoid them here."

    show cordelian frown 

    "{i}Despite reassuring himself of that, he still has to catch his breath.{/i}"

    show emory talk 

    e "We'll be fine. They wouldn't think to look for us here."

    show emory smile 
    show cordelian down frowntalk 

    c "Yes, you're right... All because of your quick thinking."
    c "I froze. All I could think about it what my father would say when he found out."

    show emory talk
    show cordelian frown 

    e "It's alright. It's not everyday that you run into this sort of situation."
    e "When the time comes, you won't hesitate to make the right decisions. I know it."

    show emory smile

    "{i}I put my hand on his shoulder.{/i}"

    if cordelian >= 6:
        show cordelian blush 

        "{i}He puts his hand on mine.{/i}"

    show cordelian up talk 

    c "Thank you..."

    show cordelian -blush smile 

    "{i}I motion for us to sit down on one of the benches.{/i}"
    "{i}He doesn't argue. We've been walking for the past hour and I know he wants to see all he can, even if while sitting down.{/i}"

    show cordelian talk 

    c "To be honest, I've never been in this cathedral before."
    c "I've been in the one a few cities over on the countryside, but not this one."
    c "It really is beautiful and well taken care of."

    show cordelian down

    c "I bet it would be grand..."

    show cordelian smile
    show emory unsure talk

    e "What would be grand?"

    show cordelian talk
    show emory frown 

    c "A wedding. Here."

    show cordelian smile 
    show emory frowntalk 

    e "A-A wedding...? What makes you say that all of a sudden?"

    show cordelian talk 
    show emory frown 

    c "Royalty used to wed all the time in cathedrals. It was tradition."
    c "It's waned off in the past few decades but... I believe it'd be a sight to behold."

    show cordelian smile 
    show emory down frowntalk 

    e "Yes, I'm sure it would be..."

    show emory unsure frown
    show cordelian down frown

    "{i}He sighs and looks around the room one last time before standing.{/i}"
    "{i}Light shines through the window, getting out from under whatever cloud was holding it back.{/i}"
    "{i}This close to him... I can see the creases under his eyes.{/i}"
    "{i}What's on your mind...?{/i}"

    show cordelian frowntalk 

    c "It should be safe for us to leave now."
    c "If they were looking for me, then they should already be checking another area. If they were just making patrols, then they should still be looking somewhere else by now."
    c "Let's go before they come back."

    show cordelian smile 
    show emory up talk 

    e "Yes, let's."

    show emory smile 

    jump goinghome

if hide == "crowd":
    e "We'll blend into the crowd and sneak out. If we don't attract their attention then they shouldn't approach us, right?"

    show emory frown 
    show cordelian frowntalk

    c "Yes... that'll work. We just have to remain calm."

    hide emory 
    hide cordelian
    with dissolve 

    "{i}We move closer to the vendors and pretend to be looking at things on their tables.{/i}"
    "{i}They have all sorts of merchandise, from fruits to incense and shoes.{/i}"
    "{i}I keep an eye out for the guards as we make out way towards one of the side alleys.{/i}"
    "{i}Of course, that's when one of the vendors becomes too talkative.{/i}"

    vendor "Ah, sir! We have the finest rugs here."
    vendor "Take a look! Here, you can see the thread count on this one. So soft, isn't it?"

    c "N-No thank you, I'm fine."

    vendor "It can be yours for a low price- I'll cut a deal with you just for today."
    vendor "I have more in the back, let me show you-"

    "{i}I grab his wrist tightly.{/i}"

    e "No thank you."

    "{i}I pull him away.{/i}"

    show cordelian disguise sunglasses down smile at rightt
    show emory disguise down frown at leftt
    with Dissolve(0.5)

    show cordelian talk 

    c "Thank you..."

    show cordelian smile 
    show emory unsure talk 

    e "Let's get going before anyone else stops you."

    show cordelian talk 
    show emory smile 

    c "Yes, let's..."

    show cordelian smile 

    hide cordelian
    hide emory 
    with dissolve 

    "{i}We wait anxiously by another stall while the guards painstakingly check seemingly all the stalls on the other side of the road.{/i}"
    "{i}Once the alley is clearer, I pull him away from the stall and leave.{/i}"

    jump goinghome

label goinghome:
    
    scene bg forest
    with fade 

    show emory disguise -sunglasses at leftt 
    show cordelian disguise at rightt
    with dissolve 

    show cordelian talk

    c "Thank you for taking me."

    show cordelian smile 
    show emory talk 

    e "It was nothing. I'm glad we were still able to go."

    show emory unsure 

    e "We're not going to be able to do this much longer."

    show emory frown 

    "{i}To be honest, I wouldn't be surprised if this was the last time we're able to sneak out together.{/i}"

    show cordelian down talk

    c "I know, I know. But I'm thankful for every minute I've had."

    show cordelian up 

    c "Well, I hope you have fun at your little dinner party."

    show cordelian smile
    show emory talk

    e "It'd only be fun if you were there too."

    show cordelian blush talk
    show emory smile 

    c "That's sweet... but I'm afraid I also have dinner plans. Maybe another time."
    c "I'll see you soon."

    show cordelian -blush smile 
    show emory talk 

    e "Goodnight, Cordelian."

    show emory smile 

    scene bg bedroomnight
    with fade

    hide cordelian -disguise
    
    "{i}After dinner with my grandparents and hiding with Cordelian, I don't think I can stand...{/i}"
    "{i}Maybe tomorrow will be a calmer day than today was.{/i}"
    
    scene black
    with fade
    
    l "[pname]..."
    l "[pname], wake up!"
    
    scene bg bedroomday
    with fadee
    
    show lisia up smile at rightt
    show emory -disguise down frown at leftt
    with Dissolve(0.5)
    
    show emory frowntalk 
    
    e "What? What is it, Lisia?"
    e "Do you realize what time it is? And that I was sleeping?"
    
    show lisia down frowntalk
    show emory frown
    
    l "I was just following orders! Your parents sent me to fetch you- they've arranged for you to spend the day at your cousin's house in a nearby town."
    l "We need to get going soon if we'll make it back before nightfall."
    
    show lisia up smile 
    show emory unsure frowntalk
    
    e "Why can't they plan things a few days ahead...?"
    
    show lisia down talk
    show emory frown
    
    l "That would be too simple and not sporadic enough for them, I'm afraid..."
    
    show lisia smile
    show emory frowntalk
    
    e "Yes... Go finished getting ready, I still need to freshen up."
    
    show emory down smile
    
    scene bg forest
    with fade
    
    show emory up smile at leftt
    show lisia up smile at rightt
    with dissolve 
    
    show emory up talk
    
    e "Okay, let's get going."
    
    e "The sooner we get there, the faster we can leave..."
    
    show emory down smile
    show lisia up talk
    
    l "Aww, try to have a better outlook on things. It's going to be fine."
    l "Just find somewhere comfortable to sit and let them do all the talking- you just sit there and nod. Act like you're interested."
    l "That's what I do, and it works fine!"
    
    show lisia smile
    
label talktoyou:
menu:
    
    "I don't think they'd want to talk to you.":
        $ talktoyouu = 'nottalktoyou'
        
    "I don't think that would work for me.":
        $ talktoyouu = 'notworkforme'
        
    "I'll try that!":
        $ talktoyouu = 'trythat'
        
if talktoyouu == 'nottalktoyou':
    
    $ lisia -= 1
    
    show emory talk
    show lisia down frown
    
    e "Lisia, I highly doubt my cousins would want to talk to you while I'm over."
    
    show emory down talk
    e "I-I mean, they're too hyper and jumpy to have a conversation with a nice, quiet girl like you."
    e "They're still in the 'girls are gross' stage."
    
    show emory down smile
    show lisia down frowntalk
    
    l "They're a year younger than you."
    
    show emory down frowntalk
    show lisia down frown
    
    e "Everyone matures at different rates!"
    
    show emory frown
    show lisia down frowntalk
    
    l "Yeah, I can see."
    
    show lisia down frown
    show emory unsure talk
    
    e "So, ah... what will you be doing while I'm being interrogated?"
    
    show emory smile
    show lisia down frowntalk
    
    l "I'll just sit in the corner and wait till it's time to leave like I normally do."
    
    show lisia down frown
    show emory talk
    
    e "Oh, right..."
    
    show emory frown
    
    jump cousinhouse
    
if talktoyouu == 'notworkforme':
    
    show emory down frowntalk
    
    e "I'm not sure that would exactly work for my case, since this will be the only time I can talk to them."
    e "My cousins might not talk a lot to me while I'm there, but my aunt and uncle definitely will, and I can't evade them."
    
    show emory down smile
    show lisia down talk
    
    l "I guess you're right. Can't evade your relatives forever..."

    show lisia smile
    
    jump cousinhouse
    
if talktoyouu == 'trythat':
    
    $ lisia += 1
    
    show emory up talk
    
    e "I'll try that when we get there."
    
    show emory down talk
    
    e "I can't evade my aunt and uncle from their pandering, however..."
    e "But I can just sit back and keep quiet if I hang around my cousins- they won't care to talk to me."
    
    show emory up smile
    show lisia smile
    
    jump cousinhouse
    
label cousinhouse:

    show lisia up talk
    
    l "Well, let's get going then. You are ready, aren't you?"
    
    show lisia up smile
    show emory up talk
    
    e "Of course! The car's pulling up now."
    
    scene bg cousinhouse
    with fade
    
    aunt "So, how have your studies been?"
    aunt "Your mother had been telling me about all of these courses you're taking."
    
    e "They've been good so far. I'm studying at senior college level now."
    
    uncle "And what exactly are you studying again?"
    
    e "I'm studying to be a business major currently."
    
    aunt "Ah, like your father! I wish these two would become passionate about their degrees!"
    
    c1 "Mom, you forced me to start my studys to become a criminal justice major."
    uncle "Well, [pname], did my brother have any say so in choosing {i}your{/i} major?"
    
    e "Well, he had... ah, a bit of influence in it..."
    e "But, I did chose my major..."
    e "...for the most part, at least."
    
    aunt "That's good that you've chosen the career path of your dreams!"
    e "{i}That's not exactly what I said, but sure, let's go with that.{/i}"
    uncle "[pname], how old are you?"
    
    e "I'm 18."

    if gender == "boy":
    
        uncle "Isn't it about time for you to find a girlfriend? I'm sure a nice young gentleman like yourself has ladies lining up for you!"

    if gender == "girl":

        uncle "Isn't it about time for you to find a boyfriend? I'm sure a pretty young girl like yourself has suitors lining up for you!"

    if gender == "niether":

        uncle "Isn't it about time for you to find a significant other? I'm sure a young, hardworking student like yourself has suitors lining up for you!"
    
    "{i}I always hate this part of trips...{/i}"
    
    e "I'm not really worried about dating at the moment. I'd rather work on my studies for the moment."
    
    aunt "Aww, but you {i}must{/i} have been interested in them before?"
    
    e "I've tried to always keep my head focused on taking over the family business when my father becomes to old to take care of it."
    
    "{i}I was wondering when these sort of questions would come up.{/i}"
    "{i}It's always got to come to these questions, huh?{/i}"
    "{i}At least they're not as bad as my parents...{/i}"
    
    aunt "Well, that is good I suppose..."

    if gender == "boy":
        aunt "But you'll need a wife eventually! You've got to start looking while you're young."

    if gender == "girl":
        aunt "But you'll need a husband eventually! You've got to start looking while you're young."

    if gender == "niether":
        aunt "But you'll need a spouse eventually! You've got to start looking while you're young."
    
    "{i}Just when I thought we had moved away from this...{/i}"
    
    e "My parents are always looking for 'potential dates' for me, so I don't worry about it too much."
    e "And besides, the perfect {i}person{/i} will come along eventually."
    
    uncle "Sure, sure. Just don't wait too long or you'll worry your parents!"
    
    e "Yes, wouldn't want to do that..."
    
    aunt "My, look at the time! How quickly these hours have flown by! And to think, it feels as though we just sat down to talk!"
    
    e "Time sure flies when you're having fun..."
        
    e "Come on, Lis-"
    
    "{i}Oh, she's not here... looks like she left as soon as our car pulled up.{/i}"
    
    e "Well, it was nice seeing you all again! Goodbye!"
    
    scene bg bedroomnight
    with fade
    
    show emory up smile at leftt
    show lisia up smile at rightt
    with Dissolve(0.5)
    
    show lisia up talk
    
    l "Well, how did you enjoy your day trip?"
    
    show lisia up smile
    show emory up talk
    
    e "It was alright, I suppose. Well, about as good as I figured it would be."
    
    show emory up frown
    show lisia up frowntalk
    
    l "What do you mean by that?"
    
    show emory down frowntalk
    show lisia up frown
    
    e "I knew the routine questions they'd ask- how is school, what do you want to do with your life, why don't you have a girlfriend, etcetera."
    e "I just sat back and gave them the answers they wanted to hear."
    
    show emory down smile
    show lisia up talk
    
    l "I guess that's good... what really counts is you made it through the trip just fine!"
    l "Well, at least till next year, huh?"
    
    show emory down frowntalk
    show lisia up smile
    
    e "Haha, yes... Hopefully I'll be able to have some say so in visiting them by the time next year rolls around. One can only dream, huh?"
    
    show emory smile 

    l frowntalk "I'm sure it'll be fine..."

    show lisia frown
    show emory frown

    "{i}Her voice drifts off.{/i}"

    e up frowntalk "Is everything alright?"

    show emory frown 

    l up frowntalk "O-Of course!"
    l down "It's just..."

    show lisia frown 

    e unsure frowntalk "Just what?"

    show emory frown

    l frowntalk "Eventually I won't accompany you on these sorts of trips, will I..."

    show lisia frown 

    e frowntalk "What do you mean, Lisia? Why wouldn't you..."

    show emory frown 

    "{i}I can't finish my sentence. Lisia has always been by my side, but wouldn't it stand to reason that it's impossible for her to stay by my side forever...?{/i}"
    "{i}Still... it's hard to imagine what I'd do without her.{/i}"

    l frowntalk "Eventually you'll move away to find a place of your own or you'll get new servants..."

    show lisia frown

    menu:
        "I won't leave.":
            $ ldoubt = "leave"
        "You'll always be by my side.":
            $ ldoubt = "side"
        "I'll never forget you.":
            $ ldoubt = "forget"

    if ldoubt == "leave":
        e talk "I won't leave here, don't worry."
        e "This is my parent's estate which was handed down from parent to parent. I doubt I'll ever try to find more than a summer home anywhere else."

        show emory smile 

        l down talk "Of course..."
        l up "Yes, you're right. As long as you're here, I'll be here with you."
        

    if ldoubt == "side":
        e talk "You'll always be by my side, don't worry."
        e "Why would we ever fire you? You're one of the sweetest maids we've had in years."
        e "I couldn't imagine you going to work somewhere else."

        show emory smile

        l talk "Thank you..."

    if ldoubt == "forget":
        $ lisia += 1

        e talk "I'll never forget you, Lisia."
        e "Yes, we won't be able to stay together forever... Eventually, we'll have to go our separate ways."
        e "But I won't ever forget you."

        show emory smile 

        l blush talk "Thank you..."


    l "I'm sorry to have upset you."

    show lisia smile

    e talk "It's alright."
    e "I'm glad you trust me enough to confide these things in me."

    show emory up talk
    
    e "It's starting to get late now, so I'll see you later. Thanks for coming with me."
    
    show emory up smile
    show lisia up talk -blush
    
    l "Of course. Goodnight!"
    
    show lisia up smile
    
    hide lisia up smile
    with Dissolve(0.5)
    
    scene bg bedroomday
    with fadee
    
    "{i}I don't know what made me more tired, the hour long trip to my auntie and uncle's house yesterday or them pestering me...{/i}"
    "{i}I'm okay with talking to people, even relatives, just not when they ask the same questions everyone over the age of 40 does.{/i}"
    "{i}But, I can't do anything about it for now, so I'll just 'suffer' through it for a bit longer until I'm able to decide where my time is best spent.{/i}"
    "{i}Speaking of which, I have the day off from my studies today! Let's go bother Cordelian.{/i}"
    
    scene bg castle
    with fade
    
    "{i}Where's Cordelian...?{/i}"
    
    show emory unsure frown at leftt
    show marco down frown at rightt
    with Dissolve(0.5)

    "{i}Oh, here's Marco.{/i}"
    
    show marco up talk

    m "Are you looking for Cordelian?"
    m "Our majesty is giving a speech in a town close to the border, and asked Cordelian to be in his company for appearances."
    m "I know that's who you were looking for."
    
    show emory unsure talk 
    show marco down frown
    
    e "Oh... No wonder I couldn't find him..."
    
    show emory up talk
    
    e "Well, what are you doing right now? What's in your hands?"
    
    show emory up smile
    show marco up talk
    
    m "It's a checklist for the grand ball next week. I was asked to find some of the tables and decorations in the storage room to make sure we have enough on hand."
    m "I've already checked one of the storage rooms, but I was about to look in the one here."
    
    show emory up talk
    show marco up frown
    
    e "Great! Let's go!"
    
    show emory up smile
    show marco down frowntalk

    m "\"Go\"? I don't need your help."

    show emory unsure talk
    show marco frown

    e "You might not, but a bit of extra company never hurts."
    e "I'll stay out of the way, I promise."

    show emory up smile
    show marco frowntalk

    m "I suppose I can't help it if you follow me..."

    show marco frown 
    
    scene bg castleinside1
    with fade
    
    show emory up smile at left:
        zoom 1.50
        yalign 0.18
    show marco down frown at right:
        zoom 1.50
        yalign 0.19
    with Dissolve(0.5)
    
    show marco down frowntalk
    
    m "You won't be so energetic about this job after a while. It took me nearly 2 hours in the first storage room."
    
    show emory up talk
    show marco down frown
    
    e "Now you have help though, so it shouldn't take nearly as long! And we can talk, so it won't be boring."
    
    show emory up smile
    show marco up talk
    
    m "We'll see... For now, you can look through the boxes over there. I'll take the boxes in this corner."
    
    show emory up talk
    show marco down frown
    
    e "Of course."
    
    show emory up smile
    
    e "..."
    
    show emory up talk
    
    e "...So, what have you been doing lately?"
    
    show emory up smile

    "{i}He sighs and looks up at me, knowing this was going to happen.{/i}"

    show marco down talk
    
    m "I've been working on making sure this gala runs smoothly. After all, it will be the first time the princess from Dersion has visited this country."
    
    show emory talk
    show marco down frown
    
    e "Say, what was her name again?"
    
    show emory up frown
    show marco down talk

    ## TODO Katherine Bovegin of Dersion
    
    m "Katherine. Katherine Bovegin. She's the only daughter of the two reigning Bovegin emperors."
    
    show marco down frown
    
    "{i}Only daughter... sounds like Cordelian. Except, of course, with a different gender.{/i}"
    
    show marco talk
    
    m "Of course, I won't be in charge of everything- they've hired assistants for different venues of the event, such as catering and setting up the decorations."
    m "They've been planning this party for well over 2 months, but they didn't want it to reach the media's ears till the last minute."
    
    show marco down frown
    
    "{i}It makes sense... The media can be vicious, even at seemingly innocent events like this. All it takes is one bad rumor...{/i}"
    
    show emory unsure frowntalk
    
    e "About that time... what did you mean by 'ulterior motives'?"
    e "...Did it have something to do with Katherine?"
    
    show emory frown
    
    m "..."
    
    show marco frowntalk
    
    m "...You've learned in your history studies that our two countries haven't always had such a peaceful time as this, haven't you?"
    
    show emory frowntalk
    show marco down frown
    
    e "Of course."
    
    show emory frown
    show marco frowntalk
    
    m "Our majesty doesn't want these two kingdoms to fall into times of turmoil like that again, so they have come up with a 'plan' in coordinance with the rules of Dersion."
    m "I haven't been told more than that, but I can tell that whatever it is it's weighing heavily on Cordelian's mind."
    
    show marco down frown
    
    "{i}I've noticed this too... Not only has he been distant, but I've seen that something has been troubling him.{/i}"
    
    show emory frowntalk
    
    e "What do you think could be weighing so heavily on him?"
    
    show emory frown

    "{i}He's quiet. As usual, he's careful about his word choice.{/i}"

    show marco frowntalk
    
    m "...I don't know."
    m "He won't tell me, and it would be rude to pry him for information."
    m "Of course, maybe you could find out... He is quite favorable to you."
    
    show emory frowntalk
    show marco down frown
    
    e "I've tried, but he just told me that he couldn't say anything about it."
    e "He also said not to worry about him..."
    e "I guess we'll be finding out what he meant soon."
    
    show emory frown
    show marco frowntalk
    
    m "Yes..."

    show marco frown 

    e "..."

    show marco talk

    m "Have you found what's on the list yet?"
    
    show emory up talk
    show marco up frown
    
    e "I found some of it. I think this whole bin over here needs to be taken out, since it has most of the items in it."
    
    show emory up smile
    show marco up talk
    
    m "That's good- take it outside, and I'll take this bin as well. This bin has the rest of what we need."
    
    show marco frown
    
    scene bg castle
    with fade
    
    show marco frown at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show marco up talk
    
    m "Please set the box down right there."
    m "Thank you for your help, [pname]."
    
    show marco frown
    show emory up talk
    
    e "Ah, it was nothing."
    e "I'll be going now, it's about dinner time. See you another day!"
    
    show emory up smile
    
    scene bg bedroomnight
    with fade
    
    scene bg bedroomday
    with fadee
    
    "{i}Today's Sunday... this week has gone by quickly.{/i}"
    "{i}Wednesday is the royal ball, where I'll finally get to meet this Princess. I'm a little excited.{/i}"
    "{i}I already have my outfit prepared, so now all that's left to do is wait. I suppose for now I'll get breakfast and head out somewhere.{/i}"
    
##########################################################################
##############################  FIRST OVERWORLD CHOICE
    
label overworld_choice1:

scene overworld
with fade

call screen overworld1

label castle1: 
    
    $ overworld1_choice = 'cordelian'
    
    $ cordelian += 1
    
    scene bg castleinside1
    with fade
    
    show emory up smile at leftt
    show cordelian smile at rightt
    with Dissolve(0.5)
    
    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"

    show cordelian up talk
    
    c "Good morning, [pname]!"
    c "How are you today? Marco told me how you helped him yesterday."
    
    show emory up talk
    show cordelian smile
    
    e "I'm good, thank you. I came here yesterday, only to find out you were gone."
    
    show emory up smile
    show cordelian down talk
    
    c "Yes, I apologize... My father decided to take an unplanned trip across the country to deliver a speech and take me along."
    c "He received word of labor strikes and tried to coerce them to go back to work, or something like that. I wasn't exactly paying too much attention."

    show cordelian frown 

    "{i}Not... paying attention?{/i}"
    "{i}What's gotten into him?{/i}"
    
    show cordelian talk
    
    c "I believed it worked, or at least made the corporate owners more open to negotiations with the group."
    c "My father brought me along so as to show me the different situations I would find myself in in a few years."

    show cordelian unsure 

    c "...And, of course, for the press to see at least some of the royal family together in public."
    
    show emory up talk
    show cordelian smile
    
    e "I see..."
    e "Tell me, what is it like that far out? I haven't traveled farther than this county in a while, especially not that far."
    
    show emory up smile
    show cordelian up talk
    
    c "It's not too much different from here. I believe they're more culturally diverse there, since it's close to the borders of two neighboring countries."
    c "Our border policy with those two countries are rather lenient, and it's the easiest time in this country's history to become a citizen."
    c "The region there is also where plenty of factories have decided to settle in the past few years, so it's become a lot bigger since the last time I visited."
    c "Ah, but it's still a lovely place. The downtown section has been cleaned and is a sight to see."
    
    show emory up talk
    show cordelian smile
    
    e "That sounds nice. The capitol is wonderful, but... oh, I'd love to get out more."
    e "I think it would be nice to see a region that's sprawled outwards instead of up."
    
    show emory up smile
    show cordelian up talk
    
    c "It was interesting definitely, though we had to pass through miles and miles of farming land to get there. Thankfully I saw them all from the air."
    
    show emory up talk
    show cordelian smile
    
    e "Definitely."
    e "I wish I could stay longer, but I need to be going."
    e "I believe my mother is having guests over and wants me there. I'll see you later!"
    
    show emory up smile
    show cordelian up talk
    
    c "Sure. See you then!"
    
    jump overworld_choice1_end
    
label forest1:
    
    $ overworld1_choice = 'marco'
    
    $ marco += 1
    
    scene bg forest
    with fade
    
    show marco down frown at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show marco up talk
    
    m "Good morning, [pname]."
    
    show marco frown
    show emory up talk
    
    e "Good morning, Marco! How are you today?"
    
    show marco up talk
    show emory up smile
    
    m "I am fine, thank you. How has your day been?"
    
    show marco down frown
    show emory up talk
    
    e "It's been good so far, although I just woke up. What are you doing out here?"
    
    show marco up talk
    show emory up smile
    
    m "Reading. I have a few hours off in the morning."
    m "I'll still have to work later today, but they let me have a few hours to myself right now."
    m "Especially today, as they figured I'd worked hard enough yesterday on the planning for the gala..."
    m "Something about relaxing every once in a while."
    m "Thank you again for helping me out yesterday, it would have taken me much longer without your help."
    
    show marco frown
    show emory up talk
    
    e "It's no problem, really."
    e "How was work after I left?"
    
    show marco talk
    show emory up smile
    
    m "Not too terrible. I had to send a few errand boys to the decoration committee afterwards, but that's to be expected."
    m "Not everyone can do their job right the first time."
    
    show marco down frown
    show emory unsure talk
    
    e "...Sure, I suppose..."
    e "...Well, what are you reading?"
    
    show marco up talk
    show emory up frown
    
    m "It's a book on botany, the study of plants. This particular book is about a rare type of flowers."
    
    show marco down frown
    show emory up talk
    
    e "Ah, so you like to study plants? Why don't you take up gardening?"
    
    show emory up smile

    m "..."
    
    show marco down frowntalk

    m "I can't."
    m "My family has always served the royal family. I can't leave this role."
    
    show marco down frown
    show emory unsure frowntalk
    
    e "Oh..."
    
    show emory frown
    
    e "..."
    
    show emory unsure talk
    
    e "...I-I should go now, my mother arranged for company to come over later today and I should be there when they arrive-{w=1.0}{nw}"
    
    show marco frowntalk
    show emory frown
    
    m "Goodbye."
    
    show marco down frown
    
    jump overworld_choice1_end
    
label home1:
    
    $ overworld1_choice = 'lisia'
    $ lisia += 1
    
    scene bg castionmanorinside
    with fade
    
    show lisia up smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"
    
    show lisia up talk
    
    l "Good morning [pname]!"
    
    show lisia up smile
    show emory up talk
    
    e "Good morning, Lisia. It's a nice day today, isn't it?"
    
    show lisia up talk
    show emory up smile
    
    l "Yes, it certainly is... Don't tell me you're going to spend the whole day cooped up here, are you?"
    
    show lisia up frown
    show emory down frowntalk
    
    e "I am... my mother is having company over later today, so I figured I should stay close to the house since she wants me to see them."
    e "It's not too bad though, I'll just... read or something..."
    
    show emory up talk
    
    e "Say, what are you doing today?"
    
    show lisia up talk
    show emory up smile
    
    l "Let's see... I've got to store some books today in the library, and then rearrange one of the bookshelves, then dust them off..."
    
    show lisia down frown
    show emory up talk
    
    e "That sounds just slightly more riveting than seeing family. I'll come with you."
    
    show lisia down frowntalk
    show emory up smile
    
    l "Umm... [pname]... You really can't help me with this."
    l "It wouldn't look right for you to be helping your maid with housework. After all, it's what I'm paid for."
    
    show lisia down frown
    show emory down frowntalk
    
    e "Oh... You're right..."
    e "I'll just look through some of the books then while you clean, okay?"
    
    show lisia down frowntalk
    show emory up smile
    
    l "Okay..."
    
    show lisia down frown
    
    scene bg emorystudy
    with fade
    
    "{i}Our library is expansive... I could spend days here.{/i}"
    "{i}I don't have to go anywhere to find any books I need, so there's almost no reason to leave...{/i}"
    "{i}This book looks new... I guess I could start reading this.{/i}"
    
    show lisia up smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show lisia up talk
    
    l "Have you found a book you like?"
    
    show lisia up smile
    show emory up talk
    
    e "I don't know- I suppose I'll find out in a bit."
    
    show lisia up talk
    show emory up smile
    
    l "What's it about?"
    
    show lisia up smile
    show emory up talk
    
    e "It's a book on European history, dating back to almost a millennial ago."
    
    show lisia up talk
    show emory up smile
    
    l "Is it interesting?"
    
    show lisia up smile
    show emory up talk
    
    e "Well, I haven't opened it yet."
    
    show lisia down frowntalk
    show emory down smile
    
    l "Oh... I'll start cleaning and leave you to read."
    
    show lisia down frown
    
    l "..."
    
    show lisia down frowntalk
    
    l "It's kinda sad how all these books are covered in dust, huh?"
    
    show lisia down frown
    show emory down frowntalk
    
    e "Yes, it is, but there are so many books here that I doubt I'll be able to read them all in my lifetime."
    
    show lisia up talk
    show emory down smile
    
    l "That's true..."

    show lisia frown 

    "{i}Lisia turns back to her dusting.{/i}"
    "{i}I open the book to the preface. Ah, maybe I should have grabbed a different one...{/i}"
    "{i}Let's see... page one...{/i}"
    
    scene bg emorystudy
    with fadee
        
    "{i}Wh-{/i}"
    "{i}...Did I fall asleep while reading?{/i}"
    "{i}...Well, it certainly wasn't the most interesting book in the world...{/i}"
    "{i}Lisia's left... I suppose she finished cleaning up and let me sleep.{/i}"
    "{i}It's almost time for dinner, too! I can't believe I slept the whole day...{/i}"
    "{i}I'd better get ready for dinner.{/i}"
    
    scene bg bedroomnight
    with fadee
    
    "{i}Another day, over with...{/i}"
    
    jump overworld_choice1_end
    
label overworld_choice1_end:

    scene bg bedroomday
    with fade

    play music "Irreplacable Warmth.mp3" fadeout 1 
    queue music "Irreplacable Warmth.mp3"
    
    "{i}Lisia must have opened the curtains earlier. It's so bright in here...{/i}"
    "{i}Hmm... I believe I have Math in an hour.{/i}"
        
    "{i}Math is an alright subject for me, it's just the teacher...{/i}"
    "{i}I feel like I'd do better with just a textbook than him sometimes. But, my parents insisted on keeping him for some reason or another- I'm sure he must be a friend from school or something.{/i}"
    "{i}Either way, I tend to drown out his lessons and just follow the steps listed in the book.{/i}"
    
    "{i}I'll just head downstairs to eat breakfast and then go to class.{/i}"
    
    scene bg emorystudy
    with fade
    
    "{i}Class wasn't too bad today... at least it went by fast.{/i}"
    "{i}Now I have the rest of the day off... where should I go today?{/i}"
    
label overworld_choice2:

    scene overworld
    with fade

    ####################################### Monday- tsm

    call screen overworld2

label castle2:
    
    $ overworld2_choice = 'cordelian'
    
    $ cordelian += 1
    
    scene bg castleinside1
    with fade
    
    show cordelian smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"
    
    show cordelian up talk
    
    c "[pname], there you are!"
    c "Since you're here, you can help me pick out something."
    
    show cordelian smile
    show emory down talk
    
    e "Pick out what?"
    
    show cordelian up talk
    show emory up frown
    
    c "You'll see."
    
    show cordelian smile
    
    "{i}Cordelian takes my arm and pulls me on inside the main room where a group of stylists are awaiting.{/i}"
    
    show cordelian up talk
    
    c "They're here to make me a new outfit for Wednesday, and now you can help me figure out if it's okay!"
    
    show cordelian smile
    show emory up talk
    
    e "Oh, sure!"
    
    show cordelian up talk
    show emory up smile
    
    c "They've already assembled some jacket choices- which color do you think would be best?"
    
    show cordelian smile
    
label clothingchoices:
menu: 
    "Purple":
        $ clothing_choice = 'purple'
        
    "Light Blue":
        $ clothing_choice = 'lightblue'
        
    "Green":
        $ clothing_choice = 'green'
        
if clothing_choice == 'purple':
    
    show emory up talk
    
    e "I think the purple jacket would look good!"
    
    show cordelian up talk
    show emory up smile
    
    c "You think so? I was thinking more light blue..."
    
    show cordelian up frown
    show emory down frowntalk
    
    e "Well, go with light blue then."

    show emory down frown
    
    "{i}Why ask me, in that case?{/i}"
    
    show cordelian down talk

    c "Okay, that's what I'll go with."
    
    jump havetochoseblue
    
if clothing_choice == 'lightblue':
    
    $ cordelian += 1
    
    show emory up talk
    
    e "I like the light blue jacket the best!"
    
    show emory up smile
    show cordelian up talk
    
    c "I believe you're right- I like that one the most too. I'll go with the light blue one."
    
    jump havetochoseblue
    
if clothing_choice == 'green':
    
    show emory up talk
    
    e "I think the green jacket be good to wear!"
    
    show cordelian up talk
    show emory up smile
    
    c "You think so? I was thinking more light blue..."
    
    show cordelian up frown
    show emory down frowntalk
    
    e "Well, go with light blue then."
    
    show emory down frown
    
    "{i}Why ask me, in that case?{/i}"
    
    show cordelian down talk
    
    c "Okay, that's what I'll go with."
    
    jump havetochoseblue
    
label havetochoseblue:
    
    c "Stylists, I pick the light blue jacket."
    
    show cordelian up talk
    
    c "Thank you for your help, [pname]."
    c "Do you have everything ready for the gala?"
    
    show cordelian smile
    show emory up talk
    
    e "Yes, I'm ready for it."
    e "I-I'm actually a bit excited for it- it'll be the first time I'll have seen her."
    
    show cordelian up talk
    show emory up smile
    
    c "Oh, you're right!"
    
    show cordelian up talk
    
    c "Well, for future reference when you do meet her, try not to outlive your stay."
    c "She can seem really distant and uninterested in what you're saying, but that's just how she is normally." 
    
    show cordelian down talk
    
    c "But, if she does try to change the subject a lot, that means she's probably trying to give you a hint to leave."
    c "She's kinda hard to talk to in that way, since she's almost always uninterested in whatever you say."
    
    show cordelian down smile
    show emory down frowntalk
    
    e "I see..."
    
    show cordelian up talk
    show emory down smile

    c "Oh, but I'm sure she'll like you!"
    c "You'll be best friends, just wait and see."
    c "For now, I've got to go to class. I'll see you later."
    
    show cordelian smile
    show emory up talk
    
    e "Okay, bye!"
    
    show emory up smile
    
    jump tiny
    
label forest2:
    
    $ overworld2_choice = 'marco'
    
    $ marco += 1
    
    scene bg forest
    with fade
    
    show marco down frown at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show emory up talk
    
    e "Good morning Marco!"
    
    show emory up smile
    show marco up talk
    
    m "Hello."
    
    show emory up talk
    show marco down frown
    
    e "What are you doing today?"
    
    show emory up smile
    show marco up talk
    
    m "I'm trying to pick out flowers for the flower arrangement at the gala."
    
if overworld1_choice == 'marco':
    
    m "Would you like to come with me to the garden to look for more flowers?" 
    
    show marco frown
    show emory up talk
    
    e "Sure!"
    
    show emory up smile
    
    jump overthegarden

else:
    
    show marco down frown
    show emory up talk
    
    e "Oh my, could I help any?"
    
    show marco up talk
    show emory up smile
    
    m "I suppose you could come with me to the garden... Just try not to make too much noise."
    
    show marco frown
    show emory up talk
    
    e "Of course I won't! Let's go!"
    
    show emory up smile
    
    jump overthegarden
    
label overthegarden:
    
    scene bg garden
    with fade
    
    show marco down frown at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show marco up talk
    
    m "There's a bigger selection of flowers to pick from from here than the forest, although some in the forest looked prettier..."
    m "Those lilacs aren't the right shade, while those petunias won't fit the pots."
    
    show marco frown
    show emory up talk
    
    e "What about those over there?"
    
    show marco up talk
    show emory up smile
    
    m "Those aren't in season this time of year, so it would take too long to have them delivered from an area where they are in season."
    
    show marco frown
    show emory down frowntalk
    
    e "Oh...."
    e "How do you know all of this?"
    e "I-I mean, I didn't pick you for the nature type."
    
    show marco up talk
    show emory up frown
    
    m "I'm studying botany."
    
if overworld1_choice == 'marco':
    
    m "Don't you remember the book I was reading yesterday?"
    
    show marco down frown
    show emory up talk
    
    e "Oh, yes! It was a book about plants!"
    e "So you've read a lot on plants?"
    
    show marco up talk
    show emory up smile
    
    m "Yes. I believe I told you that yesterday."
    
    show marco down frown
    show emory down frowntalk
    
    e "Oh, right..."
    
    jump istudybotanyidiot
    
else:
    
    show marco down frown
    show emory up talk
    
    e "Really? I didn't know that. That's amazing!"
    e "So you've researched enough that you know all these plants off the top of your head?"
    
    show marco up talk
    show emory up smile
    
    m "You could say that."
    
    jump istudybotanyidiot
    
label istudybotanyidiot:
    
    show marco up talk
    show emory up smile
    
    m "Hmm... These magnolias would look good around the pillars... I believe I'll go with these."
    m "Thank you for accompanying me here. For now I need to call the decorator to order magnolias- maybe I'll see you tomorrow."
    
    show marco down frown
    show emory up talk
    
    e "Alright, I'll see you then."
    
    show emory up smile
    
    jump tiny
    
label home2:
    
    $ overworld2_choice = 'lisia'
    
    $ lisia += 1
    
    scene bg castionmanorinside
    with fade
    
    show lisia up smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"
    
    show lisia up talk
    
    l "Hello, [pname]!"
    
    show lisia up smile
    show emory up talk
    
    e "Good morning, Lisia! How are you today?"
    
    show lisia up talk
    show emory up smile
    
    l "I'm good, how was class today?"
    l "Didn't you have math?"
    
    show lisia up smile
    show emory down frowntalk
    
    e "I did, but of course I still have the same instructor..."
    
    show lisia down talk
    show emory down smile
    
    l "Oh yeah, that guy... He's not exactly the best teacher, is he?"
    
    show lisia up smile
    show emory down frowntalk
    
    e "Not really.... I mostly just ignore him and finish my work."
    
    show emory up talk
    
    e "But, enough of that- what are you up to right now?"
    
    show lisia up talk
    show emory up smile
    
    l "I'm just dusting these plants."
    l "They're really pretty, almost as if they were real..."
    
    show lisia up smile
    show emory up talk
    
    e "If you think these fake plants are pretty, you should see the garden at the castle! It's filled with all sorts of exotic breeds of flowers."
    e "You'd love it!"
    
    show lisia down frowntalk
    show emory up smile
    
    l "I doubt I would..."
    l "Being around that many actual plants would be horrible for my allergies."
    
    show lisia up smile
    show emory unsure frown
    
    "{i}I didn't know she had that bad of allergies.{/i}"
    "{i}We have mostly fake plants in the house because my mother has bad allergies, but I didn't know Lisia was the same.{/i}"
    
    show emory unsure frowntalk
    
    e "I didn't know... sorry."
    
    show lisia up talk
    show emory up frown
    
    l "It's okay!"
    l "And besides, I've seen the garden from afar, and it is beautiful."
    l "I've taken enough of your time. Shouldn't you be studying for a test later today?"
    
    show lisia up smile
    show emory up talk
    
    e "Wha- I don't-"
    
    show emory unsure frowntalk
    
    e "I-I've got to go!"
    
    show emory down frown
    
    jump tiny
    
label tiny:
    
    scene bg bedroomnight
    with fade
    
    "{i}Today was a good day, I suppose.{/i}"
    "{i}Only one more day until the gala... I'm a bit excited.{/i}"
    "{i}I feel like getting up early in the morning, so I should go to bed now.{/i}"
    
################        Tuesday- tst    ###########     DAY BEFORE GALA

    scene bg bedroomday
    with fade
    
    "{i}It's a nice, bright day today- what should I do today?{/i}"
    
label overworld_choice3:

scene overworld
with fade

call screen overworld3

label castle3:
    
    $ overworld3_choice = 'cordelian'
    
    $ cordelian += 1
    
    scene bg castle
    with fade
    
    show cordelian smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"
    
    show emory unsure frowntalk
    
    e "What's going on around here?"
    
    show cordelian down talk
    show emory up frown
    
    c "My advisors are trying to get everything prepared for tomorrow but don't get the hint that I'm trying to study here."
    c "I suppose I shouldn't have tried to come down here to study..."
        
    if sit == 'sat':
        if overworld1_choice == 'cordelian':
            if overworld2_choice == 'cordelian':
                
                show cordelian down smile
                show emory up talk
                
                e "I know just the thing- let's go to the garden and I'll help you study there. It'll be a lot less hectic there."
                
                show cordelian up talk
                show emory up smile
                
                c "That's a good idea."
                c "Let's go now."
                
                show cordelian smile
                
                scene bg garden
                with fade

                "{i}The garden is as immaculate as usual. The only sounds are distant humming from bees.{/i}"
                "{i}It's perfect for studying, or just getting away from it all.{/i}"
                "{i}We pick a bench to sit on and Cordelian pulls out his notes.{/i}"
                
                show cordelian smile at closerright
                show emory up smile at closerleft
                with Dissolve(0.5)
                
                show cordelian up talk
                
                c "You're right, it's much less crowded here and less noisy."
                
                show cordelian smile
                show emory up talk
                
                e "So, what are you studying for anyway?"
                
                show cordelian up talk
                show emory up smile
                
                c "It's just math."
                
                show cordelian smile
                show emory up talk
                
                e "Oh, that'll probably be easy! I can definitely help you with that."
                
                show emory up smile

                "{i}He slides closer to me on the bench and opens the book.{/i}"
                
                scene bg garden
                with fade
                
                show cordelian smile at rightt
                show emory up smile at leftt
                with Dissolve(0.5)
                
                show cordelian up talk
                
                c "I believe I'm getting this now... maybe now I can do good on my test in an hour."
                c "Thanks for your help!"
                
                show cordelian smile
                show emory up talk
                
                e "It was no problem!"
                
                show emory up smile
                
                jump nerd
                
            else:
                
                jump butt
                
        else: 
            
            jump butt
            
    else: 
        
        jump butt
    
label butt:
    
    show cordelian down smile
    show emory down frowntalk
    
    e "Well, if I'm with you then maybe you can concentrate more than if you were by yourself, right?"
    
    show cordelian down talk
    show emory down smile
    
    c "You could be right... let's sit at this table over here then."
    
    show cordelian smile
    show emory up talk
    
    e "What are you studying, anyway?"
    
    show cordelian up talk
    show emory up smile
    
    c "It's just a few math problems."
    
    show cordelian smile
    show emory up talk
    
    e "We can probably finish those in a few minutes. It'll be fine."
    
    show emory up smile
    
    scene bg castleinside1
    with fade
    
    show cordelian smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show cordelian up talk
    
    c "This is making sense now... Hopefully I'll do well on the test now."
    c "Thank you for your help- my test is in an hour and I need to do a few things before then, so I'll see you later."
    
    show cordelian smile
    show emory up talk
    
    e "It was no problem!"
    
    show emory up smile
    
    jump nerd
    
label forest3:
    
    $ overworld3_choice = 'marco'
    
    $ marco += 1
    
    scene bg castleinside2
    with fade
    
    show marco frown at center
    with Dissolve(0.5)
    
    show marco up talk
    
    m "Put the chairs over there towards that corner and have the streamers hanging from those two posts."
    m "We need more lighting over here-"
    m "Oh, I didn't see you there."
    
    show marco frown
    
    show marco frown at rightt
    show emory up smile at leftt 
    with moveinleft
    
    show emory up talk
    
    e "Still busy trying to make everything go accordingly, huh?"
    
    show emory up smile
    show marco up talk
    
    m "Yes... we're almost done, thankfully. It shouldn't be too much longer and the castle will be ready for a party."
    
if overworld2_choice == 'marco':

    m "The magnolias we picked out yesterday look stunning- they were definitely the right choice."
    
    show marco down frown
    show emory up talk
    
    e "That's good. I can't wait to see them tomorrow!"
    
    show emory up smile
    
    jump ibg
    
else:
    show marco down frowntalk
    
    m "The white lillies I picked out for the staircase aren't quite matching... However, it's too late to change it."
    m "Magnolias most likely would have looked better."
    m "Ah, maybe there's still time..."
    
    show marco down frown

    "{i}He paces for a bit, lost in thought again.{/i}"
    
    jump ibg
    
label ibg:
    
    show emory up talk
    
    e "I'll sit down over here and watch from afar, is that alright?"
    
    show emory up smile
    show marco up talk
    
    m "...Mind if I sit with you?"
    m "...I need to sit down for a bit. I can direct for a bit while sitting down."
    
    show emory up talk
    show marco down frown
    
    e "Of course you can."
    
    show emory up smile
    show marco up talk
    
    m "Are you ready for tomorrow?"
    
    show emory up talk
    show marco down frown
    
    e "Yes. I have my clothes picked out and everything."
    e "I see you've gotten everything planned and ready for tomorrow."
    
    show emory up smile
    show marco down frowntalk
    
    m "I... I hope so..."
    m "I'll be fine if tomorrow night comes along smoothly."
    
    show emory up talk 
    show marco down frown
    
    e "Everything will go fine."
    e "You've done a marvelous job of planning the whole event so far, so I'm sure it'll go by great tomorrow. Just have a little faith."
    
    show emory up smile
    
if overworld1_choice == 'marco':
    if overworld2_choice == 'marco':
        show marco blush talk
        
        m "Thank you..."
        
        show marco -blush frown
        
        jump piper
        
    else: 
        
        jump boo
        
else:
    
    jump boo
    
label boo:
    
    show marco talk
    
    m "...Thank you. I hope it will go be fine..."
    
    jump piper

label piper:
    
    m "My break is over now, so I should go direct them again. I'll see you tomorrow night."
        
    show marco frown
    show emory up talk

    e "I'll see you then."

    show emory up smile

    jump nerd

label home3:
    
    $ overworld3_choice = 'lisia'
    
    $ lisia += 1
    
    scene bg bedroomday
    with fade
    
    "{i}I'm sure I'll need to rest up before the party tomorrow.{/i}"
    
    show emory up smile at leftt
    show lisia up smile at rightt
    with Dissolve(0.5)

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"
    
    show emory unsure talk
    
    e "Hello Lisia."
    
    show emory smile
    show lisia down frowntalk
    
    l "You haven't left for the day yet?"
    
    show emory talk
    show lisia frown
    
    e "No, I'm just going to spend the whole day resting up before the party tomorrow."
    
    show emory smile
    show lisia down frowntalk
    
    l "You mean you just wanted to sleep in all day."
    
    show emory up frown
    show lisia down frown
    
    e "..."
    
    show emory down frowntalk
    
    e "Maybe."
    
    show emory frown
    show lisia down frowntalk
    
    l "...Right."
    
    show lisia up talk
    
    l "Well, I hope you have fun tomorrow at least."
    
    show emory up talk
    show lisia up smile
    
    e "I hope I will too. I love going to big parties like this- there's so many new faces, and eccentric attire."
    e "And plus, I hear Marco has been working hard on arranging the whole event, so the castle is sure to look gorgeous."
    
    show emory up smile
    show lisia up talk
    
    l "I just hope the media takes lots of pictures of Princess Katherine's dress! I'm sure it'll be stunning!"
    
    show emory up talk
    show lisia up smile
    
    e "I'm excited to meet her finally."
    
if overworld2_choice == 'cordelian':
    
    show emory unsure talk
    
    e "Cordelian has told me that she can seem distant and uninterested at times, so I hope I won't bore her."
    
    jump ray
    
else: 
    
    e "I wonder what she'll be like..."
    
    jump ray
    
label ray:
    
    show emory up talk
    
    e "Well, she's sure to be pretty, and wear all the expensive clothes like you're hoping she will."
    e "Meeting royalty from another country..."
    
    show lisia down talk
    show emory up smile
    
    l "You act like you've never visited royalty..."
    
    show emory unsure talk
    
    e "It has been a while."
    
    show emory smile
    show lisia talk
    
    l "I'm sure you'll be fine."
    
    show emory up talk
    show lisia smile
    
    e "I'm not worried."
    
    show emory smile
    show lisia talk
    
    l "Well, of course you aren't."
    l "I certainly would be..."
    l "Oh, please have fun!"
    
    show lisia smile
    show emory up talk
    
    e "I will, don't worry. I'm sure you'll read all about it the next day in the papers."
    
    show emory smile    
    show lisia talk
    
    l "Yes, I'm sure I will."
    l "Goodnight Emory."
    
    show lisia smile
    show emory talk 

    e "Goodnight."

    show emory smile
    
    jump nerd

label nerd:
    
    scene bg bedroomnight
    with fade

    play music "Irreplacable Warmth.mp3" fadeout 1 
    queue music "Irreplacable Warmth.mp3"
    
    "{i}Just a few more hours till the party...{/i}"
    
######################### ♦♦♦♦♦ P A R T Y ♦♦♦ T I M E ♦♦♦♦♦ ############################
################## Wednesday

    scene bg bedroomday
    with fadee
    
    "{i}Ah, finally, the big day!{/i}"
    
    "{i}It's a shame I have class after breakfast...{/i}"
    
    "{i}Oh well, it's only French. I might as well head down to eat now.{/i}"
    
    scene bg castionmanorinside
    with fade
    
    show lisia up smile at rightt
    show emory up smile at leftt
    with Dissolve(0.5)

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"
    
    show lisia up talk
    
    l "Good morning! Sleep well?"
    
    show lisia up smile
    show emory up talk
    
    e "Yep, and breakfast was good as well."
    
    show lisia up talk
    show emory up smile
    
    l "That's good. Are you about to go to French now?"
    
    show lisia up smile
    show emory up talk
    
    e "Yes, I'm about to head there right now. It's only for an hour so it shouldn't be too bad."
    
    show lisia up talk
    show emory up smile
    
    l "Hopefully not. I'll let you go then. See you later!"
    
    show lisia up smile
    show emory up talk
    
    e "Goodbye!"
    
    show emory up smile
    
    scene bg bedroomday
    with fade
    
    "{i}French is over, but I still have almost three hours until I should be at the gala...{/i}"
    "{i}I suppose I could watch some of the TV coverage on it, since all the networks in this country are sure to be covering it.{/i}"
    "{i}Ah, it looks like there's already a lot of news anchors hanging around right outside the castle grounds.{/i}"
    "{i}It seems I'll have to find a different way of entering the castle instead of the front door if I don't want to be held up.{/i}"
    
    tv "{i}We are on site at the Hapsurry manor just hours before the grand gala to signify Princess Katherine's first entrance into the country.{/i}"
    tv "{i}The Princess has already arrived at the castle, but the other guests will be arriving within the following hours.{/i}"
    
    "{i}So she's already here... I guess it wouldn't hurt to get ready and leave early.{/i}"
    
    scene bg castle
    with fade
    
    "{i}I had to sneak in through the kitchen to avoid all the paparazzi... but at least I'm here now.{/i}"
    "{i}Even the hallways look beautiful... Marco did an amazing job setting all of this up. Tonight will be great!{/i}"
    "{i}I'll see what Cordelian's up to before the party.{/i}"
    
    scene bg cordelianbedroomday
    with fade

    "{i}Of course...{/i}"
    "{i}Rather than entertain a princess, he'd rather stay in his room.{/i}"
    
    show cordelian frown at rightt
    show emory unsure frown at leftt
    with Dissolve(0.5)

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"
    
    show emory unsure frowntalk
    
    e "What's going on here? All of your advisors are running around!"
    
    show emory up frown
    
if overworld2_choice == 'cordelian':
    
    show cordelian down talk
    
    c "They're all freaking out because the outfit we picked out the other day still isn't ready and I can't just wear the jacket to it, so I'm having to wear my regular clothes."
    
    jump rooster
    
else:
    
    show cordelian down talk
    
    c "They're all freaking out because the outfit I picked out the other day isn't ready for me to wear, so I have to wear this."
    
    jump rooster
    
label rooster:
    c "Honestly, you'd think a fire had started the way they're reacting."
    
    show cordelian down smile
    show emory down frowntalk
    
    e "I see..."
    
    show cordelian down talk
    show emory down smile
    
    c "I've told them it'll be alright but..."
    c "Oh well, I can't really stop them all from worrying, I just wish they'd stop running around without their heads."
    
    show emory up talk
    show cordelian smile
    
    e "So, where are the other guests?"
    
    show cordelian up talk
    show emory up smile
    
    c "I would assume that most of the guests have already arrived, as it's only an hour till the party. They're most likely in the down stairs main room."
    
    show cordelian down talk
    
    c "Shouldn't you have seen them when you walked in?"
    
    show cordelian down smile
    show emory down frowntalk
    
    e "I might have sneaked in through the kitchen to avoid cameras..."
    
    show cordelian down talk
    show emory down smile
    
    c "Of course you did..."
    
    show cordelian smile
    show emory up talk
    
    e "Is Katherine down there yet?"
    
    show cordelian up talk
    show emory up smile
    
    c "No, she should still be getting ready or at least waiting in the guest bedroom. I believe we'll walk down together."
    c "You'll know her when you see her, I promise."
    
    show cordelian down talk
    
    c "Well, I would say that you should probably head down there- I still need to finish getting ready, and I can't accompany you for a while when it starts."
    
    show cordelian smile
    show emory up talk
    
    e "Alright, I'll see you in a bit."
    
    show emory up smile

    ## TODO grand ballroom magnolia or lilac
    
if overworld2_choice == 'marco':
    
    scene bg ballroom
    with fade
    
    jump ytspace
    
else: 
    
    scene bg ballroom
    with fade
    
    jump ytspace
    
label ytspace:    
 
    show emory up smile
    with Dissolve(0.5)
    
    "{i}The place is full of prominent figures from here and other countries... Some of them have traveled far to get here!{/i}"
    "{i}They're all dressed so cordially and talking with each other... except for that guy.{/i}"
        
    "{i}He's just standing there jotting notes on a clipboard... Don't tell me he's still working?!{/i}"
    
    show marco down frown at rightt
    show emory up smile at leftt
    with Dissolve(0.5)
    
    show marco up talk
    
    m "Ah, I see you made it early."
    
    show marco down frown
    show emory up talk
    
    e "I wanted to beat the crowd, so I had a few kitchen workers to let me in early."
    e "Looks like I made the right decision...."
    
    show marco up talk
    show emory up smile
    
    m "The ballroom has slowly filled up with guests the closer it has gotten to the start of the dance."
    m "It appears almost everyone is here now..."
    
    show marco down frown
    
    m "..."
    
    show emory down smile
    
    "{i}He keeps looking down to check something on his clipboard...{/i}"
    
if overworld2_choice == 'marco':
    
    if overworld3_choice == 'marco':
        
        show marco up talk
        
        m "Thank you for your assistance this past week... It's been very hectic, as you know, making this event perfect."
        
        show marco frown
        show emory up talk
        
        e "Don't thank me- I'm happy it's all together finally. It's been interesting to see it all come together."
        e "You've done a great job so far, cheer up!"
        
        show marco blush talk
        
        m "Y-You're right..."
        
        show marco -blush down smile
        
        jump fiddle
        
    else:
        
        jump court
        
else: 
    
    jump court
    
label court:
    
    show marco up talk
    
    m "I apologize, you're standing here and I'm ignoring you..."
    
    show marco down frown
    show emory up talk
    
    e "D-Don't worry about it! I wouldn't want to take you away from your work."
    e "It'll all be over soon- all your hard work for the day will be finalized in half an hour."
    
    show marco up talk
    show emory up smile
    
    m "You're right..."
    m "...I hope know I'll be calmer after the party starts..."
    
    jump fiddle
    
label fiddle:
    
    show emory up talk
    
    e "That's the spirit!"
    
    show emory up smile
    
    "{i}Maybe a little more small talk will ease his nerves...{/i}"
    
    show emory up talk
    
    e "Say, who are some of these people?"
    
    show emory up smile
    show marco up talk
    
    m "The man and woman in the red attire with their backs turned over there are seat holders in office. I believe they run the Treasury department."
    m "The group over in that corner is a well-off family, so to speak."
    m "Some of the people walking around are from Dersion, invited here to promote the welfare between the two countries."
    
    show emory unsure frowntalk
    show marco down frown
    
    e "Why are there a few cameras in here?"
    
    show emory up frown
    show marco up talk
    
    m "The King allowed a limited amount of press to come inside, under the agreement that they must stay a certain distance away from the guests and cannot interact with them."
    
    show emory up talk
    show marco down frown
    
    e "Oh, I see."
    
    show emory up smile
    show marco down frown
    
    m "..."
    
    show marco up talk
    
    m "...[pname], are your parents not in attendance?"
    
    show marco down frown
    show emory down frowntalk
    
    e "...No, they couldn't make it per say..."
    e "They're already on a trip right now, and come back later this week. I think they're visiting some friends overseas."
    e "...I haven't heard from them since they arrived last week."
    
    show marco up talk
    show emory down smile
    
    m "I... I'm sorry to hear that."
    
    show marco down frown
    show emory down frowntalk
    
    e "It's okay, really..."
    
    show marco up talk
    show emory down smile
    
    m "I shouldn't have brought it up."
    
    show marco down frown
    
    "{i}That rather ruined the mood...{/i}"
    
    #TODO hey guess who has to find a ringing sound like a chime or a doorbell YOUUUUU DOOOOOO

    show marco up talk
    
    m "It appears there's only ten minutes until the gala starts now."
    m "I should check on Cordelian. I'll see you later."
    
    show marco down frown
    show emory up talk
    
    e "Yes, I'll see you soon."
    
    show emory up smile
    
    hide marco
    with moveoutright

    show emory up smile at center
    with moveinleft
    
    "{i}My, the King invited a lot of people to this party...{/i}"
    "{i}I haven't seen him pull of this big a political stunt in years. The media must be loving every second.{/i}"
    "{i}And yet, very few were let inside... or at least, very few have sneaked in...{/i}"
    "{i}Those who were let inside have a hard time deciding where to focus their cameras. It seems they've arranged a sort of agreement amongst them to film different parts and share the footage.{/i}"
    "{i}Their cameras must be capturing an amazing view of just some of the guests from far and wide, all dressed with their best.{/i}"
    "{i}All the girls here have pounds of expensive fabrics and jewels on. Lisia would love to be here.{/i}"

    if overworld_choice3 == "lisia":
        "{i}Ah, except for the flowers...{/i}"
    
    #TODO YOOOOO GUESS WHO GOTTA FIND A HORN OR TRUMPET SOUNDDD
    
    "{i}Wh- That was quick!{/i}"
    "{i}I guess it's... show time.{/i}"
    
label quickk:

    scene cg grandentrance
    show magnolia1
    show magnolia2
    with fadee

    $ renpy.pause(2.5)
    
    "{i}Sh-She's.... stunning!{/i}"
    "{i}Such a long and billowing dress... and it probably costs more than a bridal gown!{/i}"
    "{i}A cascade of flower petals falls from above, making it all seem angelic almost as the two walk.{/i}"
    "{i}Cordelian is more lively than ever. It's like his stress is gone somehow...{/i}"
    "{i}No, it's not that. I can see now that whatever is troubling him still is- he's just hiding it behind a fake smile.{/i}"
    "{i}It's the same smile he puts on when his relatives come over, or when he has to meet nobles from afar... it's the same smile he's given me this past week.{/i}"
    "{i}Maybe his real smile will appear after this is over.{/i}"
    "{i}They're walking towards the few press people that were allowed in. I suppose they're about to get the few perfect photos for the evening.{/i}"

    scene bg ballroom
    with fade

    "{i}It quieted down in here as soon as they made their entrance, but now that they're here the volume has gone back to normal.{/i}"
    "{i}I'm rather glad I'm not the one in the spotlight... it's really nerve-wracking sometimes.{/i}"
    "{i}How he handles it day in and day out is beyond me.{/i}"
    "{i}Looks like they're done with pictures now... Wait...{/i}"
    
    "{i}Are they coming this way-?{/i}"
    
    show emory unsure smile at leftt
    show cordelian smile crown at rightt
    with Dissolve(0.5)
    
    show cordelian up talk
    
    c "[pname], I'd like you to meet Katherine..."

    show cordelian smile at center
    show katherine at right
    with moveinright
    
    show emory at left:
        zoom 1.10
        yalign 0.65
    show katherine up smile at right:
        zoom 1.20
        yalign 0.60
    show cordelian talk at center:
        zoom 1.10
        yalign 0.75
    with dissolve
    
    c "...my fianc\u00E9e."
    
    show cordelian smile
    show emory sad pout 
    
    "{i}F-fianc\u00E9e?!{/i}"
    
    show cordelian up talk
    
    c "Katherine, meet [pname]."
    
    show katherine up talk
    show cordelian smile
    
    k "Cordelian has talked a lot about you, [pname]."
    
    show katherine up smile
    show emory talk 
    
    e "O-Oh, really now...?"
    
    show katherine up talk
    show emory smile
    
    k "He tells me you two get in trouble a lot, huh?"
    
    show katherine up smile

    "{i}I can't believe she's standing right here, in front of me.{/i}"
    "{i}But... there's something I can't believe even more...{/i}"

    show emory talk
    
    e "That's mostly his fault, not mine..."
    e "He just drags me along with him to share the blame."
    
    show katherine up talk
    show emory frown
    
    k "I hear... From what I've seen of this country, it's a very beautiful place."
    k "I can see why you two wouldn't want to be couped up here all day."
    k "Dersion is much colder than this place... Here, it's seemingly sunny and green all the time. It must be nice living in such a temperate climate."
    
    show katherine up smile
    show cordelian up talk:
        xzoom -1
    
    c "Well, I don't suppose you'll have to go through too many more cold, Dersion winters. The winters here are much nicer."
    
    show katherine up talk
    show cordelian smile
    
    k "Oh, yes, weren't you there for a few days this past year? We had an exceptionally cold season then!"
    
    show katherine up smile
    show cordelian up talk
    
    c "I did! My father and I stayed for half a week, but I believe you were off visiting relatives."
    c "It snowed every day we were there, and caused our train to be delayed by a day."
    
    show cordelian smile
    
    "{i}They realize I'm still here, right?{/i}"
    "{i}How long have these two known each other...?{/i}"

    show cordelian up talk:
        xzoom 1
    
    c "Ah, [pname], you should visit the capital in Dersion! There are much taller buildings there than here, so you can walk around for hours without being touched by sunlight!"
    
    show cordelian smile
    show katherine up talk
    
    k "Ah, it is a bit weird to get used to, having to go to almost the outskirts of the town before the buildings stop blocking the light... But it's just one of the things that comes with a bustling city."
    k "Most of the buildings are filled with businesses while the outer buildings are for homes and apartments."
    
    show katherine up smile
    
    "{i}Thank you for informing me on what the term 'third wheel' really means...{/i}"
    
    show cordelian up talk:
        xzoom -1
    
    c "I remember driving through the areas where the houses are, and they were very nice! It's a very active community there."
    
    show cordelian smile
    show katherine up talk
    
    k "Oh, but this capital is so much nicer! It's got a certain older charm to it that is absolutely lovely. I can't wait to see more of this city this week."
    
    show katherine up smile
    show cordelian up talk
    
    c "I won't be able to show you all of it this week... Maybe you'll have to catch another flight over here before our big day?"
    
    show cordelian smile
    
    e "{i}My head's starting to hurt...{/i}"
    
    show cordelian up talk
    
    c "Tomorrow we can see some of the taller buildings, and maybe Friday head out to the downtown district..."
    
    show cordelian smile
    show katherine up talk
    
    k "That sounds wonderful! I'd love to become better acquainted with here in the mean time."
    k "We still have a couple of months till then, so it might be enough time before I'm fully situated here!"
    
    show katherine up smile
    
    "{i}A couple of months-? \"Better situated here\"?{/i}"
    "{i}Don't tell me... Is she going to live here?{/i}"
    
    show cordelian up talk
    
    c "We'll definitely be able to get you familiar with the city{w=0.5}{nw}"
    
    show cordelian down frown:
        xzoom 1
    show katherine down frown
    show emory sad frowntalk
    
    e "I-I'm sorry, I need to go... Err... To the break room."
    
    show cordelian down talk:
        xalign 0.45
    show emory pout
    
    c "Are you okay? You're looking a bit pale{w=0.5}{nw}"
    
    show cordelian down frown 
    show emory frowntalk
    
    e "I-I'm fine! I just need to... I'll be right back..."
    
    show cordelian frowntalk
    
    c "Are you sure you're okay{w=0.4}{nw}"

    hide emory 
    with vpunch 
    
    hide cordelian 
    hide katherine 
    with vpunch
    
    "{i}I'm just... going to... sit down...{/i}"
    "{i}...at home...{/i}"
    
    scene bg bedroomnight
    with fadee
    
    $ renpy.pause(2.0)
    
    scene black 
    with fade 

    jump postdemo

    "Thank you for playing the beta demo for Paths Taken!"
    "We hoped you've enjoyed what you've seen so far, and give our team any feedback you have!"
    "The full game will be on Itch.io and Steam for free and will include routes for all 4 main characters (i.e. Cordelian, Katherine, Lisia, and Marco)."
    "You can follow development on {a=https://twitter.com/CrystalGameWork/}Twitter{/a} and {a=https://crystalgameworks.itch.io/}Itch.io{/a}."
    "Thank you again for checking Paths Taken out!"

    return
