define y = Character("You")
define yn = Character("[playername]")
define q = Character("???")
define tuna = Character("Yuna")
define cod = Character("Doc")
define shark = Character("George")
define salmon = Character("Banquo")
define g = Character("Gupsby")
define jelly = Character("Jolie")
# The game starts here.

label start:
    $fishlist = ["tuna", "cod", "salmon", "g", "jel"]
    $killcount = 0

    scene bg shore
    y "What a wonderful day to go fishing."
    y "Maybe I'll find a friend... or more. ( ͡° ͜ʖ ͡°)"
    "(You cast your rod into the ocean, and a few minutes later you feel a bite.)"
    "(As you reel in your catch, you find yourself face-to-face with a tuna.)"
    show yuna neutral with dissolve
    voice "yuna_hithere.mp3"
    q "Hi there!"
    y "Hello..."
    voice "yuna_whatsyourname.mp3"
    q "What’s your name?"
    y "Oh, it’s..."
    python:
        playername = renpy.input("What's your name?", length=16)
        playername = playername.strip()
        if not playername:
            playername = "Jeff"
        elif playername.lower() == "gaster":
            renpy.scene()
            renpy.show("bg black")
            renpy.pause(1.0)
            renpy.jump("start")
            playername = playername.capitalize()


    yn "It's... [playername]?"
    voice "yuna_thatsanicename.mp3"
    q "[playername] huh, that’s a nice name."
    voice "yuna_minesyuna.mp3"
    tuna "Mine’s Yuna."
    yn "So... do you want to hang out somewhere?"
    show yuna blush with dissolve
    voice "yuna_theresthisrestaurant.mp3"
    tuna "There's this restaurant I've been wanting to go to recently."
    yn "Sounds good to me!"
    scene bg dinner with fade
    show yuna neutral
    show fg dinner
    "(You are now on a romantic candle-lit dinner with Yuna the Tuna.)"
    voice "yuna_haveyoutriedsharkfin.mp3"
    tuna "Have you tried the shark fin soup here?"
    menu:
        "Yeah, it's delicious!":
            voice "yuna_iknowright.mp3"
            tuna "I know, right?"
            jump postchoice1
        "Wait, isn't that illegal?":
            show yuna blush with dissolve
            voice "yuna_itsnotillegal.mp3"
            tuna "It's not illegal if you don't get caught!~"
            yn "Well, I caught you, didn't I?"
            voice "yuna_ohyeahgoodpoint.mp3"
            tuna "oh yeah good point"
            jump postchoice1
        "...":
            show yuna annoyed with dissolve
            voice "yuna_wellithinkitstasty.mp3"
            tuna "Well I think it's tasty."
            jump postchoice1


label postchoice1:
    show yuna neutral with dissolve
    voice "yuna_myspeciesisbeingoverfished.mp3"
    tuna "My species has been being overfished, so I've been kind of on edge recently."
    show yuna cry with dissolve
    voice "yuna_imissmywife.mp3"
    tuna "I miss my wife, [playername]."
    voice "yuna_imissheralot.mp3"
    tuna "I miss her a lot."
    voice "yuna_illbeback.mp3"
    tuna "I'll be back."
    yn "You have a wife?"
    "(Yuna didn't respond as they got up dramatically from the table.)"
    hide yuna with dissolve
    scene bg black with fade
    "(You sat there idly, twiddling your thumbs until Yuna came back about 10 minutes later.)"
    scene bg dinner with fade
    show yuna neutral 
    show fg dinner
    voice "yuna_sorryformakingyouwait.mp3"
    tuna "Sorry for making you wait."
    menu:
        "What took you so long?":
            show yuna blush with dissolve
            voice "yuna_ihadsomebusiness.mp3"
            tuna "I had some... business to take care of."
            voice "yuna_illsaynomoreonthesubject.mp3"
            tuna "...I'll say no more on the subject."
            jump postchoice2
        "You good bro?":
            voice "yuna_yeahimallright.mp3"
            tuna "Yeah, I'm alright..."
            jump postchoice2
        "...":
            show yuna annoyed with dissolve
            voice "yuna_thesilenttreatment.mp3"
            tuna "...The silent treatment, huh? Harsh."
            voice "yuna_itsnotlikeillghost.mp3"
            tuna "It's not like I was gonna ghost you, y'know."
            jump postchoice2


