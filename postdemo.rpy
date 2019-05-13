#######################################################################################################################
label musicinfo:
## TODO Lisia's theme is Encounter.mp3

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"

## TODO Marco's theme is 

## TODO Cordelian's theme is Tabi.mp3

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"

## TODO Katherine's theme is FNM.mp3

    play music "FNM.mp3" fadeout 1 
    queue music "FNM.mp3"   

## General music is Irreplacable Warmth and Dash
    
    play music "Irreplacable Warmth.mp3" fadeout 1 
    queue music "Irreplacable Warmth.mp3"

    play music "Dash.wav" fadeout 1 
    queue music "Dash.wav"   

    



################################################### Post-demo script ##################################################

label postdemo:

    scene bg bedroomday
    with fadee

    en "It's a new day, thankfully..."

    ## call an imagemap

    scene overworld
    with fade

    call screen overworld4


#if overworld_choice4 == "lisia":
label forest4:

    $ lisia += 1

    en "I think I'll take a newer route today. Maybe I should go around the forest..."

    scene bg forest
    with fade

    show lisia up frown at rightt
    show emory up frown at leftt
    with dissolve

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"

    l frowntalk "[pname]..."

    show lisia frown

    e frowntalk "Lisia! What are you doing here? I thought you took the evening off, since I was supposed to, well, not be here."

    show emory frown

    l frowntalk  "I did. I was in my room, reading, when I heard you open the front door."

    show lisia frown

    e frowntalk "Seems like I'm not quite as sneaky as I thought."

    show emory frown

    l frowntalk "Apparently. You look pale, though. Are you feeling well?"

    show lisia down frown

    e frowntalk "I'm fine."

    show emory frown

    l frowntalk "You don't look fine. Do you want me to call the doctor?"

    show lisia frown

    e down frowntalk "No! It's nothing like that. It's just that Cordelian is... getting married."

    show emory frown

    l up frowntalk "Married? To whom?"

    show lisia frown

    e frowntalk "Princess Katherine of Dersion."

    show emory frown

    l frowntalk "That would explain his frequent trips.  Why're you looking so worried about it? Is that why you left the party?"

    show lisia frown

    e frowntalk "It is. He introduced me to her and both of them just started talking to each other about their future life, while I stood there like a fool."
    
    show emory frown

    l talk "Ah. You're scared that he's going to change and not spend time with you, aren't you?"

    show lisia smile

    en up "Lisia is much more perceptive than I thought!"
    e frowntalk "I suppose. I mean, we barely have time to meet each other anymore, what with all his studies and trips."
    e "I'm just afraid that it'll get worse."

    show emory frown

    l talk "What about Katherine? What kind of person is she?"

    show lisia smile

    e frowntalk "She's very agreeable, and beautiful."

    show emory frown

    l frowntalk "But?"

    show lisia frown 

    e frowntalk "But, she seems to be a bit cold and reserved. Towards me, that is. She seems to speak her mind to Cordelian, though."
    
    show emory frown

    l down frowntalk "Maybe, instead of running away, you should have spoken to Cordelian about this, [pname]."

    show lisia frown

    e unsure frowntalk "Well, I might have just rushed away too quickly..."
    e "You're right, Lisia."
    e up "I'm going to talk to him tomorrow."

    show emory frown

    l up talk "Good. Now, get some sleep. You look exhausted."

    show lisia smile

    e talk "So do you. Good night!"

    show emory smile

    l talk "Good night, [pname]!"

    show lisia smile

    jump night4

    
label garden4:
#if overworld_choice4 == "marco":

    $ marco += 1

    en "I think I'll stick to the path I know today. I'll walk through the forest."

    scene bg forest
    with fade

    show marco down frown at rightt
    show emory up frown at leftt
    with dissolve

    play music "Irreplacable Warmth.mp3" fadeout 1 
    queue music "Irreplacable Warmth.mp3"
        
    m frowntalk "[pname]! Wait!"

    show marco frown

    e frowntalk "Marco? Slow down! What are you doing here?"

    show emory frown

    m frowntalk "Cordelian... {i}pant{/i}... sent... me... to..." 

    show marco frown

    e down frowntalk "Find me? Why?"

    show emory frown

    m frowntalk "He's your friend. He was worried when you left like that."
    m "What happened? Why did you leave? Did you not like the party?"

    show marco frown

    e up frowntalk "The party was great, Marco. You really did an incredible job. No, it was something else."

    show emory frown

    m frowntalk "What was it then?"

    show marco frown

    e frowntalk "Well, Cordelian just announced to me that he was engaged to Princess Katherine, and I-"

    show emory frown

    m frowntalk "He's engaged? Already?"

    show marco frown

    e down frowntalk "...You didn't know?"

    show emory frown

    m frowntalk "He didn't tell me."
    m "I was expecting it to be announced eventually, but not so soon."
    m "I was quite busy with the party, but even so, he could have at least spoken to me."

    show marco frown

    e frowntalk "Or me. I had no idea the King and Queen were planning this."
    e "Katherine seems lovely, but I'm worried that this is going to come in between our friendship."
    e "As it is, we have to sneak out to spend time together."

    show emory frown

    m frowntalk "I'm sure his parents wouldn't mind if you visited them, even after they are married."
    m up "Besides, he should have more time then, since he won't be travelling to Dersion as frequently anymore."

    show marco frown

    e frowntalk "But then I'll have to visit {i}them{/i}! She'll always be there with him, and we won't be able to spend time alone anymore."
    
    show emory frown

    m frowntalk "In that case, I think you should tell Cordelian your concerns."
    m "Both of you can find a way around all of it."
    m "Besides, Princess Katherine isn't that bad, really."

    show marco frown

    e frowntalk "Well, she isn't..."
    e up "I'll talk to Cordelian tomorrow. Thank you, Marco."

    show emory frown

    m frowntalk "You're welcome. Shall I tell him you weren't feeling very well and will speak to him later?"

    show marco up frown

    e frowntalk "Yes, please."

    show emory frown

    m talk "Alright. Good night, then."

    show marco smile

    e talk "Good night, Marco. Enjoy the rest of the day!"

    show emory smile

    m talk "I will. Bye!"

    show marco smile

    jump night4

label castle4:
#if overworld_choice4 == "cordelian":

    $ cordelian += 1

    en "I'll see Cordelian. I suppose I owe him an explanation for last night... or at the very least, an apology."

    scene bg castle
    with fade

    show cordelian up smile at rightt
    show emory down frown at leftt
    with dissolve 

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"
    

    e frowntalk "Cordelian? Could I speak to you for a few minutes?"

    show emory frown

    c talk "Oh, hello [pname]! Could you wait a bit, please? I have some work to finish."

    show cordelian smile

    e frowntalk "I... I'll wait downstairs."

    hide cordelian with moveoutright

    en frown "It seems he's speaking to Katherine."
    en "...of course he is."
    en "She is the only person he seems to speak to, nowadays."
    en "I guess all I can do is wait."
    en "I can't believe that they have already started cleaning up the castle for the wedding!"

    show katherine up smile at rightt
    with moveinright

    k talk "[pname], was it?"

    show katherine smile

    e frowntalk "Huh? Oh, Princess Katherine. Good morning."

    show emory frown

    k talk "Good morning."

    show katherine smile

    e down "..."
    k frown "..."

    show cordelian up smile at center
    show emory at left
    show katherine at right
    with moveinright

    c talk "[pname]! Katherine! I see you two are getting along. That's great!"

    show cordelian smile

    e frowntalk "Yes, well-"

    show emory frown

    k frowntalk "I think I should leave now, Cordelian."

    show katherine frown

    menu:
        "Goodbye.":
            $ cordelian += 1
            $ katherine_leaving = "goodbye"
        "Can you stay longer?":
            $ katherine += 1
            $ katherine_leaving = "stay"

    if katherine_leaving == "goodbye":
        e frowntalk "Goodbye."

        show emory frown

        c frowntalk "So soon? Must you? I was planning to show you our city today."

        show cordelian frown

        k frowntalk "Perhaps later, Cordelian. You seem to be occupied."
        k talk "Bye, Cordelian, [pname]."

        show katherine smile

        hide katherine with moveoutright

        c talk "So, what was it you wanted to talk about?"

        show cordelian smile

        e frowntalk "Your wedding."

        show emory frown

        c talk "Alright, what about it?"

        show cordelian smile

        e unsure frowntalk "You should have told me about it before!"
        e "I was completely caught unawares when you introduced Katherine to me."

        show emory frown

        c frowntalk "My parents forbade me to talk about it until yesterday."
        c "You left just before the official announcement."
        c "Why did you leave?"

        show cordelian frown

        e frowntalk "I was feeling extremely awkward at the party."
        e "I'm sorry I left so suddenly, though."
        e "I just felt uncomfortable standing there while you spoke to Katherine."

        show emory frown

        c frowntalk "I'm sorry, [pname]."
        c "I had no choice."
        c "This alliance with Dersion is very important."
        c talk "Perhaps we could spend some time together tomorrow?"
        c "I'm sure Marco can handle things for one day."
        c "Only if you want to, of course."

        show cordelian smile

        e frowntalk "I'll... I'll see if I can make it."

        show emory unsure smile

        c talk "Great! See you then!"

        show cordelian smile
        
    if katherine_leaving == "stay":
        
        e talk "Perhaps you could stay for a little longer, Princess."

        show emory smile

        c talk "You really should stay, Kath."

        show cordelian smile

        en down frown "Kath?"

        show emory smile

        k frowntalk "Very well. If you insist."

        show katherine frown

        c talk "So, what was it you wanted to talk about, [pname]?"

        show cordelian smile

        e up talk "Oh... I can't remember. I'm sure it can wait."

        show emory smile

        c talk "Oh, alright. I-"

        show cordelian frown

        m "Cordelian! Your parents want to speak to you!"

        c frowntalk "Again?"
        c "...alright. Tell them I'll be there in a moment."
        c "I'm sorry, [pname], Katherine."

        show cordelian frown

        k "..."
        c talk "Oh right! I promised Katherine I'd show her the city."
        c "[pname], could you do it instead? I'd ask Marco, but he's terribly busy too."

        show cordelian smile

        e frowntalk "I, err..."

        show emory frown

        c talk "Great! Thank you!"
        c "I'll see you both later. Have fun!"

        show cordelian smile

        hide cordelian with moveoutleft

        e up frowntalk "...So, I suppose we should head out, then."

        show emory frown

        k frowntalk "In that case, you will have to lead the way."

        scene bg city2
        with fade

        show emory up frown at leftt
        show katherine up frown at rightt
        with dissolve
            
        e frowntalk "This is our Central Square."
        e "Most of the merchants and craftsmen display their wares here."
        e "Those buildings over there are where most of the shopkeepers live."

        show emory frowntalk

        k frowntalk "I see."

        show katherine down frown

        en "She doesn't seem to be very interested."
        en "I did promise Cordelian, though... Well, he assumed I'd do it. Same thing to him."
        en "I could always show her the seamstresses' and weavers' shops."
        en "She might be interested in those."
        en "Or I could take her to the stables, though I doubt she will like it."

        k frowntalk "Why have we paused?"

        show katherine up frown

        e up frowntalk "Oh... err... no reason. Would you like to go to the stables next?"

        show emory frown

        k talk "Stables?"

        show katherine frown

        e frowntalk "Yes. There are some close by. Nobles, and sometimes even the King himself, like to visit sometimes, even though most of them have their personal stables as well."
        e "So, shall we go there?"

        show emory smile

        k talk "That would be agreeable."

        en "She always speaks so formally..."

        scene bg stables
        with fade

        show emory up smile at leftt
        show katherine up smile at rightt
        with dissolve

        play music "FNM.mp3" fadeout 1 
        queue music "FNM.mp3" 
            
        stablehand "Good evening [xir] [pname]. Here for Aria again?"

        e talk "Actually, my friend here would like to explore the stables."
        e "Do you mind if I just show her around?"

        show emory smile

        stablehand "Of course not! Please make yourself at home, [xir]."

        e talk "The ponies are on the other side of the stables, while most of the horses are stabled here."

        show emory smile

        k talk "Is Aria your mare?"

        show katherine smile

        e talk "Not technically, but I do ride her often."
        e "According to the stable hands, she doesn't like other people riding her. She can be a bit wild, sometimes."
        e "I also take care of grooming her."
        e "So the answer to your question is yes, in a way."
        e "Oh look, there she is."

        show emory smile

        k talk "She is beautiful! We don't have many thoroughbreds in my kingdom..."

        show katherine smile

        e talk "I'm rather proud of her."

        show emory smile

        k talk "And what's this one's name?"

        show katherine smile

        e talk "That's Orchid. She's somewhat new here."

        show emory smile

        k talk "Could we go for a ride then, [pname]?"

        show katherine smile

        en "I've never seen Katherine this... expressive before! She looks like a little child in front of a candy store. She really must love horses."
        e talk "I don't see why not. I'll just get the tack."
            
        e "Here you go."
        en smile "She is definitely an experienced rider, from the way she mounts. Who would've thought?"

        k talk "Would you like to race until we reach that fence?"

        show katherine smile

        e frowntalk "Are you sure you want to? I mean, you've only just met Orchid-"

        show emory frown

        k talk "Are you afraid of losing, [pname]?"

        show katherine smile

        e frowntalk "Absolutely not! Let's go!"

        hide katherine
        hide emory 
        with dissolve

        en "She is faster than I thought!"

        scene bg stables
        with fade

        show emory up smile at leftt
        show katherine up smile at rightt
        with dissolve
            
        e talk "I didn't know you were fond of riding, Princess."

        show emory smile

        k talk "I love horses, but my father's ministers..."

        show katherine down frown

        e frowntalk "Well?"

        show emory frown

        k frowntalk "Nothing. It doesn't matter."
        k up "We ought to return to the castle now."
        k "I suppose Cordelian will be waiting."

        show katherine frown

        en "Why does she keep closing up like that?"

        e frowntalk "Alright."

        show emory frown

label night4:

    scene bg bedroomnight
    with fade

    play music "Irreplacable Warmth.mp3" fadeout 1 
    queue music "Irreplacable Warmth.mp3"

    ################# day 2 ###################

    scene bg bedroomday
    with fadee

        
    en "What should I do today?"
    en "I could help Marco out with the wedding preparations in the castle garden."
    en "He roped in Lisia for those too. My mother didn't mind, of course."
    en "I could go assist Lisia in the banquet hall."
    en "Or I could go to meet Cordelian."
    en "I suppose I could also give Katherine some company..."
    en "Where should I go?"
        
    scene overworld
    with fade

    ## call an imagemap

    call screen overworld5

