################# Post-demo script ###################

    scene bg bedroomday
    with fadee

    en "It's a new day, thankfully..."

    ## call an imagemap


if overworld_choice4 == "lisia":

    en "I think I'll take a newer route today. Maybe I should go around the forest..."

    scene bg forest
    with fade

    show lisia up frown at rightt
    show emory up frown at leftt
    with dissolve

    l frowntalk "Emory..."

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

    l down frowntalk "Maybe, instead of running away, you should have spoken to Cordelian about this, Emory."

    show lisia frown

    e unsure frowntalk "Well, I might have just rushed away too quickly..."
    e "You're right, Lisia."
    e up "I'm going to talk to him tomorrow."

    show emory frown

    l up talk "Good. Now, get some sleep. You look exhausted."

    show lisia smile

    e talk "So do you. Good night!"

    show emory smile

    l talk "Good night, Emory!"

    show lisia smile

    

if overworld_choice4 == "marco":
    en "I think I'll stick to the path I know today. I'll walk through the forest."

    scene bg forest
    with fade

    show marco down frown at rightt
    show emory up frown at leftt
    with dissolve
        
    m frowntalk "Emory! Wait!"

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


if overworld_choice4 == "cordelian":
    en "I'll see Cordelian. I suppose I owe him an explanation for last night... or at the very least, an apology."

    scene bg castle
    with fade

    show cordelian up smile at rightt
    show emory down frown at leftt
    with dissolve 

    e frowntalk "Cordelian? Could I speak to you for a few minutes?"

    show emory frown

    c talk "Oh, hello Emory! Could you wait a bit, please? I have some work to finish."

    show cordelian smile

    e frowntalk "I... I'll wait downstairs."
    en frown "It seems he's speaking to Katherine."
    en "...of course he is."
    en "She is the only person he seems to speak to, nowadays."
    en "I guess all I can do is wait."
    en "I can't believe that they have already started cleaning up the castle for the wedding!"

    hide cordelian
    show katherine up smile at leftt
    with moveinright

    k talk "Emory, was it?"

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

    c talk "Emory! Katherine! I see you two are getting along. That's great!"

    show cordelian smile

    e frowntalk "Yes, well-"

    show emory frown

    k frowntalk "I think I should leave now, Cordelian."

    show katherine frown

    menu:
        "Goodbye.":
            $ cordelian += 5
            $ katherine_leaving = "goodbye"
        "Can you stay longer?":
            $ katherine += 5
            $ katherine_leaving = "stay"

    if katherine_leaving == "goodbye":
        e frowntalk "Goodbye."

        show emory frown

        c frowntalk "So soon? Must you? I was planning to show you our city today."

        show cordelian frown

        k frowntalk "Perhaps later, Cordelian. You seem to be occupied."
        k talk "Bye, Cordelian, Emory."

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

        c frowntalk "I'm sorry, Emory."
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

        c talk "So, what was it you wanted to talk about, Emory?"

        show cordelian smile

        e up talk "Oh... I can't remember. I'm sure it can wait."

        show emory smile

        c talk "Oh, alright. I-"

        show cordelian frown

        m "Cordelian! Your parents want to speak to you!"

        c frowntalk "Again?"
        c "...alright. Tell them I'll be there in a moment."
        c "I'm sorry, Emory, Katherine."

        show cordelian frown

        k "..."
        c talk "Oh right! I promised Katherine I'd show her the city."
        c "Emory, could you do it instead? I'd ask Marco, but he's terribly busy too."

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

        k talk "Could we go for a ride then, Emory?"

        show katherine smile

        en "I've never seen Katherine this... expressive before! She looks like a little child in front of a candy store. She really must love horses."
        e talk "I don't see why not. I'll just get the tack."
            
        e "Here you go."
        en smile "She is definitely an experienced rider, from the way she mounts. Who would've thought?"

        k talk "Would you like to race until we reach that fence?"

        show katherine smile

        e frowntalk "Are you sure you want to? I mean, you've only just met Orchid-"

        show emory frown

        k talk "Are you afraid of losing, Emory?"

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


    scene bg emorybednight
    with fade

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
        
    ## call an imagemap


if overworld_choice5 == "lisia":

    scene bg castle
    with fade

    show emory up smile at leftt
    show lisia up smile at rightt
    with dissolve

    l talk "Good morning, Emory! Which shade of blue do you think will look better for the drapes over there?"

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
    with moveinleft

    m talk "Surprising to see you here, Emory!"

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
        
if overworld_choice5 == "marco"

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
    with moveinleft

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

    scene bg diner
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

    mother "Emory?"

    show mother down frown at right
    hide marco
    with moveinright

    show lisia down frown

    mother frowntalk "Emory? What are you doing here?"

    show mother frown

    e frowntalk "Mum! I didn't know you were going to be in town today!"

    show emory frown

    mother frowntalk "I could say the same for you. I was under the impression you would be with Cordelian today."

    show mother frown

    e frowntalk "I... uhh... He's busy. I think."

    show emory frown

    mother frowntalk "I see."
    mother "Perhaps you should come home with me, Emory."
    mother "As should you, Lisia."

    show mother frown

    e frowntalk "But-"

    show emory frown

    mother frowntalk "Now, Emory!"

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
        
        
if overworld_choice5 == "cordelian":

    scene bg castle
    with fade

    show emory up smile at leftt
    show cordelian up smile at rightt
    with dissolve

    e talk "I do hope you'll have some time to spend with me today, Cordelian."

    show emory smile

    c talk "I should. I don't have much to do today."

    show cordelian smile

    e talk "So, what would you like to do?"

    show emory smile

    c talk "I was thinking I could paint something and..."

    show cordelian smile

    e frowntalk "You know how your paintings turn out, Cordelian."

    shoe emory frown

    c frowntalk "Hey. What's that supposed to mean?"

    show cordelian frown

    e frowntalk "Well, do you remember the "Idyllic Beach" you painted, for example?"

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

    c frowntalk "Stop it, Emory!"

    show cordelian frown

    e talk "Alright, alright. Let's see you do this. Mind if I grab a brush too?"

    show emory smile

    c talk "Go ahead!"

    hide cordelian
    hide emory 
    with dissolve

    $ renpy.pause(1.0)

    show emory up smile at leftt
    show cordelian up smile at rightt
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
    c "Don't you agree, Emory?"

    show cordelian smile

    e frowntalk "...Yes."

    show emory frown

    c talk "We were just going to the gallery. I haven't shown Emory the paintings I got from Auqecia."

    show cordelian smile

    k talk "I see."

    show katherine smile

    c talk "Yes, well, shall we?"

    show cordelian smile


    
    