label postchoice2:
    show yuna neutral with dissolve
    voice "yuna_ienjoyedthefood.mp3"
    tuna "Well, I certainly enjoyed the food."
    "(You notice that Yuna didn't mention anything about your company.)" 
    show yuna blush with dissolve
    voice "yuna_whatareyougoingtodonow.mp3"
    tuna "So... what are you going to do now?"  
    "(After hanging out with a fish, you will have the opportunity to either keep or release them.)"
    "Will you catch or release Yuna the Tuna?" 
    menu:
        "Release Yuna":
            $fishlist.remove("tuna")
            show yuna cry with dissolve
            voice "yuna_youresendingmeback.mp3"
            tuna "You're sending me back?"
            voice "yuna_isupposeiwontmeetthesamefate.mp3"
            tuna "I suppose I won't meet the same fate as my family today."
            jump postchoice3
        "Keep Yuna":
            $killcount += 1
            jump postchoice3


label postchoice3:
   scene bg shore with fade
   "(A day has passed since your date with Yuna the Tuna.)"
   "(You decide to go back to your fishing spot.)"
   "(Upon reeling in your rod, your second catch of the week appears in your view.)"
   show doc neutral with dissolve
   voice "Doc_whatareyou.mp3"
   q "What are YOU lookin at"
   yn "You, I guess."
   voice "Doc_fairenough.mp3"
   q "Fair enough"
   voice "Doc_imdoc.mp3"
   cod "I'm Dr. Simon Scalesworth III but you can just call me The Doc"
   voice "doc_nofurther.mp3"
   cod "If you have no further business with me I'll be on my way"
   yn "Wait! Do you want to go have dinner with me? Pwetty pweeeease? uwu 👉👈" 
   voice "Doc_surewhynot.mp3"
   cod "Sure why not"
   scene bg dinner with fade
   show doc neutral
   show fg dinner
   voice "Doc_niceplace.mp3"
   cod "This is a nice place" 
   if "tuna" in fishlist:
       show yuna side at left with moveinleft
       voice "yuna_whosthis.mp3"
       tuna "Who's this?"
       yn "This is Doc."
       voice "yuna_HIIIII.mp3"
       tuna "HIIII"
       voice "Doc_okthen.mp3"
       cod "Ok then"
       hide yuna with moveoutleft
   voice "Doc_announcement.mp3"
   cod "I've come to make an announcement"
   voice "Doc_wannahearit.mp3"
   cod "Wanna hear it?"


   menu:
       "Sure why not?": 
           voice "Doc_research.mp3"
           cod "So I've been doing some research"
           voice "Doc_increaseinoverfishing.mp3"
           cod "There's been an increase in overfishing"
           voice "Doc_hugeamount.mp3"
           cod "Like a huge amount"
           voice "Doc_cringe.mp3"
           cod "It's pretty cringe"
           jump postchoice4
       "No not really":
           voice "Doc_ohokthen.mp3"
           cod "Oh, okay then"
           jump postchoice4
       "...":
           voice "Doc_donttalkmuch.mp3"
           cod "You don't talk much do you?"
           voice "Doc_thatsfineiguess.mp3"
           cod "That's fine I guess"
           jump postchoice4
label postchoice4:
   voice "Doc_thoughtsonpollution.mp3"
   cod "What are your thoughts on pollution"
   menu:
       "I don't like it, it's stinky.":
           voice "Doc_ithinksotoo.mp3"           
           cod "I think so too"
           show doc angry with dissolve
           voice "Doc_barelygooutside.mp3"
           cod "I can barely go outside my house without running into a pile of plastic bags"
           jump postchoice5
       "It's based.":
           show doc angry with dissolve
           voice "Doc_wellthatopinionwasnt.mp3"
           cod "Well, that opinion certainly isn't"
           voice "Doc_icantbelieveyou.mp3"
           cod "I can't believe you" 
           jump postchoice5
       "...":
           voice "Doc_imjustgoingtoassume.mp3"
           cod "I'm just gonna assume you don't like it"
           jump postchoice5