label ballroom5:
#if overworld_choice5 == "lisia":

    $ lisia += 1

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"

    scene bg castle
    with fade

    show emory up smile at leftt
    show lisia up smile at rightt
    with dissolve

    l talk "Good morning, [pname]! Which shade of blue do you think will look better for the drapes over there?"

    show lisia smile

    e frowntalk "Umm... The left one, I suppose."

    show emory smile

    l talk "That's what I was thinking too!"
    l "Well, are you here to talk to Cordelian?"

    show lisia smile

    e talk "Actually, I'm here to see if you need help. All this sounds like a lot of work."

    show emory smile

    l talk "It is, although it's fun, in a way."
    l "Are you sure your mother won't mind you helping me here?"

    show lisia smile

    e talk "I don't think she will. My tutor is sick, remember?"
    e "I don't have much else to do all day."

    show emory smile

    l talk "Alright then. What do you want to do? Help with the decorations or the table settings?"

    show lisia smile

    e talk "I could help with the table settings."

    show emory smile

    l talk "Marco has shortlisted some over there. Go through them and pick the ones you like. Just make sure they complement the colours of the rest of the decorations."
    l "Ah! There is Marco now!"

    show lisia smile at right
    show emory smile at left
    show marco up smile at center
    with moveinright

    m talk "Surprising to see you here, [pname]!"

    show marco smile

    e talk "I'm just here to help Lisia out. I'll go select the table settings."

    show emory smile

    m talk "Perfect. We'll be done quicker with an extra pair of hands helping. Maybe we could go out to town later today!"

    show marco smile

    l talk "That sounds like a plan!"

    show lisia smile

    e talk "I better go finish my work then."

    show emory smile

    hide emory
    hide marco
    hide lisia
    with dissolve

    en "Phew. Marco really didn't pay attention to the \"short\" in \"shortlist\", did he?"
    en "That was a lot of selections. And he had too much to criticize to select them!"
    en "I'm glad it's over."
    en "Lisia and Marco both seem to be done too."
    en "So we can have our time off after all!"

    jump overworld5_marcoandlisia
        
label castle5:
#if overworld_choice5 == "marco":

    $ marco += 1

    scene bg castle
    with fade

    show emory up smile at leftt
    show marco up frown at rightt
    with dissolve

    e talk "You look busy, Marco."

    show emory smile

    m frowntalk "I am. I can't believe I have to get all of this done in so little time!"
    m "It's like Cordelian and his parents expect me to be in ten different places at the same time."

    show marco frown

    e frowntalk "Any way I could help?"

    show emory frown

    m talk "Oh, of course!"
    m "The florist is waiting for me to finalise the flower arrangements."
    m "Could you do that, please?"

    show marco smile

    e talk "That doesn't seem too hard. Sure, I'll do it."

    show emory smile

    m talk "Here, you'll need this."

    show marco smile

    e frowntalk "A book of flower meanings?"

    show emory frown

    m frowntalk "Absolutely. It's a royal wedding. Every detail has to be taken care of."
    m "See that you check these meanings before making selections."
    m "Wouldn't want the bridal bouquet to have orange lilies, for example!"

    show marco frown

    e frowntalk "No... I suppose not."

    hide marco
    with moveoutright

    en frown "Do I really have to go through all this?"
    en "I promised him, though, so I might as well get to it."

    show lisia up smile at rightt
    show emory up frown at left
    with moveinright

    l talk "Hello!"

    show lisia smile

    e frowntalk "Gah!"
    e "Oh, it's you, Lisia. You scared me."

    show emory frown

    l talk "Helping Marco, I see."

    show lisia smile

    e talk "Yes. As are you, apparently."

    show emory smile

    l talk "I'm just taking a short break."
    l "But since you're helping now, I guess we'll be finished with this faster. Maybe we'll even have time to head to town later today!"
    
    show lisia smile

    e talk "I'd love to."

    show emory smile

    l talk "Great! I'll ask Marco too."

    show lisia smile

    hide lisia
    with moveoutright

    hide emory
    with dissolve

    en "Well, that was an ordeal."
    en "But I'm done now, and by the looks of it, so are Lisia and Marco."
    en "I should just ask if they're ready to head out!"

    jump overworld5_marcoandlisia
        
label overworld5_marcoandlisia:

    scene bg castionmanorinside
    with fade

    show marco up smile at right
    show lisia up smile at center
    show emory up smile at left
    with dissolve

    m talk "It feels like a while since I've actually had some time off."

    show marco smile

    l talk "This is fun, isn't it?"

    show lisia smile

    e talk "It is, but my stomach is grumbling."

    show emory smile

    l talk "I'm rather hungry too. How about we head to those food stalls over there?"

    show lisia smile

    e talk "My parents used to bring me here when I was younger."
    e "The food is absolutely delicious!"

    show emory smile

    l talk "I'd love to try the tuna nigiri!"

    show lisia smile

    m talk "I think I'll have the wrap."

    show marco smile

    e talk "Well, my favorite used to be the-"

    show emory frown

    mother "[pname]?"

    show mother down frown at right
    hide marco
    with moveinright

    show lisia down frown

    mother frowntalk "[pname]? What are you doing here?"

    show mother frown

    e frowntalk "Mum! I didn't know you were going to be in town today!"

    show emory frown

    mother frowntalk "I could say the same for you. I was under the impression you would be with Cordelian today."

    show mother frown

    e frowntalk "I... uhh... He's busy. I think."

    show emory frown

    mother frowntalk "I see."
    mother "Perhaps you should come home with me, [pname]."
    mother "As should you, Lisia."

    show mother frown

    e frowntalk "But-"

    show emory frown

    mother frowntalk "Now, [pname]!"

    show mother frown

    l frowntalk "Yes, ma'am. We'll be right along."

    show lisia frown

    hide lisia
    hide mother
    with moveoutleft

    show marco at rightt
    with dissolve

    e frowntalk "I'm sorry Marco. Looks like we'll have to cut this trip short."

    show emory frown

    m frowntalk "Don't worry about it."
    m "I'll be at the castle if you need me."

    show marco smile

    e frowntalk "I suppose we should go now."

    show emory frown

    ## end day

    jump day6
        
        
label castle5_1:

    scene bg castleinside1
    with fade

    show emory up smile at leftt
    show cordelian up smile at rightt
    with dissolve

    play music "Tabi.mp3" fadeout 1 
    queue music "Tabi.mp3"

    $ cordelian += 1
    

    e talk "I do hope you'll have some time to spend with me today, Cordelian."

    show emory smile

    c talk "I should. I don't have much to do today."

    show cordelian smile

    e talk "So, what would you like to do?"

    show emory smile

    c talk "I was thinking I could paint something and..."

    show cordelian smile

    e frowntalk "You know how your paintings turn out, Cordelian."

    show emory frown

    c frowntalk "Hey. What's that supposed to mean?"

    show cordelian frown

    e frowntalk "Well, do you remember the \"Idyllic Beach\" you painted, for example?"

    show emory frown

    c frowntalk "Yeah. What about it? It was one of my best!"

    show cordelian frown

    e frowntalk "Remember how the Queen thought it was some kind of otherworldly beast?"

    show emory frown

    c "..."
    c frowntalk "...This one will be better."

    show cordelian frown

    e frowntalk "Don't you say that every time?"

    show emory frown

    c frowntalk "Stop it, [pname]!"

    show cordelian frown

    e talk "Alright, alright. Let's see you do this. Mind if I grab a brush too?"

    show emory smile

    c talk "Go ahead!"

    hide cordelian
    hide emory 
    with dissolve

    $ renpy.pause(1.0)

    show emory up smile at closeleft
    show cordelian up smile at closeright
    with dissolve

    e talk "How's the..uhhh...upside down rabbit coming along?"

    show emory smile

    c frowntalk "What're you talking about? This looks nothing like a rabbit."

    show cordelian frown

    e talk "No. Of course, not. I meant the... snowman?"

    show emory smile

    c frowntalk "It's the clouds! On a summer day!"
    c "Obviously."

    show cordelian frown

    e talk "Right. How could I not see that?"

    show emory smile

    c frowntalk "It's really that bad, isn't it?"

    show cordelian frown

    e talk "Yup."
    e "In all fairness, mine's not exactly a masterpiece either."

    show emory smile

    c down talk "Shall we just go to the castle gallery?"
    c up "I bought some new paintings last time I was in Auqecia. They're beautiful!"

    show cordelian smile

    e talk "We should-"

    show emory frown

    show emory at left
    show cordelian at center
    show katherine up smile at right
    with moveinright

    k talk "Good evening, gentlemen."

    show katherine smile

    en "She is starting to get on my nerves now."

    c talk "Evening, Kathy."

    show cordelian smile

    en "Didn't it used to be Kath?"

    e frowntalk "Hello, Princess."

    show emory frown

    k talk "Would it be a terrible inconvenience if I joined you?"

    show katherine smile

    c talk "Of course not! We'd love it."
    c "Don't you agree, [pname]?"

    show cordelian smile

    e frowntalk "...Yes."

    show emory frown

    c talk "We were just going to the gallery. I haven't shown [pname] the paintings I got from Auqecia."

    show cordelian smile

    k talk "I see."

    show katherine smile

    c talk "Yes, well, shall we?"

    show cordelian smile

    jump overworld5_cordelianandkatherine

label castle5_2:

    scene bg castleinside2
    with fade

    show emory up smile at leftt
    show katherine up smile at rightt
    with dissolve

    $ katherine += 1

    e talk "Good morning, Princess."

    show emory smile

    k talk "Hello, [pname]."

    show katherine frown

    minister "Your Highness, perhaps we should go and inform your father about your plans for the wedding dress."

    k frowntalk "Must we go now?"

    show katherine down frown

    minister "It would be convenient if we did, yes."

    k frowntalk "I believe [pname] would not like to be abandoned, considering we just met."

    show katherine frown

    e frowntalk "If it's important, Katherine-"

    show emory frown

    minister "Please address the Princess with respect."

    k frowntalk "That will be enough, Ms. Melton."
    k "It would be nice if you could leave now."

    show katherine frown

    minister "Your Highness, I didn't mean to sound-"

    k frowntalk "Do I need to repeat myself?"

    show katherine frown

    minister "No, Your Highness."

    $ renpy.pause(1.0)

    k up frowntalk "Please forgive her behavior, [pname]."

    show katherine frown

    e frowntalk "That's... that's quite alright, really."

    show emory frown

    k frowntalk "*sigh* My father's ministers think they have the right to dictate my every move."

    show katherine frown

    e frowntalk "Oh. Doesn't your father mind?"

    show emory frown

    k down frowntalk "Mind? He encourages them."
    k "I suppose he doesn't quite trust me to make my own decisions, yet."

    show katherine frown

    e frowntalk "...Aren't you getting married in a week?"

    show emory frown

    k frowntalk "Yes. It's an agreement our parents made, to protect both kingdoms."
    k "I had no say in it."

    show katherine frown

    e sad frowntalk "So, you don't love Cordelian?"

    show emory frown

    k "..."
    k up frowntalk "...I'm not sure if I do, to be honest."
    k down "[pname]?"

    show katherine frown

    e frowntalk "I was just thinking about what you said, is all."

    show emory frown

    k frowntalk "Could you... not speak of this to Cordelian?"

    show katherine frown

    e up frowntalk "Of course."

    show emory frown

    k frowntalk "I don't want any conflicts, not this close to the wedding."

    show katherine frown

    e frowntalk "I understand, Katherine."
    e "But, if I might give you some advice, I'd say you should speak to Cordelian yourself."
    e "He's a much more understanding person than he seems to be."

    show emory frown

    k down frowntalk "I can't, [pname]."

    show katherine frown

    e sad frowntalk "Why is that? If you need me to be there, that won't be a problem."

    show emory frown

    k frowntalk "That is not what I meant."
    k "My parents wouldn't approve of my telling him."
    k "In fact, I shouldn't have told you so much, either."

    show katherine frown

    e up frowntalk "I won't tell anyone about it."
    e "Especially Cordelian."

    show emory up frown at left
    show katherine up frown at center
    show cordelian up smile at right
    with moveinright

    c talk "Did someone say my name?"

    show cordelian smile

    e frowntalk "Oh! Yes. We were just speaking about... err..."

    show emory smile

    k talk "Your castle's gallery."

    show katherine smile

    e talk "Yes, we were wondering if we should go there."

    show emory smile

    c talk "Well, how about we all go together?"

    show cordelian smile

    e talk "Sounds perfect!"

    jump overworld5_cordelianandkatherine

label overworld5_cordelianandkatherine:

    scene bg gallery
    with fade

    show emory up smile at left
    show cordelian up smile at center
    show katherine up frown at right
    with dissolve
    
    c talk "I absolutely adore this one."

    show cordelian smile

    e talk "I can see why!"

    show emory smile

    k "Hmm."

    show cordelian:
        xzoom -1

    c frowntalk "What is it, Kath?"

    show cordelian frown

    en "Isn't that man over there one of Katherine's father's ministers?"
    en "What is he doing here?"

    minister "A very good afternoon to Your Highnesses, and to... the friend of the prince."

    en down "I have a name..."

    k frowntalk "What do you require?"

    show katherine frown

    minister "Nothing, Princess. Your father simply wishes that I be at your side at all times."
    minister "It is important to him, in fact."

    k down frowntalk "To my father? You're lying."

    show katherine frown

    minister "I beg your pardon?"

    k frowntalk "Tch. My father is barely the one holding onto your reins, Minister."

    minister "I'm not sure that is an appropriate statement..."

    k frowntalk "Your concern for my speech is touching, but I would like you to leave us alone, now."

    minister "I cannot."

    c down frowntalk "I'm sure you remember this is my castle and not yours, Minister."

    show cordelian frown

    e frowntalk "And I'm sure you heard your Princess. Certainly, you do not claim to have more authority than the woman who is to be Queen in a week?"

    show emory frown

    c frowntalk "Please leave, good sir."

    show cordelian frown

    minister "Chief Minister Laclen will hear of this, Your Highness."

    k "..."

    c up frowntalk "So, who is this Laclen? I have a feeling he is more than just Chief Minister."

    show cordelian frown

    k up frowntalk "It is a long story, Cordelian."
    k talk "One for another time, perhaps."

    show katherine smile

    c frowntalk "I will not push you, Kath. But if there is anything you want to speak about, you know you can come to me."

    show cordelian smile

    k talk "Thank you for the offer. It is much appreciated."

    show katherine smile



    ################################################################################################
    ##################################      Carnival Day        ####################################


