# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#movie 

#stock images

#after sakura scene
label day1:
    play music "music/relax.mp3"
    pause 3

    m "what was that?"
    
    m "who was that"
    
    m "i keep having the same dream of a girl calling my name" 

    m "each day my dream progresses more and feels more vivid"

    m "and she tells me i need to go somewhere"

    m "but where"

    m "its always the same dream ive had for years"

    m "but ive been having them more frequently"

    m "it used to be that i just heard her calling me"

    m "but tonight was different"

    m "it was more vivid like i was there"

    m "and she was injured"

    m "who is she?"

    m "and why did she know me"

    m "how did i know her"

    m "it was if i had known her since long ago"

    m "i felt "

    m "why am i crying"

    m "just who was that girl"

    m "~i kept thinking about that dream and before i knew it "

    m "i had fallen back to sleep~"
    

    #intro 
    $ renpy.movie_cutscene("music/fakelove.mpg")

    

    play music "music/never be alone.mp3" fadein 1.0
    
    "{b}day [day]{/b}"


    menu:
        "I reach to the drawer and i grab"

        
        "book":
            $ intellect = 100
        "cell":
            $ intuition = 100
        "grapple watch":
            $ athletic = 100


    menu:
        "{b}~Alarm clock~{/b}"
        "wake up":
            jump wake

        "Sleep 10 more min":
            jump sleep
            
label wake:
    $ maturity += 5
    stop music fadeout 1.0
    "{b}~7:00 AM~{/b}"
    m "i have to get up"

    $ first_met = "Kaori"
    show kaori 
  
    #WIP@@@@@@@@@@@@@
    hide kaori
 
    jump day_one_morning 
    #dont run late so we walk to school meet Megumi and motoko 
    # neither are affected + kaori




label sleep:
    $ maturity -= 5
    stop music fadeout 1.0
    show bedroom day
    with dissolve
    m "five more minutes"

    "{b}~8:00 AM~{/b}"
    #WAKES UP LATE!!! scene my room mess desk 
    m "IM LATE!!!"
    
    #footsteps sound downstairs
    #rushes scene
    
    m "maybe i should get something quick to eat"
    define ate = False
    menu:

        "get someting quick to eat":
          #will be extra late and meet motoko 
         jump eat1

        "dont eat anything im running late already":
         jump dont_eat1

    label eat1:

       $ ate = True
       show living room evening
       with dissolve

       m "well i guess some leftover Mg tonalds"

       show food 2
       with dissolve
       #show food sandwich 
       m ""
       m "i need to hurry or i'll be late to the opening ceremony"

       jump transport
    label dont_eat1:

       $ ate = False 
       m "i dont have time to get something to eat"

       jump transport

   




label game:


label day_one_morning:

#meets megumi and motoko 



jump day_one_day


####


label transport:

     #show street
    show house exterior
    with dissolve
    m "i need to hurry what should i take? "
    menu:

      "go on bike":
        jump bike

      "go on bus":
        jump bus

      "go by foot":
        jump foot

      "give up and go home": 
        jump go_home

    label bike:
      $ athletic += 5
      $ first_met = "Akane"
      "i'll get to school faster if i take my bike"


      #show bike and bike riding 
      

      jump day_one_day

    label bus:
       play music "music/other/shelter.mp3"
       $ first_met = "Nagisa"

       m "~i think i'll take the bus or i'll have to walk from the parking lot to class, ~"
       m "~the bus will drop me off in front of my hall~"
       
       m "~ i got on the bus nearest my house and to my luck it just in time~"

       m "~i looked for an empty seat but they seemed to be all taken~"

       nagisa "uhm...you can sit here if you want"

       m "~ i looked toward what seemed to be a shy girl she had a petite figure wiht short hair"

       m "thank you"

       m "~either though she didnt look like the glamourus type she had put on a really nice perfume"

       m "and was well dressed"
       "ate = [ate]"
       #talks
       if(ate == False):
         m "~{b} ...groak..churn{/b}"

         nagisa "he.he..he.giggle what was that"

         $ nagisa_pts += 1

         m "oh my god how embarrrasing"
         
         nagisa "did you not have breakfast this morning"

         m "well i over slept and didnt have the time to get something to eat"

       m "~we talked for a bit before i knew it we were at school~"

       jump day_one_day

    label foot:
       $ athletic += 5
       play music "music/other/mine_re.mp3"
       m  "its not that far i might make it if i run"

       if(ate == True):
         m "grlk..maybe it was a bad idea to eat that much my stomach is getting upset"
       
         m "~i kept running~"

       megumi "HEY WATCH OUT!!!"


       "SMASH"

       $ first_met = "Megumi"
       
       m "as if in an anime or a manga someone crashed into me and landed on the floor"

       megumi "im sorry im late to class and was in a hurry here let me help you"

       m "thanks.."

       m "well i was also late this morning and came running to school too"

       megumi "well i guess we both overlept huh so whats your name"

       if (ate == True):
         m "~it seemed that my stomach finally caught up with my body and ~"

         megumi "im ..blauh"

         m "~and as luck would have it my stomach had a really good sense of humour~"

         megumi "uhm are you ok.."

         m "yeah im okay"

         m "sorry so whats your name"

         $ megumi_pts += 1

         megumi "well blaah my name is megumi"

       else:

         m "my name is [player_name] nice to meat umm"

         megumi "im Megumi"



       jump day_one_day


    label go_home:
      $ maturity -= 10
      #show home
      #show bed 
      m "i'm going back to sleep i'll just go tomorrow besides its the first day what can go wrong"
       
      jump day_two_morning


 ################     
label day_one_day:

    
    
    











    show bedroom_night 
    with dissolve
    play music "music/other/Plastic Memories OP.mp3"
    m "today was fun "
    m "i cant remember the last day something exciting happened"
    m "i hope im able to meet new friends and enjoy my first year in Tokyo U"

    
    m "as i drift to sleep i cant help but think about [first_met]"
 

    #$ renpy.movie_cutscene("music/canoe.mp4")
###########   

    # This ends the game.
  
#script