label postchoice5:
   show doc neutral with dissolve
   voice "Doc_whatsnextbucko.mp3"
   cod "So what next bucko"
   menu:
       "Release Doc":
           $fishlist.remove("cod")
           voice "Doc_sothatsit.mp3"
           cod "So that's it then"
           voice "Doc_backtomycave.mp3"
           cod "Back to my cave I go"
           jump postchoice6
       "Keep Doc": 
           $killcount += 1
           voice "Doc_whatareyoudoing.mp3"
           cod "Wait what are you doing"
           voice "Doc_dontputme.mp3"
           cod "Don't put me in your fishbowl nooooooo"
           jump postchoice6

label postchoice6:
    scene bg shore
    "(It's a new day, and a new fish to catch.)"
    "(After reeling in your line, you see a very fancy-looking guppy.)"
    show gupsby neutral with dissolve
    voice "gup_hellothereoldchum.mp3"
    q "Hello there, Old Chum."
    voice "gup_mightilearnyourname.mp3"
    q "Might I learn your name?"
    yn "It's [playername]."
    voice "gup_verywellmetindeed.mp3"
    q "[playername]... very well met, indeed."
    voice "gup_mynamesgupsyoldchum.mp3"
    g "My name is Gupsby, Old Chum."
    voice "gup_ithinkwemightbecomegreatfriends.mp3"
    g "I think we might become great friends."
    yn "You want to go grab a bite?"
    show gupsby glass with dissolve
    voice "gup_iwouldbehonoredoldchum.mp3"
    g "I would be honored, Old Chum."
    show gupsby neutral with dissolve
    if "tuna" in fishlist:
        show yuna side at left with moveinleft
        voice "yuna_canicometoo.mp3"
        tuna "Can I come too?"
        yn "no"
        voice "yuna_awww.mp3"
        tuna "awwww :("
        hide yuna with moveoutleft
    if "cod" in fishlist and "tuna" in fishlist:
        show doc side at left with moveinleft
        voice "Doc_donttrust.mp3"
        cod "DON'T TRUST- mmmfggh"
        hide doc with moveoutleft
        yn "What was that noise? Hahaha..."
        show gupsby smile with dissolve
        voice "gup_illthinknothingofitoldchum.mp3"
        g "I'll think nothing of it, Old Chum."
    voice "gup_shallweaway.mp3"
    g "Shall we away?"
    scene bg dinner with fade
label choice7:
    show gupsby neutral
    show fg dinner
    voice "gup_whatwouldyouliketodiscuss.mp3"
    g "Well, Old Chum, what would you like to discuss?"
    menu:
        "Finances":
            show gupsby smile with dissolve
            voice "gup_imdoingquitewellformyself.mp3"
            g "I'd say I'm doing quite well for myself, Old Chum."
            voice "gup_ihavealovelymanor.mp3"
            g "I have a lovely manor over in East Kelp."
            show gupsby glass with dissolve
            voice "gup_youshouldcometoparty.mp3"
            g "You should come to one of my parties; they're a wonderful time, Old Chum."
            jump choice7
        "Overfishing":
            voice "gup_ithinkimayhaveasolution.mp3"
            g "I think I might have a solution for that, Old Chum."
            voice "gup_regulatefishingcompanies.mp3"
            g "I say we should heavily regulate the major fishing companies."
            voice "gup_thatwayusfishcansleepbetter.mp3"
            g "That way us fish can sleep better at night."
            show gupsby smile with dissolve
            voice "gup_bestcourseofaction.mp3"
            g "I feel this is the best course of action, Old Chum."
            jump choice7
        "...":
            voice "gup_whatswrongoldchum.mp3"
            g "What's wrong, Old Chum?"
            show gupsby smile with dissolve
            voice "gup_catfishgotyourtongue.mp3"
            g "Catfish got your tongue?"
            voice "gup_illkeepeatingthisfinefood.mp3"
            g "I suppose I'll just keep eating this fine food."
            show gupsby glass with dissolve
            voice "gup_generoustipforchef.mp3"
            g "I shall have to leave a generous tip for the chef."
            jump postchoice7