label day6:
    
    scene bg bedroomnight
    with fade

    scene bg bedroomday
    with fadee

    show lisia up smile at closerright
    show emory up smile at closerleft
    with dissolve

    l talk "It's the carnival!"

    show lisia smile

    e unsure talk "I don't know how you're so excited and awake this early in the morning, Lisia."

    show emory smile

    l talk "But the carnival!"

    show lisia smile

    e talk "Yes, I know. You've been repeating this for the past ten minutes."

    show emory smile

    l talk "Ah. Sorry. I'm a bit excited, you see."

    show lisia smile

    e talk "I do see. Where did the others ask us to meet them, again?"

    show emory up smile

    l talk "The gazebo, I think they said."

    show lisia smile

    e talk "Alright then. Shall we?"

    show emory smile

    scene bg carnival
    with fade

    show emory up smile at leftt
    show lisia up smile at rightt
    with dissolve

    l talk "There they are! Marco! Cordelian! Princess!"

    show lisia smile

    e talk "I'm sure you don't need to shout quite so loudly..."

    show emory smile

    show emory at left
    show lisia at center:
        xzoom -1
    show cordelian up smile at right
    with moveinright

    c talk "Hello everyone!"

    hide cordelian
    show marco up smile at right
    with moveinright

    m talk "Hello."

    hide marco
    show katherine up smile at right
    with moveinright

    k talk "Good morning."

    show katherine smile

    e talk "I'm glad we found you. Now, where to?"

    show emory smile

    hide katherine
    show cordelian up smile at right
    with moveinright

    c talk "Marco's the organiser of this entire event, so he'll tell us the best places to be!"

    show cordelian smile

    en "I'm not really surprised..."

    hide cordelian
    show marco up smile at right
    with moveinright

    m talk "So there are the rides, the food, the various performances and the shops."
    m "I say we head to the rides first, and food after that."

    show marco smile

    e talk "I don't think the performances have started yet, have they?"

    show emory smile

    m talk "No, not really. We better keep those for later."

    show marco smile

    l talk "Rides! Those are fun."

    show lisia smile

    hide marco
    show katherine up frown at right
    with moveinright

    k down talk "Yes. Fun."

    show katherine smile

    e unsure frowntalk "I do hope you believe in the concept of fun..."

    show emory frown
    show katherine frown

    hide katherine
    show cordelian up frown at right
    with moveinright

    c frowntalk "Be nice, [pname]."

    show cordelian frown

    e up frowntalk "Okay, okay."

    show emory talk
    show cordelian smile
    
    e "So, who wants to go to the carousel with me?"

    show emory smile

    l talk "I'll come along!"

    show lisia smile

    c talk "Count me in!"

    hide cordelian
    show marco up frown at right
    with moveinright

    m talk "Well, if everyone else is going..."

    show marco smile

    hide marco
    show katherine up frown at right
    with moveinright

    k frowntalk "I think I would prefer to stay here."
    k "Please go ahead and enjoy yourselves."
    k "I will wait here by this bench."

    show katherine smile

    l talk "Princess! I'm sure you'll enjoy this! Come with us!"

    show lisia smile

    k down talk "I don't think..."

    show katherine smile

    l frowntalk "Please, Your Highness."

    show lisia frown

    hide lisia
    show cordelian up frown at center
    with moveinright

    c frowntalk "She is right, my dear."

    show cordelian frown

    k talk "...If you insist."

    show katherine smile
    show cordelian smile

    scene bg carnival
    with fade

    show emory down frown at left
    show lisia down frown at center
    show cordelian up smile at right
    with dissolve
        
    l frowntalk "Can't...stop...spinning."

    show lisia frown

    e frowntalk "I don't think I can keep standing."

    show emory frown

    c talk "That was amazing! I have never ridden such a fast moving carousel!"

    hide cordelian
    show marco down frown at right
    with moveinright

    m frowntalk "I'm not feeling very well..."

    show marco frown

    hide marco
    show katherine down frown at right
    with moveinright

    k frowntalk "I... erm..."

    show katherine frown

    hide katherine
    show cordelian up talk at right
    with moveinright

    c "What are you all talking about? I haven't had this much fun in a long time!"
    c "Should we go on another ride?"

    show cordelian smile

    e frowntalk "I don't think I will be able to handle it."

    hide cordelian
    show katherine down frown at right
    with moveinright

    k frowntalk "I agree with [pname]. Perhaps we should see some of the other attractions?"

    show katherine frown

    hide katherine
    show marco down frown at right
    with moveinright

    m talk "How about the musicians who are visiting from Daphate? I think they must have set up by now."

    show marco smile

    l talk "Daphate is known for its rich culture, isn't it? I would love to hear their music!"

    show lisia smile

    e talk "I agree."

    show emory smile

    hide lisia
    show cordelian up frown at center
    with moveinright

    c frowntalk "...Alright. You are no fun at all. But if you insist..."

    show cordelian frown

    hide cordelian
    show katherine down frown at center
    with moveinright

    k frowntalk "I believe we do."

    show katherine frown

    m talk "This way. The podium for the musicians should be right around here."

    scene bg carnival
    with fade

    show emory up smile at left
    show lisia up smile at center
    show marco up smile at right
    with dissolve

    l talk "Wasn't it beautiful?"

    show lisia smile

    e talk "Absolutely. How long are they staying here, Cordelian?"
    e "Perhaps I can convince my father to invite them for a concert later this week?"

    show emory frown

    m frowntalk "I'm afraid you won't be able to, [pname]. They're leaving tonight."
    m "They were supposed to stay and play at the wedding, but they had to leave."

    show marco frown

    e frowntalk "Oh. Is there a problem of some sort?"

    show emory frown

    m frowntalk "I'm not sure, actually. I suppose there must be."

    show marco frown
    show lisia frown

    hide marco
    show cordelian down frown at right
    with moveinright

    show emory down

    c frowntalk "I overheard my mother saying Daphate has been captured, although unofficially, by Leodipia."
    c down "Their king is paying a hefty tribute to Leodipia and must do so every year from now on."

    show cordelian frown

    l frowntalk "Isn't that the kingdom that has been trying to capture ours for years now?"

    show lisia frown

    hide cordelian
    show katherine down frown at right
    with moveinright

    k frowntalk "I believe it is. Dersion, too, has been trying to evade them for some time."
    k "However, I hear that they have grown stronger recently."

    show katherine frown

    hide katherine
    show cordelian down frown at right
    with moveinright

    c frowntalk "They already have the Daphate army at their disposal, if what mother said is true."

    show cordelian frown

    hide lisia
    show katherine down frown at center
    with moveinright

    k frowntalk "They have other puppet kings as well."

    show katherine frown

    e frowntalk "This isn't good. For either of our two kingdoms."

    show emory frown

    hide katherine
    show marco down frown at center
    with moveinright

    m frowntalk "Our army is always ready in case of a war."

    show marco frown

    c frowntalk "I know, Marco. But if we can avoid war altogether, it would be better."

    show cordelian frown

    hide marco
    show katherine down frown at center
    with moveinright

    k talk "Perhaps we could do what we came here to do, and enjoy the festival."
    k "Besides, Lisia is not as familiar with politics as any of us, and it wouldn't do to leave her out."

    show katherine smile

    e talk "Oh. I... uhh... Let's go to the food stalls then."

    show emory smile

    hide cordelian
    show lisia up smile at right
    with moveinright

    l talk "Yes! Thank you, Katherine."

    scene bg bedroomnight
    with fade

    en "Well, that was certainly fun."
    en "It's been months since I've seen Cordelian so happy."
    en "I hope everyone else had fun..."
    en "There's not too many more days until the wedding. The wedding... my best friend is getting married! I'm way too young to start going to friends' weddings!"
    en "I need to lie down..."

    ## TODO insert another day or a few here

label night6:

    scene bg bedroomnight
    with fade

    play music "Irreplacable Warmth.mp3" fadeout 1 
    queue music "Irreplacable Warmth.mp3"



    ############################### day 2 ##################################



    scene bg bedroomday
    with fadee

        
    en "The wedding feels so close now..."
    en "It almost feels like I'm running out of time, yet I'm not the one getting married."
    en "He may act nonchalant about it, but I know Cordelian is nervous too. Maybe I should go seem him today."
    en "Of course, I could go see Katherine before she goes home for a while."
        
    ## call an imagemap

    scene overworld
    with fade

    #call screen overworld6

label day7_marco:
    scene bg garden
    with fade

    $ marco += 1

    show marco up smile at closerright
    show emory up smile at closerleft
    with dissolve

    e talk "Good morning, Marco!"

    show emory smile

    m talk "Good morning. Is it a rather good morning for you?"

    show marco smile

    menu:
        "Yes, I'd say so.":
            e talk "Yes, I'd say so. I slept well last night and had a good breakfast this morning."

            show emory smile

            m talk "That's good. It's supposed to start drizzling around lunchtime, so I hope you have an umbrella with you."

        "I don't know yet.":
            e talk "I don't know yet, to be honest. The day is still young."

            show emory smile

            m talk "Hopefully it'll turn into a good morning for you then."
            m "It's supposed to start drizzling around lunchtime, so I hope you have an umbrella with you."

    show marco smile

    e frowntalk "No, I did not. None of the maids mentioned it before I left."

    show emory frown

    m talk "Maybe it won't rain too much. Forecasts can be wrong."

    show marco smile

    e frowntalk "Hopefully."

    show emory frown

    m frowntalk "I'm wanting it not to rain as well- the rose bushes on the walkway in the courtyard won't make it through another heavy rain."
    m "They'll be a terrible sight if they lose any more petals."

    show marco frown

    e unsure frowntalk "Isn't it almost time to prune them back?"

    show emory frown

    m frowntalk "Yes, {i}almost{/i}. They look hideous when pruned though so I've got to wait until after the wedding to prune them, though."

    show marco frown

    e up frowntalk "Oh, I see."
    e talk "What about the roses over here?"

    show emory smile

    m talk "They're roses I'm growing myself."
    m "A shopkeeper downtown gave the seeds to me to grow- yellow and white roses are hard to come by here."

    show marco smile

    e talk "You've done an excellent job, then. They look beautiful."

    show emory smile

    m talk "Thank you."

    show marco smile

    en "He takes a pair of sheers and cuts one at the stem."

    e unsure frowntalk "Wh-"

    show emory frown

    m talk "Here, take this."
    m "The yellow rose represents friendship and joy."

    show marco smile

    e talk "Thank you..."
    e "So, are you ready for the wedding?"   

    show emory smile

    m frowntalk "Oh, no. I wouldn't be ready for it if it were a year away."
    m "I feel like there's not enough time for {i}anything{/i}- like the whole country will collapse if the cakes aren't the right flavor or if the doilies aren't laid out."
    m "The chefs ran me out of the kitchen, protesting that I spend an hour outside before coming back."

    show marco frown

    e talk "Sounds like a good choice on their part."
    e "I'm surprised you haven't become ill because of this."

    show emory smile

    m frowntalk "Oh, I will once the wedding day comes."
    m "Dr. Jameson prescribed me multi-vitamins the other day to take daily. But, vitamins won't exactly keep my immune system healthy forever."

    show marco frown

    e talk "No, but taking time off might."

    show emory smile

    na "Marco! Where were the lights stored?"

    m frowntalk "They should be in the closet near the staircase."

    show marco frown

    na "What about the table cloths? Were we going to use red or blue?"

    m down frowntalk "R-Red-?!"
    m "Emory, you'll have to excuse me."

    show marco frown

    e frowntalk "Alright..."
    e talk "Try to get enough sleep and water, alright?"

    show emory smile

    m up frowntalk "I can't make any promises."

    if marco > 6:
        m talk "But I'll try."

    show marco smile

    jump night7

label day7_lisia:
    scene bg emorystudy
    with fade

    $ lisia += 1

    play music "Encounter.mp3" fadeout 1 
    queue music "Encounter.mp3"

    show emory up frown at leftt
    show lisia up smile at rightt
    with dissolve

    e frowntalk "Lisia, what's with all the racket down here?"

    show emory frown

    l frowntalk "Oh, sorry! Did I wake you?"

    show lisia frown

    e frowntalk "Somewhat... it was about the time for me to get up anyway. But still."

    show emory frown

    l frowntalk "I was just cleaning up some old books."
    l "...And they might have avalanched."
    l "A couple times."

    show lisia frown

    e unsure talk "Do you need help picking them up?"

    show emory smile

    l frowntalk "No, that's fine- wait! I said I could do it!"

    show lisia frown

    e up talk "It was rhetorical. I'm going to help you anyway."

    show emory smile

    l down talk "Okay..."

    show lisia smile

    en "It looks like one of the shelves gave way and made most of this mess... which caused another shelf to give way..."
    en "I pick up some of the books on the floor beside me."
    en "Thankfully for Lisia, most of these books are newer. The older ones would have been damaged from hitting the floor."
    en "Maybe Mother didn't hear all the noise..."

    e talk "Oh, what's this?"

    show emory frown

    l up frowntalk "Huh?"
    l "It looks sort of like an astrology book."

    show lisia frown

    e frowntalk "Yes, you're right I think. The one on top of it seems to be a farmer's almanac."
    e "I don't really remember these."

    show emory frown

    l frowntalk "Maybe they're your mother's?"

    show lisia frown

    e frowntalk "I never thought of her as the type for such, but it's possible. They're certainly not Father's."

    show emory frown

    l "Hmm..."
    l talk "Are you sure they're not yours~?"

    show lisia smile

    menu:
        "Of course not!":
            e down frowntalk "Of course not! Why would I read something like that?"

            show emory unsure frown

            l frowntalk "I don't know... they might be interesting."

            show lisia frown

        "They're not, but they could be.":
            e unsure talk "They're not, but they could be. They might be interesting."

            show emory smile

            l talk "Why don't you get back to me on that one in a week or two?"

            show lisia smile

            e up talk "Maybe I will."

            show emory smile

    en "She straightens up the stack she's working on on the floor and puts it on the table."

    l down talk "I called one of the maintenance crew to come by later and reinstall the shelves. I don't want to put them back just for the books to fall again."

    show lisia up smile

    e talk "That's a good idea."




label day7_cordelian:
    scene bg castleinside2
    with fade

    $ cordelian += 1

    e "hi"

label day7_katherine:
    scene bg castleinside1
    with fade

    $ katherine += 1

    e "HI"








label night7:

    #### TODO route diverges
    if cordelian > marco or katherine > marco or cordelian > lisia or katherine > lisia:
        jump cordeliankatherine_commonroute
    else:
        jump marcolisia_commonroute
    


label cordeliankatherine_commonroute:
    
    scene bg castleinside1
    with fade

    show emory up smile at center
    with dissolve

    e talk "Do you know where Cordelian might be at?"

    show emory smile

    maid "He's in a meeting right now down the hallway."

    e talk "Thank you, I'll go see him."

    show emory smile

    en frown "A meeting, huh? It seems like he's been going to more of those as of late."
    en "Is it about Leodipia's advances?"
    en "Surely, if things get bad, we'll be prepared. Surely, Father will come back from overseas before that..."

    show emory up frown at leftt
    show cordelian down frown at rightt
    with moveinright

    e talk "Oh-{w=1.0}{nw}"

    show emory sad frown

    e "..."

    c "..."
    c up talk "Ah, [pname]! Good morning."

    e frowntalk "Cordelian..."
    e "Everything's not alright, is it?"

    show emory frown

    c down frown "..."

    e up "!"

    hide emory
    hide cordelian
    with moveoutleft

    scene bg darkroom
    with fade

    show emory up frown at left:
        zoom 1.55
        yalign 0.3
    show cordelian unsure frown at right:
        zoom 1.55
        yalign 0.3
    show emorytint at left:
        zoom 1.55
        yalign 0.36
        alpha 0.3
    show cordeliantint:
        zoom 1.55
        yalign 0.36
        xalign -0.82
        alpha 0.3
    with dissolve

    en "He grabs me by the arm and pulls me into one of the unused rooms."

    c "..."
    c frowntalk "No..."
    c "I'm starting to doubt myself now."

    show cordelian frown

    en "I try to reassure him by resting a hand on his arm."

    e talk "I know whatever you've chosen was for the best because {i}you{/i} chose it."

    show emory sad smile

    c frowntalk "Yes... but was it best for me or was it best for my country?"

    show cordelian frown

    e talk "You're not a selfish person. You would pick your country any day over yourself."

    show emory smile

    c frowntalk "And that's what got me into this, isn't it? Thinking about the longterm future for my country rather than myself..."
    c "...What am I even doing? There's no backing out now. It's too close."

    show cordelian frown

    e frowntalk "T-Too close? Is they army going to be able to prepare in such short time?"

    show emory frown

    c up frowntalk "The army? What does that have to do with the wed-"
    c talk "Y-Yes, the army! Of course, they're ready at a moments notice."
    c frowntalk "They've been planning for months in case of an emergency. Our consuls in Daphate have been sending back troubling news but we'll be ready for anything."
    c talk "But, don't worry. Our generals have in under control. We'll be deploying more troops to the Daphate border."

    show cordelian smile

    e talk "That's comforting."

    show emory smile

    c talk "But, let's get to a lighter subject."
    c "It's almost lunch- would you like to eat with Katherine and I?"

    show cordelian smile

    e talk "That's sounds great."

    show emory smile

    scene bg castleinside2
    with fade

    en "I thought the atmosphere was tense before, but it's almost as dreadful here."
    en "Katherine is sitting at the table, idly stirring her tea."

    show emory unsure frown at left
    show cordelian up frown at center
    show katherine up frown at right
    with dissolve

    k frowntalk "Oh, [pname], are you going to eat with us?"

    show katherine smile

    c talk "Yes, I thought I would invite [xim] so it wouldn't be just the two of us."
    c frowntalk "I-I mean, we could eat alone, but I thought since [xe] was already here you know-{w=1.0}{nw}"

    show cordelian frown
    show emory smile

    k talk "Yes, yes, that's fine. I don't ever mind your company, [pname]."
    k "I hope you like grilled duck or roast beef, though."

    show katherine smile

    menu:
        "I love grilled duck.":
            e up talk "Oh, I love grilled duck. As long as Susanna is cooking it tonight, it'll come out wonderful."

            show emory smile

            k talk "It does sound good. To be honest, I've never tried it before."
            k "But Cordelian kept persisting I try it, so here we are."

            show katherine smile

        "I love roast beef.":
            e up talk "Oh, I love roast beef. When Roberto lets it marinate in the vegetables for a few hours, it's wonderful."

            show emory smile

            k talk "I'm not one to love vegetables but it does sound good."

            show katherine smile

            c talk "I'm sure you'll love it."

            show cordelian smile

        "I'll eat the sides.":
            e talk "Ah, maybe I should just eat the side dishes..."

            show emory smile

            k talk "I'm sure everything will be good regardless."

            show katherine smile

    hide katherine
    hide cordelian
    hide emory
    with dissolve

    en "A group of maids come over to set the dishes down on the table."
    en "Despite it being just the three of us, they seemed to have cook enough for five or six people."
    en "We eat in relative silence- I'm not normally sensitive to silence, but today is just different. There's a feeling of unease in the air."
    en "The wedding is just a few days away."
    en "I thought they'd be more happy right now."

    menu:
        "Break the silence":
            en "I can't stand this anymore."

            show emory up frown at left
            show cordelian up frown at center
            show katherine up frown at right
            with dissolve

            e frowntalk "Katherine, how has your day been?"

            show emory frown

            k frowntalk "Alright, I suppose. I had to attend a few meetings in the morning and then try on my dress for the 30th time."
            k "The tailors wanted to make sure it would fit perfectly without any stray strands."

            show katherine frown

            c talk "I'm sure the dress looks fine."

            show cordelian smile

            e talk "Have you met with your tailor yet, Cordelian?"

            show emory smile

            c frowntalk "For what?"
            c talk "O-Oh, for the wedding! Yes, I've met with my tailor a few times."
            c "We have a light blue military suit planned."

            show cordelian smile

            e talk "I'm sure they both look great."

            show emory smile

        "...":
            e "..."

            en "I finish off my plate and set my fork down."
            en "Cordelian finished his main meal a minute ago and is stirring his soup listlessly."

            maid "Your highness, may I take your plate?"
            maid "..."

            ## TODO redo sprite sidesweep animation
            show cordelian up frown at center:
                xzoom -1
                zoom 1.4
                yalign 0.3
                xalign 0.2
            with dissolve

            show cordelian:
                xalign 0.8
            with MoveTransition(5.0)

            maid "Ah... your highness?"

            c frowntalk "O-Oh, yes, sure."

            show cordelian frown
            $ renpy.pause(0.1)
            hide cordelian with dissolve

            maid "Are you done, my lady?"
            maid "..."

            show katherine up frown at center:
                zoom 1.4
                yalign 0.3
                xalign 0.8
            with dissolve

            show katherine:
                xalign 0.2
            with MoveTransition(5.0)

            maid "Lady Katherine?"

            k "..."

            if katherine > cordelian:
                show katherine up frown at rightt:
                    zoom 1.0
                show emory unsure frown at leftt
                with dissolve

                e frowntalk "Katherine, are you done?"

                show emory frown

            else:
                show katherine up frown at rightt:
                    zoom 1.0
                show cordelian unsure frown at leftt:
                    xzoom -1
                with dissolve
                
                c frowntalk "Katherine, are you done?"

                show cordelian frown

            k frowntalk "...Yes, I'm done."

            show katherine frown

        en "The maids take their plates and begin clearing the table."

    show emory sad frown at left
    show katherine at center
    show cordelian at right:
        xzoom -1
    with dissolve

    menu:
        "I need to talk to him.":
            $ cordelian += 1
            jump cordelianroute
        "I need to talk to her.":
            $ katherine += 1
            jump katherineroute

label cordelianroute:
    e up frowntalk "Cordelian, do you mind walking with me to the garden? Marco told me to meet him there in a few minutes, probably something about the wedding plans."

    show emory frown

    c frowntalk "I suppose..."

    show cordelian frown

    scene bg garden
    with fade

    en "I have to see what he's thinking."

    show emory up frown at closerleft
    show cordelian up frown at closerright
    with dissolve

    e unsure frowntalk "Cordelian..."
    e "How are things?"

    show emory frown

    c talk "Things are as they always are, of course. Everything's fine."
    c "The meeting this morning rustled my nerves but after lunch I'm feeling much better."

    show cordelian smile

    e frowntalk "Are you?"
    e "How are {i}you{/i} actually doing?"

    show emory frown

    c "..."
    c unsure "..."
    c frowntalk "I..."

    #show cordelian frown

    if cordelian < 6:
        c up "Nothing. It's nothing."

        show cordelian frown

        e sad frowntalk "Cordelian!"
        e "How can you lie to me- to {i}yourself{/i}- like that?"
        e "You're miserable."

        show emory frown

        c frowntalk "You don't know what I'm thinking."

        show cordelian frown

        e frowntalk "Then tell me what you're thinking, because I don't think you even realize it yet."

        show emory frown

        c frowntalk "I'm worried about becoming king, of course."

        show cordelian frown

        menu:
            "Is that true?":
                e frowntalk "Is that really the truth?"
                e "I feel like that's not the thing you're most worried about."

                show emory frown

                c frowntalk "Why wouldn't I be? Becoming king is no small role, especially when war is near."

            "You're worried about something else.":
                e frowntalk "I know you're worried about something else."
                e "You're unsure about the wedding, aren't you?"

                show emory frown

                c frowntalk "Of course I am."
                c "We'll be in front of thousands giving our vows. It's nerve-wracking just thinking about it."

        c "You should leave the worrying to me."

        show cordelian frown

        e frowntalk "I'll be able to stop worrying about you when you start being truthful with yourself."
        e "You don't want to get married, do you?"

        show emory frown

        c down frowntalk "[pname]... I don't want to hear another word of this."

        show cordelian frown

        e frowntalk "Cordelian!"
        e "Listen to yourself! You won't even entertain the thought that you're not happy!"

        show emory frown

        c frowntalk "It doesn't matter!"
        c "Leave well enough alone!"

        show cordelian frown

        e frowntalk "It's not well enough if you're miserable!"
        e "Let me help you. Please."

        show emory frown

        c frowntalk "I told you, I..."
        c unsure "I..."
        c frown "..."


    elif cordelian >= 7:
        c "I don't know anymore."
        c "I thought I could handle all of this."
        extend "I thought I could manage."
        c "But, I..."
        c "I don't even know now."

        show cordelian frown

        e talk "It's alright. We can talk this through together."

        show emory smile

        c frowntalk "Together..."
        c frown "..."

    c frowntalk "[pname]..."
    c "Can we... keep something secret between the two of us?"

    show cordelian frown

    e up frowntalk "Of course, anything. I just want honesty."

    show emory frown

    c frowntalk "I..."
    c "I don't think I can do this."
    c "The marriage."
    c "At first, I thought that maybe I was just unqualified, that I couldn't be a good husband."
    c "The word scares me. I've had the prospect of \"king\" shoved at me for so long that I've grown numb to it, but \"husband\" is something else entirely."
    c "How can I be a \"husband\" to someone when I'm barely 20?"
    c "So then I thought that I just needed to try harder to fill those shoes."
    c "I tried to be more welcoming, more sociable, more thoughtful."
    c "But it didn't matter."
    c "It wasn't that she wasn't trying. She would always put on her most meek but gentle smile when I was around."
    c "It's that every time I saw her I couldn't help but think of my parents. Aging, together. Growing old, together."
    c "I couldn't see myself growing old with her. No, it's not that I {i}couldn't{/i} see it- I didn't want to."
    c "I kept pushing it off in the corner of my mind. \"It's something I'll worry about later\"."
    c "\"I'll invite her over for diner and we'll start to click more then\"."
    c "And now we're here."

    show cordelian frown

    $ renpy.pause(1.0)

    e frowntalk "Cordelian... what do you want?"

    show emory frown

    c frowntalk "What do I want... I don't even know that anymore."
    c "I want us to have a time of peace. The planning for going to war has been hammering at my nerves more than the wedding has had time to do."
    c "I don't want to get married. She's not the easiest to read but I know if there were an easy way out of all this she would take it."
    c "And..."
    c "...I want to be able to live with whatever happens. To know I didn't just make a rash decision that'll detriment everyone else."

    show cordelian frown

    e frowntalk "Maybe we can figure out something that'll work."

    show emory frown

    c frowntalk "I've tried."

    show cordelian frown

    e talk "You didn't have me helping."

    show cordelian smile

    en smile "I put my hand on his. He sighs."
    e talk "Alright, let's start from the top. Why is the marriage necessary?"
    e "Tell me in your own words. ...Your highness."

    show emory smile

    c frowntalk "The marriage... my father said it would unite Sharan and Dersion against Leodipia."

    show cordelian frown

    e frowntalk "But why marriage? Couldn't you unite the two without it?"

    show emory frown

    c frowntalk "{i}We{/i} most likely could, however..."
    c "I'm starting to think it was a two-folded answer."
    c "It's a sound way to unite two kingdoms, yes, but it's also an easy way to make sure I marry royalty."

    show cordelian frown

    e frowntalk "That's {i}it{/i}?"
    e "And you didn't try to argue with him?"

    show emory frown

    c frowntalk "How could I? I tried to ask if it was really necessary, but he'd give me the same answers every time."
    c "I couldn't be direct with him, lest he send me away and storm off."

    show cordelian frown

    e sad frowntalk "You have to confront him. This is the rest of your life we're talking about."

    show emory frown

    c frowntalk "I know, I know..."

    show cordelian frown

    e frowntalk "I know you're scared of what he'll say, but you have to stand up for yourself."
    e "What good is a miserable king?"

    show emory frown

    c "..."
    c frowntalk "You're right..."
    c "I'll talk to him tonight."

    show cordelian smile

    e talk "Now you're just putting it off."

    show emory smile

    c talk "I call it giving myself time to mentally prep myself."
    c "Still, it is a shame that all of this work on the wedding will go to waste."

    show cordelian frown

    e talk "Who's to say it has to all go to waste?"
    e "What if we hold a ball instead?"

    show emory smile

    c talk "It's cute you think it'd be that easy..."
    c "Alright, let's see..."
    c "I won't get married. He'll be ballistic, for sure."
    c "I'll ask Katherine to be by my side to convince him there's another way. Maybe the two of us can convince him that we don't need to be married to defend our countries."
    c "We'll cancel all the wedding plans and instead declare war on Leodipia."
    c "We were always going to have to declare war eventually... Maybe now it can give people something else to concentrate on rather than a faux wedding."
    c "As for the wedding venue itself... we can turn it into a dance maybe."
    c "One last \"hurrah\" I suppose before we turn all our efforts elsewhere."
    c "Does that sound somewhat reasonable?"

    show cordelian smile

    e up talk "You already know it sounds perfectly fine to me. I just wish you had done it sooner."

    show emory smile

    c unsure talk "And why is that?"

    show cordelian smile

    e talk "So you weren't so miserable for so long and could move on."

    show emory smile

    c talk "Move on..."
    c "And how would you do that?"

    show cordelian smile

    menu:
        "I'd spend time with someone else.":
            e talk "I'd spend time with someone else than focusing on her all the time."
            e "I know your friends, but the only reason you were spending so much time with her was because of the marriage, correct?"
            e "So... I'd spend it with someone you want to be with."

            show emory smile

            c talk "Someone I want to be with... I believe that's sound advice."

        "I'd find a hobby.":
            e talk "I'd find a hobby. Something to get the stress off- you'll need it soon."
            e "Perhaps take up an instrument? Or checkers?"

            show emory smile

            c talk "Checkers? Not chess? My, do you think I'll need to prepare for becoming old already?"
            c "Hmm... That is an interesting idea, though. Maybe I'll pick something up in my spare time- if I have any."
            c "Of course, it's always easier to start something new when you have someone by your side."

            show cordelian smile

            e talk "I'll always be here, no matter what you pick. I thought you knew that."

            show emory smile

            c talk "I do- I just forgot it for a time. I won't forget it anymore."

    c "Thank you, [pname]. Really."
    c "Now... what's say we join my soon-to-be ex fiancée?"

    scene black
    with fadee

    $ renpy.pause(0.5)

    e "Cordelian!"
    e "Cordelian...?"

    scene bg cordelianbedroomnight
    with fade

    en "Is he even in here?"
    e "Hello...?"

    c "Over... here..."

    #show cordelian sad frown at closerright
    show emory sad frown at closerleft
    show emorytint at closerleft:
        yalign 0.39
        xalign -0.28
        alpha 0.3
    with dissolve

    e frowntalk "Cor... Cordelian...?"
    en frown "He's slumped down on his bed- his hair ruffled and the bedsheets thrown about."
    e frowntalk "Is..."

    show emory frown

    c "..."

    menu:
        "Sit down beside him":
            e frowntalk "I'm here."

            show emory frown

    c "..."
    c "He... took it about as well as I expected..."
    c "Said I was... unfit to be king... if I didn't want to make sacrifices..."
    c "Said a few other pleasantries while he was at it..."
    c "Katherine ran off to her room..."
    c "I..."
    c "I don't know what to do."
    c "I just want out of this."
    c "[pname]. Please."
    
    e "..."
    en "Is there even anything left we can try...?"
    en "Is this just something we'll all have to live with?"
    en "I grab his hand."
    e frowntalk "What does the queen think about it all?"

    show emory frown

    c "Last I heard, she's going along with it all."

    e unsure frowntalk "Last you heard?"

    show emory frown

    c "She's out of town right now- no, she was. She was visiting her brother a couple hours away for a week but she should be coming back today."

    e up frowntalk "Cordelian! What if we can get her on our side?"
    e "She could convince the king otherwise."

    show emory frown

    c "{i}Our{/i} side? [pname], you're not the one being forced to marry someone."

    e down frowntalk "You act like you're the only one affected by it!"
    e "Cordelian, don't you- don't you realize..."
    e sad "I... I thought... after all this time..."

    show emory frown

    c "Don't I realize {i}what{/i}?"

    hide emory
    hide emorytint

    menu:
        "Kiss him":
            en "I quickly lean down and kiss him on the lips. Even if he wanted to react, he's too stunned to."
            en "I close my eyes and immediately realize I've never kissed anyone before. And now I'm kissing my best friend. The prince. Oh God."
            en "All the times I've been here... all the years I've spent with him..."
            en "What an idiot."

            $ renpy.pause(1.0)

            c "..."
            if pname == "Emory":
                c "E-Emory..."
            else:
                c "[pname]..."

            e "I-I thought that... maybe you had at least an inkling of an idea..."
            c "I did- I mean, I do, it's just..."
            c "I... just... I haven't had time to consider it recently..."
            c "There have been other things on my mind lately, you know..."
            c "Maybe... Maybe after all of this is over..."
            e "..."
            c "Please- please don't look at me like that."
            en "He clasps his hands on mine, giving me a pleading look."
            c "If the circumstances were different, perhaps, but I can't dream of that right now. Not when I'm still engaged."
            e "...I understand."
            en "He gently lifts my hand and lightly kisses it. Please don't play with my heart like this."
            e "Shouldn't it be my kissing your hand, your Highness?"
            c "I think you've done enough kissing for one day."
            en "He presses his forehead against mine."
            c "Maybe another day."

        "Call him an idiot":
            e "You're an idiot! That's what!"
            c "What for-?!"
            e "For a lot of things I can think of!"
            e "Wanting to go through all of this, not listening to your own feelings, not listening to my feelings-"
            c "{i}Your{/i} feelings? Again, I didn't know you had an arranged fiancée behind your back!"
            e "And I didn't know a person almost married could be so blind to the thought of someone liking him!"
            c "Oh, please, Katherine doesn't-{w=0.5}{nw}"
            c "..."
            c "[pname]... you..."
            e "You're so daft... spent all that time studying law and economics but can't even understand others..."
            c "I... I didn't realize... I'm sorry..."
            en "He caresses my hands and leans slightly closer."
            en "Please don't get too close. Your obliviousness hurts enough as it is."
            c "I've been focused so intensely on the wedding and the war, I've been ignoring you..."
            c "I'm sorry."
            c "I wish... I wish this could all be over with... you've had time to figure out your feelings, but I haven't yet..."
            e "We'll get you out of this. And then... you can figure out your feelings."
            c "Won't you help me?"
            e "It took me forever just to get it through your head how I feel."
            c "But you help keep me level-headed. With you by my side, I could probably even end this war."
            e "Now you're just saying whatever comes to mind first to make me feel better."
            c "Is it working?"
            e "No, not really."
            c "Then... maybe..."
            en "He closes his eyes and it takes a second too late to realize why."
            en "His soft lips press against mine while one of his hands rests on my neck, keeping me close."
            en "Our lips part but in a small act of selfishness I lean closer for one last kiss."
            c "There."
            e "There?"

    e "You know, they definitely didn't teach you how to kiss before having you engaged."
    c "Wh-What is that supposed to mean-?!"
    e "I thought you had kissed Katherine before for the papers?"
    c "I-- I might have..."
    e "Oh dear."
    c "Oh dear?!"
    e "You could have always asked to practice on me."
    c "I-I don't see myself ever doing that..."
    c "...And besides, you're not an amazing kisser either."
    e "..."
    c "Maybe... maybe we can learn together once I don't have a wedding to attend in just a few days."
    en "I squeeze his hand."
    e "For now... I think it's about time you go see your mother."

    scene bg castleinside1
    with fadee

    king "You're falling for these dillusions too, Morgan?"
    queen "Henry, if he was simply trying to get out of commitment he would have voiced his concerns long ago. Look at him."
    queen "Is this forced marriage really worth the happiness of our son? Will this really aid us that much in the long run?"
    king "Listen to yourself! You agreed to this not long ago!"
    queen "I know, I know-"
    king "We made a deal!"
    queen "Deals can be changed!"
    queen "They're our allies- we can barter for something else such as lowered tariffs or taxation!"
    queen "Why must you insist we barter with {i}lives{/i}?"
    king "You were fine with that just last week!"
    queen "And now I've come to my senses!"
    