label postchoice7:
    show gupsby neutral with dissolve
    voice "gup_wellthiswasquitenice.mp3"
    g "Well, this was quite nice, Old Chum."
    voice "gup_whatshalwedonow.mp3"
    g "What shall we do now?"
    menu:
      "Release Gupsby":
         $fishlist.remove("g")
         voice "gup_wellthenoldchum.mp3"
         g "Well then, Old Chum..."
         voice "gup_iguessillseeyoulater.mp3"
         g "I guess I'll see you later."
      "Keep Gupsby":
        $killcount += 1
        voice "gup_isee.mp3"
        g "I see."
        voice "gup_inthatcasekeepmeinanaquarium.mp3"
        g "In that case, might you keep me in that aquarium behind us?"
        hide Gupsby with dissolve
        scene bg dinner gupsby with dissolve
        show fg dinner
        voice "gup_thanksoldchum.mp3"
        g "Thanks, Old Chum."


    scene bg shore
    "(With the new day, there is another fish to catch.)"
    "(A throw of the rod, it only takes a few seconds for your fourth catch of the week to appear in your view.)"
    show banquo neutral with dissolve
    q "Huh?"
    yn "Who are you?"
    q "Who, me?"
    yn "Do you see anyone else here?"
    show banquo right with dissolve
    q "No, I suppose not."
    show banquo neutral with dissolve
    salmon "I'm Banquo." 
    yn "I'm [playername]."
    salmon "Nice to meet you [playername]."
        
    yn "So do you want to hang out?"
    show banquo sad with dissolve
    salmon "I don't know." 
    if killcount >= 3:
        salmon "A lot of my friends are missing."
        salmon "I miss them a lot." 
        yn "Oh no. That's terrible..."
        yn "Do you want to talk about it over dinner?"
        show banquo left with dissolve
        salmon "I guess so."
    elif killcount == 2:
        salmon "I was talking with a friend of mine..."
        if not "tuna" in fishlist:
            salmon "I think it was Yuna..."
        elif not "cod" in fishlist:
            salmon "I'm pretty sure it was Doc..."
        else:
            salmon "I believe it was Gupsby..."
        salmon "And they mentioned just how many fish have gone missing over the years."
        show banquo left with dissolve
        salmon "Like a lot."
        show banquo right with dissolve
        salmon "It's honestly kind of scary."
        show banquo sad with dissolve
        salmon "You don't know if you're going to be next..."
        salmon "And the ocean is getting kind of empty..."
        salmon "Like, sure, there's plenty of fish in the sea..."
        salmon "But I still miss my friends."
        yn "That sounds rough."
        yn "Maybe we can discuss this more over some food?"
        show banquo neutral with dissolve
        salmon "I suppose we could."
    else:
        salmon "I was supposed to meet with a friend today..."
        salmon "But I couldn't find them." 
        salmon "I hope that they're okay."
        salmon "It's kind of scary."
        show banquo right with dissolve
        salmon "Overfishing has increased a lot lately."
        salmon "I've lost a few of my friends." 
        salmon "Sure, there's plenty of fish in the sea..."
        show banquo sad with dissolve
        salmon "But I miss my friends."
        salmon "I miss my family."
        salmon "I just wish humans didn't fish as much as they did."
        yn "That's terrible, I'm sorry to hear that."
        yn "Do you want to get some food?"
        salmon "Yeah... I'd like that."
    if "g" in fishlist:
        scene bg dinner gupsby with fade
    else:
        scene bg dinner with fade
    show banquo neutral
    show fg dinner
    salmon "This is nice."
    yn "Thanks"
    if "g" in fishlist:
        show banquo right with dissolve
        salmon "Is that…Gupsby?"
        show gupsby side at left with moveinleft
        g "Hello new fish! Hello Old Chum!"
        salmon "Uh…hi?"
        hide gupsby with moveoutleft
    show banquo neutral with dissolve
    salmon "But yeah, a few of my friends are missing."
    salmon "I don't know if they just moved away…"
    salmon "Or if the humans got them."
    show banquo left with dissolve
    salmon "I hope that the second isn't true..."
    salmon "I just wished the humans fished in the ocean a little less."
    salmon "I'm not asking them to stop completely..." 
    show banquo right with dissolve
    salmon "Just... do less fishing then what they're going right now."
    salmon "'Cause it's not just the ocean that's being  overfished."
    show banquo sad with dissolve
    salmon "The ocean ecosystem is being affected by the lack of fish."
    yn "I'm sorry to hear that."
    yn "I hope that you find your friends."
    show banquo neutral with dissolve
    salmon "Thanks."
    salmon "So uh…what do you want to do now?"
    menu:      
        "Release Banquo":
            $fishlist.remove("salmon")
            show banquo right with dissolve
            salmon "Yeah, I should probably get going now..." 
            show banquo neutral with dissolve
            salmon "You seem nice."
            salmon "Maybe I'll see you soon."
            jump postchoice8
        "Keep Banquo":
            show banquo left with dissolve
            salmon "Wait hold on..."
            show banquo neutral with dissolve
            $killcount += 1
            if killcount >= 1:
                salmon "You're part of the problem!"
                salmon "You're overfishing!"
            salmon "Don't put me in your fish bowl!"
            salmon "NOOOOOOOOOOOOOOOOOOOOO-"
            jump postchoice8