label katherineroute:
    e up frowntalk "Katherine, would you mind walking with me to the garden? When I was walking by, some of the maids were fussing over what color your dress would be."

    show emory frown

    k frowntalk "Yes, sure."

    show katherine frown

    scene bg garden
    with fade

    en "I have to see what she's thinking."
    
    show emory up frown at closerleft
    show katherine up smile at closerright:
        yalign 0.4
        zoom 1.1
    with dissolve

    k talk "It's a lovely day out, isn't it?"

    show katherine smile

    e talk "Yes, it is."

    show emory smile

    k frowntalk "...[pname], I don't see the maids you were talking about."

    show katherine frown

    e sad frowntalk "Katherine..."
    e "I wanted to talk to you. Alone."

    show emory frown

    menu:
        "I'm worried about you.":
            e frowntalk"I'm just... I'm worried about you."
            show emory frown
            k frowntalk "Worried about me...? Why?"
            show katherine frown
            e frowntalk "Are you- are both of you alright?"
            e "Today, at lunch... you both seemed so- so distant."
            show emory frown
            k frowntalk "We're fine, really."
        "Is everything alright?":
            e frowntalk "Is everything alright?"
            e "With... you know, the wedding and all."
            show emory frown
            k frowntalk "Of course it is."

    k "It's all going to plan- well, aside from the daffodils being rained on, that is. Marco was in such a fuss, I feel so bad for him."
    k "It'll go off without a hitch, I'm sure."

    show katherine smile

    e frowntalk "I'm sure it will too, but... that's not what I meant."
    e "Katherine, if there's anything on your mind, anything you want to talk about... I'm here."

    show emory frown

    k talk "Thank you [pname], that's really sweet of you."

    show katherine smile

    e frowntalk "That includes, of course, any wedding troubles."

    show emory frown

    k frowntalk "I already told you everything is alright with the wedding."
    k "Why do you keep persisting?"

    show katherine frown

    e frowntalk "Because-"
    e "I know I haven't known you as long as Cordelian has, but I do know something- you're both a lot more alike than you know."
    e "Cordelian could be bleeding from his arm and still insist that someone else needed bandages for their papercut more than he needed them."

    show emory frown

    k frowntalk "Thats... a very colorful and specific analogy..."

    show katherine frown

    e frowntalk "What I mean by it is that Cordelian refuses to ask for help. It's not him trying to act macho- okay, maybe a tiny bit- but instead it's his way of trying to not be in anyone's way."
    e "He thinks he's being helpful by not asking for help."
    e "Katherine... you're somewhat like that, aren't you?"
    e "If you have any concerns about the marriage- not the wedding, the marriage- then please... I'm here."

    show emory frown

    k "..."
    k frowntalk "[pname]..."
    k "What would you do?"
    k "If you were told this was something you had to do for the better of everyone else... that it's selfish to not do so..."
    k "That you're the only one who can do so, so you have to do it..."

    show katherine frown

    e frowntalk "Katherine..."

    show emory frown

    k frowntalk "Cordelian... he's really nice, isn't he?"
    k "I'm sure... I'm sure it'll be fine..."

    show katherine frown

    e frowntalk "Katherine...!"
    e "If you don't want to get married, just say so! If you tell me, I can help you-{w=0.5}{nw}"

    show emory frown

    k frowntalk "Help me what? Help me not do the only thing I can do?"
    k "I'm the only one who can do this."
    k "So... "
    extend "please..."
    k "Don't give me hope."

    show katherine frown

    hide katherine with dissolve

    en "She slumps down- still somewhat gracefully, naturally- on a concrete bench."
    e frowntalk "Katherine."
    e "I don't want to hear any more of this despair talk. I just want answers."
    e "Why is the marriage so important? What will it solve that nothing else can?"
    e "Tell me in your own words... and what you were told."
    e "If no one else will listen to it, then I will."

    show emory frown

    show katherine sad frown at closerright:
        yalign 0.4
    with Dissolve(1.0)

    k "..."
    k frowntalk "The marriage... my father told me it would unite our kingdoms."
    k "Dersion- I hate to admit it, but even Cordelian knows it- isn't strong enough to fight of Leodipia alone."
    k "Sharan might be able to fight them off by itself, but it'd be a long and terse fight."
    k "My father arranged for a deal with Cordelian's father. In exchange for protection from Leodipia, I would marry Cordelian."
    k "The king... he always wanted Cordelian to marry back into royalty. It was a perfect deal for them both."
    k "Without the marriage, I don't know if Sharan would protect us."
    k "Cordelian would certainly try, but we need something stronger than \"trying\"...."

    show katherine frown

    en "That's true..."







label marcolisia_commonroute:

    scene bg bedroomday
    with fade

    show emory up smile at closeleft
    show lisia down smile at closeright
    with dissolve

    e talk "I can't believe the wedding is tomorrow!"

    show emory smile

    l talk "Me neither. It seems just like yesterday that we first heard about Katherine."

    show lisia smile

    e talk "You've grown close to her over the past week, though."

    show emory smile

    l talk "She's really nice if you get to know her."

    show lisia smile

    e frown "Hmm."

    show lisia frown
    
    e frowntalk "What are you wearing to the party tonight?"

    show emory frown

    l frowntalk "Well..."

    show lisia frown

    e frowntalk "What is it?"

    show emory frown

    l frowntalk "I'm not going, [pname]."

    show lisia frown

    e down frowntalk "What? Why not?"

    show emory frown

    l frowntalk "Your mother forbade me from going."

    show lisia frown

    e frowntalk "Did she really? Do you know why?"

    show emory frown

    l frowntalk "I... I think she doesn't like the servants, that is, Marco and me, spending too much time around you and the other nobles."

    show lisia frown

    e frowntalk "But that's ridiculous, Lisia! You're our friend!"
    e "I'm going to have a word with mother."

    show emory frown

    l frowntalk "[pname], what if she gets angry at you?"

    show lisia frown

    e frowntalk "It's better than not trying."

    show emory frown

    scene bg castionmanorinside
    with fade

    show emory up frown at left
    show mother up frown at right
    with dissolve

    e frowntalk "Mother, could I speak to you?"

    show emory frown

    mother talk "Oh, of course dear! Are you ready for the ball?"

    show mother smile

    e frowntalk "I am, but that's not what I wanted to talk about."

    show emory frown

    mother talk "Alright, what is it?"

    show mother frown

    e down frowntalk "Why are you not allowing Lisia to come with us?"

    show emory frown

    mother down frowntalk "[pname], how could you ask that?!"
    mother "She is a servant. She has no place at a ball!"

    show mother frown

    menu:
        "She's my friend.":

            e frowntalk "She is my friend."

            show emory frown

            mother frowntalk "Then you need to find better friends."
            

        "I don't care.":

            e frowntalk "I don't care. I want her to go."

            show emory frown

            mother frowntalk "I frankly have to disagree."

    show mother frown

    e frowntalk "I'm sure Cordelian would disagree with you. I've seen how he treats Marco."
    e "And I know for a fact, that Marco will be at the ball."

    show emory frown

    mother frowntalk "When I say no, I mean it."

    show mother frown

    e frowntalk "In that case, I'm not going either."

    show emory frown
    show mother frown at center with moveinright

    mother frowntalk "[pname], don't test my patience. You will come to the party with us."

    show mother frown

    e frowntalk "I will, but only if Lisia comes too."

    show emory frown

    mother frowntalk "Stay at home then! Cordelian will be disappointed and ashamed of you."

    show mother frown

    e frowntalk "I doubt he'll be ashamed. Good evening, mother."

    show emory frown

    hide emory frown with moveoutleft

    scene bg emorystudy
    with fade

    show lisia down smile at right
    show emory down frown at left
    with dissolve

    l frowntalk "Well, how did it go?"

    show lisia frown

    e frowntalk "I'm sorry, Lisia..."

    show emory frown

    l frowntalk "Oh. That's alright. Don't worry about it. At least you tried. Thank you."
    l "You should get going, or you'll be late."

    show lisia frown

    e up frowntalk "I'm not going either."

    show emory frown

    l frowntalk "What are you talking about, [pname]? It's your best friend's pre-wedding celebrations! You have to go."

    show lisia frown

    e frowntalk "I don't, actually. I've already sent a message to him, and he was quite understanding."

    # TODO knocking sound here

    show emory up frown at left
    show lisia down frown at center
    show marco up smile at right
    with moveinright

    m talk "May I intrude?"

    show marco smile

    l up talk "Oh hello, Marco."

    show lisia smile

    e talk "He's here to spend some time with us. The party was obviously boring."

    show emory smile

    l down talk "I'm sure it wasn't, but thank you all the same."

    show lisia smile

    m talk "Sure."
    m "So, any ideas on what to do?"

    show marco smile

    e talk "Lisia and I were just chatting, but maybe we should do something else."

    show emory smile

    m talk "You play the violin, don't you, [pname]?"

    show marco smile

    e frowntalk "I do. What does that have to do with anything?"

    show emory frown

    m talk "Well, Lisia here can sing very well."

    show marco

    e unsure frowntalk "She can? Why did you never tell me this, Lis?"

    show emory frown

    en "I suppose she does like to hum a lot while cleaning..."

    l frowntalk "I suppose... it never came up..."
    l "And I'm not very good either..."

    show lisia smile

    e up talk "Pfft! Quit being so modest. Marco can play the piano and I can play the violin, so let's have some fun!"

    show emory smile

    l talk "I don't know..."

    show lisia smile

    m talk "Well, I suppose I'll walk all the way back to the castle then..."

    show marco frown

    l talk "Oh, okay."

    show lisia smile

    # TODO knocking sound here too

    # *music*
    # *knocks*

    e frowntalk "Huh?"

    show emory frown
    show marco frown

    l down frowntalk "No one should be here now..."
    l "Could it be robbers?"

    show lisia frown

    m frowntalk "Of course not!"

    show marco frown

    e unsure frowntalk "The rest of the staff has the evening off, too."
    e "I must admit, I am a bit scared."

    show emory frown

    m frowntalk "I'll open it. You two stay put."

    show marco frown

    l frowntalk "Be careful."

    show lisia frown

    m frowntalk "Please, it's nothing."

    scene bg castionmanorinside
    with fade

    show mother down frown at left:
        xzoom -1
    show marco up frown at rightt
    with dissolve

    # TODO emory's last name
    m talk "Good evening Lady (surname)."

    show marco smile

    mother talk "What are you doing here, Marco?"
    mother "Shouldn't you be at the party?"

    show mother smile

    m talk "I received permission from Cor-His Highness to come here and spend the evening."

    show marco smile

    mother frowntalk "And he was...amiable to it?"

    show mother frown

    m talk "Yes, Ma'am."

    show marco frown

    mother frowntalk "It seems I must speak to the Prince about what is acceptable behavior."
    mother "I am certainly very disappointed in him."

    show mother frown

    hide marco
    show mother at center:
        xzoom 1
    show emory up frown at left
    show lisia down frown at right
    with moveinleft

    e frowntalk "Good evening, mother."

    show emory frown

    mother frowntalk "[pname]."

    show mother frown

    e frowntalk "I couldn't help but overhear what you were just saying to Marco."

    show emory frown

    mother frowntalk "Surely, I have taught you better than to eavesdrop on others? In any case, this one did pertain to you."
    mother "I can hardly believe that you stayed back to spend time with the servants."

    show mother frown

    e frowntalk "I will tell you again, mother. They are my friends."

    show emory frown

    mother down frowntalk "And yet, they work here as our servants."
    mother "Perhaps if their friendship is so precious to you, then they can stop being paid."

    show mother frown
    show emory down

    l frowntalk "Please... Please, don't do that."

    show lisia frown

    e frowntalk "Mother, you can't!"

    show emory frown

    mother frowntalk "Do not test my patience, [pname]."

    show mother frown

    e sad frowntalk "I..."

    show emory frown

    mother frowntalk "Enough!"
    mother "Lisia, go to the kitchens. I'm sure there must be some work there."
    mother "And Marco, you will leave for the castle immediately."

    show mother frown

    hide lisia
    show marco down frown at right
    with moveinright

    m frowntalk "With all due respect, ma'am, you are not my employer."
    m "I am not obliged to listen to you."

    show marco frown

    mother frowntalk "How dare you! The king and queen will hear about this."

    show mother frown

    m frowntalk "I'm sure they will, ma'am. In the meantime, it is Lisia's evening off, so she may do as she wants as well."

    show marco frown

    mother "!!!"

    hide marco
    show lisia down frown at right
    with moveinright

    l frowntalk "Marco, perhaps I should just..."

    show lisia frown

    e frowntalk "No, Lisia, you can stay here."

    show emory frown

    mother frowntalk "Lisia, I told you to leave!"

    show mother frown

    hide lisia
    show marco down frown at right
    with moveinright

    m frowntalk "That hardly seems fair, Lady (surname)!"

    show marco frown

    mother frowntalk "I think you both need to learn your place."
    mother "You both have corrupted [pname] as well!"

    show mother frown

    e frowntalk "That's not true, I'm here of my own accord."

    show emory frown

    mother frowntalk "We will have this discussion later, [pname]."
    mother "I am returning to the ball, and I don't want to see any more of this nonsense when I come back."

    show mother frown

    hide mother
    with moveoutleft

    show lisia down frown at center with dissolve

    e sad frown "..."
    e frowntalk "I... I'm sorry about that."

    show emory frown

    l frowntalk "It's alright..."
    l frown "..."

    show marco up frown

    m frowntalk "It will all be fine, Lisia."

    show marco smile

    l talk "Yeah..."

    show lisia smile

    m talk "With that, I'll be off. I'll see you both bright and early tomorrow, right?"

    show marco smile

    e up talk "Yes, definitely."

    show emory smile

    hide marco
    with dissolve

    e talk "Come on Lisia. It's going to be a big day tomorrow."

    show emory smile




    #####################################################################################################
    #####################################       Wedding day         #####################################

    show emory up smile at closeleft
    show lisia up smile at closeright
    with dissolve

    e blush talk "Oh!"

    show emory smile

    l talk "Good morning, [pname]."

    show lisia smile

    e talk "I almost didn't recognise you, Lisia!"

    show emory smile

    l blush talk "Ummm..."

    show lisia smile

    e talk "I mean, you really look wonderful!"
    e "You just took me by surprise."

    show emory smile

    l talk "Ah. You look... nice too, Emory."
    l "Your father is calling you downstairs."

    show lisia smile

    e unsure talk "Is it time already?"
    e "So soon?"

    show emory -blush smile

    l -blush talk "It is! Are you excited?"

    show lisia smile

    e talk "Somewhat, I suppose. I'm a bit nervous too."
    e "I hope nothing goes wrong."
    e "We've all planned for so much and... well."

    show emory smile

    l talk "I'm sure Marco has it all under control."

    show lisia smile

    e talk "Knowing him, you're right."
    e "I'm glad Cordelian chose him to be the Best Man. Even if his parents weren't exactly thrilled."

    show emory smile

    l talk "He does deserve it, after all the work he has done!"
    l "Perhaps you should head downstairs now..."

    show lisia smile

    e talk "Right. Of course."

    
    #####################################       After the Wedding

    scene bg ballroom
    with fade

    show emory up smile at leftt
    show cordelian up smile at rightt
    with dissolve

    e talk "I can't believe it's over."

    show emory smile

    c talk "Over? Pfft, Emory. The ceremony is over but the ball has just begun!"

    show cordelian smile

    e unsure talk "I did mean the ceremony..."
    e "And I still can't wrap my head around the fact that my best friend is married."
    e "How does it feel?"

    show emory up smile

    c talk "It is a bit overwhelming, to be honest."
    c "Though, my father assures me I will get used to it."

    show cordelian smile

    e talk "Where's Katherine anyway?"

    show emory smile

    c talk "Oh, she's over there with her parents. They're leaving in a week, you know."

    show cordelian smile

    e frowntalk "So soon?"

    show emory frown

    ## attacking country- Leodipia
    c down frowntalk "Yes... I believe they are having some issues with the threats from Leodipia."
    c "Besides, they need to settle on how we are going to unite the kingdoms."

    show cordelian frown

    e frowntalk "I hear it's a long process, something like that."

    show emory frown

    c frowntalk "Yes, well. "
    c up talk "But onto more pressing matters, who are you going to dance with?"

    show cordelian smile

    e down frowntalk "That is not a pressing matter, Cordelian."

    show emory frown

    c talk "I think it most certainly is!"
    c "I am not going to allow my best friend to mope in a corner at my wedding!"

    show cordelian smile

    e unsure talk "I'm really alright, Cordelian."

    show emory smile

    c talk "Come on, Emory. Pick a partner."

    show cordelian smile

    menu:
        "Lisia":
            $ partner = "lisia"
        "Marco":
            $ partner = "marco"

    if partner == "lisia":
        e talk "I wonder if Lisia is still here?"

        show emory smile

        c talk "Ah! I knew it! There is something there!"

        show cordelian smile

        e frowntalk "What are you talking about?"
        e "I was only going to ask her because she does not know many people here and..."

        show emory frown

        c talk "Of course you were. Well, go on then!"

        show cordelian smile

        hide cordelian with moveoutleft

        $ renpy.pause(1.0)

        show lisia up smile at rightt with moveinright
            
        e talk "Lisia?"

        show emory smile

        l talk "Oh, hello [pname]."

        show lisia smile

        e talk "Are you enjoying yourself?"

        show emory smile

        l down talk "I suppose..."
        l "I mean, the food is nice."

        show lisia smile

        e talk "That's good to hear..."
        e blush "I was wondering... if you'd like to dance with me?"

        show emory smile

        l blush up frowntalk "Dance... with... you?"

        show lisia frown

        e talk "Yes?"

        show emory smile

        l down talk "I'm a terrible dancer."

        show lisia smile

        e talk "I'm sure you are not."
        e "Come on!"

        show emory smile

        l frowntalk "I... well... oooh!"

        show lisia up frown at closeright
        show emory at closeleft

        e talk "See? You're doing great!"

        show emory smile

        l frowntalk "I'm not so sure."

        show lisia frown

        e talk "There aren't any rules to dancing, you know."
        e "Just try to enjoy yourself."

        show emory smile

        l down frowntalk "Umm, okay..."

        show lisia frown

        hide lisia
        hide emory
        with dissolve

        $ renpy.pause(2.0)

        show lisia blush up smile at closerright
        show emory blush up smile at closerleft
        with dissolve
            
        e talk "Well? Wasn't that fun?"

        show emory smile

        l talk "Yes, it was. You were right."
        l "Emory..."

        show lisia smile

        e "Hmm?"

        l talk "Thank you."

        show lisia smile

        e talk "Of course! It was nothing."

        show emory smile

        l talk "You're a good friend."
        l "Thank you!"

        show lisia smile
            
        c talk "I knew it!"

    if partner == "marco":
        e talk "Have you seen Marco around?"

        show emory smile

        c talk "Marco? Hmm..."
        c "That's interesting..."

        show cordelian smile

        e frowntalk "What is?"

        show emory frown

        c talk "Nothing at all- Look, there he is!"
        c "Go on then! Ask him to dance."

        show cordelian smile

        e frowntalk "I doubt he'll agree, Cordelian."

        show emory frown

        c talk "The least you could do is try!"
        c "Come on!"

        show cordelian smile

        e talk "Alright, then."

        show emory smile

        hide cordelian with moveoutleft

        $ renpy.pause(1.0)

        show marco up smile at right with moveinright
            
        e talk "Marco?"

        show emory smile

        m talk "Yes, [pname]? Is there something you'd like?"

        show marco smile

        e talk "I was simply checking in on you."

        show emory smile

        m frowntalk "Why?"

        show marco frown

        e talk "Because I wanted to see if you were having fun?"

        show emory smile

        m frowntalk "I have quite a few responsibilities here."

        show marco frown

        e talk "That wasn't what I asked, you know."
        e "You need to loosen up for a while."
        e "It's meant to be a celebration."

        show emory smile

        m frowntalk "Thank you for your concern, but I am fine here."
        m "Maybe you can go back to talking with Cordelian, since you're starting to sound just like him."

        show marco frown

        e frowntalk "You don't sound fine..."
        e talk "Would you like to dance with me?"

        show emory smile

        m frowntalk "I'm sorry?"

        show marco frown

        e blush talk "I asked if you would like a dance-"

        show emory smile

        m down frowntalk "I... I can't..."
        m frown "I don't dance."

        show marco frown

        e talk "It's easy, really. You don't have to do much."
        e "I'll show you."

        show emory smile

        m blush up "What are you- oooh!"

        show marco frown at closerright
        show emory smile at closerleft

        e talk "Fun, isn't it?"

        show emory smile

        m frowntalk "I suppose..."

        show marco frown

        e talk "Admit it, Marco."
        e "Aren't you enjoying yourself? At least a little bit?"

        show emory smile

        m talk "...I am."
        m "You're a good dancer."

        show marco smile

        e talk "Only because mother insisted on my having lessons as a child."

        show emory smile

        m talk "She did? I don't seem to remember..."

        show marco smile

        e talk "Yes, it was a long time ago, I believe. Before I was close to Cordelian, even."
        e "But you're dancing better than me! So much for not being able to dance!"

        show emory smile

        m talk "It is... one of my guilty pleasures, I'll admit."

        show marco smile

        e talk "Aren't you glad I asked you?"

        show emory smile

        m talk "Yes..."

        show marco smile

        hide marco
        hide emory
        with dissolve

        $ renpy.pause(2.0)

        show marco blush up smile at closerright
        show emory blush up smile at closerleft
        with dissolve
            
        m talk "Thank you for that, Emory."
        m down "I know your mother disapproves of you spending time with Lisia or me..."

        show marco smile

        e talk "Oh, nevermind her! See? Even she is too happy to be scolding me today."

        show emory smile

        m talk "I noticed that..."
        m "You are a good friend to me."

        show marco smile

        e talk "Of course!"
        e "You are too, to all of us."
        en smile "Even if you don't like admitting it..."


    #####################################       Post-Wedding        ####################################

    scene bg emorystudy
    with fade

    show lisia up frown at rightt
    show emory up smile at leftt
    with dissolve

    l frowntalk "Emory, can I talk to you?"
    l down "Oh, wait. You look busy. Nevermind, then."

    show lisia  frown

    e talk "Oh no, it's nothing at all."
    e unsure "I was just trying to study, but I can't seem to concentrate today."

    show emory smile

    l frowntalk "I wanted to talk to you... about my father."

    show lisia frown

    e frowntalk "Your father? But I thought he was..."

    show emory frown

    l frowntalk "He might be. I really don't even know."

    show lisia frown

    e frowntalk "Hmm? What do you mean?"

    show emory frown

    l frowntalk "Well, I never really saw him."
    l "And my mother has never spoken about him, either."

    show lisia frown

    e sad frowntalk "Oh."
    e "I'm sorry."
    e "But... why are you telling me this?"

    show emory frown

    l frowntalk "I wanted your help, actually."

    show lisia frown

    e frowntalk "Help with what?"

    show emory frown

    l frowntalk "Looking for him."

    show lisia frown

    e frowntalk "You want to find him? But he could be anywhere in this entire world!"

    show emory frown

    l up frowntalk "Not quite anywhere. He apparently was part of this guild in town. Before he... well."

    show lisia frown

    e frown "I... Oh. I didn't know."

    show emory frown

    l frowntalk "That is why I need you to help me with this."
    l talk "So, will you?"

menu:
    "Yes, of course I will!":
        $ lisia += 1
        $ help_lisia = "yes"
    "I'm sorry, I needed to go see Marco about something...":
        $ marco += 1
        $ help_lisia = "no"

        
if help_lisia == "yes":
    e up talk "Yes, of course I will!"
    e "I'd love to help you."

    show emory smile

    l talk "I was hoping you'd say that!"
    l "I think I know where to begin."

    show lisia smile

    e frowntalk "You do?"

    show emory smile

    l talk "Yes! Among the few things I do know about my father, I also know that he apparently gifted this to me before he left. My mother gave it to me."

    show lisia smile

    e frowntalk "Is that a brooch?"

    show emory smile

    l up talk "A badge, actually."
    l "It has the symbol of his guild, right here, see?"

    show lisia smile

    e frowntalk "But, why did he give it to you?"

    show emory smile

    l frowntalk "I... I'm not sure."
    l "My mother thought that, perhaps, he expected I would be a part of this guild too."

    show lisia smile

    e talk "Well, will you?"

    show emory smile

    l frowntalk "I don't know yet, Emory."
    l "I haven't really been trained in it, you see."
    l "And I hear they only take the best of the best, though what they do exactly is kept very secret."

    show lisia smile

    e talk "Ah yes, I've heard that too."
    e "But you know, if you wish, I could help you train for swordsmanship."

    show emory smile

    l talk "Perhaps, one day."
    l "Thank you for offering."

    show lisia smile

    menu:
        "Don't thank me, we're friends.":
            $ lisia_friendss = "yes"
        "Of course, any time.":
            $ lisia_friendss = "no"

    if lisia_friendss == "yes":

        e talk "Don't thank me! We are friends, aren't we?"

        show emory smile

        l down talk "I... yes."

        show lisia smile

        e talk "And that is what friend's do!"

    if lisia_friendss == "no":

        e talk "Of course, any time."

    show emory frown

    mother "Lisia! Lisia! Come here right now!"

    l down frowntalk "Oh no! I must leave, Emory."

    show lisia frown

    e "*sigh*"
    e sad frowntalk "Yes, you better."
    e "I would not want you to get into trouble with my mother again."
    e up talk "But day after tomorrow, meet me at noon."

    show emory smile

    l up frowntalk "Why?"

    show lisia smile

    e talk "We'll go look for some clues about your father, of course."

    show emory smile

    l talk "Thank you! Now, I must run!"

    show lisia smile

    hide lisia with moveoutleft

    en "Well, day after tomorrow should be fun."