label postchoice8:
    scene bg shore with fade
    "(A new day has come once more.)"
    "(Casting your line, you fish up a Jellyfish.)"
    show jolie neutral with dissolve
    q "HOOIIIIII"
    jelly "ME  JOLIE"
    yn "Uh…"
    jelly "WANNA GO ON DATE WITH JOLIE"
    yn "Wait what-"
    if "g" in fishlist:
        scene bg dinner gupsby with fade
    else:
        scene bg dinner with fade
    show jolie neutral with dissolve
    show fg dinner
    "(Jolie has forcefully taken you to the restaurant.)"
    jelly "DATE START" 
    yn "So uh…"
    yn "Do you have a favorite food?"
    jelly "PLANKTON"
    jelly "AND FISH"
    jelly "BUT THERE LESS FISH"
    jelly "SO ME EAT MORE PLANKTON"
    yn "That's…great"
    menu:
        "Do you always scream like this?":
            show jolie sad with dissolve
            jelly "ME NOT SCREAM"
            jelly "DO YOU WANNA HEAR ME SCREAM?"
            jelly "{size=-10}ahhhh{/size}" 
            jump postchoice9
        "Do you eat anything other than plankton?":
            jelly "EVERYTHING I EAT IS PLANKTON"
            jelly "EVEN WHAT I EAT RIGHT NOW"
            jelly "IT SPAGHETTI WITH PLANKTON SAUCE"
            jump postchoice9
        "...":
            show jolie sad with dissolve
            jelly "WHY YOU QUIET?"
            jelly "DO YOU NO LIKE ME??? D:"
            jump postchoice9
label postchoice9:
    show jolie neutral with dissolve
    jelly "ME ENJOY TIME"
    jelly "DATE END"
    jelly "UNLESS YOU NO WANT THAT...?"
    menu:
        "Release Jolie":
            $fishlist.remove("jel")
            jelly "OK"
            jelly "BYE BYE"
        "Keep Jolie":
            $killcount += 1
            show jolie sad with dissolve
            jelly "WHERE YOU PUT ME"
            jelly "I NO LIKE THIS"
            jelly "{size=-10}ahhhh{/size}" 

label postchoice10:
    scene bg shore with fade
    "(It's a beautiful day outside.)"
    "(After the wacky fish you met the previous days...)"
    "(...You decide that today is the last day you'll go fishing.)"
    "(Ever.)"
    "(So you reel in your last fish.)"
    show george neutral with dissolve
    q "Sup, bro."
    yn "Bro?"
    q "Name's George."
    shark "I'm a shark."
    shark "Obviously."
    yn "I can see that."
    yn "Do you…"
    yn "Want to go out?"
    show george shock with dissolve
    shark "Right now?"
    shark "A bit forward ain't it?"
    show george neutral with dissolve
    shark "But I've been meaning to talk to ya, so I guess I'll come along."
    if "g" in fishlist:
        scene bg dinner gupsby
    else:
        scene bg dinner
    show george neutral with dissolve
    show fg dinner with dissolve
    if killcount == 5:
        jump geno
    elif killcount >= 1:
        jump neut
    else:
        jump paci   

label geno:
    shark "So, you've been busy, huh?"
    show george unamused with dissolve
    shark "The ocean's a lot less crowded these days."
    shark "All the overfishing and pollution..."
    show george neutral with dissolve
    shark "I bet you've heard about it from your previous dates, right?"
    shark "Heh..."
    show george unamused with dissolve
    shark "Well, kiddo, you're part of the problem."
    shark "You didn't let a single one of those fish leave your grasp."
    shark "You took them away from their friends, their families..."
    shark "And to what end?"
    show george sad with dissolve
    shark "Why would you take them all?"
    menu:
        "Because I felt like it":
            shark "..."
            shark "...That's all you have to say for yourself?"
            shark "You just {i}\"Felt like it?\"{/i}"
            show george unamused with dissolve
            shark "Disgusting."
            jump postchoicegeno
        "Because I'm lonely":
            shark "Well, you could have done something more rational than kidnapping."
            show george unamused with dissolve
            shark "Maybe just ask for their number next time."
            shark "Insane concept, I know."
            jump postchoicegeno
        "...":
            show george unamused with dissolve
            shark "No defense, huh?"
            shark "No higher goal?"
            shark "A crime with no motive is worse than a crime with a stupid one, in my book."
            jump postchoicegeno