if help_lisia == "no":
    e frowntalk "I'm sorry, I needed to go see Marco about something..."

    show emory frown

    l frowntalk "Of course. I understand."

    show lisia frown

    e frowntalk "I'm sorry, Lisia."

    show emory frown

    l frowntalk "It's alright, really! Bye, Emory!"

    show lisia frown

    e frowntalk "Bye!"

    show emory frown

    hide lisia with moveoutleft

    hide emory with dissolve

    en "That was so terrible of me..."
    en "But I am afraid of what my mother will do if she finds out that I am helping Lisia."
    en "But she is my friend, after all. And I do want to help."
    en "Perhaps I should... tell Marco to help her too?"
    en "Yes, that will do quite well I think."
    en "I really hope I haven't hurt Lisia..."

    scene bg garden
    with fade

    show marco up frown at closeright
    show emory up smile at closeleft
    with dissolve

    e talk "Marco!"

    show emory smile

    m frowntalk "Oww!"

    show marco frown

    e frowntalk "Oh, everything alright?"

    show emory frown

    m frowntalk "No, you made me prick myself on a thorn..."

    show marco frown

    e down talk "Oops. Sorry, Marco."

    show emory up smile

    m frowntalk "It's... it's alright."
    m "Did you need anything?"

    show marco frown

    e talk "What? Can't I simply visit my friend without needing anything?"

    show emory smile

    m "..."
    m frowntalk "Considering how rarely you do..."

    show marco frown

    e frowntalk "Oh, alright, alright. I just wanted to talk to you about..."

    show emory frown

    m frowntalk "Yes?"

    show marco frown

    e talk "Lisia."

    show emory smile

    m down frowntalk "{i}Of course you did...{/i}"

    show marco frown

    e up frowntalk "Huh? Did you say something?"

    show emory frown

    m frowntalk "No."
    m up "Anyway, Lisia? What about her?"

    show marco frown

    e frowntalk "Do you know anything about her father?"

    show emory frown

    m frowntalk "He disappeared years ago, I heard."
    m "He was quite high up in his guild, wasn't he?"

    show marco frown

    e frowntalk "You knew about the guild?"

    show emory frown

    m frowntalk "She told me he was in it, once. And I'd seen her carry the badge. It bore the marks of a higher up of the guild."
    m "As for the guild itself... Most know Dominic Randolph essentially ruled it."

    show marco frown

    en "Marco knows a lot about guilds... why?"
    e frowntalk "Who is he, then? This Dominic Randolph?"

    show emory frown

    m frowntalk "He is, or rather, was a master swordsman. The king trusted him immensely."
    m "Supposedly, he suddenly gave it all up one day."
    m "Decided to become a trader and sailed away across the sea."

    show marco frown

    e frowntalk "Did he ever come back?"

    show emory frown

    m frowntalk "Not that anyone knows of, no."
    m "But, why this sudden interest?"

    show marco frown

    e frowntalk "Well... Lisia may have asked me to help her..."

    show emory frown

    m frowntalk "With?"

    show marco frown

    e frowntalk "Finding her father."

    show emory frown

    m frowntalk "He's been gone for years, Emory."

    show marco frown

    e frowntalk "I know... And when she asked me, I wasn't sure what to do."
    e "So, I told her I needed to come meet you!"

    show emory frown

    m frowntalk "And she believed you?"

    show marco frown

    e frowntalk "Of course she did! Why wouldn't she?"

    show emory frown

    m frowntalk "No reason."
    m "Well, if you are done questioning me, then perhaps I can go back to these roses."

    show marco frown

    e frowntalk "Oh, sorry. Am I distracting you too much?"

    show emory frown

    m frowntalk "Not exactly. But I do need to get this done and head back to the castle."

    show marco frown

    e frowntalk "Oh. Of course."

    show emory frown

    m talk "Goodbye, [pname]."

    show marco frown

    e talk "Good luck with your roses!"

    show emory smile

    hide emory
    hide marco
    with dissolve

    en "Was it just me or did Marco sound a bit... bitter?"