label postchoicegeno:
    shark "Well, it's plain to see you're beyond saving."
    shark "I just hope you're happy with the path you chose."
    shark "...Just kidding. I don't really hope that."
    show george angry
    shark "Go to Davy Jones' Locker."
    scene bg black with fade
    "(George got up, with a disgusted look on his face.)"
    "(You reflect upon his words to you.)"
    "(You need to clear your head, so you decide to go back to your fishing spot.)"
    scene bg shore with fade
    "(You've been here for hours.)"
    "(You've cast your line more times than you can count.)"
    scene bg black
    "(...but nobody came.)"
    "{b}BAD ENDING{/b}"
    return
label paci:
    show george neutral
    shark "I'm glad to see that you didn't keep any of the fish you caught."
    shark "The ocean is still plenty lively."
    shark "It's nice that you did the right thing and didn't screw anything up."
    shark "You're welcome to come by anytime."
label paciend:
    scene bg black with fade
    "(George got up, with a slight smile on his face.)"
    "(You reflect on your actions, and decide that what you did was for the best.)"
    "{b}GOOD ENDING{/b}"
    return
label neut:
    show george unamused with dissolve
    shark "You think you're subtle, don't you?"
    shark "Like some of us wouldn't notice a few fish missing from the ocean."
    if "g" in fishlist:
        shark "I bet, you didn't think I wouldn't notice an old pal of mine, right behind me."
        shark "Hey, Gupsby."
        show gupsby side at left with moveinleft
        voice "gup_hellooldfriend.mp3"
        g "Hello old friend!"
        show george sad with dissolve
        shark "You know, East Kelp has been real quiet without you, Gupsby."
        voice "gup_iwouldcomebackbutstuckintank.mp3"
        g "I would come back but I'm stuck in this tank!"
        hide gupsby with moveoutleft
        show george unamused with dissolve
        shark "Anyway..."
    if killcount == 4:
        shark "I bet you feel real good about yourself."
        show george shock with dissolve
        shark "You released ONE fish..."
        show george unamused with dissolve
        shark "...So you could barely squeak by without being judged even more harshly."
        shark "Pathetic."
        shark "I have no more words for you."
        jump neutend       
    elif killcount >= 2:
        shark "What, did you flip a coin?"
        shark "To decide who to release or who to keep?"
        menu:
            "Yes":
                shark "Can't be bothered to make decisions on your own, huh?"
                shark "You didn't think about how that would affect the ocean?"
                shark "I doubt it."
                jump neutpostchoice1
              
            "No":
                shark "You think you can just pick and choose who stays and who goes?"
                shark "Like picking a toy from the store?"
                shark "Is that how you see us?"
                shark "Mere playthings?"
                jump neutpostchoice1
            "...":
                shark "Too ashamed to answer?"
                jump neutpostchoice1
    else:
        shark "So you only took one fish with you."
        shark "Are they the love of your life or something?"
        shark "Did you even ask if they wanted to stay with you?"
        shark "Did their opinion matter to you?"
        shark "Clearly not."
        jump neutend
label neutpostchoice1:
        shark "Well, I suppose it could have been worse."
        show george shock with dissolve
        shark "Now, if you took ALL of the fish I'd be really mad."
        show george unamused with dissolve
        shark "But it's not like you can go back in time."
        shark "But is that all you strive for with your character?"
        shark "That you \"could be worse?\""   
        jump neutend
         
label neutend:
    scene bg black with fade
    "(George got up, the expression on his face being one you couldn't quite tell.)"
    "(You reflect on your actions up to this point.)"
    "(Did you really need to keep any of the fish?)"
    "(You're not sure.)"
    "{b}NEUTRAL ENDING{/b}"
    return

return