label marcolisia_commonroutecontinued:

    ####################### TODO I have no clue where this scene with Marco goes

    scene bg garden
    with fade

    show emory up smile at left
    show lisia up smile at center:
        xzoom -1
    show marco up frown at right
    with dissolve

    e talk "So, how long are you going to spend cooped up in this greenhouse?"

    show emory smile

    m frowntalk "As long as it takes for me to plant all these crocus bulbs."
    m "You both seem to have made it your personal goal to make my task harder, however."

    show marco frown

    l down talk "It's not like that, Marco..."

    show lisia smile

    m frowntalk "It certainly seems like it to me."

    show marco frown

    e frowntalk "You need to get out more, you know."
    e "I know you love this garden, but you almost never leave the castle grounds."

    show emory frown

    m frowntalk "Has it ever occured to you that I don't want to?"

    show marco frown

    e frowntalk "Well, why not? The city is gorgeous and villages at the outskirts are even better."

    show emory frown

    m frowntalk "I would prefer to work here, thank you very much."

    show marco frown

    l talk "Please, Marco?"
    l "Wouldn't it be fun to have an adventure once in a while?"

    show lisia smile

    m frowntalk "You say that with all the enthusiasm of a child in a sweet shop."
    m "\"Adventures\" don't just happen."
    m "And when they do, they're often dangerous."
    m "I'd rather stay here."

    show marco frown

    e frowntalk "Well, we do have an adventure waiting, actually."
    e "I told you about Lisia's father, remember?"
    e talk "You could come to the city with us and help us make enquiries!"

    show emory smile

    m frowntalk "You're persistent."

    show marco frown

    l frowntalk "You're stubborn..."

    show lisia frown

    m frowntalk "...Alright."
    m "Give me a few minutes to finish up."

    show marco frown

    e talk "Of course!"
    en smile "I can't believe we convinced him!"


    scene bg city
    with fade

    show emory up smile at left
    show lisia up smile at center:
        xzoom -1
    show marco up frown at right
    with dissolve


    m frowntalk "Where were you planning to begin?"
    m "Or did you come here with the purpose of wandering the market aimlessly?"

    show marco frown

    e talk "Cheer up a bit, Marco! Isn't it a lovely day?"

    show emory smile

    m frowntalk "Yes, it is. A lovely day I would rather spend planting crocus bulbs..."

    show marco frown

    l frowntalk "I'm sorry you find this an inconvenience, Marco."
    l "We just thought it would be nice to spend some time with you. And this search will be easier with more people helping out."

    show lisia frown

    e unsure talk "Look, both of you!"

    show emory frown

    l frowntalk "What is it, Emory?"

    show lisia frown

    e talk "That sign over there!"

    show emory smile

    m frowntalk "It says Windglade..."
    m "That would be your father's guild, Lisia."

    show marco frown

    l frowntalk "It... is?"

    show lisia frown

    e up talk "Well? What are we waiting for? Let's go!"

    show emory smile

    m frowntalk "Do you plan to simply barge in there and demand answers?"

    show marco frown

    e sad frowntalk "I... err..."
    en frown "I actually hadn't thought about that..."
    e up frowntalk "Do either of you have any ideas, then?"

    show emory frown

    l talk "I do, actually."
    l "I was hoping we could tell them we wanted to join their guild. Perhaps they might tell us something important if we strike up a conversation."

    show lisia smile

    m frowntalk "...I have my concerns but that's most likely the best option on such short notice. [pname]?"

    show marco frown

    e talk "Of course! It's a great idea. Alright."

    show emory smile


    scene bg guild
    with fade


    show emory up smile at left
    show lisia up smile at center
    show marco up frown at right
    with dissolve


    e frowntalk "Hello? Excuse me?"

    show emory smile

    l frowntalk "Erm... is anyone here?"

    show lisia frown

    na "YES?"

    show lisia frowntalk
    show emory frowntalk

    el "Ahh!"

    en "Where did this man suddenly come from?"

    show lisia frown
    show emory frown

    m talk "Good morning, sir."

    show marco smile

    gm "You young ones shouldn't be here. Who are you?"

    m talk "We have heard a lot about your guild, sir, and we were hoping to join it."

    show marco smile

    e talk "Yes, as my friend here said, we would really love it if you could accept us and show us the ropes."

    show emory smile

    gm "..."

    l talk "...Please, sir. It would really mean a lot to us. We are ready to try our hand at any tasks you assign us."

    show lisia smile

    gm "The guild is highly exclusive in its selection of members. We cannot just accept any... amateurs."

    e talk "Which is why we are ready to prove to you that we are most certainly not amateurs!"

    show emory smile

    l talk "Yes, absolutely!"

    show lisia smile

    gm "I see you are rather stubborn."
    gm "Very well. Follow me, then."

    en "I hope this ends well!"
        
    gm "Sir! We have some... children here, who want to join us."
    gmm "Children?"
    gm "See for yourself, sir."

    en "A stout man walks in, observing us."

    gmm "Ah. You were right, Corbyn. Children it is."
    gmm "So tell me about yourselves. Your names, and why you thought it would be a good idea to walk into one of the most renowned guilds without any clue as to what you are doing."

    $ gmname = "Corbyn"

    m talk "I am-"

    show marco frown

    gm "If I may, sir?"

    gmm "Yes?"

    gm "I see no use in wasting our time with them."
    gm "It would be better so simply...{i} clear them out.{/i}"

    en frown "Oh no... That does not sound pleasant, somehow."

    gmm "I don't disagree, I'm afraid."
    gmm "You were saying, young man?"

    m talk "Yes, well. I am Marco, and these are Lisia and Emory."

    show marco smile

    l talk "It is lovely to meet-"

    show lisia frown
    show marco frown

    gmm "There is no need for pleasantries. Continue. Tell me why you are here."

    l frowntalk "Uh... we heard about this guild and-"

    gmm "There is something you must know about me, girl. I hate lies. And therefore, I am seriously starting to reconsider Corbyn's proposal."

    l down frowntalk "I... umm..."

    show lisia frown

    en "What do I do?"

    menu:
        "Help Lisia and tell the truth.":
            $ lisia += 1
            $ guildmenu = "lisia"

        "Nudge Marco to speak.":
            $ marco += 1
            $ guildmenu = "marco"


    if guildmenu == "lisia":
        e frowntalk "Sir, if you want to know the truth, we are here to look for someone."

        show emory frown

        l frowntalk "Emory, what are you doing?"

        show lisia frown

        e frowntalk "Helping us stay alive."
        e "We knew a member of this guild."
        e "Or rather, Lisia does."

        show emory frown

        gmm "I am listening."

        e frowntalk "We heard he disappeared years ago."
        e "It is very important that we find him."

        show emory frown

        gmm "Is that so?"

        gm "Sir, I propose we get rid of these fools immediately!"

        gmm "Quiet, Corbyn! Let me think."
        gmm "This man, what was his name?"

        l down frowntalk "I... I don't know."

        show lisia frown

        gmm "You don't know the name of this very important man you are looking for?"

        l frowntalk "...my father..."

        show lisia frown

        gmm "What did you say? Speak up, girl!"

        l frowntalk "We are looking for my father. However, my mother refuses to tell me anything except that he once worked here."

        show lisia frown

        gmm "I see. And why should we help you?"

        l frowntalk "Because he helped this guild. He had friends here. He rose up its ranks. He cared."

        show lisia frown

        en up frown "I have never seen Lisia speak so boldly!"

        gmm "Watch your tongue, young girl. Lisia, was it?"

        l frowntalk "Lisia Wenest, sir."

        show lisia frown

        gmm "Wenest?"

        l frowntalk "...yes?"

        show lisia frown
            
    if guildmenu == "marco":

        m talk "Sir. We wish to learn the finest skills from this guild in the art of trading."

        show marco frown

        gmm "I see someone has looked into the workings of this guild."
        gmm "It is not often we get apprentices who actually know what the guild is about."
        gmm "After all, we do pride ourselves on our secrecy."

        en "Trading? Why so much secrecy for something like that?"
        en "And how does Marco know about it, if it is so hush-hush?"

        gmm "Tell me, Marco, how do you know of our guild?"

        m frowntalk "I... once knew someone who was a part of it."

        show marco frown

        gmm "Oh? And who was this member who would so willingly give away our secrets?"

        m frowntalk "He did not give away your secrets, sir. I deduced them myself."
        m "From many different sources, may I add."

        show marco frown

        gmm "You certainly seem resourceful, young man. You would be a good addition to Windglade."
        gmm "However, I am not so certain about your friends."

        e frowntalk "Sir..."

        show emory frown

        m frowntalk "I'm afraid that if I join, so must they."

        show marco frown

        gmm "Then, I am sorry that none of you will be a part of our guild."
        gmm "If there is nothing else you wish to-"

        m frowntalk "Actually, there is."
        m "Can you recognise a member simply by looking at their brooch?"

        show marco frown

        gmm "Yes. Guild brooches have unique markings referring to positions and achievements within the guild."

        l frowntalk "What about... former members?"

        show lisia frown

        gmm "The rules are the same."

        e up frowntalk "Then could you please do one last thing for us?"

        show emory frown

        gmm "What would that be?"

        l frowntalk "Could you tell us who this belonged to? It was my father's, and I don't even know his name..."

        show lisia up frown

        gm "Odd... That looks familiar."
        gm "!!!"
        gm "Sir! This was-"

        gmm "I know."


    gmm "LEAVE!"

    show lisia frowntalk
    show emory down frowntalk

    el "Pardon?"

    show lisia frown
    show emory frown

    gmm "I TOLD YOU TO LEAVE!"
    gmm "Corbyn, show them out."

    m frowntalk "[pname], it is in our best interests to listen to him."

    show marco frown

    e frowntalk "All right, them. Lisia, come on."

    show emory frown

    l frowntalk "But..."

    show lisia frown

    e frowntalk "Please, Lisia. We will find your father. But there is no point in endangering ourselves."

    show emory frown

    gmm "Listen to your friend, girl! He is right."

    l "..."

    gm "This way. Stay behind me."

    m frowntalk "I'm sorry we couldn't be of more help, Lisia."

    show marco frown

    l frowntalk "It's... okay."

    show lisia frown

    e frowntalk "Lisia..."

    show emory frown

    l frowntalk "I just need some time to think quietly. Please."

    show lisia frown

    e frowntalk "Oh. Of course."

    show emory frown

    l "..."
    m down "..."

    en "They both look disappointed..."

    gm "Here we are."

    e up frowntalk "...thank you."

    show emory frown

    gm "Before you leave, there is something I must tell you, young girl."
    gm "Your father, Joseph Wenest, was a brilliant man and a good friend."

    l up frowntalk "You... you knew him?"

    show lisia frown

    gm "Of course! He was the leader of the guild, even young as he was. Before Hugo, who you just met."
    gm "In his time, even kings and nobles used to consult with us..."
    gm "Things have gone downhill since his disappearance."

    l frowntalk "Do you know anything about how he vanished?"

    show lisia frown

    gm "I wish I did. I do hope you find him, however."
    gm "If there is anything you need, please don't hesitate to ask me."

    l talk "Thank you."
    l "It is good to have some knowledge about my father, at least."
    l "Even if it from a long time ago."

    show lisia smile

    m up frowntalk "Could I ask you a question, sir?"

    show marco frown

    gm "Go on."

    m frowntalk "How do I make my way into and up the guild?"

    show marco frown

    gm "!!!"
    gm "You really wish to be a part of it?"

    m frowntalk "Perhaps."

    show marco frown

    gm "Then you have your work cut out for you. You may have impressed Hugo, but there is more to it than that."

    m frowntalk "Such as?"

    show marco frown

    gm "Marco, there are things I cannot reveal at present. Not with... so many people around. [pname], Lisia, it's not that I can't trust you, but-"

    e up frowntalk "No, it's quite alright. We understand."

    show emory frown

    gm "Ah, thank you. However, if you visit again, Marco, preferably alone, then perhaps we can discuss this."

    m frowntalk "Very well. Thank you."

    show marco frown

    gm "My pleasure. You three ought to get going now."

    e frowntalk "He's right. Let's head back."

    show emory frown


    scene bg castleinside3
    with fade

    show emory unsure smile at left
    show lisia down smile at center
    show marco up frown at right
    with dissolve


    e talk "Well. I would not say that was particularly successful. But at least we have some information about your father."

    show emory smile

    l talk "I know his name, [pname]. And that is more than just 'some' information. We have a real lead!"
    l up "It is much easier to look for someone once you know their name!"

    show lisia smile

    e talk "I can't argue with that! Marco, what do you think?"

    show emory up smile

    m "..."

    e unsure talk "Marco?"

    show emory smile

    l up frowntalk "Is everything alright?"

    show lisia frown

    m frowntalk "Huh?"
    m "Of course! I'm fine."

    show marco frown

    e frowntalk "You look a bit off..."

    show emory frown

    l frowntalk "[pname]'s right. What is it? You know you can trust us."

    show lisia frown

    m frowntalk "I already told you, it's nothing!"

    show marco frown

    e frowntalk "But-"

    show emory frown

    mother "[pname]!"

    l down frowntalk "Oh dear."

    show lisia frown

    hide marco with moveoutright

    show mother down frown with moveinright

    e up frowntalk "Mother! What are you doing here at the castle? I thought you would be home!"

    show emory frown

    mother frowntalk "I was, until your tutor informed me that you had missed your class today!"

    show mother frown

    e frowntalk "Oh! I must have forgotten. I was out with Lisia and Marc-"

    show emory frown

    mother frowntalk "I can see that."

    show mother frown

    e sad frowntalk "I am sorry, Mother. It won't happen again."

    show emory frown

    mother frowntalk "I was told that this isn't the first time it happened, [pname]. How can you expect me to trust you again?"

    show mother frown

    e frowntalk "I..."

    show emory frown

    mother frowntalk "Besides, it would be one thing if I found you with Cordelian or the Princess. But these two! How many times have I told you that you are not to be seen around them?"
    mother "And Lisia! I will have a word with you in a moment. Alone. Right after I finish with [pname]."

    show mother frown

    en "Wait, does that mean..."

    e frowntalk "You can't fire her, mother!"

    show emory frown

    mother frowntalk "You will not tell me what i can or cannot do. As it is, you have done enough for today."

    show mother frown

    e frowntalk "But Lisia-"

    show emory frown

    mother frowntalk "Will soon be returning to her home."

    show mother frown

    l down frowntalk "Madam, please."
    l "I promise you, I will not speak to [pname] again. Or go anywhere with him."
    l "But please, I need this position."

    show lisia frown

    mother frowntalk "I have made up my mind. You will be packing your things up. I want you to leave by tomorrow evening at the latest."

    show mother frown

    hide mother with moveoutright
    show marco up frown at right with moveinright

    m frowntalk "Well, I hear Her Highness calling me. Good bye, [pname], Lisia."

    show marco frown

    e "!!!"
    e frowntalk "Aren't you going to help?"

    show emory frown

    m frowntalk "With what, exactly?"

    show marco frown

    e frowntalk "Lisia and this... situation. You helped out last time..."

    show emory frown

    m frowntalk "That does not mean I will today. I have more important things to do. I'm sorry. Please excuse me."

    show marco frown

    hide marco with dissolve

    en "What happened to Marco? Why is he acting so strange?"

    show mother down frown at right with moveinright

    mother frowntalk "Enough of this nonsense. Return home immediately, [pname]! You will apologise to your tutor, as well as attend extra lessons to make up for the ones you have lost."
    mother "As for you, Lisia, you better start getting your things together."

    show mother frown

    l frowntalk "...ye-yes, ma'am."

    show lisia frown

    scene bg castleinside2
    with fadee

    
    en "I don't understand."
    en "How could have everything gone so wrong so quickly?"
    en "Perhaps going to the guild had been a terrible idea, after all."
    en "But what do I do now?"


    show emory sad frown at closeleft
    show cordelian up smile at closeright
    with dissolve


    c talk "[pname]!"

    show cordelian smile

    e unsure talk "Oh, hello, Cordelian! It's been a while, hasn't it?"

    show emory smile

    c talk "It has! I heard you've been getting yourself into quite a soup recently."

    show cordelian smile

    e frowntalk "What? I have not been doing anything of the sort!"

    show emory frown 

    c unsure talk "Oh? What's this about you sneaking away with Lisia and Marco, then?"

    show cordelian smile

    e frowntalk "Nothing... I was just out in town. My mother, as always, overreacted."

    show emory frown 

    c talk "While I can believe that, something tells me there's more to it. And this wasn't the only time either, now, was it?"
    c "Why, [pname], you can't keep it from me!"
    c "Do you {i}like{/i} one of them?"

    show cordelian smile

    e down blush frowntalk "What do you mean?"

    show emory frown

    c talk "Oh, you know what I mean! Quit playing the fool! So, which is it?"

    show cordelian smile

    e frowntalk "It's not like that! Cordelian! Do stop it!"
    e -blush "And besides, that trip to the town cost Lisia her job."

    show emory frown

    c down frowntalk "So I heard. I'm terribly sorry about it. I meant to speak to your mother and convince her, but she is never here when I visit."

    show cordelian frown

    e up frowntalk "Would you really do that? Why, thank you, Cordelian! I think my mother will be home this evening. Do you think you can make it then?"

    show emory smile

    c talk "I'll certainly try. Lisia is my friend too, after all. So... you were telling me about Marco and Lisia..."

    show cordelian smile

    e down blush frowntalk "I was not! Why don't you tell me about Katherine, instead?"
    e -blush talk "How has it been with you two?"

    show emory unsure frown

    c sad frowntalk "Kath is a wonderful person. But... there is this looming threat of the war, and I can't stop thinking about it."
    c "After all, the primary reason we married was because of Leodipia threatening us."
    c "Even if we love each other now, I can't help associating..."

    show cordelian frown

    e frowntalk "It's alright, Cordelian."
    e "Have you spoken to Katherine about it? The war, I mean."

    show emory frown

    c frowntalk "I haven't, actually. But her father is well aware of the dangers Leodipia poses. Both our armies are preparing for war."
    
    show cordelian frown

    e frowntalk "Is it that bad? Are you all absolutely certain that there will be a battle?"

    show emory frown

    c frowntalk "I'm afraid so."

    show cordeliam frown

    e frowntalk "Oh. I'm... I don't know what to say, Cordelian."

    show emory frown

    c frowntalk "Then maybe we shouldn't talk about it."
    c talk "Come on! I get to speak to you after so long and you bring up all the sad things!"

    show cordelian up smile

    e frowntalk "I'm the one who brought up your wife."

    show emory frown

    c talk "Speaking of which, when're you going to have one? Or will it be a husband?"

    show cordelian smile

    e frowntalk "Here we go again..."
    e unsure "Do you really not have anything better to talk about than my non existent romantic endeavours?"

    show emory frown

    c talk "Cut me some slack, Emory. I'll have my whole life to talk about serious matters."
    c "But we only get to have fun now!"

    show cordelian smile

    e frowntalk "I'm not sure I agree with your idea of fun."
    e "How does Marco even deal with you all day?"

    show emory frown

    c talk "Oh, so you wanted to talk about him."
    c "Have you noticed something odd about him lately?"

    show cordelian frown

    e frowntalk "Now that you've brought it up, I have. He was acting very strange that day on our way back from town."
    e sad "Almost as if he was... lost, somehow."

    show emory frown

    c frowntalk "I've seen him like that too! Especially since that day."
    c "I wanted to ask you, where exactly did you go? It might help to decipher this behavior of Marco's."

    show cordelian frown

    menu:
        "Tell Cordelian":
            $ marco += 1
            $ tell_cordelian = True
        "Don't tell Cordelian":
            $ lisia += 1
            $ tell_cordelian = False

    
    if tell_cordelian:
        e frowntalk "I don't really see how it could help, but we went to a guild."

        show emory frown

        c frowntalk "A guild? What for?"

        show cordelian frown

        e frowntalk "Well... we were looking for something."
        e "Something we could only find there."

        show emory frown

        c frowntalk "What do you mean? What were you looking for? And did you find it?"

        show cordelian frown

        e frowntalk "Not exactly. But we have some information, and maybe even some leads. So I'd say it was worth it."

        show emory frown

        c talk "You sound like you're on a treasure hunt, Emory! Why didn't you invite me?"

        show cordelian smile

        e down frowntalk "It's not a treasure hunt, Cordelian. And I couldn't invite you. Not without..."
        e "Nevermind."
        e "Besides, you were busy, what with everything that has been happening recently."

        show emory frown

        c talk "Well yes, that {i}is{/i} true, I suppose. Nonetheless, an invitation would have been nice."
        c frowntalk "Anyway, what guild was it? And did you see Marco acting odd?"

        show cordelian frown

        e frowntalk "You're surprisingly inquisitive today!"
        e "And, to answer your question, we went to Windglade."

        show emory frown

        c frowntalk "Windglade! I've heard of it! I've also heard they keep their business under wraps."

        show cordelian frown

        e frowntalk "Evidently everyone, with myself as the exception, knows about that."

        show emory frown

        c talk "That's only because you live under a rock. And you didn't answer the most important question!"
        c "About Marco!"

        show cordelian frown

        e up frowntalk "Oh! Right. I did think he had been acting a bit off at the guild."
        e "He actually surprised everyone by his knowledge about Windglade."
        e "In fact, he did seem suspiciously keen on actually joining the guild as well..."
        e "And when we came back, he brushed off Lisia, almost rudely, and returned to the castle."

        show emory frown

        c frowntalk "That doesn't really sound like him at all, does it?"

        show cordelian frown

        
    if tell_cordelian == False:
        e sad frowntalk "I'm sorry, Cordelian, but I really couldn't tell you."

        show emory frown

        c down frowntalk "Why not? Since when do we keep such secrets from each other?"

        show cordelian frown

        e frowntalk "...Says the one who didn't tell me he was getting {i}married{/i}."

        show emory frown

        c frowntalk "Touche."
        c "But jokes aside, will you, at least, reveal why you won't tell me?"

        show cordelian frown

        e frowntalk "It's... not my secret. I cannot let someone I care for, down."

        show emory frown

        c frowntalk "Oh. I understand. I think I do, at least."

        show cordelian frown

        e frowntalk "I'm really sorry, Cordelian. You know I would, if I could."

        show emory frown

        c frowntalk "I know."
        c "I had just... not expected that one little decision could change so much."

        show cordelian frown

        e frowntalk "What do you mean by that?"

        show emory frown

        c frowntalk "I just realised that I haven't even spoken to Marco, or you, properly in weeks."

        show cordelian frown

        e frowntalk "It's not your fault... You've simply been preoccupied."

        show emory frown

        c frowntalk "Too preoccupied to talk to my friends? I shouldn't have been."
        c "I should have noticed any problems Marco might have had ages ago."
        c "After all, he always does the same for me!"
        c "But I've been too negligent."

        show cordelian frown

        e down frowntalk "What you're doing right now, indulging in self-pity, won't help anyone, Cordelian. You know that."
        e "If you want to fix everything, you need to tell him everything you've told me."

        show emory frown
        
    c frowntalk "[pname], do you think he could be... unhappy? At the castle, I mean."

    show cordelian frown

    e frowntalk "I... don't really know."

    show emory frown

    c frowntalk "But you spend so much time with him, nowadays! Even more than I do!"

    show cordelian frown

    e frowntalk "That is true, but he has always been rather closed off."

    show emory frown

    c frowntalk "He doesn't exactly like to share his problems, I'm aware of that."
    c "I really need to speak to him, instead of sitting around and hypothesizing, don't I?"

    show cordelian frown

    e down frowntalk "You're smarter than you look."

    show emory smile

    c frowntalk "Oi! What's that supposed to mean?"

    show cordelian frown

    e talk "Nothing. Nothing at all. Now, don't you have a conversation you're late for?"

    show emory up smile

    c up frowntalk "Mhm..."
    c "You're right, [pname]. I'll let you know if I need your help, all right?"

    show cordelian smile

    e talk "Of course!"

    show emory smile

    hide cordelian with moveoutleft




    ###### Marco route
    scene bg garden
    with fade

    show emory up smile at closerleft
    show marco up frown at closerright
    with dissolve
        
    e frowntalk "So, did he speak to you? Cordelian, I mean. He said he had something to say-"

    show emory frown

    m frowntalk "Yes, he did, [pname]. But I don't see why that is something you should be bothered about."

    show marco frown

    e sad frowntalk "...are you angry at me, Marco?"
    e "What is it? What did I do? You have been this way ever since that day at Windglade."

    show emory frown

    m frowntalk "I don't see what you mean. I would appreciate if you left me alone."

    show marco frown

    e frowntalk "Not until you tell me what is going on. Neither Cordelian nor I can figure it out for the life of us!"

    show emory frown

    m frowntalk "Then you should give up. It doesn't matter."

    show marco frown

    e frowntalk "Of course, it does! You're our friend, Marco!"

    show emory frown

    m frowntalk "A friend who you only come to when you need something from him?"

    show marco frown

    e frowntalk "What would make you say something like that?"

    show emory frown

    m frowntalk "Only your actions up until now."


    return

    